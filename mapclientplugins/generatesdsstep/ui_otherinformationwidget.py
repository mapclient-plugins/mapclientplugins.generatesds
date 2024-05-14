# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otherinformationwidget.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_OtherInformation(object):
    def setupUi(self, OtherInformation):
        if not OtherInformation.objectName():
            OtherInformation.setObjectName(u"OtherInformation")
        OtherInformation.resize(400, 300)
        self.gridLayout = QGridLayout(OtherInformation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox__dataset_description__Identifier_description = QComboBox(OtherInformation)
        self.comboBox__dataset_description__Identifier_description.setObjectName(u"comboBox__dataset_description__Identifier_description")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier_description.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier_description.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier_description.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Identifier_description.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Identifier_description, 0, 1, 1, 1)

        self.comboBox__dataset_description__Relation_type = QComboBox(OtherInformation)
        self.comboBox__dataset_description__Relation_type.setObjectName(u"comboBox__dataset_description__Relation_type")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Relation_type.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Relation_type.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Relation_type.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Relation_type.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Relation_type, 1, 1, 1, 1)

        self.labelIdentifier = QLabel(OtherInformation)
        self.labelIdentifier.setObjectName(u"labelIdentifier")
        self.labelIdentifier.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelIdentifier, 2, 0, 1, 1)

        self.labelIdentifierType = QLabel(OtherInformation)
        self.labelIdentifierType.setObjectName(u"labelIdentifierType")
        self.labelIdentifierType.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelIdentifierType, 3, 0, 1, 1)

        self.labelRelationType = QLabel(OtherInformation)
        self.labelRelationType.setObjectName(u"labelRelationType")
        self.labelRelationType.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelRelationType, 1, 0, 1, 1)

        self.comboBox__dataset_description__Identifier = QComboBox(OtherInformation)
        self.comboBox__dataset_description__Identifier.setObjectName(u"comboBox__dataset_description__Identifier")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Identifier.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Identifier, 2, 1, 1, 1)

        self.labelIdentifierDescription = QLabel(OtherInformation)
        self.labelIdentifierDescription.setObjectName(u"labelIdentifierDescription")
        self.labelIdentifierDescription.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelIdentifierDescription, 0, 0, 1, 1)

        self.comboBox__dataset_description__Identifier_type = QComboBox(OtherInformation)
        self.comboBox__dataset_description__Identifier_type.setObjectName(u"comboBox__dataset_description__Identifier_type")
        sizePolicy.setHeightForWidth(self.comboBox__dataset_description__Identifier_type.sizePolicy().hasHeightForWidth())
        self.comboBox__dataset_description__Identifier_type.setSizePolicy(sizePolicy)
        self.comboBox__dataset_description__Identifier_type.setMinimumSize(QSize(127, 0))
        self.comboBox__dataset_description__Identifier_type.setEditable(True)

        self.gridLayout.addWidget(self.comboBox__dataset_description__Identifier_type, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)


        self.retranslateUi(OtherInformation)

        QMetaObject.connectSlotsByName(OtherInformation)
    # setupUi

    def retranslateUi(self, OtherInformation):
        OtherInformation.setWindowTitle(QCoreApplication.translate("OtherInformation", u"OtherInformation", None))
        self.labelIdentifier.setText(QCoreApplication.translate("OtherInformation", u"Identifier:", None))
        self.labelIdentifierType.setText(QCoreApplication.translate("OtherInformation", u"Identifier type:", None))
        self.labelRelationType.setText(QCoreApplication.translate("OtherInformation", u"Relation type:", None))
        self.labelIdentifierDescription.setText(QCoreApplication.translate("OtherInformation", u"Identifier description:", None))
    # retranslateUi

