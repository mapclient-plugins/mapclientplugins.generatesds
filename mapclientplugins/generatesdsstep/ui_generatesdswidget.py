# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatesdswidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_GenerateSDSWidget(object):
    def setupUi(self, GenerateSDSWidget):
        if not GenerateSDSWidget.objectName():
            GenerateSDSWidget.setObjectName(u"GenerateSDSWidget")
        GenerateSDSWidget.resize(1025, 871)
        self.verticalLayout_5 = QVBoxLayout(GenerateSDSWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_1 = QFrame(GenerateSDSWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_1.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBoxBasicInformation = QGroupBox(self.frame_1)
        self.groupBoxBasicInformation.setObjectName(u"groupBoxBasicInformation")
        self.gridLayout = QGridLayout(self.groupBoxBasicInformation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 12, -1, -1)
        self.comboBox__dataset_description__Subtitle = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Subtitle.setObjectName(u"comboBox__dataset_description__Subtitle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Subtitle.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Subtitle.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Subtitle.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Subtitle.setMaximumSize(QSize(1040, 16777215))
        self.comboBox__dataset_description__Subtitle.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Subtitle, 2, 1, 1, 2)

        self.labelDatasetTitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetTitle.setObjectName(u"labelDatasetTitle")
        self.labelDatasetTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetTitle, 1, 0, 1, 1)

        self.labelDatasetAcknowledgments = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetAcknowledgments.setObjectName(u"labelDatasetAcknowledgments")
        self.labelDatasetAcknowledgments.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetAcknowledgments, 4, 0, 1, 1)

        self.labelDatasetSubtitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetSubtitle.setObjectName(u"labelDatasetSubtitle")
        self.labelDatasetSubtitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetSubtitle, 2, 0, 1, 1)

        self.labelDatasetLicense = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetLicense.setObjectName(u"labelDatasetLicense")
        self.labelDatasetLicense.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetLicense, 7, 0, 1, 1)

        self.comboBox__dataset_description__Type = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Type.addItem("")
        self.comboBox__dataset_description__Type.addItem("")
        self.comboBox__dataset_description__Type.addItem("")
        self.comboBox__dataset_description__Type.setObjectName(u"comboBox__dataset_description__Type")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Type.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Type.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Type.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Type.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Type, 0, 1, 1, 2)

        self.comboBox__dataset_description__License = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__License.setObjectName(u"comboBox__dataset_description__License")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__License.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__License.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__License.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__License.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__License, 7, 1, 1, 1)

        self.comboBox__dataset_description__Acknowledgments = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Acknowledgments.setObjectName(u"comboBox__dataset_description__Acknowledgments")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Acknowledgments.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Acknowledgments.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Acknowledgments.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Acknowledgments.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Acknowledgments, 4, 1, 1, 1)

        self.widgetForChips__dataset_description__Keywords = QWidget(self.groupBoxBasicInformation)
        self.widgetForChips__dataset_description__Keywords.setObjectName(u"widgetForChips__dataset_description__Keywords")

        self.gridLayout.addWidget(self.widgetForChips__dataset_description__Keywords, 9, 1, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.databaseOnlyComboBox__dataset_description__Keywords = QComboBox(self.groupBoxBasicInformation)
        self.databaseOnlyComboBox__dataset_description__Keywords.setObjectName(u"databaseOnlyComboBox__dataset_description__Keywords")
        sizePolicy.setHeightForWidth(self.databaseOnlyComboBox__dataset_description__Keywords.sizePolicy().hasHeightForWidth())
        self.databaseOnlyComboBox__dataset_description__Keywords.setSizePolicy(sizePolicy)
        self.databaseOnlyComboBox__dataset_description__Keywords.setMinimumSize(QSize(127, 0))
        self.databaseOnlyComboBox__dataset_description__Keywords.setEditable(True)

        self.horizontalLayout_6.addWidget(self.databaseOnlyComboBox__dataset_description__Keywords)

        self.pushButtonAddKeyword = QPushButton(self.groupBoxBasicInformation)
        self.pushButtonAddKeyword.setObjectName(u"pushButtonAddKeyword")

        self.horizontalLayout_6.addWidget(self.pushButtonAddKeyword)


        self.gridLayout.addLayout(self.horizontalLayout_6, 8, 1, 1, 2)

        self.comboBox__dataset_description__Title = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Title.setObjectName(u"comboBox__dataset_description__Title")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Title.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Title.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Title, 1, 1, 1, 2)

        self.labelDatasetKeywords = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetKeywords.setObjectName(u"labelDatasetKeywords")
        self.labelDatasetKeywords.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetKeywords, 8, 0, 1, 1)

        self.labelDatasetType = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetType.setObjectName(u"labelDatasetType")
        self.labelDatasetType.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetType, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBoxBasicInformation)

        self.groupBox_2 = QGroupBox(self.frame_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelDatasetFunding = QLabel(self.groupBox_2)
        self.labelDatasetFunding.setObjectName(u"labelDatasetFunding")
        self.labelDatasetFunding.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelDatasetFunding, 0, 0, 1, 1)

        self.labelAwardNumber_2 = QLabel(self.groupBox_2)
        self.labelAwardNumber_2.setObjectName(u"labelAwardNumber_2")
        self.labelAwardNumber_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelAwardNumber_2, 3, 0, 1, 1)

        self.comboBox__dataset_description__Funding = QComboBox(self.groupBox_2)
        self.comboBox__dataset_description__Funding.setObjectName(u"comboBox__dataset_description__Funding")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Funding.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Funding.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Funding.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Funding.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__dataset_description__Funding, 0, 1, 1, 1)

        self.comboBox__dataset_description__Award_number = QComboBox(self.groupBox_2)
        self.comboBox__dataset_description__Award_number.setObjectName(u"comboBox__dataset_description__Award_number")
        self.comboBox__dataset_description__Award_number.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__dataset_description__Award_number, 3, 1, 1, 1)

        self.comboBox__dataset_description__Funding_consortium = QComboBox(self.groupBox_2)
        self.comboBox__dataset_description__Funding_consortium.setObjectName(u"comboBox__dataset_description__Funding_consortium")
        self.comboBox__dataset_description__Funding_consortium.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__dataset_description__Funding_consortium, 1, 1, 1, 1)

        self.labelFundingConsortium_2 = QLabel(self.groupBox_2)
        self.labelFundingConsortium_2.setObjectName(u"labelFundingConsortium_2")
        self.labelFundingConsortium_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelFundingConsortium_2, 1, 0, 1, 1)

        self.labelFundingAgency = QLabel(self.groupBox_2)
        self.labelFundingAgency.setObjectName(u"labelFundingAgency")
        self.labelFundingAgency.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelFundingAgency, 2, 0, 1, 1)

        self.comboBox__dataset_description__Funding_agency = QComboBox(self.groupBox_2)
        self.comboBox__dataset_description__Funding_agency.setObjectName(u"comboBox__dataset_description__Funding_agency")
        self.comboBox__dataset_description__Funding_agency.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__dataset_description__Funding_agency, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 4, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.groupBox_2)


        self.horizontalLayout_4.addWidget(self.frame_1)

        self.frame_2 = QFrame(GenerateSDSWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBoxStudyInformation = QGroupBox(self.frame_2)
        self.groupBoxStudyInformation.setObjectName(u"groupBoxStudyInformation")
        self.gridLayout_2 = QGridLayout(self.groupBoxStudyInformation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelStudyTechnique = QLabel(self.groupBoxStudyInformation)
        self.labelStudyTechnique.setObjectName(u"labelStudyTechnique")
        self.labelStudyTechnique.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyTechnique, 6, 0, 1, 1)

        self.labelStudyApproach = QLabel(self.groupBoxStudyInformation)
        self.labelStudyApproach.setObjectName(u"labelStudyApproach")
        self.labelStudyApproach.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyApproach, 4, 0, 1, 1)

        self.labelStudyOrganSystem = QLabel(self.groupBoxStudyInformation)
        self.labelStudyOrganSystem.setObjectName(u"labelStudyOrganSystem")
        self.labelStudyOrganSystem.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyOrganSystem, 3, 0, 1, 1)

        self.plainTextEdit__dataset_description__Study_data_collection = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_data_collection.setObjectName(u"plainTextEdit__dataset_description__Study_data_collection")

        self.gridLayout_2.addWidget(self.plainTextEdit__dataset_description__Study_data_collection, 1, 1, 1, 1)

        self.labelStudyDataCollection = QLabel(self.groupBoxStudyInformation)
        self.labelStudyDataCollection.setObjectName(u"labelStudyDataCollection")
        self.labelStudyDataCollection.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.labelStudyDataCollection, 1, 0, 1, 1)

        self.labelStudyCollectionTitle = QLabel(self.groupBoxStudyInformation)
        self.labelStudyCollectionTitle.setObjectName(u"labelStudyCollectionTitle")
        self.labelStudyCollectionTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyCollectionTitle, 5, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.databaseOnlyComboBox__dataset_description__Study_technique = QComboBox(self.groupBoxStudyInformation)
        self.databaseOnlyComboBox__dataset_description__Study_technique.setObjectName(u"databaseOnlyComboBox__dataset_description__Study_technique")
        sizePolicy.setHeightForWidth(self.databaseOnlyComboBox__dataset_description__Study_technique.sizePolicy().hasHeightForWidth())
        self.databaseOnlyComboBox__dataset_description__Study_technique.setSizePolicy(sizePolicy)
        self.databaseOnlyComboBox__dataset_description__Study_technique.setMinimumSize(QSize(127, 0))
        self.databaseOnlyComboBox__dataset_description__Study_technique.setEditable(True)

        self.horizontalLayout_7.addWidget(self.databaseOnlyComboBox__dataset_description__Study_technique)

        self.pushButtonAddStudy_technique = QPushButton(self.groupBoxStudyInformation)
        self.pushButtonAddStudy_technique.setObjectName(u"pushButtonAddStudy_technique")

        self.horizontalLayout_7.addWidget(self.pushButtonAddStudy_technique)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 6, 1, 1, 1)

        self.labelStudyPurpose = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPurpose.setObjectName(u"labelStudyPurpose")
        self.labelStudyPurpose.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyPurpose, 0, 0, 1, 1)

        self.plainTextEdit__dataset_description__Study_primary_conclusion = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_primary_conclusion.setObjectName(u"plainTextEdit__dataset_description__Study_primary_conclusion")

        self.gridLayout_2.addWidget(self.plainTextEdit__dataset_description__Study_primary_conclusion, 2, 1, 1, 1)

        self.comboBox__dataset_description__Study_organ_system = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_organ_system.setObjectName(u"comboBox__dataset_description__Study_organ_system")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_organ_system.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_organ_system.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_organ_system.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_organ_system.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_organ_system, 3, 1, 1, 1)

        self.comboBox__dataset_description__Study_purpose = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_purpose.setObjectName(u"comboBox__dataset_description__Study_purpose")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_purpose.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_purpose.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_purpose.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_purpose.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_purpose, 0, 1, 1, 1)

        self.labelStudyPrimaryConclusion = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPrimaryConclusion.setObjectName(u"labelStudyPrimaryConclusion")
        self.labelStudyPrimaryConclusion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.labelStudyPrimaryConclusion, 2, 0, 1, 1)

        self.widgetForChips__dataset_description__Study_technique = QWidget(self.groupBoxStudyInformation)
        self.widgetForChips__dataset_description__Study_technique.setObjectName(u"widgetForChips__dataset_description__Study_technique")

        self.gridLayout_2.addWidget(self.widgetForChips__dataset_description__Study_technique, 7, 1, 1, 1)

        self.comboBox__dataset_description__Study_approach = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_approach.setObjectName(u"comboBox__dataset_description__Study_approach")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_approach.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_approach.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_approach.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_approach.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_approach, 4, 1, 1, 1)

        self.comboBox__dataset_description__Study_collection_title = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_collection_title.setObjectName(u"comboBox__dataset_description__Study_collection_title")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_collection_title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_collection_title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_collection_title.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_collection_title.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_collection_title, 5, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBoxStudyInformation)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(GenerateSDSWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.groupBoxDynamic = QGroupBox(self.frame_3)
        self.groupBoxDynamic.setObjectName(u"groupBoxDynamic")
        self.gridLayout_5 = QGridLayout(self.groupBoxDynamic)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidgetDynamic = QStackedWidget(self.groupBoxDynamic)
        self.stackedWidgetDynamic.setObjectName(u"stackedWidgetDynamic")
        self.pageSubjectsAndSamples = QWidget()
        self.pageSubjectsAndSamples.setObjectName(u"pageSubjectsAndSamples")
        self.gridLayout_6 = QGridLayout(self.pageSubjectsAndSamples)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.labelNumberOfSamples = QLabel(self.pageSubjectsAndSamples)
        self.labelNumberOfSamples.setObjectName(u"labelNumberOfSamples")
        self.labelNumberOfSamples.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelNumberOfSamples, 1, 0, 1, 1)

        self.spinBox__dataset_description__Number_of_samples = QSpinBox(self.pageSubjectsAndSamples)
        self.spinBox__dataset_description__Number_of_samples.setObjectName(u"spinBox__dataset_description__Number_of_samples")

        self.gridLayout_6.addWidget(self.spinBox__dataset_description__Number_of_samples, 1, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.pushButtonAddSubject = QPushButton(self.pageSubjectsAndSamples)
        self.pushButtonAddSubject.setObjectName(u"pushButtonAddSubject")

        self.horizontalLayout_10.addWidget(self.pushButtonAddSubject)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.pushButtonRemoveSubject = QPushButton(self.pageSubjectsAndSamples)
        self.pushButtonRemoveSubject.setObjectName(u"pushButtonRemoveSubject")

        self.horizontalLayout_10.addWidget(self.pushButtonRemoveSubject)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.gridLayout_6.addLayout(self.horizontalLayout_10, 3, 0, 1, 2)

        self.spinBox__dataset_description__Number_of_subjects = QSpinBox(self.pageSubjectsAndSamples)
        self.spinBox__dataset_description__Number_of_subjects.setObjectName(u"spinBox__dataset_description__Number_of_subjects")

        self.gridLayout_6.addWidget(self.spinBox__dataset_description__Number_of_subjects, 0, 1, 1, 1)

        self.labelNumberOfSubjects = QLabel(self.pageSubjectsAndSamples)
        self.labelNumberOfSubjects.setObjectName(u"labelNumberOfSubjects")
        self.labelNumberOfSubjects.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_6.addWidget(self.labelNumberOfSubjects, 0, 0, 1, 1)

        self.widgetSpacer_1 = QWidget(self.pageSubjectsAndSamples)
        self.widgetSpacer_1.setObjectName(u"widgetSpacer_1")

        self.gridLayout_6.addWidget(self.widgetSpacer_1, 4, 0, 1, 1)

        self.stackedWidgetDynamic.addWidget(self.pageSubjectsAndSamples)
        self.pageScaffoldManifest = QWidget()
        self.pageScaffoldManifest.setObjectName(u"pageScaffoldManifest")
        self.gridLayout_7 = QGridLayout(self.pageScaffoldManifest)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.labelSpecies = QLabel(self.pageScaffoldManifest)
        self.labelSpecies.setObjectName(u"labelSpecies")
        self.labelSpecies.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.labelSpecies, 0, 0, 1, 1)

        self.comboBox__manifest__species = QComboBox(self.pageScaffoldManifest)
        self.comboBox__manifest__species.setObjectName(u"comboBox__manifest__species")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__species.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__species.setSizePolicy(sizePolicy)
        self.comboBox__manifest__species.setMinimumSize(QSize(127, 0))
        self.comboBox__manifest__species.setEditable(True)

        self.gridLayout_7.addWidget(self.comboBox__manifest__species, 0, 1, 1, 1)

        self.labelOrgan = QLabel(self.pageScaffoldManifest)
        self.labelOrgan.setObjectName(u"labelOrgan")
        self.labelOrgan.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.labelOrgan, 1, 0, 1, 1)

        self.comboBox__manifest__organ = QComboBox(self.pageScaffoldManifest)
        self.comboBox__manifest__organ.setObjectName(u"comboBox__manifest__organ")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__organ.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__organ.setSizePolicy(sizePolicy)
        self.comboBox__manifest__organ.setMinimumSize(QSize(127, 0))
        self.comboBox__manifest__organ.setEditable(True)

        self.gridLayout_7.addWidget(self.comboBox__manifest__organ, 1, 1, 1, 1)

        self.widgetSpacer = QWidget(self.pageScaffoldManifest)
        self.widgetSpacer.setObjectName(u"widgetSpacer")

        self.gridLayout_7.addWidget(self.widgetSpacer, 2, 1, 1, 1)

        self.stackedWidgetDynamic.addWidget(self.pageScaffoldManifest)

        self.gridLayout_5.addWidget(self.stackedWidgetDynamic, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.groupBoxDynamic)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBoxStandardsInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxStandardsInformation.setObjectName(u"groupBoxStandardsInformation")
        self.gridLayout_4 = QGridLayout(self.groupBoxStandardsInformation)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.comboBox__dataset_description__Data_standard = QComboBox(self.groupBoxStandardsInformation)
        self.comboBox__dataset_description__Data_standard.setObjectName(u"comboBox__dataset_description__Data_standard")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Data_standard.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Data_standard.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Data_standard.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Data_standard.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__dataset_description__Data_standard, 0, 1, 1, 1)

        self.labelConsortiumDataStandard = QLabel(self.groupBoxStandardsInformation)
        self.labelConsortiumDataStandard.setObjectName(u"labelConsortiumDataStandard")
        self.labelConsortiumDataStandard.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelConsortiumDataStandard, 0, 0, 1, 1)

        self.comboBox__dataset_description__Data_standard_version = QComboBox(self.groupBoxStandardsInformation)
        self.comboBox__dataset_description__Data_standard_version.setObjectName(u"comboBox__dataset_description__Data_standard_version")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Data_standard_version.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Data_standard_version.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Data_standard_version.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Data_standard_version.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__dataset_description__Data_standard_version, 1, 1, 1, 1)

        self.labelMilestoneAchieved = QLabel(self.groupBoxStandardsInformation)
        self.labelMilestoneAchieved.setObjectName(u"labelMilestoneAchieved")
        self.labelMilestoneAchieved.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelMilestoneAchieved, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBoxStandardsInformation)

        self.groupBox = QGroupBox(GenerateSDSWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButtonAddOther = QPushButton(self.groupBox)
        self.pushButtonAddOther.setObjectName(u"pushButtonAddOther")

        self.horizontalLayout_5.addWidget(self.pushButtonAddOther)

        self.pushButtonRemoveOther = QPushButton(self.groupBox)
        self.pushButtonRemoveOther.setObjectName(u"pushButtonRemoveOther")

        self.horizontalLayout_5.addWidget(self.pushButtonRemoveOther)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tabWidgetOthers = QTabWidget(self.groupBox)
        self.tabWidgetOthers.setObjectName(u"tabWidgetOthers")

        self.verticalLayout_3.addWidget(self.tabWidgetOthers)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.groupBoxContributorInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxContributorInformation.setObjectName(u"groupBoxContributorInformation")
        self.verticalLayout = QVBoxLayout(self.groupBoxContributorInformation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButtonAddContributor = QPushButton(self.groupBoxContributorInformation)
        self.pushButtonAddContributor.setObjectName(u"pushButtonAddContributor")

        self.horizontalLayout_2.addWidget(self.pushButtonAddContributor)

        self.pushButtonRemoveContributor = QPushButton(self.groupBoxContributorInformation)
        self.pushButtonRemoveContributor.setObjectName(u"pushButtonRemoveContributor")

        self.horizontalLayout_2.addWidget(self.pushButtonRemoveContributor)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidgetContributors = QTabWidget(self.groupBoxContributorInformation)
        self.tabWidgetContributors.setObjectName(u"tabWidgetContributors")

        self.verticalLayout.addWidget(self.tabWidgetContributors)


        self.horizontalLayout_3.addWidget(self.groupBoxContributorInformation)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonDone = QPushButton(GenerateSDSWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(GenerateSDSWidget)

        self.stackedWidgetDynamic.setCurrentIndex(0)
        self.tabWidgetOthers.setCurrentIndex(-1)
        self.tabWidgetContributors.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(GenerateSDSWidget)
    # setupUi

    def retranslateUi(self, GenerateSDSWidget):
        GenerateSDSWidget.setWindowTitle(QCoreApplication.translate("GenerateSDSWidget", u"GenerateSDS Widget", None))
        self.groupBoxBasicInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Basic information", None))
        self.labelDatasetTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Title:  ", None))
        self.labelDatasetAcknowledgments.setText(QCoreApplication.translate("GenerateSDSWidget", u"Acknowledgments:  ", None))
        self.labelDatasetSubtitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Subtitle:  ", None))
        self.labelDatasetLicense.setText(QCoreApplication.translate("GenerateSDSWidget", u"License:  ", None))
        self.comboBox__dataset_description__Type.setItemText(0, QCoreApplication.translate("GenerateSDSWidget", u"computational", None))
        self.comboBox__dataset_description__Type.setItemText(1, QCoreApplication.translate("GenerateSDSWidget", u"experimental", None))
        self.comboBox__dataset_description__Type.setItemText(2, QCoreApplication.translate("GenerateSDSWidget", u"device", None))

        self.pushButtonAddKeyword.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.labelDatasetKeywords.setText(QCoreApplication.translate("GenerateSDSWidget", u"Keywords:  ", None))
        self.labelDatasetType.setText(QCoreApplication.translate("GenerateSDSWidget", u"Type:  ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Funding information", None))
        self.labelDatasetFunding.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding:  ", None))
        self.labelAwardNumber_2.setText(QCoreApplication.translate("GenerateSDSWidget", u"Award number:  ", None))
        self.labelFundingConsortium_2.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding consortium:  ", None))
        self.labelFundingAgency.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding agency:  ", None))
        self.groupBoxStudyInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Study information", None))
        self.labelStudyTechnique.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study technique:", None))
        self.labelStudyApproach.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study approach:", None))
        self.labelStudyOrganSystem.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study organ system:", None))
        self.labelStudyDataCollection.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study data collection:", None))
        self.labelStudyCollectionTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study collection title:", None))
        self.pushButtonAddStudy_technique.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.labelStudyPurpose.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study purpose:", None))
        self.labelStudyPrimaryConclusion.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study primary conclusion:", None))
        self.groupBoxDynamic.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Dynamic Group Box", None))
        self.labelNumberOfSamples.setText(QCoreApplication.translate("GenerateSDSWidget", u"Number of samples:", None))
        self.pushButtonAddSubject.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add Subject", None))
        self.pushButtonRemoveSubject.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove Subject", None))
        self.labelNumberOfSubjects.setText(QCoreApplication.translate("GenerateSDSWidget", u"Number of subjects:", None))
        self.labelSpecies.setText(QCoreApplication.translate("GenerateSDSWidget", u"Species:  ", None))
        self.labelOrgan.setText(QCoreApplication.translate("GenerateSDSWidget", u"Organ:  ", None))
        self.groupBoxStandardsInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Standards information", None))
        self.labelConsortiumDataStandard.setText(QCoreApplication.translate("GenerateSDSWidget", u"Data standard:  ", None))
        self.labelMilestoneAchieved.setText(QCoreApplication.translate("GenerateSDSWidget", u"Data standard version:  ", None))
        self.groupBox.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Other information", None))
        self.pushButtonAddOther.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.pushButtonRemoveOther.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove", None))
        self.groupBoxContributorInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Contributor information", None))
        self.pushButtonAddContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.pushButtonRemoveContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove", None))
        self.pushButtonDone.setText(QCoreApplication.translate("GenerateSDSWidget", u"Done", None))
    # retranslateUi

