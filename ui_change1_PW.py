# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change1_PW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(405, 264)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 121, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 61, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 150, 71, 31))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 30, 221, 31))
        self.lineEdit.setEchoMode(QLineEdit.Password)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(150, 90, 221, 31))
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(150, 150, 221, 31))
        self.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 210, 131, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u66f4\u6539\u5bc6\u7801", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u5f53\u524d\u6587\u4ef6\u7684\u5bc6\u7801\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u65b0\u5bc6\u7801\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u65b0\u5bc6\u7801\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi

