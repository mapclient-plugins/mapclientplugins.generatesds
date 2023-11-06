
from PySide6 import QtWidgets
from mapclientplugins.generatesdsstep.ui_configuredialog import Ui_ConfigureDialog
import os.path

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class ConfigureDialog(QtWidgets.QDialog):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)

        self._workflow_location = None
        # Keep track of the previous identifier so that we can track changes
        # and know how many occurrences of the current identifier there should
        # be.
        self._previousIdentifier = ''
        # Set a place holder for a callable that will get set from the step.
        # We will use this method to decide whether the identifier is unique.
        self.identifierOccursCount = None
        self._previousLocation = ''

        self._makeConnections()

    def _makeConnections(self):
        self._ui.lineEdit0.textChanged.connect(self.validate)
        self._ui.lineEditDatasetName.textChanged.connect(self.validate)
        self._ui.lineEditDirectoryLocation.textChanged.connect(self.validate)
        self._ui.pushButtonDirectoryChooser.clicked.connect(self._directory_chooser_clicked)

    def _directory_chooser_clicked(self):
        location = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory', self._previousLocation)

        if location:
            self._previousLocation = location
            display_location = self._output_location(location)
            self._ui.lineEditDirectoryLocation.setText(display_location)

    def _output_location(self, location=None):
        if location is None:
            display_path = self._ui.lineEditDirectoryLocation.text()
        else:
            display_path = location
        if self._workflow_location and os.path.isabs(display_path):
            display_path = os.path.relpath(display_path, self._workflow_location)

        return display_path

    def setWorkflowLocation(self, location):
        self._workflow_location = location

    def accept(self):
        """
        Override the accept method so that we can confirm saving an
        invalid configuration.
        """
        result = QtWidgets.QMessageBox.Yes
        if not self.validate():
            result = QtWidgets.QMessageBox.warning(self, 'Invalid Configuration',
                'This configuration is invalid.  Unpredictable behaviour may result if you choose \'Yes\', '
                'are you sure you want to save this configuration?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        elif self.dataset_exists():
            result = QtWidgets.QMessageBox.warning(self, 'Dataset exists',
                'The dataset folder already exists. Files in the folder may be overwritten if you choose \'Yes\', '
                'are you sure you want to save this configuration?',
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if result == QtWidgets.QMessageBox.Yes:
            QtWidgets.QDialog.accept(self)

    def dataset_exists(self):
        config = self.getConfig()
        output_dir = config['outputDir'] if os.path.isabs(config['outputDir']) else os.path.join(
            self._workflow_location, config['outputDir'])
        return os.path.isdir(output_dir)

    def validate(self):
        """
        Validate the configuration dialog fields.  For any field that is not valid
        set the style sheet to the INVALID_STYLE_SHEET.  Return the outcome of the
        overall validity of the configuration.
        """
        # Determine if the current identifier is unique throughout the workflow
        # The identifierOccursCount method is part of the interface to the workflow framework.
        value = self.identifierOccursCount(self._ui.lineEdit0.text())
        valid = (value == 0) or (value == 1 and self._previousIdentifier == self._ui.lineEdit0.text())
        if valid:
            self._ui.lineEdit0.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.lineEdit0.setStyleSheet(INVALID_STYLE_SHEET)

        dataset_name_valid = len(self._ui.lineEditDatasetName.text())
        self._ui.lineEditDatasetName.setStyleSheet(DEFAULT_STYLE_SHEET
                                                   if dataset_name_valid else INVALID_STYLE_SHEET)

        dir_path = self._output_location()
        if self._workflow_location:
            dir_path = os.path.join(self._workflow_location, dir_path)

        directory_valid = os.path.isdir(dir_path) and len(self._ui.lineEditDirectoryLocation.text())
        self._ui.lineEditDirectoryLocation.setStyleSheet \
            (DEFAULT_STYLE_SHEET if directory_valid else INVALID_STYLE_SHEET)

        return valid and directory_valid

    def getConfig(self):
        """
        Get the current value of the configuration from the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = self._ui.lineEdit0.text()
        output_dir = os.path.join(self._output_location(), self._ui.lineEditDatasetName.text())
        config = {'identifier': self._ui.lineEdit0.text(), 'DatasetName': self._ui.lineEditDatasetName.text(),
                  'DatasetType': self._ui.comboBoxDatasetType.currentText(),
                  'DerivativeExists': self._ui.checkBoxDerivativeDataExists.isChecked(),
                  'Directory': self._output_location(), 'outputDir': output_dir}
        return config

    def setConfig(self, config):
        """
        Set the current value of the configuration for the dialog.  Also
        set the _previousIdentifier value so that we can check uniqueness of the
        identifier over the whole of the workflow.
        """
        self._previousIdentifier = config['identifier']
        self._ui.lineEdit0.setText(config['identifier'])
        self._ui.lineEditDatasetName.setText(config['DatasetName'])
        self._ui.comboBoxDatasetType.setCurrentText(config['DatasetType'])
        self._ui.checkBoxDerivativeDataExists.setChecked(config['DerivativeExists'])
        self._ui.lineEditDirectoryLocation.setText(config['Directory'])
