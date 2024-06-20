# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(526, 224)
        MainWindow.setMinimumSize(QSize(526, 224))
        MainWindow.setMaximumSize(QSize(550, 250))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 120, 231, 31))
        self.lineEdit_2.setMaxLength(3200)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 160, 111, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 81, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 60, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 40, 261, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 40, 161, 31))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(270, 90, 241, 111))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u52a0\u5bc61.0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u63a7\u5bc6\u7801\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u6587\u4ef6\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5bc6\u7801\u6587\u4ef6...", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600; color:#0000ff;\">\u5bc6\u7801\u7ba1\u7406\u5668\uff1a</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ff0000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#5500ff;\">\u4ecb\u7ecd\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  1. \u7ba1\u7406\u5404\u7c7b\u8d26\u53f7\u5bc6\u7801\uff0c\u8f6f\u4ef6\u4e0d\u8054\u7f51\uff0c\u76f4\u63a5\u52a0\u5bc6\u5b58\u50a8\u5728\u672c\u5730\uff0c\u65e0\u9700\u62c5\u5fc3\u5bc6\u7801\u88ab\u4e0a\u4f20\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  2. \u4e3a\u4e86\u65b9\u4fbf\u53ef\u4ee5\u5c06\u6587\u4ef6\u653e\u5728\u81ea\u5df1\u7f51\u76d8\u548c\u90ae\u7bb1\uff0c\u9700\u8981\u7528\u65f6\u968f\u65f6\u4e0b\u8f7d\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  3. \u6587\u4ef6\u52a0\u5bc6\u5b58\u50a8\uff0c\u5373\u4f7f\u522b\u4eba\u62ff\u5230\u4e5f\u65e0\u6cd5\u67e5\u770b\u91cc\u9762\u5185\u5bb9\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  4. \u8f6f\u4ef6\u4e0d\u8054\u7f51\u4e5f\u65e0\u9700\u66f4\u65b0,\u53ef\u4ee5\u4e00\u76f4\u4f7f\u7528\u3002</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ff0000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#5500ff;\">\u4f7f\u7528\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#00ff00;\">  </span><span style=\" color:#ff0000;\">1. \u4e0d\u9009\u62e9\u52a0\u5bc6\u6587\u4ef6\uff0c\u76f4\u63a5\u8f93\u5165\u4e3b\u63a7\u5bc6\u7801\uff0c\u4f1a\u65b0\u5efa\u4e00\u4e2a\u7a7a\u7684\u52a0\u5bc6\u6587\u4ef6\u3002</span></p>\n"
"<p style=\" margin-top:0px; ma"
                        "rgin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  2. \u589e\u52a0\u6216\u4fee\u6539\u8d26\u53f7\u90fd\u9700\u8981\u70b9\u51fb\u786e\u8ba4\u3002\u5220\u9664\u4f1a\u76f4\u63a5\u5220\u9664\u5f53\u524d\u9009\u4e2d\u7684\u9879\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  3. \u4f7f\u7528\u4e2d\u9047\u5230BUG\uff0c\u8bf7\u81ea\u5df1\u514b\u670d\uff0c\u767d\u5ad6\u8fd8\u8981\u4ec0\u4e48\u81ea\u884c\u8f66\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ff0000;\">  4. \u4e25\u91cdbug\uff0c\u5728pride.ysepan.com\u7559\u8a00\u63d0\u4ea4\u3002</span></p></body></html>", None))
    # retranslateUi

