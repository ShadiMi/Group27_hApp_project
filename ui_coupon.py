# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coupon.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_coupons(object):
    def setupUi(self, coupons):
        if not coupons.objectName():
            coupons.setObjectName(u"coupons")
        coupons.resize(919, 672)
        self.filler1 = QLabel(coupons)
        self.filler1.setObjectName(u"filler1")
        self.filler1.setGeometry(QRect(180, 50, 71, 21))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.filler1.setFont(font)
        self.filler1.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.sumpoint = QLabel(coupons)
        self.sumpoint.setObjectName(u"sumpoint")
        self.sumpoint.setGeometry(QRect(50, 50, 131, 23))
        self.sumpoint.setFont(font)
        self.sumpoint.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.label = QLabel(coupons)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 100, 451, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setScaledContents(False)
        self.ptsF = QLineEdit(coupons)
        self.ptsF.setObjectName(u"ptsF")
        self.ptsF.setGeometry(QRect(470, 100, 81, 20))
        self.ptsF.setEchoMode(QLineEdit.Normal)
        self.ptsF.setClearButtonEnabled(True)
        self.stackedWidget = QStackedWidget(coupons)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(380, 210, 481, 381))
        self.info = QWidget()
        self.info.setObjectName(u"info")
        self.label_2 = QLabel(self.info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 40, 261, 211))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.stackedWidget.addWidget(self.info)
        self.history = QWidget()
        self.history.setObjectName(u"history")
        self.cList = QListWidget(self.history)
        self.cList.setObjectName(u"cList")
        self.cList.setGeometry(QRect(90, 50, 281, 281))
        self.label_3 = QLabel(self.history)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 20, 331, 31))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.stackedWidget.addWidget(self.history)
        self.History = QPushButton(coupons)
        self.History.setObjectName(u"History")
        self.History.setGeometry(QRect(170, 340, 141, 71))
        self.generate = QPushButton(coupons)
        self.generate.setObjectName(u"generate")
        self.generate.setGeometry(QRect(470, 130, 121, 31))
        self.infobtn = QPushButton(coupons)
        self.infobtn.setObjectName(u"infobtn")
        self.infobtn.setGeometry(QRect(170, 270, 141, 71))
        self.backv = QPushButton(coupons)
        self.backv.setObjectName(u"backv")
        self.backv.setGeometry(QRect(20, 10, 75, 23))
        self.error = QLabel(coupons)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(560, 100, 291, 16))

        self.retranslateUi(coupons)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(coupons)
    # setupUi

    def retranslateUi(self, coupons):
        coupons.setWindowTitle(QCoreApplication.translate("coupons", u"Coupons", None))
        self.filler1.setText(QCoreApplication.translate("coupons", u"0", None))
        self.sumpoint.setText(QCoreApplication.translate("coupons", u"Your Points :", None))
        self.label.setText(QCoreApplication.translate("coupons", u"Enter the amount of points you want to convert:", None))
        self.label_2.setText(QCoreApplication.translate("coupons", u"<html><head/><body><p>Services Cost:</p><p><br/></p><p align=\"center\">Advice: 50 points</p><p align=\"center\">Lecture: 150 points</p><p align=\"center\">Spectate: 200 points</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("coupons", u"Coupon                Points               Status", None))
        self.History.setText(QCoreApplication.translate("coupons", u"History", None))
        self.generate.setText(QCoreApplication.translate("coupons", u" Generate Coupon", None))
        self.infobtn.setText(QCoreApplication.translate("coupons", u"Information", None))
        self.backv.setText(QCoreApplication.translate("coupons", u"Back", None))
        self.error.setText("")
    # retranslateUi

