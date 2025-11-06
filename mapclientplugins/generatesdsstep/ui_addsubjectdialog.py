# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addsubjectdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QWidget)

class Ui_AddSubjectDialog(object):
    def setupUi(self, AddSubjectDialog):
        if not AddSubjectDialog.objectName():
            AddSubjectDialog.setObjectName(u"AddSubjectDialog")
        AddSubjectDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(AddSubjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.retranslateUi(AddSubjectDialog)
        self.buttonBox.accepted.connect(AddSubjectDialog.accept)
        self.buttonBox.rejected.connect(AddSubjectDialog.reject)

        QMetaObject.connectSlotsByName(AddSubjectDialog)
    # setupUi

    def retranslateUi(self, AddSubjectDialog):
        AddSubjectDialog.setWindowTitle(QCoreApplication.translate("AddSubjectDialog", u"Add Subject", None))
    # retranslateUi

