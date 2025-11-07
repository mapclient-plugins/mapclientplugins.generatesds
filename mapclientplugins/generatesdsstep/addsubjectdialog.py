import requests
from PySide6 import QtWidgets, QtCore

from mapclientplugins.generatesdsstep.ui_addsubjectdialog import Ui_AddSubjectDialog
from mapclientplugins.generatesdsstep.utitilities.excel import resolve_doi_to_url, check_subject_id_is_in_dataset


class AddSubjectDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(AddSubjectDialog, self).__init__(parent)

        self._ui = Ui_AddSubjectDialog()
        self._ui.setupUi(self)

        self._make_connections()

    def _make_connections(self):
        self._ui.lineEdit_subject_id.textEdited.connect(self._subject_id_text_edited)

    def _subject_id_text_edited(self, text):
        self._ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(text != '')

    def _valid_input(self):

        if self._ui.lineEdit_also_in_dataset_doi.text() != '':
            doi = self._ui.lineEdit_also_in_dataset_doi.text()
            if self._ui.radioButton_virtual.isChecked() and doi.startswith('https://doi.org/10.26275'):
                return True

            check_failed = True
            subject_id = self._ui.lineEdit_subject_id.text()
            try:
                QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.CursorShape.WaitCursor)

                check_failed = not check_subject_id_is_in_dataset(subject_id, doi)
                print('check failed:', check_failed)
            finally:
                QtWidgets.QApplication.restoreOverrideCursor()

            if check_failed:
                QtWidgets.QMessageBox.warning(self, 'Invalid input', f'Could not find subject {subject_id} in dataset.')
                return False

        return True

    def _get_data_as_dict(self):
        prefix = "lineEdit_"

        data_dict = {'virtual': self._ui.radioButton_virtual.isChecked(),}
        all_line_edits = self.findChildren(QtWidgets.QLineEdit)
        for line_edit in all_line_edits:
            object_name = line_edit.objectName()
            if object_name.startswith(prefix):
                key = object_name[len(prefix):]
                key = key.replace("_", " ")
                value = line_edit.text()
                data_dict[key] = value

        return data_dict

    def accepted_data(self):
        return self._get_data_as_dict()

    def accept(self):

        if not self._valid_input():
            return

        super().accept()
