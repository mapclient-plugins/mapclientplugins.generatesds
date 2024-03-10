from PySide6 import QtCore, QtWidgets
from mapclientplugins.generatesdsstep.ui_generatesdswidget import Ui_GenerateSDSWidget
import os.path
import pandas as pd

INVALID_STYLE_SHEET = 'background-color: rgba(239, 0, 0, 50)'
DEFAULT_STYLE_SHEET = ''


class GenerateSDSWidget(QtWidgets.QWidget):
    """
    Configure dialog to present the user with the options to configure this step.
    """

    def __init__(self, dataset_loc, dataset_type, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_GenerateSDSWidget()
        self._ui.setupUi(self)

        self._workflow_location = None
        self._dataset_loc = dataset_loc
        self._description_df = None
        self._submission_df = None
        self._manifest_df = None
        self._dataset_type = dataset_type

        self._makeConnections()
        self._df = None  # To store the loaded DataFrame

        self.load_dataset_description()
        self.load_submission()
        if self._dataset_type == "Scaffold":
            self._ui.manifestGroupBox.setEnabled(True)
            self.load_manifest()

        self._callback = None

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._ui.dateEditMilestoneCompletionDate.setDisplayFormat("d-MMM-yyyy")

    # ==============Load=============
    def load_dataset_description(self):
        self._description_df = pd.read_excel(os.path.join(self._dataset_loc, "dataset_description.xlsx"), index_col=0).fillna('')
        # Assuming these columns exist in the Excel file
        self._ui.lineEditDatasetTitle.setText(str(self._description_df.at["    Title", "Value"]))
        self._ui.lineEditDatasetSubtitle.setText(str(self._description_df.at['    Subtitle', "Value"]))
        self._ui.lineEditDatasetKeywords.setText(str(self._description_df.at['    Keywords', "Value"]))
        self._ui.lineEditDatasetFunding.setText(str(self._description_df.at['    Funding', "Value"]))
        self._ui.lineEditDatasetAcknowledgments.setText(str(self._description_df.at['    Acknowledgments', "Value"]))

    def load_submission(self):
        self._submission_df = pd.read_excel(os.path.join(self._dataset_loc, "submission.xlsx"), index_col=0).fillna('')
        # Assuming these columns exist in the Excel file
        self._ui.lineEditSPARCAwardNumber.setText(str(self._submission_df.at["Award number", "Value"]))
        self._ui.lineEditMilestoneAchieved.setText(str(self._submission_df.at['Milestone achieved', "Value"]))
        completion_date = QtCore.QDate.fromString(str(self._submission_df.at['Milestone completion date', "Value"]), "d-MMM-yyyy")
        self._ui.dateEditMilestoneCompletionDate.setDate(completion_date)

    def load_manifest(self):
        if os.path.exists(os.path.join(self._dataset_loc, 'primary', "manifest.xlsx")):
            self._manifest_df = pd.read_excel(os.path.join(self._dataset_loc, 'primary', "manifest.xlsx")).fillna('')
            # Assuming these columns exist the in Excel file
            self._ui.lineEditSpecies.setText(str(self._manifest_df.at[0, "species"]))
            self._ui.lineEditOrgan.setText(str(self._manifest_df.at[0, 'organ']))
        else:
            self._manifest_df = pd.DataFrame([["",""]], columns=['species', 'organ'])

    # ==============Save=============
    def save_dataset_description(self):
        if self._description_df is not None:
            # Update the DataFrame with the modified values
            self._description_df.at["    Title", "Value"] = self._ui.lineEditDatasetTitle.text()
            self._description_df.at["    Subtitle", "Value"] = self._ui.lineEditDatasetSubtitle.text()
            self._description_df.at["    Keywords", "Value"] = self._ui.lineEditDatasetKeywords.text()
            self._description_df.at["    Funding", "Value"] = self._ui.lineEditDatasetFunding.text()
            self._description_df.at["    Acknowledgments", "Value"] = self._ui.lineEditDatasetAcknowledgments.text()

            # Save the DataFrame back to the same Excel file
            self._description_df.to_excel(os.path.join(self._dataset_loc, "dataset_description.xlsx"))

    def save_submission(self):
        if self._submission_df is not None:
            # Update the DataFrame with the modified values
            self._submission_df.at["Award number", "Value"] = self._ui.lineEditSPARCAwardNumber.text()
            self._submission_df.at['Milestone achieved', "Value"] = self._ui.lineEditMilestoneAchieved.text()
            self._submission_df.at['Milestone completion date', "Value"] = self._ui.dateEditMilestoneCompletionDate.text()

            # Save the DataFrame back to the same Excel file
            self._submission_df.to_excel(os.path.join(self._dataset_loc, "submission.xlsx"))

    def save_manifest(self):
        print(self._manifest_df)
        if self._manifest_df is not None:
            # Update the DataFrame with the modified values
            self._manifest_df["species"] = self._ui.lineEditSpecies.text()
            self._manifest_df['organ'] = self._ui.lineEditOrgan.text()

            # Save the DataFrame back to the Excel file
            self._manifest_df.to_excel(os.path.join(self._dataset_loc, 'primary', "manifest.xlsx"))

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        self.save_dataset_description()
        self.save_submission()
        self.save_manifest()

        self._callback()
