from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_addsubjectdialog import Ui_AddSubjectDialog


class AddSubjectDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(AddSubjectDialog, self).__init__(parent)

        self.ui = Ui_AddSubjectDialog()
        self.ui.setupUi(self)
