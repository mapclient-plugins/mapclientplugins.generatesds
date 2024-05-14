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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_GenerateSDSWidget(object):
    def setupUi(self, GenerateSDSWidget):
        if not GenerateSDSWidget.objectName():
            GenerateSDSWidget.setObjectName(u"GenerateSDSWidget")
        GenerateSDSWidget.resize(1038, 859)
        self.verticalLayout_2 = QVBoxLayout(GenerateSDSWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBoxBasicInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxBasicInformation.setObjectName(u"groupBoxBasicInformation")
        self.gridLayout = QGridLayout(self.groupBoxBasicInformation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelDatasetKeywords = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetKeywords.setObjectName(u"labelDatasetKeywords")
        self.labelDatasetKeywords.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetKeywords, 2, 0, 1, 1)

        self.comboBox__dataset_description__Acknowledgments = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Acknowledgments.setObjectName(u"comboBox__dataset_description__Acknowledgments")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Acknowledgments.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Acknowledgments.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Acknowledgments.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Acknowledgments.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Acknowledgments, 4, 1, 1, 1)

        self.comboBox__dataset_description__Funding = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Funding.setObjectName(u"comboBox__dataset_description__Funding")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Funding.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Funding.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Funding.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Funding.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Funding, 3, 1, 1, 1)

        self.labelDatasetSubtitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetSubtitle.setObjectName(u"labelDatasetSubtitle")
        self.labelDatasetSubtitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetSubtitle, 1, 0, 1, 1)

        self.labelDatasetAcknowledgments = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetAcknowledgments.setObjectName(u"labelDatasetAcknowledgments")
        self.labelDatasetAcknowledgments.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetAcknowledgments, 4, 0, 1, 1)

        self.labelDatasetTitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetTitle.setObjectName(u"labelDatasetTitle")
        self.labelDatasetTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetTitle, 0, 0, 1, 1)

        self.comboBox__dataset_description__Keywords = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Keywords.setObjectName(u"comboBox__dataset_description__Keywords")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Keywords.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Keywords.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Keywords.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Keywords.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Keywords, 2, 1, 1, 1)

        self.labelDatasetFunding = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetFunding.setObjectName(u"labelDatasetFunding")
        self.labelDatasetFunding.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelDatasetFunding, 3, 0, 1, 1)

        self.comboBox__dataset_description__Title = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Title.setObjectName(u"comboBox__dataset_description__Title")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Title.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Title.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Title, 0, 1, 1, 1)

        self.comboBox__dataset_description__Subtitle = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Subtitle.setObjectName(u"comboBox__dataset_description__Subtitle")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Subtitle.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Subtitle.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Subtitle.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Subtitle.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Subtitle, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupBoxBasicInformation)

        self.groupBoxStudyInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxStudyInformation.setObjectName(u"groupBoxStudyInformation")
        self.gridLayout_2 = QGridLayout(self.groupBoxStudyInformation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox__dataset_description__Study_collection_title = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_collection_title.setObjectName(u"comboBox__dataset_description__Study_collection_title")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_collection_title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_collection_title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_collection_title.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_collection_title.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_collection_title, 6, 1, 1, 1)

        self.labelStudyApproach = QLabel(self.groupBoxStudyInformation)
        self.labelStudyApproach.setObjectName(u"labelStudyApproach")
        self.labelStudyApproach.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyApproach, 4, 0, 1, 1)

        self.comboBox__dataset_description__Study_approach = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_approach.setObjectName(u"comboBox__dataset_description__Study_approach")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_approach.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_approach.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_approach.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_approach.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_approach, 4, 1, 1, 1)

        self.labelStudyOrganSystem = QLabel(self.groupBoxStudyInformation)
        self.labelStudyOrganSystem.setObjectName(u"labelStudyOrganSystem")
        self.labelStudyOrganSystem.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyOrganSystem, 3, 0, 1, 1)

        self.comboBox__dataset_description__Study_organ_system = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_organ_system.setObjectName(u"comboBox__dataset_description__Study_organ_system")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_organ_system.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_organ_system.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_organ_system.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_organ_system.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_organ_system, 3, 1, 1, 1)

        self.labelStudyTechnique = QLabel(self.groupBoxStudyInformation)
        self.labelStudyTechnique.setObjectName(u"labelStudyTechnique")
        self.labelStudyTechnique.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyTechnique, 5, 0, 1, 1)

        self.labelStudyPurpose = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPurpose.setObjectName(u"labelStudyPurpose")
        self.labelStudyPurpose.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyPurpose, 0, 0, 1, 1)

        self.labelStudyPrimaryConclusion = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPrimaryConclusion.setObjectName(u"labelStudyPrimaryConclusion")
        self.labelStudyPrimaryConclusion.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.labelStudyPrimaryConclusion, 2, 0, 1, 1)

        self.plainTextEdit__dataset_description__Study_primary_conclusion = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_primary_conclusion.setObjectName(u"plainTextEdit__dataset_description__Study_primary_conclusion")

        self.gridLayout_2.addWidget(self.plainTextEdit__dataset_description__Study_primary_conclusion, 2, 1, 1, 1)

        self.plainTextEdit__dataset_description__Study_data_collection = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_data_collection.setObjectName(u"plainTextEdit__dataset_description__Study_data_collection")

        self.gridLayout_2.addWidget(self.plainTextEdit__dataset_description__Study_data_collection, 1, 1, 1, 1)

        self.comboBox__dataset_description__Study_purpose = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_purpose.setObjectName(u"comboBox__dataset_description__Study_purpose")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_purpose.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_purpose.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_purpose.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_purpose.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_purpose, 0, 1, 1, 1)

        self.labelStudyCollectionTitle = QLabel(self.groupBoxStudyInformation)
        self.labelStudyCollectionTitle.setObjectName(u"labelStudyCollectionTitle")
        self.labelStudyCollectionTitle.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.labelStudyCollectionTitle, 6, 0, 1, 1)

        self.comboBox__dataset_description__Study_technique = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_technique.setObjectName(u"comboBox__dataset_description__Study_technique")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_technique.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_technique.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_technique.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Study_technique.setEditable(True)

        self.gridLayout_2.addWidget(self.comboBox__dataset_description__Study_technique, 5, 1, 1, 1)

        self.labelStudyDataCollection = QLabel(self.groupBoxStudyInformation)
        self.labelStudyDataCollection.setObjectName(u"labelStudyDataCollection")
        self.labelStudyDataCollection.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)

        self.gridLayout_2.addWidget(self.labelStudyDataCollection, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupBoxStudyInformation)

        self.groupBoxManifest = QGroupBox(GenerateSDSWidget)
        self.groupBoxManifest.setObjectName(u"groupBoxManifest")
        self.gridLayout_3 = QGridLayout(self.groupBoxManifest)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelSpecies = QLabel(self.groupBoxManifest)
        self.labelSpecies.setObjectName(u"labelSpecies")
        self.labelSpecies.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelSpecies, 0, 0, 1, 1)

        self.comboBox__manifest__species = QComboBox(self.groupBoxManifest)
        self.comboBox__manifest__species.setObjectName(u"comboBox__manifest__species")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__species.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__species.setSizePolicy(sizePolicy)
        self.comboBox__manifest__species.setMinimumSize(QSize(127, 0))
        self.comboBox__manifest__species.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__manifest__species, 0, 1, 1, 1)

        self.labelOrgan = QLabel(self.groupBoxManifest)
        self.labelOrgan.setObjectName(u"labelOrgan")
        self.labelOrgan.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelOrgan, 1, 0, 1, 1)

        self.comboBox__manifest__organ = QComboBox(self.groupBoxManifest)
        self.comboBox__manifest__organ.setObjectName(u"comboBox__manifest__organ")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__organ.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__organ.setSizePolicy(sizePolicy)
        self.comboBox__manifest__organ.setMinimumSize(QSize(127, 0))
        self.comboBox__manifest__organ.setEditable(True)

        self.gridLayout_3.addWidget(self.comboBox__manifest__organ, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.groupBoxManifest)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBoxSubmissionInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxSubmissionInformation.setObjectName(u"groupBoxSubmissionInformation")
        self.gridLayout_4 = QGridLayout(self.groupBoxSubmissionInformation)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelConsortiumDataStandard = QLabel(self.groupBoxSubmissionInformation)
        self.labelConsortiumDataStandard.setObjectName(u"labelConsortiumDataStandard")
        self.labelConsortiumDataStandard.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelConsortiumDataStandard, 0, 0, 1, 1)

        self.comboBox__submission__Consortium_data_standard = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Consortium_data_standard.setObjectName(u"comboBox__submission__Consortium_data_standard")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Consortium_data_standard.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Consortium_data_standard.setSizePolicy(sizePolicy)
        self.comboBox__submission__Consortium_data_standard.setMinimumSize(QSize(127, 0))
        self.comboBox__submission__Consortium_data_standard.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__submission__Consortium_data_standard, 0, 1, 1, 1)

        self.labelFundingConsortium = QLabel(self.groupBoxSubmissionInformation)
        self.labelFundingConsortium.setObjectName(u"labelFundingConsortium")
        self.labelFundingConsortium.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelFundingConsortium, 1, 0, 1, 1)

        self.comboBox__submission__Funding_consortium = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Funding_consortium.setObjectName(u"comboBox__submission__Funding_consortium")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Funding_consortium.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Funding_consortium.setSizePolicy(sizePolicy)
        self.comboBox__submission__Funding_consortium.setMinimumSize(QSize(127, 0))
        self.comboBox__submission__Funding_consortium.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__submission__Funding_consortium, 1, 1, 1, 1)

        self.labelAwardNumber = QLabel(self.groupBoxSubmissionInformation)
        self.labelAwardNumber.setObjectName(u"labelAwardNumber")
        self.labelAwardNumber.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelAwardNumber, 2, 0, 1, 1)

        self.comboBox__submission__Award_number = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Award_number.setObjectName(u"comboBox__submission__Award_number")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Award_number.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Award_number.setSizePolicy(sizePolicy)
        self.comboBox__submission__Award_number.setMinimumSize(QSize(127, 0))
        self.comboBox__submission__Award_number.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__submission__Award_number, 2, 1, 1, 1)

        self.labelMilestoneAchieved = QLabel(self.groupBoxSubmissionInformation)
        self.labelMilestoneAchieved.setObjectName(u"labelMilestoneAchieved")
        self.labelMilestoneAchieved.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelMilestoneAchieved, 3, 0, 1, 1)

        self.comboBox__submission__Milestone_achieved = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Milestone_achieved.setObjectName(u"comboBox__submission__Milestone_achieved")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Milestone_achieved.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Milestone_achieved.setSizePolicy(sizePolicy)
        self.comboBox__submission__Milestone_achieved.setMinimumSize(QSize(127, 0))
        self.comboBox__submission__Milestone_achieved.setEditable(True)

        self.gridLayout_4.addWidget(self.comboBox__submission__Milestone_achieved, 3, 1, 1, 1)

        self.labelMilestoneCompletionDate = QLabel(self.groupBoxSubmissionInformation)
        self.labelMilestoneCompletionDate.setObjectName(u"labelMilestoneCompletionDate")
        self.labelMilestoneCompletionDate.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.labelMilestoneCompletionDate, 4, 0, 1, 1)

        self.calendarWidget__submission__Milestone_completion_date = QCalendarWidget(self.groupBoxSubmissionInformation)
        self.calendarWidget__submission__Milestone_completion_date.setObjectName(u"calendarWidget__submission__Milestone_completion_date")

        self.gridLayout_4.addWidget(self.calendarWidget__submission__Milestone_completion_date, 4, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBoxSubmissionInformation)

        self.groupBox = QGroupBox(GenerateSDSWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonDone = QPushButton(GenerateSDSWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(GenerateSDSWidget)

        self.tabWidgetOthers.setCurrentIndex(-1)
        self.tabWidgetContributors.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(GenerateSDSWidget)
    # setupUi

    def retranslateUi(self, GenerateSDSWidget):
        GenerateSDSWidget.setWindowTitle(QCoreApplication.translate("GenerateSDSWidget", u"GenerateSDS Widget", None))
        self.groupBoxBasicInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Basic information", None))
        self.labelDatasetKeywords.setText(QCoreApplication.translate("GenerateSDSWidget", u"Keywords:  ", None))
        self.labelDatasetSubtitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Subtitle:  ", None))
        self.labelDatasetAcknowledgments.setText(QCoreApplication.translate("GenerateSDSWidget", u"Acknowledgments:  ", None))
        self.labelDatasetTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Title:  ", None))
        self.labelDatasetFunding.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding:  ", None))
        self.groupBoxStudyInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Study information", None))
        self.labelStudyApproach.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study approach:", None))
        self.labelStudyOrganSystem.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study organ system:", None))
        self.labelStudyTechnique.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study technique:", None))
        self.labelStudyPurpose.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study purpose:", None))
        self.labelStudyPrimaryConclusion.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study primary conclusion:", None))
        self.labelStudyCollectionTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study collection title:", None))
        self.labelStudyDataCollection.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study data collection:", None))
        self.groupBoxManifest.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Scaffold manifest", None))
        self.labelSpecies.setText(QCoreApplication.translate("GenerateSDSWidget", u"Species:  ", None))
        self.labelOrgan.setText(QCoreApplication.translate("GenerateSDSWidget", u"Organ:  ", None))
        self.groupBoxSubmissionInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Submission information", None))
        self.labelConsortiumDataStandard.setText(QCoreApplication.translate("GenerateSDSWidget", u"Consortium data standard:", None))
        self.labelFundingConsortium.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding consortium:", None))
        self.labelAwardNumber.setText(QCoreApplication.translate("GenerateSDSWidget", u"Award number:  ", None))
        self.labelMilestoneAchieved.setText(QCoreApplication.translate("GenerateSDSWidget", u"Milestone achieved:  ", None))
        self.labelMilestoneCompletionDate.setText(QCoreApplication.translate("GenerateSDSWidget", u"Milestone completion date:  ", None))
        self.groupBox.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Other information", None))
        self.pushButtonAddOther.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.pushButtonRemoveOther.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove", None))
        self.groupBoxContributorInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Contributor information", None))
        self.pushButtonAddContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.pushButtonRemoveContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove", None))
        self.pushButtonDone.setText(QCoreApplication.translate("GenerateSDSWidget", u"Done", None))
    # retranslateUi

