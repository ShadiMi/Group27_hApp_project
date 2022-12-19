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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_conumerprofile(object):
    def setupUi(self, conumerprofile):
        if not conumerprofile.objectName():
            conumerprofile.setObjectName(u"conumerprofile")
        conumerprofile.resize(790, 470)
        conumerprofile.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.welcomelabel = QLabel(conumerprofile)
        self.welcomelabel.setObjectName(u"welcomelabel")
        self.welcomelabel.setGeometry(QRect(10, 80, 161, 41))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(23)
        font.setBold(True)
        self.welcomelabel.setFont(font)
        self.welcomelabel.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.welcomelabel.setTextFormat(Qt.AutoText)
        self.profilecost = QPushButton(conumerprofile)
        self.profilecost.setObjectName(u"profilecost")
        self.profilecost.setGeometry(QRect(0, 0, 181, 61))
        self.profilecost.setStyleSheet(u"")
        self.collectioncost = QPushButton(conumerprofile)
        self.collectioncost.setObjectName(u"collectioncost")
        self.collectioncost.setGeometry(QRect(180, 0, 161, 61))
        self.Couponcost = QPushButton(conumerprofile)
        self.Couponcost.setObjectName(u"Couponcost")
        self.Couponcost.setGeometry(QRect(340, 0, 171, 61))
        self.Logoutcost = QPushButton(conumerprofile)
        self.Logoutcost.setObjectName(u"Logoutcost")
        self.Logoutcost.setGeometry(QRect(510, 0, 151, 61))
        self.sumpoint = QLabel(conumerprofile)
        self.sumpoint.setObjectName(u"sumpoint")
        self.sumpoint.setGeometry(QRect(20, 260, 99, 23))
        font1 = QFont()
        font1.setPointSize(14)
        self.sumpoint.setFont(font1)
        self.sumpoint.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.sumpoint.setFrameShape(QFrame.NoFrame)
        self.sumpoint.setFrameShadow(QFrame.Plain)
        self.sumpoint.setLineWidth(1)
        self.filler = QLabel(conumerprofile)
        self.filler.setObjectName(u"filler")
        self.filler.setGeometry(QRect(110, 165, 141, 21))
        self.filler.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.welcomemsg = QLabel(conumerprofile)
        self.welcomemsg.setObjectName(u"welcomemsg")
        self.welcomemsg.setGeometry(QRect(160, 80, 281, 141))
        self.welcomemsg.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")
        self.points = QLabel(conumerprofile)
        self.points.setObjectName(u"points")
        self.points.setGeometry(QRect(130, 260, 161, 31))
        self.points.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground),\n"
"")

        self.retranslateUi(conumerprofile)

        QMetaObject.connectSlotsByName(conumerprofile)
    # setupUi

    def retranslateUi(self, conumerprofile):
        conumerprofile.setWindowTitle(QCoreApplication.translate("conumerprofile", u"Costumerprofile", None))
        self.welcomelabel.setText(QCoreApplication.translate("conumerprofile", u"<html><head/><body><p><span style=\" font-size:22pt; font-style:italic; color:#000000;\">Welcome, </span></p></body></html>", None))
        self.profilecost.setText(QCoreApplication.translate("conumerprofile", u"Profile ", None))
        self.collectioncost.setText(QCoreApplication.translate("conumerprofile", u"Collection", None))
        self.Couponcost.setText(QCoreApplication.translate("conumerprofile", u"Coupon", None))
        self.Logoutcost.setText(QCoreApplication.translate("conumerprofile", u"Logout", None))
        self.sumpoint.setText(QCoreApplication.translate("conumerprofile", u"Your Point :", None))
        self.filler.setText("")
        self.welcomemsg.setText("")
        self.points.setText("")
    # retranslateUi

