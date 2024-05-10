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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFormLayout,
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
        self.formLayout = QFormLayout(self.groupBoxBasicInformation)
        self.formLayout.setObjectName(u"formLayout")
        self.labelDatasetTitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetTitle.setObjectName(u"labelDatasetTitle")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelDatasetTitle)

        self.comboBox__dataset_description__Title = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Title.setObjectName(u"comboBox__dataset_description__Title")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Title.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox__dataset_description__Title)

        self.labelDatasetSubtitle = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetSubtitle.setObjectName(u"labelDatasetSubtitle")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelDatasetSubtitle)

        self.comboBox__dataset_description__Subtitle = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Subtitle.setObjectName(u"comboBox__dataset_description__Subtitle")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Subtitle.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Subtitle.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Subtitle.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox__dataset_description__Subtitle)

        self.labelDatasetKeywords = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetKeywords.setObjectName(u"labelDatasetKeywords")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.labelDatasetKeywords)

        self.comboBox__dataset_description__Keywords = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Keywords.setObjectName(u"comboBox__dataset_description__Keywords")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Keywords.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Keywords.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Keywords.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox__dataset_description__Keywords)

        self.labelDatasetFunding = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetFunding.setObjectName(u"labelDatasetFunding")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.labelDatasetFunding)

        self.comboBox__dataset_description__Funding = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Funding.setObjectName(u"comboBox__dataset_description__Funding")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Funding.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Funding.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Funding.setEditable(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox__dataset_description__Funding)

        self.labelDatasetAcknowledgments = QLabel(self.groupBoxBasicInformation)
        self.labelDatasetAcknowledgments.setObjectName(u"labelDatasetAcknowledgments")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.labelDatasetAcknowledgments)

        self.comboBox__dataset_description__Acknowledgments = QComboBox(self.groupBoxBasicInformation)
        self.comboBox__dataset_description__Acknowledgments.setObjectName(u"comboBox__dataset_description__Acknowledgments")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Acknowledgments.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Acknowledgments.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Acknowledgments.setEditable(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.comboBox__dataset_description__Acknowledgments)


        self.horizontalLayout_4.addWidget(self.groupBoxBasicInformation)

        self.groupBoxStudyInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxStudyInformation.setObjectName(u"groupBoxStudyInformation")
        self.formLayout_2 = QFormLayout(self.groupBoxStudyInformation)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.labelStudyPurpose = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPurpose.setObjectName(u"labelStudyPurpose")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.labelStudyPurpose)

        self.comboBox__dataset_description__Study_purpose = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_purpose.setObjectName(u"comboBox__dataset_description__Study_purpose")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_purpose.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_purpose.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_purpose.setEditable(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox__dataset_description__Study_purpose)

        self.labelStudyDataCollection = QLabel(self.groupBoxStudyInformation)
        self.labelStudyDataCollection.setObjectName(u"labelStudyDataCollection")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.labelStudyDataCollection)

        self.comboBox__dataset_description__Study_data_collection = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_data_collection.setObjectName(u"comboBox__dataset_description__Study_data_collection")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_data_collection.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_data_collection.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_data_collection.setEditable(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.comboBox__dataset_description__Study_data_collection)

        self.labelStudyPrimaryConclusion = QLabel(self.groupBoxStudyInformation)
        self.labelStudyPrimaryConclusion.setObjectName(u"labelStudyPrimaryConclusion")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.labelStudyPrimaryConclusion)

        self.labelStudyOrganSystem = QLabel(self.groupBoxStudyInformation)
        self.labelStudyOrganSystem.setObjectName(u"labelStudyOrganSystem")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.labelStudyOrganSystem)

        self.comboBox__dataset_description__Study_organ_system = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_organ_system.setObjectName(u"comboBox__dataset_description__Study_organ_system")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_organ_system.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_organ_system.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_organ_system.setEditable(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.comboBox__dataset_description__Study_organ_system)

        self.labelStudyApproach = QLabel(self.groupBoxStudyInformation)
        self.labelStudyApproach.setObjectName(u"labelStudyApproach")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.labelStudyApproach)

        self.labelStudyTechnique = QLabel(self.groupBoxStudyInformation)
        self.labelStudyTechnique.setObjectName(u"labelStudyTechnique")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.labelStudyTechnique)

        self.comboBox__dataset_description__Study_technique = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_technique.setObjectName(u"comboBox__dataset_description__Study_technique")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_technique.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_technique.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_technique.setEditable(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.comboBox__dataset_description__Study_technique)

        self.labelStudyCollectionTitle = QLabel(self.groupBoxStudyInformation)
        self.labelStudyCollectionTitle.setObjectName(u"labelStudyCollectionTitle")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.labelStudyCollectionTitle)

        self.comboBox__dataset_description__Study_collection_title = QComboBox(self.groupBoxStudyInformation)
        self.comboBox__dataset_description__Study_collection_title.setObjectName(u"comboBox__dataset_description__Study_collection_title")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Study_collection_title.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Study_collection_title.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Study_collection_title.setEditable(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.comboBox__dataset_description__Study_collection_title)

        self.plainTextEdit__dataset_description__Study_primary_conclusion = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_primary_conclusion.setObjectName(u"plainTextEdit__dataset_description__Study_primary_conclusion")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.plainTextEdit__dataset_description__Study_primary_conclusion)

        self.plainTextEdit__dataset_description__Study_approach = QPlainTextEdit(self.groupBoxStudyInformation)
        self.plainTextEdit__dataset_description__Study_approach.setObjectName(u"plainTextEdit__dataset_description__Study_approach")

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.plainTextEdit__dataset_description__Study_approach)


        self.horizontalLayout_4.addWidget(self.groupBoxStudyInformation)

        self.groupBoxManifest = QGroupBox(GenerateSDSWidget)
        self.groupBoxManifest.setObjectName(u"groupBoxManifest")
        self.formLayout_5 = QFormLayout(self.groupBoxManifest)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.labelSpecies = QLabel(self.groupBoxManifest)
        self.labelSpecies.setObjectName(u"labelSpecies")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.labelSpecies)

        self.comboBox__manifest__species = QComboBox(self.groupBoxManifest)
        self.comboBox__manifest__species.setObjectName(u"comboBox__manifest__species")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__species.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__species.setSizePolicy(sizePolicy)
        self.comboBox__manifest__species.setEditable(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.comboBox__manifest__species)

        self.labelOrgan = QLabel(self.groupBoxManifest)
        self.labelOrgan.setObjectName(u"labelOrgan")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.labelOrgan)

        self.comboBox__manifest__organ = QComboBox(self.groupBoxManifest)
        self.comboBox__manifest__organ.setObjectName(u"comboBox__manifest__organ")
        sizePolicy.setHeightForWidth(self.comboBox__manifest__organ.sizePolicy().hasHeightForWidth())
        self.comboBox__manifest__organ.setSizePolicy(sizePolicy)
        self.comboBox__manifest__organ.setEditable(True)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.comboBox__manifest__organ)


        self.horizontalLayout_4.addWidget(self.groupBoxManifest)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBoxSubmissionInformation = QGroupBox(GenerateSDSWidget)
        self.groupBoxSubmissionInformation.setObjectName(u"groupBoxSubmissionInformation")
        self.formLayout_4 = QFormLayout(self.groupBoxSubmissionInformation)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.labelConsortiumDataStandard = QLabel(self.groupBoxSubmissionInformation)
        self.labelConsortiumDataStandard.setObjectName(u"labelConsortiumDataStandard")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.labelConsortiumDataStandard)

        self.comboBox__submission__Consortium_data_standard = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Consortium_data_standard.setObjectName(u"comboBox__submission__Consortium_data_standard")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Consortium_data_standard.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Consortium_data_standard.setSizePolicy(sizePolicy)
        self.comboBox__submission__Consortium_data_standard.setEditable(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBox__submission__Consortium_data_standard)

        self.labelFundingConsortium = QLabel(self.groupBoxSubmissionInformation)
        self.labelFundingConsortium.setObjectName(u"labelFundingConsortium")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.labelFundingConsortium)

        self.comboBox__submission__Funding_consortium = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Funding_consortium.setObjectName(u"comboBox__submission__Funding_consortium")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Funding_consortium.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Funding_consortium.setSizePolicy(sizePolicy)
        self.comboBox__submission__Funding_consortium.setEditable(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBox__submission__Funding_consortium)

        self.labelAwardNumber = QLabel(self.groupBoxSubmissionInformation)
        self.labelAwardNumber.setObjectName(u"labelAwardNumber")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.labelAwardNumber)

        self.comboBox__submission__Award_number = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Award_number.setObjectName(u"comboBox__submission__Award_number")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Award_number.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Award_number.setSizePolicy(sizePolicy)
        self.comboBox__submission__Award_number.setEditable(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.comboBox__submission__Award_number)

        self.labelMilestoneAchieved = QLabel(self.groupBoxSubmissionInformation)
        self.labelMilestoneAchieved.setObjectName(u"labelMilestoneAchieved")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.labelMilestoneAchieved)

        self.comboBox__submission__Milestone_achieved = QComboBox(self.groupBoxSubmissionInformation)
        self.comboBox__submission__Milestone_achieved.setObjectName(u"comboBox__submission__Milestone_achieved")
        sizePolicy.setHeightForWidth(self.comboBox__submission__Milestone_achieved.sizePolicy().hasHeightForWidth())
        self.comboBox__submission__Milestone_achieved.setSizePolicy(sizePolicy)
        self.comboBox__submission__Milestone_achieved.setEditable(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.comboBox__submission__Milestone_achieved)

        self.labelMilestoneCompletionDate = QLabel(self.groupBoxSubmissionInformation)
        self.labelMilestoneCompletionDate.setObjectName(u"labelMilestoneCompletionDate")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.labelMilestoneCompletionDate)

        self.calendarWidget__submission__Milestone_completion_date = QCalendarWidget(self.groupBoxSubmissionInformation)
        self.calendarWidget__submission__Milestone_completion_date.setObjectName(u"calendarWidget__submission__Milestone_completion_date")

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.calendarWidget__submission__Milestone_completion_date)


        self.horizontalLayout_3.addWidget(self.groupBoxSubmissionInformation)

        self.groupBox = QGroupBox(GenerateSDSWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_3 = QFormLayout(self.groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.labelIdentifierDescription = QLabel(self.groupBox)
        self.labelIdentifierDescription.setObjectName(u"labelIdentifierDescription")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.labelIdentifierDescription)

        self.comboBox__dataset_description__Identifier_description = QComboBox(self.groupBox)
        self.comboBox__dataset_description__Identifier_description.setObjectName(u"comboBox__dataset_description__Identifier_description")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier_description.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier_description.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier_description.setEditable(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox__dataset_description__Identifier_description)

        self.labelRelationType = QLabel(self.groupBox)
        self.labelRelationType.setObjectName(u"labelRelationType")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.labelRelationType)

        self.comboBox__dataset_description__Relation_type = QComboBox(self.groupBox)
        self.comboBox__dataset_description__Relation_type.setObjectName(u"comboBox__dataset_description__Relation_type")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Relation_type.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Relation_type.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Relation_type.setEditable(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.comboBox__dataset_description__Relation_type)

        self.labelIdentifier = QLabel(self.groupBox)
        self.labelIdentifier.setObjectName(u"labelIdentifier")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.labelIdentifier)

        self.comboBox__dataset_description__Identifier = QComboBox(self.groupBox)
        self.comboBox__dataset_description__Identifier.setObjectName(u"comboBox__dataset_description__Identifier")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier.setEditable(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.comboBox__dataset_description__Identifier)

        self.labelIdentifierType = QLabel(self.groupBox)
        self.labelIdentifierType.setObjectName(u"labelIdentifierType")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.labelIdentifierType)

        self.comboBox__dataset_description__Identifier_type = QComboBox(self.groupBox)
        self.comboBox__dataset_description__Identifier_type.setObjectName(u"comboBox__dataset_description__Identifier_type")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier_type.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier_type.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier_type.setEditable(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.comboBox__dataset_description__Identifier_type)


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

        self.tabWidgetContributors.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(GenerateSDSWidget)
    # setupUi

    def retranslateUi(self, GenerateSDSWidget):
        GenerateSDSWidget.setWindowTitle(QCoreApplication.translate("GenerateSDSWidget", u"GenerateSDS Widget", None))
        self.groupBoxBasicInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Basic information", None))
        self.labelDatasetTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Title:  ", None))
        self.labelDatasetSubtitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Subtitle:  ", None))
        self.labelDatasetKeywords.setText(QCoreApplication.translate("GenerateSDSWidget", u"Keywords:  ", None))
        self.labelDatasetFunding.setText(QCoreApplication.translate("GenerateSDSWidget", u"Funding:  ", None))
        self.labelDatasetAcknowledgments.setText(QCoreApplication.translate("GenerateSDSWidget", u"Acknowledgments:  ", None))
        self.groupBoxStudyInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Study information", None))
        self.labelStudyPurpose.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study purpose:", None))
        self.labelStudyDataCollection.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study data collection:", None))
        self.labelStudyPrimaryConclusion.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study primary conclusion:", None))
        self.labelStudyOrganSystem.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study organ system:", None))
        self.labelStudyApproach.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study approach:", None))
        self.labelStudyTechnique.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study technique:", None))
        self.labelStudyCollectionTitle.setText(QCoreApplication.translate("GenerateSDSWidget", u"Study collection title:", None))
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
        self.labelIdentifierDescription.setText(QCoreApplication.translate("GenerateSDSWidget", u"Identifier description:", None))
        self.labelRelationType.setText(QCoreApplication.translate("GenerateSDSWidget", u"Relation type:", None))
        self.labelIdentifier.setText(QCoreApplication.translate("GenerateSDSWidget", u"Identifier:", None))
        self.labelIdentifierType.setText(QCoreApplication.translate("GenerateSDSWidget", u"Identifier type:", None))
        self.groupBoxContributorInformation.setTitle(QCoreApplication.translate("GenerateSDSWidget", u"Contributor information", None))
        self.pushButtonAddContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Add", None))
        self.pushButtonRemoveContributor.setText(QCoreApplication.translate("GenerateSDSWidget", u"Remove", None))
        self.pushButtonDone.setText(QCoreApplication.translate("GenerateSDSWidget", u"Done", None))
    # retranslateUi

