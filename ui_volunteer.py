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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QLCDNumber,
    QLabel, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSplitter, QVBoxLayout,
    QWidget)

class Ui_volunteerprofile(object):
    def setupUi(self, volunteerprofile):
        if not volunteerprofile.objectName():
            volunteerprofile.setObjectName(u"volunteerprofile")
        volunteerprofile.resize(1280, 768)
        volunteerprofile.setStyleSheet(u"QFrame\n"
"{\n"
"background:rgba(6, 16, 28, 0.8);\n"
"border-radius:15px;\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(volunteerprofile)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(240, -40, 2, 2))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.welcomemsg = QLabel(volunteerprofile)
        self.welcomemsg.setObjectName(u"welcomemsg")
        self.welcomemsg.setGeometry(QRect(370, 20, 187, 94))
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(30)
        font.setBold(True)
        self.welcomemsg.setFont(font)
        self.welcomemsg.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg.setTextFormat(Qt.AutoText)
        self.welcomemsg_3 = QLabel(volunteerprofile)
        self.welcomemsg_3.setObjectName(u"welcomemsg_3")
        self.welcomemsg_3.setGeometry(QRect(570, 20, 187, 94))
        self.welcomemsg_3.setFont(font)
        self.welcomemsg_3.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg_3.setTextFormat(Qt.AutoText)
        self.welcomemsg_2 = QLabel(volunteerprofile)
        self.welcomemsg_2.setObjectName(u"welcomemsg_2")
        self.welcomemsg_2.setGeometry(QRect(500, 80, 591, 191))
        self.welcomemsg_2.setFont(font)
        self.welcomemsg_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.welcomemsg_2.setTextFormat(Qt.AutoText)
        self.frame = QFrame(volunteerprofile)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 260, 831, 401))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.svCalendar = QCalendarWidget(self.frame)
        self.svCalendar.setObjectName(u"svCalendar")
        self.svCalendar.setGeometry(QRect(10, 10, 501, 381))
        font1 = QFont()
        font1.setPointSize(12)
        self.svCalendar.setFont(font1)
        self.svCalendar.setStyleSheet(u"background:rgba(205,205,235,1);")
        self.svListWidget = QListWidget(self.frame)
        self.svListWidget.setObjectName(u"svListWidget")
        self.svListWidget.setGeometry(QRect(530, 10, 281, 381))
        self.svListWidget.setStyleSheet(u"background:rgba(255,255,255,0.7);")
        self.svListWidget.setDefaultDropAction(Qt.MoveAction)
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(510, 10, 21, 381))
        self.line.setStyleSheet(u"background:black")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.frame_2 = QFrame(volunteerprofile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 10, 241, 681))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.vlogout = QPushButton(self.frame_2)
        self.vlogout.setObjectName(u"vlogout")
        self.vlogout.setGeometry(QRect(10, 450, 181, 81))
        font2 = QFont()
        font2.setFamilies([u"century gothic"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.vlogout.setFont(font2)
        self.vlogout.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")
        self.vcoupon = QPushButton(self.frame_2)
        self.vcoupon.setObjectName(u"vcoupon")
        self.vcoupon.setGeometry(QRect(10, 180, 181, 81))
        self.vcoupon.setFont(font2)
        self.vcoupon.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")
        self.vprofile = QPushButton(self.frame_2)
        self.vprofile.setObjectName(u"vprofile")
        self.vprofile.setGeometry(QRect(10, 360, 181, 81))
        self.vprofile.setFont(font2)
        self.vprofile.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")
        self.vservices = QPushButton(self.frame_2)
        self.vservices.setObjectName(u"vservices")
        self.vservices.setGeometry(QRect(10, 270, 181, 81))
        self.vservices.setFont(font2)
        self.vservices.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")
        self.filler2 = QLabel(self.frame_2)
        self.filler2.setObjectName(u"filler2")
        self.filler2.setGeometry(QRect(140, 620, 71, 20))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.filler2.setFont(font3)
        self.filler2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:rgb(194, 194, 194)")
        self.filler1 = QLabel(self.frame_2)
        self.filler1.setObjectName(u"filler1")
        self.filler1.setGeometry(QRect(140, 560, 71, 21))
        self.filler1.setFont(font3)
        self.filler1.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:rgb(194, 194, 194)")
        self.sumpoint = QLabel(self.frame_2)
        self.sumpoint.setObjectName(u"sumpoint")
        self.sumpoint.setGeometry(QRect(10, 560, 111, 23))
        font4 = QFont()
        font4.setPointSize(14)
        self.sumpoint.setFont(font4)
        self.sumpoint.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.sumtotal = QLabel(self.frame_2)
        self.sumtotal.setObjectName(u"sumtotal")
        self.sumtotal.setGeometry(QRect(10, 610, 107, 23))
        self.sumtotal.setFont(font4)
        self.sumtotal.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 70, 47, 21))
        self.label_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 71, 21))
        self.label_3.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 61, 21))
        self.label.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(120, 50, 64, 46))
        self.splitter.setStyleSheet(u"color:rgb(194, 194, 194)")
        self.splitter.setOrientation(Qt.Vertical)
        self.ptsIcd = QLCDNumber(self.splitter)
        self.ptsIcd.setObjectName(u"ptsIcd")
        self.ptsIcd.setStyleSheet(u"background: black")
        self.ptsIcd.setDigitCount(4)
        self.ptsIcd.setSegmentStyle(QLCDNumber.Filled)
        self.splitter.addWidget(self.ptsIcd)
        self.hrsIcd = QLCDNumber(self.splitter)
        self.hrsIcd.setObjectName(u"hrsIcd")
        font5 = QFont()
        font5.setBold(False)
        self.hrsIcd.setFont(font5)
        self.hrsIcd.setStyleSheet(u"background: black")
        self.hrsIcd.setDigitCount(4)
        self.splitter.addWidget(self.hrsIcd)
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(120, 100, 108, 21))
        self.progressBar.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.progressBar.setValue(24)
        self.frame_3 = QFrame(volunteerprofile)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(950, 650, 121, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.saveButton = QPushButton(self.frame_3)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(10, 20, 101, 31))
        font6 = QFont()
        font6.setFamilies([u"century gothic"])
        font6.setPointSize(12)
        self.saveButton.setFont(font6)
        self.saveButton.setStyleSheet(u"QPushButton\n"
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

        self.retranslateUi(volunteerprofile)

        QMetaObject.connectSlotsByName(volunteerprofile)
    # setupUi

    def retranslateUi(self, volunteerprofile):
        volunteerprofile.setWindowTitle(QCoreApplication.translate("volunteerprofile", u"volunteerprofile", None))
        self.welcomemsg.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-style:italic;\">Welcome,</span></p></body></html>", None))
        self.welcomemsg_3.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-style:italic;\">&lt;name&gt;</span></p></body></html>", None))
        self.welcomemsg_2.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p>&lt;msg&gt;</p></body></html>", None))
        self.vlogout.setText(QCoreApplication.translate("volunteerprofile", u"Logout", None))
        self.vcoupon.setText(QCoreApplication.translate("volunteerprofile", u"Coupons", None))
        self.vprofile.setText(QCoreApplication.translate("volunteerprofile", u"Profile", None))
        self.vservices.setText(QCoreApplication.translate("volunteerprofile", u"Services", None))
        self.filler2.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#c2c2c2;\">0</span></p></body></html>", None))
        self.filler1.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#c2c2c2;\">0</span></p></body></html>", None))
        self.sumpoint.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Your Points :</span></p></body></html>", None))
        self.sumtotal.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Total hours :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c2c2c2;\">Hours :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c2c2c2;\">Progress :</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("volunteerprofile", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#c2c2c2;\">Points :</span></p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("volunteerprofile", u"Save", None))
    # retranslateUi

