# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.labelDatasetName = QLabel(self.configGroupBox)
        self.labelDatasetName.setObjectName(u"labelDatasetName")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDatasetName)

        self.lineEditDatasetName = QLineEdit(self.configGroupBox)
        self.lineEditDatasetName.setObjectName(u"lineEditDatasetName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDatasetName)

        self.labelDatasetType = QLabel(self.configGroupBox)
        self.labelDatasetType.setObjectName(u"labelDatasetType")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDatasetType)

        self.comboBoxDatasetType = QComboBox(self.configGroupBox)
        self.comboBoxDatasetType.addItem("")
        self.comboBoxDatasetType.addItem("")
        self.comboBoxDatasetType.addItem("")
        self.comboBoxDatasetType.setObjectName(u"comboBoxDatasetType")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxDatasetType)

        self.labelDerivativeData = QLabel(self.configGroupBox)
        self.labelDerivativeData.setObjectName(u"labelDerivativeData")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelDerivativeData)

        self.checkBoxDerivativeDataExists = QCheckBox(self.configGroupBox)
        self.checkBoxDerivativeDataExists.setObjectName(u"checkBoxDerivativeDataExists")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.checkBoxDerivativeDataExists)

        self.labelOutputDirectory = QLabel(self.configGroupBox)
        self.labelOutputDirectory.setObjectName(u"labelOutputDirectory")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelOutputDirectory)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditDirectoryLocation = QLineEdit(self.configGroupBox)
        self.lineEditDirectoryLocation.setObjectName(u"lineEditDirectoryLocation")

        self.horizontalLayout.addWidget(self.lineEditDirectoryLocation)

        self.pushButtonDirectoryChooser = QPushButton(self.configGroupBox)
        self.pushButtonDirectoryChooser.setObjectName(u"pushButtonDirectoryChooser")

        self.horizontalLayout.addWidget(self.pushButtonDirectoryChooser)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure generatesds", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.labelDatasetName.setText(QCoreApplication.translate("ConfigureDialog", u"Dataset Name:  ", None))
        self.labelDatasetType.setText(QCoreApplication.translate("ConfigureDialog", u"Dataset Type:  ", None))
        self.comboBoxDatasetType.setItemText(0, QCoreApplication.translate("ConfigureDialog", u"Code", None))
        self.comboBoxDatasetType.setItemText(1, QCoreApplication.translate("ConfigureDialog", u"Experiment", None))
        self.comboBoxDatasetType.setItemText(2, QCoreApplication.translate("ConfigureDialog", u"Scaffold", None))

        self.labelDerivativeData.setText(QCoreApplication.translate("ConfigureDialog", u"Derivative data:  ", None))
        self.checkBoxDerivativeDataExists.setText(QCoreApplication.translate("ConfigureDialog", u"Exists", None))
        self.labelOutputDirectory.setText(QCoreApplication.translate("ConfigureDialog", u"Output directory:  ", None))
        self.pushButtonDirectoryChooser.setText(QCoreApplication.translate("ConfigureDialog", u"...", None))
    # retranslateUi

