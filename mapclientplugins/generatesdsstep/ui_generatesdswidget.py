# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatesdswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_GenerateSDSWidget(object):
    def setupUi(self, GenerateSDSWidget):
        if not GenerateSDSWidget.objectName():
            GenerateSDSWidget.setObjectName(u"GenerateSDSWidget")
        GenerateSDSWidget.resize(714, 584)
        self.verticalLayout = QVBoxLayout(GenerateSDSWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.datasetGroupBox = QGroupBox(GenerateSDSWidget)
        self.datasetGroupBox.setObjectName(u"datasetGroupBox")
        self.formLayout = QFormLayout(self.datasetGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.labelDatasetTitle = QLabel(self.datasetGroupBox)
        self.labelDatasetTitle.setObjectName(u"labelDatasetTitle")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDatasetTitle)

        self.lineEditDatasetTitle = QLineEdit(self.datasetGroupBox)
        self.lineEditDatasetTitle.setObjectName(u"lineEditDatasetTitle")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditDatasetTitle)

        self.labelDatasetSubtitle = QLabel(self.datasetGroupBox)
        self.labelDatasetSubtitle.setObjectName(u"labelDatasetSubtitle")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDatasetSubtitle)

        self.lineEditDatasetSubtitle = QLineEdit(self.datasetGroupBox)
        self.lineEditDatasetSubtitle.setObjectName(u"lineEditDatasetSubtitle")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditDatasetSubtitle)

        self.labelDatasetKeywords = QLabel(self.datasetGroupBox)
        self.labelDatasetKeywords.setObjectName(u"labelDatasetKeywords")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDatasetKeywords)

        self.lineEditDatasetKeywords = QLineEdit(self.datasetGroupBox)
        self.lineEditDatasetKeywords.setObjectName(u"lineEditDatasetKeywords")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEditDatasetKeywords)

        self.labelDatasetFunding = QLabel(self.datasetGroupBox)
        self.labelDatasetFunding.setObjectName(u"labelDatasetFunding")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelDatasetFunding)

        self.lineEditDatasetFunding = QLineEdit(self.datasetGroupBox)
        self.lineEditDatasetFunding.setObjectName(u"lineEditDatasetFunding")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEditDatasetFunding)

        self.labelDatasetAcknowledgments = QLabel(self.datasetGroupBox)
        self.labelDatasetAcknowledgments.setObjectName(u"labelDatasetAcknowledgments")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelDatasetAcknowledgments)

        self.lineEditDatasetAcknowledgments = QLineEdit(self.datasetGroupBox)
        self.lineEditDatasetAcknowledgments.setObjectName(u"lineEditDatasetAcknowledgments")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEditDatasetAcknowledgments)


        self.verticalLayout.addWidget(self.datasetGroupBox)

        self.submissionGroupBox = QGroupBox(GenerateSDSWidget)
        self.submissionGroupBox.setObjectName(u"submissionGroupBox")
        self.submissionFormLayout = QFormLayout(self.submissionGroupBox)
        self.submissionFormLayout.setObjectName(u"submissionFormLayout")
        self.labelSPARCAwardNumber = QLabel(self.submissionGroupBox)
        self.labelSPARCAwardNumber.setObjectName(u"labelSPARCAwardNumber")

        self.submissionFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelSPARCAwardNumber)

        self.lineEditSPARCAwardNumber = QLineEdit(self.submissionGroupBox)
        self.lineEditSPARCAwardNumber.setObjectName(u"lineEditSPARCAwardNumber")

        self.submissionFormLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditSPARCAwardNumber)

        self.labelMilestoneAchieved = QLabel(self.submissionGroupBox)
        self.labelMilestoneAchieved.setObjectName(u"labelMilestoneAchieved")

        self.submissionFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelMilestoneAchieved)

        self.lineEditMilestoneAchieved = QLineEdit(self.submissionGroupBox)
        self.lineEditMilestoneAchieved.setObjectName(u"lineEditMilestoneAchieved")

        self.submissionFormLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditMilestoneAchieved)

        self.labelMilestoneCompletionDate = QLabel(self.submissionGroupBox)
        self.labelMilestoneCompletionDate.setObjectName(u"labelMilestoneCompletionDate")

        self.submissionFormLayout.setWidget(2, QFormLayout.LabelRole, self.labelMilestoneCompletionDate)

        self.calendarWidgetMilestoneCompletionDate = QCalendarWidget(self.submissionGroupBox)
        self.calendarWidgetMilestoneCompletionDate.setObjectName(u"calendarWidgetMilestoneCompletionDate")

        self.submissionFormLayout.setWidget(2, QFormLayout.FieldRole, self.calendarWidgetMilestoneCompletionDate)


        self.verticalLayout.addWidget(self.submissionGroupBox)

        self.manifestGroupBox = QGroupBox(GenerateSDSWidget)
        self.manifestGroupBox.setObjectName(u"manifestGroupBox")
        self.manifestFormLayout = QFormLayout(self.manifestGroupBox)
        self.manifestFormLayout.setObjectName(u"manifestFormLayout")
        self.labelSpecies = QLabel(self.manifestGroupBox)
        self.labelSpecies.setObjectName(u"labelSpecies")

        self.manifestFormLayout.setWidget(0, QFormLayout.LabelRole, self.labelSpecies)

        self.lineEditSpecies = QLineEdit(self.manifestGroupBox)
        self.lineEditSpecies.setObjectName(u"lineEditSpecies")

        self.manifestFormLayout.setWidget(0, QFormLayout.FieldRole, self.lineEditSpecies)

        self.labelOrgan = QLabel(self.manifestGroupBox)
        self.labelOrgan.setObjectName(u"labelOrgan")

        self.manifestFormLayout.setWidget(1, QFormLayout.LabelRole, self.labelOrgan)

        self.lineEditOrgan = QLineEdit(self.manifestGroupBox)
        self.lineEditOrgan.setObjectName(u"lineEditOrgan")

        self.manifestFormLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditOrgan)


        self.verticalLayout.addWidget(self.manifestGroupBox)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDone = QPushButton(GenerateSDSWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(GenerateSDSWidget)

        QMetaObject.connectSlotsByName(GenerateSDSWidget)
    # setupUi

    def retranslateUi(self, GenerateSDSWidget):
        GenerateSDSWidget.setWindowTitle(QCoreApplication.translate("GenerateSDSWidget", u"GenerateSDS Widget", None))
        self.datasetGroupBox.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Dataset description", None))
        self.labelDatasetTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Title:  ", None))
        self.labelDatasetSubtitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Subtitle:  ", None))
        self.labelDatasetKeywords.setText(QCoreApplication.translate("GenerateSDSWidget", u"Keywords:  ", None))
        self.labelDatasetFunding.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding:  ", None))
        self.labelDatasetAcknowledgments.setText(QCoreApplication.translate("GenerateSDSWidget", u"Acknowledgments:  ", None))
        self.submissionGroupBox.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Submission", None))
        self.labelSPARCAwardNumber.setText(QCoreApplication.translate("GenerateSDSWidget", u"SPARC Award number:  ", None))
        self.labelMilestoneAchieved.setText(QCoreApplication.translate("GenerateSDSWidget", u"Milestone achieved:  ", None))
        self.labelMilestoneCompletionDate.setText(QCoreApplication.translate("GenerateSDSWidget", u"Milestone completion date:  ", None))
        self.manifestGroupBox.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Scaffold manifest", None))
        self.labelSpecies.setText(QCoreApplication.translate("GenerateSDSWidget", u"Species:  ", None))
        self.labelOrgan.setText(QCoreApplication.translate("GenerateSDSWidget", u"Organ:  ", None))
        self.pushButtonDone.setText(QCoreApplication.translate("GenerateSDSWidget", u"Done", None))
    # retranslateUi

