from PySide6 import QtWidgets

from mapclientplugins.generatesdsstep.ui_removesubjectdialog import Ui_RemoveSubjectDialog


class RemoveSubjectDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(RemoveSubjectDialog, self).__init__(parent)

        self.ui = Ui_RemoveSubjectDialog()
        self.ui.setupUi(self)
