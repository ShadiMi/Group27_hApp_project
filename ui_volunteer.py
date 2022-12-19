# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'volunteer.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLCDNumber, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

class Ui_volunteerprofile(object):
    def setupUi(self, volunteerprofile):
        if not volunteerprofile.objectName():
            volunteerprofile.setObjectName(u"volunteerprofile")
        volunteerprofile.resize(1121, 799)
        volunteerprofile.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.verticalLayoutWidget_2 = QWidget(volunteerprofile)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(240, -40, 2, 2))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushlogout = QPushButton(volunteerprofile)
        self.pushlogout.setObjectName(u"pushlogout")
        self.pushlogout.setGeometry(QRect(0, 300, 141, 81))
        self.collection = QPushButton(volunteerprofile)
        self.collection.setObjectName(u"collection")
        self.collection.setGeometry(QRect(0, 230, 141, 71))
        self.sumtotal = QLabel(volunteerprofile)
        self.sumtotal.setObjectName(u"sumtotal")
        self.sumtotal.setGeometry(QRect(20, 530, 107, 23))
        font = QFont()
        font.setPointSize(14)
        self.sumtotal.setFont(font)
        self.sumtotal.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.filler1 = QLabel(volunteerprofile)
        self.filler1.setObjectName(u"filler1")
        self.filler1.setGeometry(QRect(150, 480, 71, 21))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.filler1.setFont(font1)
        self.filler1.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.sumpoint = QLabel(volunteerprofile)
        self.sumpoint.setObjectName(u"sumpoint")
        self.sumpoint.setGeometry(QRect(20, 480, 99, 23))
        self.sumpoint.setFont(font)
        self.sumpoint.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.filler2 = QLabel(volunteerprofile)
        self.filler2.setObjectName(u"filler2")
        self.filler2.setGeometry(QRect(150, 530, 71, 20))
        self.filler2.setFont(font1)
        self.filler2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.calendarWidget = QCalendarWidget(volunteerprofile)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(380, 310, 691, 471))
        self.calendarWidget.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.welcomemsg = QLabel(volunteerprofile)
        self.welcomemsg.setObjectName(u"welcomemsg")
        self.welcomemsg.setGeometry(QRect(380, 20, 187, 94))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.welcomemsg.setFont(font2)
        self.welcomemsg.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg.setTextFormat(Qt.AutoText)
        self.label = QLabel(volunteerprofile)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 47, 13))
        self.label.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.label_2 = QLabel(volunteerprofile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 70, 47, 13))
        self.label_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.progressBar = QProgressBar(volunteerprofile)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(59, 91, 108, 21))
        self.progressBar.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.progressBar.setValue(24)
        self.label_3 = QLabel(volunteerprofile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 91, 42, 16))
        self.label_3.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.welcomemsg_3 = QLabel(volunteerprofile)
        self.welcomemsg_3.setObjectName(u"welcomemsg_3")
        self.welcomemsg_3.setGeometry(QRect(570, 20, 187, 94))
        self.welcomemsg_3.setFont(font2)
        self.welcomemsg_3.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg_3.setTextFormat(Qt.AutoText)
        self.welcomemsg_2 = QLabel(volunteerprofile)
        self.welcomemsg_2.setObjectName(u"welcomemsg_2")
        self.welcomemsg_2.setGeometry(QRect(500, 110, 591, 191))
        self.welcomemsg_2.setFont(font2)
        self.welcomemsg_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg_2.setTextFormat(Qt.AutoText)
        self.pushprofile = QPushButton(volunteerprofile)
        self.pushprofile.setObjectName(u"pushprofile")
        self.pushprofile.setGeometry(QRect(0, 160, 141, 71))
        self.pushprofile.setStyleSheet(u"")
        self.splitter = QSplitter(volunteerprofile)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(60, 40, 64, 46))
        self.splitter.setOrientation(Qt.Vertical)
        self.ptsIcd = QLCDNumber(self.splitter)
        self.ptsIcd.setObjectName(u"ptsIcd")
        self.ptsIcd.setStyleSheet(u"background: black")
        self.splitter.addWidget(self.ptsIcd)
        self.hrsIcd = QLCDNumber(self.splitter)
        self.hrsIcd.setObjectName(u"hrsIcd")
        self.hrsIcd.setStyleSheet(u"background: black")
        self.splitter.addWidget(self.hrsIcd)

        self.retranslateUi(volunteerprofile)

        QMetaObject.connectSlotsByName(volunteerprofile)
    # setupUi

    def retranslateUi(self, volunteerprofile):
        volunteerprofile.setWindowTitle(QCoreApplication.translate("volunteerprofile", u"volunteerprofile", None))
        self.pushlogout.setText(QCoreApplication.translate("volunteerprofile", u"Logout", None))
        self.collection.setText(QCoreApplication.translate("volunteerprofile", u"Collection", None))
        self.sumtotal.setText(QCoreApplication.translate("volunteerprofile", u"Total hours :", None))
        self.filler1.setText(QCoreApplication.translate("volunteerprofile", u"0", None))
        self.sumpoint.setText(QCoreApplication.translate("volunteerprofile", u"Your Point :", None))
        self.filler2.setText(QCoreApplication.translate("volunteerprofile", u"0", None))
        self.welcomemsg.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-style:italic;\">Welcome,</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("volunteerprofile", u"Pts", None))
        self.label_2.setText(QCoreApplication.translate("volunteerprofile", u"hrs", None))
        self.label_3.setText(QCoreApplication.translate("volunteerprofile", u"progress", None))
        self.welcomemsg_3.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-style:italic;\">&lt;name&gt;</span></p></body></html>", None))
        self.welcomemsg_2.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p>&lt;msg&gt;</p></body></html>", None))
        self.pushprofile.setText(QCoreApplication.translate("volunteerprofile", u"Profile", None))
    # retranslateUi

