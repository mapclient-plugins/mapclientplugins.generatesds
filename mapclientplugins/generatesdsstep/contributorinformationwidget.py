from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_contributorinformationwidget import Ui_ContributorInformation


class ContributorInformationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_ContributorInformation()
        self._ui.setupUi(self)

        self._contributor_database = []

        self._make_connections()

    def _make_connections(self):
        self._ui.comboBox__dataset_description__Contributor_name.currentIndexChanged.connect(self._name_changed)
        self._ui.comboBox__dataset_description__Contributor_ORCiD.currentIndexChanged.connect(self._orcid_changed)

    def _name_changed(self, new_name_index):
        self._block_ui_signals(True)
        self._ui.comboBox__dataset_description__Contributor_ORCiD.setCurrentIndex(new_name_index)
        self._ui.comboBox__dataset_description__Contributor_affiliation.setCurrentIndex(new_name_index)
        self._ui.comboBox__dataset_description__Contributor_role.setCurrentIndex(new_name_index)
        self._block_ui_signals(False)

    def _orcid_changed(self, new_orcid_index):
        self._block_ui_signals(True)
        self._ui.comboBox__dataset_description__Contributor_name.setCurrentIndex(new_orcid_index)
        self._ui.comboBox__dataset_description__Contributor_affiliation.setCurrentIndex(new_orcid_index)
        self._ui.comboBox__dataset_description__Contributor_role.setCurrentIndex(new_orcid_index)
        self._block_ui_signals(False)

    def _block_ui_signals(self, state):
        self._ui.comboBox__dataset_description__Contributor_ORCiD.blockSignals(state)
        self._ui.comboBox__dataset_description__Contributor_name.blockSignals(state)

    def clear_current(self):
        self._block_ui_signals(True)
        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                element = getattr(self._ui, attr)
                element.setCurrentText("")

        self._block_ui_signals(False)

    def ui_elements(self):
        return dir(self._ui)

    def ui_owner(self):
        return self._ui

    def current_name(self):
        return self._ui.comboBox__dataset_description__Contributor_name.currentText()

    def load_database_contributor_information(self, contributor_information):
        self._contributor_database = contributor_information
        self._block_ui_signals(True)
        for contributor_info in contributor_information:
            for object_name in contributor_info:
                ui_element = getattr(self._ui, object_name)
                if ui_element.findText(contributor_info[object_name]) == -1:
                    ui_element.addItem(contributor_info[object_name])
        self._block_ui_signals(False)

    def save_database_contributor_information(self):
        contributor_information = {}
        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                element = getattr(self._ui, attr)
                contributor_information[attr] = element.currentText()

        return contributor_information
