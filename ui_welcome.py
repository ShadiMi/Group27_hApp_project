# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 768)
        MainWindow.setStyleSheet(u"QFrame\n"
"{\n"
"background:rgba(6, 16, 28, 0.8);\n"
"border-radius:15px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(440, 190, 471, 321))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.createacc = QPushButton(self.frame)
        self.createacc.setObjectName(u"createacc")
        self.createacc.setGeometry(QRect(40, 210, 361, 31))
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setPointSize(12)
        self.createacc.setFont(font)
        self.createacc.setStyleSheet(u"QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}\n"
"QPushButton\n"
"\n"
"{\n"
"background:skyblue;\n"
"}")
        self.signL = QLabel(self.frame)
        self.signL.setObjectName(u"signL")
        self.signL.setGeometry(QRect(107, 120, 231, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.signL.setFont(font1)
        self.signL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:rgb(194, 194, 194)")
        self.welcomeL = QLabel(self.frame)
        self.welcomeL.setObjectName(u"welcomeL")
        self.welcomeL.setGeometry(QRect(10, 20, 461, 56))
        font2 = QFont()
        font2.setFamilies([u"Bookman Old Style"])
        font2.setPointSize(36)
        font2.setBold(True)
        self.welcomeL.setFont(font2)
        self.welcomeL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:rgb(194, 194, 194)")
        self.login = QPushButton(self.frame)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(40, 170, 361, 31))
        self.login.setFont(font)
        self.login.setStyleSheet(u"QPushButton\n"
"{\n"
"color:white;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:10px;\n"
"background:#49ebff;\n"
"}\n"
"QPushButton\n"
"\n"
"{\n"
"background:skyblue;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.createacc.setText(QCoreApplication.translate("MainWindow", u"Signup", None))
        self.signL.setText(QCoreApplication.translate("MainWindow", u"Sign in or make a new account", None))
        self.welcomeL.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome to hApp</p></body></html>", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

