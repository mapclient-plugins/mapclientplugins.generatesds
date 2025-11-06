# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'removesubjectdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_RemoveSubjectDialog(object):
    def setupUi(self, RemoveSubjectDialog):
        if not RemoveSubjectDialog.objectName():
            RemoveSubjectDialog.setObjectName(u"RemoveSubjectDialog")
        RemoveSubjectDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(RemoveSubjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelRemoveSubject = QLabel(RemoveSubjectDialog)
        self.labelRemoveSubject.setObjectName(u"labelRemoveSubject")
        self.labelRemoveSubject.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelRemoveSubject)

        self.comboBoxRemoveSubject = QComboBox(RemoveSubjectDialog)
        self.comboBoxRemoveSubject.setObjectName(u"comboBoxRemoveSubject")

        self.horizontalLayout.addWidget(self.comboBoxRemoveSubject)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 191, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttonBox = QDialogButtonBox(RemoveSubjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(RemoveSubjectDialog)
        self.buttonBox.accepted.connect(RemoveSubjectDialog.accept)
        self.buttonBox.rejected.connect(RemoveSubjectDialog.reject)

        QMetaObject.connectSlotsByName(RemoveSubjectDialog)
    # setupUi

    def retranslateUi(self, RemoveSubjectDialog):
        RemoveSubjectDialog.setWindowTitle(QCoreApplication.translate("RemoveSubjectDialog", u"Remove Subject", None))
        self.labelRemoveSubject.setText(QCoreApplication.translate("RemoveSubjectDialog", u"Remove subject:  ", None))
    # retranslateUi

