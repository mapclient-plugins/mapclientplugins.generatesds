"""
MAP Client Plugin Step
"""
import logging
import os
import json
import shutil

from PySide6 import QtGui, QtWidgets, QtCore

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.generatesdsstep.configuredialog import ConfigureDialog
from mapclientplugins.generatesdsstep.generatesdswidget import GenerateSDSWidget
from mapclientplugins.generatesdsstep.definitions import PROTOCOL_LAYOUT, DERIVATIVE_FOLDER
from mapclientplugins.generatesdsstep.protocolhandlers.simplescaffold import run_protocol

logger = logging.getLogger(__name__)


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
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#sds_protocol
        # Config:
        self._config = {'identifier': '', 'OverwriteExisting': False}

    def _prepare_layout(self):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            output_dir = self._portData0.get('inputs')[0]['value']
            dataset_type = self._portData0.get('type')

            layout = PROTOCOL_LAYOUT[dataset_type]
            print("output directory", output_dir)
            generate_folders(output_dir, layout.dirs())
            here = os.path.dirname(__file__)
            for _f in layout.files():
                output_file = os.path.join(output_dir, _f)
                if not os.path.isfile(output_file) or self._config['OverwriteExisting']:
                    shutil.copy2(os.path.join(here, 'resources', _f), output_file)
        except shutil.Error as exc:
            errors = exc.args[0]
            for error in errors:
                src, dst, msg = error
                QtWidgets.QMessageBox.critical(self._main_window, 'Permission denied', f"Cannot write to {dst}.")
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

    def _populate_protocol_data(self):
        try:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
            if self._portData0:
                output_dir = self._portData0.get('inputs')[0]['value']
                print("populate protocol data", self._portData0.get('name'), self._portData0.get('value'))
                print(output_dir)
                if self._portData0['name'] == 'SimpleScaffold':
                    run_protocol(self._main_window.model(), self._portData0['value'], output_dir)
                else:
                    print('run protocol', self._portData0['name'])

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
        print('execute')
        print(self._portData0)
        self._prepare_layout()
        self._populate_protocol_data()

        self._view = GenerateSDSWidget(self._portData0)
        self._view.register_done_execution(self._doneExecution)
        self._setCurrentWidget(self._view)

    def _show_critical_error(self):
        QtWidgets.QMessageBox.critical(self._main_window, 'SDS Protocol failed', f"Could not apply protocol: {self._portData1['name']}.")

    def setPortData(self, index, dataIn):
        print(':')
        print(dataIn)
        self._portData0 = dataIn  # http://physiomeproject.org/workflow/1.0/rdf-schema#sds_protocol

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


def _valid_connection(connection_info, scaffold_creator_index, argon_viewer_index):
    connection_ports_valid = connection_info[1] == 0 and connection_info[3] == 0
    connection_indexes_valid = connection_info[0] == scaffold_creator_index and connection_info[2] == argon_viewer_index
    return connection_ports_valid and connection_indexes_valid
