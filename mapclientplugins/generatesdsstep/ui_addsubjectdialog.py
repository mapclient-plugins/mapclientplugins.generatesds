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
    QFormLayout, QLabel, QLineEdit, QRadioButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddSubjectDialog(object):
    def setupUi(self, AddSubjectDialog):
        if not AddSubjectDialog.objectName():
            AddSubjectDialog.setObjectName(u"AddSubjectDialog")
        AddSubjectDialog.resize(715, 565)
        self.verticalLayout = QVBoxLayout(AddSubjectDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(AddSubjectDialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 689, 499))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.lineEdit_subject_id = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_subject_id.setObjectName(u"lineEdit_subject_id")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_subject_id)

        self.lineEdit_pool_id = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_pool_id.setObjectName(u"lineEdit_pool_id")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.lineEdit_pool_id)

        self.lineEdit_age = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_age.setObjectName(u"lineEdit_age")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.lineEdit_age)

        self.lineEdit_sex = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_sex.setObjectName(u"lineEdit_sex")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lineEdit_sex)

        self.lineEdit_species = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_species.setObjectName(u"lineEdit_species")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.lineEdit_species)

        self.lineEdit_strain = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_strain.setObjectName(u"lineEdit_strain")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.lineEdit_strain)

        self.lineEdit_body_mass = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_body_mass.setObjectName(u"lineEdit_body_mass")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.FieldRole, self.lineEdit_body_mass)

        self.lineEdit_laboratory_internal_id = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_laboratory_internal_id.setObjectName(u"lineEdit_laboratory_internal_id")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.FieldRole, self.lineEdit_laboratory_internal_id)

        self.label_subject_id = QLabel(self.scrollAreaWidgetContents)
        self.label_subject_id.setObjectName(u"label_subject_id")
        self.label_subject_id.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_subject_id)

        self.lineEdit_also_in_dataset_doi = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_also_in_dataset_doi.setObjectName(u"lineEdit_also_in_dataset_doi")

        self.formLayout.setWidget(12, QFormLayout.ItemRole.FieldRole, self.lineEdit_also_in_dataset_doi)

        self.label_also_in_dataset_doi = QLabel(self.scrollAreaWidgetContents)
        self.label_also_in_dataset_doi.setObjectName(u"label_also_in_dataset_doi")
        self.label_also_in_dataset_doi.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(12, QFormLayout.ItemRole.LabelRole, self.label_also_in_dataset_doi)

        self.label_strain = QLabel(self.scrollAreaWidgetContents)
        self.label_strain.setObjectName(u"label_strain")
        self.label_strain.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.label_strain)

        self.label_species = QLabel(self.scrollAreaWidgetContents)
        self.label_species.setObjectName(u"label_species")
        self.label_species.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.label_species)

        self.label_sex = QLabel(self.scrollAreaWidgetContents)
        self.label_sex.setObjectName(u"label_sex")
        self.label_sex.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_sex)

        self.label_age = QLabel(self.scrollAreaWidgetContents)
        self.label_age.setObjectName(u"label_age")
        self.label_age.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_age)

        self.label_pool_id = QLabel(self.scrollAreaWidgetContents)
        self.label_pool_id.setObjectName(u"label_pool_id")
        self.label_pool_id.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_pool_id)

        self.label_body_mass = QLabel(self.scrollAreaWidgetContents)
        self.label_body_mass.setObjectName(u"label_body_mass")

        self.formLayout.setWidget(16, QFormLayout.ItemRole.LabelRole, self.label_body_mass)

        self.label_laboratory_internal_id = QLabel(self.scrollAreaWidgetContents)
        self.label_laboratory_internal_id.setObjectName(u"label_laboratory_internal_id")

        self.formLayout.setWidget(18, QFormLayout.ItemRole.LabelRole, self.label_laboratory_internal_id)

        self.radioButton_virtual = QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_virtual.setObjectName(u"radioButton_virtual")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.radioButton_virtual)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(AddSubjectDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(AddSubjectDialog)
        self.buttonBox.accepted.connect(AddSubjectDialog.accept)
        self.buttonBox.rejected.connect(AddSubjectDialog.reject)

        QMetaObject.connectSlotsByName(AddSubjectDialog)
    # setupUi

    def retranslateUi(self, AddSubjectDialog):
        AddSubjectDialog.setWindowTitle(QCoreApplication.translate("AddSubjectDialog", u"Add Subject", None))
        self.label_subject_id.setText(QCoreApplication.translate("AddSubjectDialog", u"Subject ID:  ", None))
        self.lineEdit_also_in_dataset_doi.setPlaceholderText(QCoreApplication.translate("AddSubjectDialog", u"https://doi.org/10.26275/xxxx-yyyy", None))
        self.label_also_in_dataset_doi.setText(QCoreApplication.translate("AddSubjectDialog", u"Also in dataset DOI:  ", None))
        self.label_strain.setText(QCoreApplication.translate("AddSubjectDialog", u"Strain:  ", None))
        self.label_species.setText(QCoreApplication.translate("AddSubjectDialog", u"Species:  ", None))
        self.label_sex.setText(QCoreApplication.translate("AddSubjectDialog", u"Sex:  ", None))
        self.label_age.setText(QCoreApplication.translate("AddSubjectDialog", u"Age:  ", None))
        self.label_pool_id.setText(QCoreApplication.translate("AddSubjectDialog", u"Pool ID:  ", None))
        self.label_body_mass.setText(QCoreApplication.translate("AddSubjectDialog", u"Body mass:  ", None))
        self.label_laboratory_internal_id.setText(QCoreApplication.translate("AddSubjectDialog", u"Laboratory internal ID:  ", None))
        self.radioButton_virtual.setText(QCoreApplication.translate("AddSubjectDialog", u"Virtual", None))
    # retranslateUi

