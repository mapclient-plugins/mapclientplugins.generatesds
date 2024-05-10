from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_contributorinformationwidget import Ui_ContributorInformation


class ContributorInformationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_ContributorInformation()
        self._ui.setupUi(self)

    def ui_elements(self):
        return dir(self._ui)

    def ui_owner(self):
        return self._ui

    def current_name(self):
        return self._ui.comboBox__dataset_description__Contributor_name.currentText()
