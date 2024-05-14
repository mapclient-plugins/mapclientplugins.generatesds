from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_otherinformationwidget import Ui_OtherInformation


class OtherInformationWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self._ui = Ui_OtherInformation()
        self._ui.setupUi(self)

        self._other_database = []

    def clear_current(self):
        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                element = getattr(self._ui, attr)
                element.setCurrentText("")

    def ui_elements(self):
        return dir(self._ui)

    def ui_owner(self):
        return self._ui

    def is_empty(self):
        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                element = getattr(self._ui, attr)
                if element.currentText():
                    return False

        return True

    def load_database_other_information(self, other_information):
        self._other_database = other_information
        for attr in other_information:
            ui_element = getattr(self._ui, attr)
            for entry in other_information[attr]:
                if ui_element.findText(entry) == -1:
                    ui_element.addItem(entry)

    def save_database_other_information(self):
        other_information = {}
        for attr in dir(self._ui):
            if attr.startswith("comboBox"):
                element = getattr(self._ui, attr)
                other_information[attr] = element.currentText()

        return other_information
