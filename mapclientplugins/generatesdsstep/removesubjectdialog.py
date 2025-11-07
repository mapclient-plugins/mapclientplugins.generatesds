from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_removesubjectdialog import Ui_RemoveSubjectDialog


class RemoveSubjectDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(RemoveSubjectDialog, self).__init__(parent)

        self._ui = Ui_RemoveSubjectDialog()
        self._ui.setupUi(self)

        self._make_connections()

    def _make_connections(self):
        self._ui.comboBoxRemoveSubject.currentIndexChanged.connect(self._current_index_changed)

    def _current_index_changed(self):
        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(self._ui.comboBoxRemoveSubject.currentIndex() != 0)

    def set_subjects(self, subjects):
        items = ['--'] + subjects
        self._ui.comboBoxRemoveSubject.addItems(items)

    def selected_subject(self):
        return self._ui.comboBoxRemoveSubject.currentText()
