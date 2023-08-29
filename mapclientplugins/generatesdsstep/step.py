"""
MAP Client Plugin Step
"""
import os
import json
import shutil

from PySide6 import QtGui, QtWidgets, QtCore

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.generatesdsstep.configuredialog import ConfigureDialog
from mapclientplugins.generatesdsstep.definitions import REQUIRED_FOLDER_LIST, CODE_FOLDER_LIST, EXPERIMENT_FOLDER_LIST

import os


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
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        self._icon = QtGui.QImage(':/generatesdsstep/images/data-source.png')
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location'))
        # Port data:
        self._portData0 = None  # http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location
        # Config:
        self._config = {'identifier': '', 'DatasetName': '', 'DatasetType': '', 'Directory': '', 'outputDir': ''}

    def execute(self):
        """
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        """
        # Put your execute step code here before calling the '_doneExecution' method.
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)
        output_dir = self._config['outputDir'] if os.path.isabs(self._config['outputDir']) else os.path.join(
            self._location, self._config['outputDir'])
        output_dir = os.path.realpath(output_dir)
        try:
            shutil.copytree('mapclientplugins/generatesdsstep/resources/required', output_dir, dirs_exist_ok=True)
            generate_folders(output_dir, REQUIRED_FOLDER_LIST)
            if self._config['DatasetType'] == "Code":
                shutil.copytree('mapclientplugins/generatesdsstep/resources/code', output_dir, dirs_exist_ok=True)
                generate_folders(output_dir, CODE_FOLDER_LIST)
            elif self._config['DatasetType'] == "Experiment":
                shutil.copytree('mapclientplugins/generatesdsstep/resources/experiment', output_dir, dirs_exist_ok=True)
                generate_folders(output_dir, EXPERIMENT_FOLDER_LIST)
        except FileExistsError:
            pass
        finally:
            QtWidgets.QApplication.restoreOverrideCursor()

        self._doneExecution()

    def getPortData(self, index):
        """
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.

        :param index: Index of the port to return.
        """
        return os.path.realpath(os.path.join(self._location, self._config[
            'Directory']))  # http://physiomeproject.org/workflow/1.0/rdf-schema#directory_location

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
