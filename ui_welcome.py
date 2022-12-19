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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 470)
        MainWindow.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.welcomeL = QLabel(self.centralwidget)
        self.welcomeL.setObjectName(u"welcomeL")
        font = QFont()
        font.setFamilies([u"Bookman Old Style"])
        font.setPointSize(36)
        font.setBold(True)
        self.welcomeL.setFont(font)
        self.welcomeL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.welcomeL, 1, 1, 1, 1)

        self.login = QPushButton(self.centralwidget)
        self.login.setObjectName(u"login")

        self.gridLayout.addWidget(self.login, 3, 1, 1, 1)

        self.createacc = QPushButton(self.centralwidget)
        self.createacc.setObjectName(u"createacc")
        self.createacc.setSizeIncrement(QSize(0, 0))
        self.createacc.setBaseSize(QSize(1024, 768))

        self.gridLayout.addWidget(self.createacc, 4, 1, 1, 1)

        self.signL = QLabel(self.centralwidget)
        self.signL.setObjectName(u"signL")
        font1 = QFont()
        font1.setPointSize(12)
        self.signL.setFont(font1)
        self.signL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.signL, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.welcomeL.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Welcome </p></body></html>", None))
        self.login.setText(QCoreApplication.translate("MainWindow", u"Login ", None))
        self.createacc.setText(QCoreApplication.translate("MainWindow", u"Creat a new account", None))
        self.signL.setText(QCoreApplication.translate("MainWindow", u"Sign in or make a new account", None))
    # retranslateUi

