# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_image_dialogqWCgSi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QDialogButtonBox,
                               QHBoxLayout, QLabel, QLayout, QSizePolicy,
                               QVBoxLayout)


class Ui_Image_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 241)
        font = QFont()
        font.setFamilies([u"Verdana"])
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QIcon()
        icon.addFile(u"resources/info_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QLabel#nameLabel, #typeLabel, #commentLabel, #widthLabel, #heightLabel{\n"
                             "	color: rgb(231, 34, 88);\n"
                             "	font: 10pt \"Verdana\";\n"
                             "}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.nameLabel = QLabel(Dialog)
        self.nameLabel.setObjectName(u"nameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.nameLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.nameLabel)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.typeLabel = QLabel(Dialog)
        self.typeLabel.setObjectName(u"typeLabel")
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.typeLabel)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.widthLabel = QLabel(Dialog)
        self.widthLabel.setObjectName(u"widthLabel")
        sizePolicy.setHeightForWidth(self.widthLabel.sizePolicy().hasHeightForWidth())
        self.widthLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.widthLabel)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.heightLabel = QLabel(Dialog)
        self.heightLabel.setObjectName(u"heightLabel")
        sizePolicy.setHeightForWidth(self.heightLabel.sizePolicy().hasHeightForWidth())
        self.heightLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.heightLabel)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Image Infos", None))
        self.label_2.setText(QCoreApplication.translate("Dialog",
                                                        u"<html><head/><body><p><span style=\" color:#191a2b;\">Name:</span></p></body></html>",
                                                        None))
        self.nameLabel.setText(
            QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog",
                                                        u"<html><head/><body><p><span style=\" color:#191a2b;\">Format:</span></p></body></html>",
                                                        None))
        self.typeLabel.setText(
            QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Dialog",
                                                        u"<html><head/><body><p><span style=\" color:#191a2b;\">Width:</span></p></body></html>",
                                                        None))
        self.widthLabel.setText(
            QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Dialog",
                                                         u"<html><head/><body><p><span style=\" color:#191a2b;\">Height:</span></p></body></html>",
                                                         None))
        self.heightLabel.setText(
            QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi
