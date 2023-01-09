# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consumer.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_conumerprofile(object):
    def setupUi(self, conumerprofile):
        if not conumerprofile.objectName():
            conumerprofile.setObjectName(u"conumerprofile")
        conumerprofile.resize(1280, 768)
        conumerprofile.setStyleSheet(u"QFrame\n"
"{\n"
"background:rgba(140, 21, 49, 0.8);\n"
"border-radius:15px;\n"
"}")
        self.welcomelabel = QLabel(conumerprofile)
        self.welcomelabel.setObjectName(u"welcomelabel")
        self.welcomelabel.setGeometry(QRect(820, 40, 161, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(23)
        font.setBold(True)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.welcomelabel.setTextFormat(Qt.AutoText)
        self.sumpoint = QLabel(conumerprofile)
        self.sumpoint.setObjectName(u"sumpoint")
        self.sumpoint.setGeometry(QRect(850, 170, 131, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.sumpoint.setFont(font1)
        self.sumpoint.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.sumpoint.setFrameShape(QFrame.NoFrame)
        self.sumpoint.setFrameShadow(QFrame.Plain)
        self.sumpoint.setLineWidth(1)
        self.welcomemsg = QLabel(conumerprofile)
        self.welcomemsg.setObjectName(u"welcomemsg")
        self.welcomemsg.setGeometry(QRect(980, 30, 281, 131))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.welcomemsg.setFont(font2)
        self.welcomemsg.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.points = QLabel(conumerprofile)
        self.points.setObjectName(u"points")
        self.points.setGeometry(QRect(970, 170, 111, 31))
        self.points.setFont(font1)
        self.points.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.frame = QFrame(conumerprofile)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(410, 280, 831, 401))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.scCalendar = QCalendarWidget(self.frame)
        self.scCalendar.setObjectName(u"scCalendar")
        self.scCalendar.setGeometry(QRect(10, 10, 501, 381))
        font3 = QFont()
        font3.setPointSize(12)
        self.scCalendar.setFont(font3)
        self.scCalendar.setAutoFillBackground(False)
        self.scCalendar.setStyleSheet(u"background:rgba(6, 16, 28,1);\n"
"color:rgb(240, 150, 194)")
        self.scCalendar.setGridVisible(True)
        self.scListWidget = QListWidget(self.frame)
        self.scListWidget.setObjectName(u"scListWidget")
        self.scListWidget.setGeometry(QRect(530, 10, 281, 381))
        self.scListWidget.setStyleSheet(u"background:rgba(255,255,255,0.7);")
        self.scListWidget.setDefaultDropAction(Qt.MoveAction)
        self.frame_2 = QFrame(conumerprofile)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 781, 101))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.cprofile = QPushButton(self.frame_2)
        self.cprofile.setObjectName(u"cprofile")
        self.cprofile.setGeometry(QRect(10, 10, 181, 81))
        font4 = QFont()
        font4.setFamilies([u"century gothic"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.cprofile.setFont(font4)
        self.cprofile.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.cservicesB = QPushButton(self.frame_2)
        self.cservicesB.setObjectName(u"cservicesB")
        self.cservicesB.setGeometry(QRect(200, 10, 181, 81))
        self.cservicesB.setFont(font4)
        self.cservicesB.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.ccoupon = QPushButton(self.frame_2)
        self.ccoupon.setObjectName(u"ccoupon")
        self.ccoupon.setGeometry(QRect(390, 10, 181, 81))
        self.ccoupon.setFont(font4)
        self.ccoupon.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.clogout = QPushButton(self.frame_2)
        self.clogout.setObjectName(u"clogout")
        self.clogout.setGeometry(QRect(580, 10, 181, 81))
        self.clogout.setFont(font4)
        self.clogout.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")

        self.retranslateUi(conumerprofile)

        QMetaObject.connectSlotsByName(conumerprofile)
    # setupUi

    def retranslateUi(self, conumerprofile):
        conumerprofile.setWindowTitle(QCoreApplication.translate("conumerprofile", u"consumer", None))
        self.welcomelabel.setText(QCoreApplication.translate("conumerprofile", u"<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#000000;\">Welcome, </span></p></body></html>", None))
        self.sumpoint.setText(QCoreApplication.translate("conumerprofile", u"Your Point :", None))
        self.welcomemsg.setText(QCoreApplication.translate("conumerprofile", u"<name>", None))
        self.points.setText(QCoreApplication.translate("conumerprofile", u"0", None))
        self.cprofile.setText(QCoreApplication.translate("conumerprofile", u"Profile", None))
        self.cservicesB.setText(QCoreApplication.translate("conumerprofile", u"Services", None))
        self.ccoupon.setText(QCoreApplication.translate("conumerprofile", u"Coupons", None))
        self.clogout.setText(QCoreApplication.translate("conumerprofile", u"Logout", None))
    # retranslateUi

