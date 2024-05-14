"""
MAP Client Plugin Step
"""
import os
import json
import shutil

from PySide6 import QtGui, QtWidgets, QtCore

from mapclient.core.utils import copy_step_additional_config_files, get_steps_additional_config_files
from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint, workflowStepFactory
from mapclientplugins.generatesdsstep.configuredialog import ConfigureDialog
from mapclientplugins.generatesdsstep.generatesdswidget import GenerateSDSWidget
from mapclientplugins.generatesdsstep.definitions import PROTOCOL_LAYOUT, DERIVATIVE_FOLDER, SCAFFOLD_INFO_FILE


def generate_folders(output_dir, folder_name_list):
    """
    Create folders in the specified output directory.

    This function takes an output directory path and a list of folder names. It checks if each folder
    from the provided list already exists in the output directory. If not, it creates the folder.

    Parameters:
        output_dir (str): The path of the output directory where the folders will be created.
        folder_name_list (list): A list of strings containing the names of folders to be created.

    Returns:
        None: The function does not return anything explicitly, but it creates folders in the output directory.
    """
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    for folder_name in folder_name_list:
        abs_folder = os.path.join(output_dir, folder_name)
        if not os.path.isdir(abs_folder):
            os.mkdir(abs_folder)


class GenerateSDSStep(WorkflowStepMountPoint):
    """
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    """

    def __init__(self, location):
        super(GenerateSDSStep, self).__init__('GenerateSDS', location)
        self._view = None
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/generatesdsstep/images/data-source.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#sds_protocol'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location'))
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location
        self._portData1 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#sds_protocol
        # Config:
        self._config = {'identifier': '', 'DatasetName': '', 'DatasetType': '', 'Directory': '',
                        'DerivativeExists': False, 'outputDir': '', 'OverwriteExisting': False}

    def _prepare_layout(self, output_dir):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            layout = PROTOCOL_LAYOUT[self._config['DatasetType']]
            generate_folders(output_dir, layout.dirs())
            here = os.path.dirname(__file__)
            for _f in layout.files():
                output_file = os.path.join(output_dir, _f)
                if not os.path.isfile(output_file) or self._config['OverwriteExisting']:
                    shutil.copy2(os.path.join(here, 'resources', _f), output_file)
            if self._config['DerivativeExists']:
                generate_folders(output_dir, DERIVATIVE_FOLDER)
        except shutil.Error as exc:
            errors = exc.args[0]
            for error in errors:
                src, dst, msg = error
                QtWidgets.QMessageBox.critical(self._main_window, 'Permission denied', f"Cannot write to {dst}.")
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _populate_protocol_data(self, output_dir):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            if self._portData1:
                if self._portData1['name'] == 'SimpleScaffold':
                    model = self._main_window.model()
                    wm = model.workflowManager()
                    ws = wm.scene()
                    scaffold_creator_config_files = []
                    required_steps = []
                    for i in self._portData1['inputs']:
                        if i['type'] == 'identifier_file':
                            source_configuration_dir = os.path.dirname(i['value'])
                            target_configuration_dir = os.path.join(output_dir, i['destination'])

                            shutil.copy(i['value'], target_configuration_dir)

                            step_identifier, configuration_ext = os.path.splitext(os.path.basename(i['value']))
                            wf = wm.load_workflow_virtually(source_configuration_dir)
                            step_name = ws.get_step_name_from_identifier(wf, step_identifier)
                            required_steps.append((step_name, step_identifier))
                            step = workflowStepFactory(step_name, target_configuration_dir)
                            step.setIdentifier(step_identifier)
                            step.setLocation(source_configuration_dir)

                            if step.getName() == "Scaffold Creator":
                                config_files = get_steps_additional_config_files(step)
                                if len(config_files) > 0:
                                    scaffold_creator_config_files.append(config_files[0])

                            copy_step_additional_config_files(step, source_configuration_dir, target_configuration_dir)
                        elif i['type'] == 'directory':
                            src = i['value']
                            dst = os.path.join(output_dir, i['destination'])
                            os.makedirs(dst, exist_ok=True)
                            names = os.listdir(src)
                            for name in names:
                                src_name = os.path.join(src, name)
                                dst_name = os.path.join(dst, name)
                                if os.path.isfile(src_name):
                                    shutil.copy2(src_name, dst_name)
                        elif i['type'] == 'dict':
                            with open(os.path.join(output_dir, i['destination']), 'w') as f:
                                json.dump(i['value'], f)

                    workflow_location = os.path.join(output_dir, 'primary')
                    wf = wm.create_empty_workflow(workflow_location)
                    ws.create_from(wf, required_steps, workflow_location)
                    wf_file = os.path.basename(wf.fileName())
                    scaffold_info = {
                        'id': 'scaffold-info-using-map-client-workflow',
                        'version': '1.0.0',
                        'mapping-tools-workflow-file': wf_file,
                        'scaffold-settings-files': scaffold_creator_config_files,
                    }
                    with open(os.path.join(output_dir, 'primary', SCAFFOLD_INFO_FILE), 'w') as f:
                        json.dump(scaffold_info, f, default=lambda o: o.__dict__, sort_keys=True, indent=2)

        except shutil.Error as exc:
            self._show_critical_error()
            raise exc
        except OSError as exc:
            self._show_critical_error()
            raise exc
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        output_dir = self._config['outputDir'] if os.path.isabs(self._config['outputDir']) else os.path.join(
            self._location, self._config['outputDir'])
        output_dir = os.path.realpath(output_dir)

        self._prepare_layout(output_dir)
        self._populate_protocol_data(output_dir)

        self._view = GenerateSDSWidget(output_dir, self._config['DatasetType'])
        self._view.register_done_execution(self._doneExecution)
        self._setCurrentWidget(self._view)

    def _show_critical_error(self):
        QtWidgets.QMessageBox.critical(self._main_window, 'SDS Protocol failed', f"Could not apply protocol: {self._portData1['name']}.")

    def setPortData(self, index, dataIn):
        self._portData1 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#sds_protocol

    def getPortData(self, index):
        """
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        # http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location
        return os.path.realpath(os.path.join(self._location, self._config['outputDir']))

    def configure(self):
        """
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        """
        dlg = ConfigureDialog(self._main_window)
        dlg.setWorkflowLocation(self._location)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        """
        The identifier is a string that must be unique within a workflow.
        """
        return self._config['identifier']

    def setIdentifier(self, identifier):
        """
        The framework will set the identifier for this step when it is loaded.
        """
        self._config['identifier'] = identifier

    def serialize(self):
        """
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        """
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        """
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.

        :param string: JSON representation of the configuration in a string.
        """
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.setWorkflowLocation(self._location)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()
