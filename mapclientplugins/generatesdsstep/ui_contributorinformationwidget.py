# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contributorinformationwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_ContributorInformation(object):
    def setupUi(self, ContributorInformation):
        if not ContributorInformation.objectName():
            ContributorInformation.setObjectName(u"ContributorInformation")
        ContributorInformation.resize(400, 300)
        self.gridLayout = QGridLayout(ContributorInformation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(ContributorInformation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBox__dataset_description__Contributor_ORCiD = QComboBox(ContributorInformation)
        self.comboBox__dataset_description__Contributor_ORCiD.setObjectName(u"comboBox__dataset_description__Contributor_ORCiD")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Contributor_ORCiD.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Contributor_ORCiD.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Contributor_ORCiD.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Contributor_ORCiD.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Contributor_ORCiD, 1, 1, 1, 1)

        self.comboBox__dataset_description__Contributor_role = QComboBox(ContributorInformation)
        self.comboBox__dataset_description__Contributor_role.setObjectName(u"comboBox__dataset_description__Contributor_role")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Contributor_role.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Contributor_role.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Contributor_role.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Contributor_role.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Contributor_role, 3, 1, 1, 1)

        self.label_4 = QLabel(ContributorInformation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label = QLabel(ContributorInformation)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(ContributorInformation)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBox__dataset_description__Contributor_affiliation = QComboBox(ContributorInformation)
        self.comboBox__dataset_description__Contributor_affiliation.setObjectName(u"comboBox__dataset_description__Contributor_affiliation")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Contributor_affiliation.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Contributor_affiliation.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Contributor_affiliation.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Contributor_affiliation.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Contributor_affiliation, 2, 1, 1, 1)

        self.comboBox__dataset_description__Contributor_name = QComboBox(ContributorInformation)
        self.comboBox__dataset_description__Contributor_name.setObjectName(u"comboBox__dataset_description__Contributor_name")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Contributor_name.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Contributor_name.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Contributor_name.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Contributor_name.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Contributor_name, 0, 1, 1, 1)

        self.widgetSpacer = QWidget(ContributorInformation)
        self.widgetSpacer.setObjectName(u"widgetSpacer")

        self.gridLayout.addWidget(self.widgetSpacer, 4, 1, 1, 1)


        self.retranslateUi(ContributorInformation)

        QMetaObject.connectSlotsByName(ContributorInformation)
    # setupUi

    def retranslateUi(self, ContributorInformation):
        ContributorInformation.setWindowTitle(QCoreApplication.translate("ContributorInformation", u"ContributorInformation", None))
        self.label_3.setText(QCoreApplication.translate("ContributorInformation", u"Affiliation:", None))
        self.label_4.setText(QCoreApplication.translate("ContributorInformation", u"Role:", None))
        self.label.setText(QCoreApplication.translate("ContributorInformation", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("ContributorInformation", u"ORCiD:", None))
    # retranslateUi

