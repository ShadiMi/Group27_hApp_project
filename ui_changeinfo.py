# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changeinfo.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_changeprofile(object):
    def setupUi(self, changeprofile):
        if not changeprofile.objectName():
            changeprofile.setObjectName(u"changeprofile")
        changeprofile.resize(732, 518)
        changeprofile.setStyleSheet(u"")
        self.pLabel = QLabel(changeprofile)
        self.pLabel.setObjectName(u"pLabel")
        self.pLabel.setGeometry(QRect(270, 10, 171, 41))
        self.pLabel.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.layoutWidget = QWidget(changeprofile)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 200, 118, 121))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.newemailF = QLineEdit(self.layoutWidget)
        self.newemailF.setObjectName(u"newemailF")
        self.newemailF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.newemailF)

        self.newpwF = QLineEdit(self.layoutWidget)
        self.newpwF.setObjectName(u"newpwF")
        self.newpwF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.newpwF)

        self.confirmnewpwF = QLineEdit(self.layoutWidget)
        self.confirmnewpwF.setObjectName(u"confirmnewpwF")
        self.confirmnewpwF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.confirmnewpwF)

        self.layoutWidget2 = QWidget(changeprofile)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(34, 199, 211, 120))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.newemailL = QLabel(self.layoutWidget2)
        self.newemailL.setObjectName(u"newemailL")
        font = QFont()
        font.setPointSize(11)
        self.newemailL.setFont(font)
        self.newemailL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout_2.addWidget(self.newemailL)

        self.newpwL = QLabel(self.layoutWidget2)
        self.newpwL.setObjectName(u"newpwL")
        self.newpwL.setFont(font)
        self.newpwL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout_2.addWidget(self.newpwL)

        self.cnewpwL = QLabel(self.layoutWidget2)
        self.cnewpwL.setObjectName(u"cnewpwL")
        self.cnewpwL.setFont(font)
        self.cnewpwL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout_2.addWidget(self.cnewpwL)

        self.applyB = QPushButton(changeprofile)
        self.applyB.setObjectName(u"applyB")
        self.applyB.setGeometry(QRect(150, 340, 75, 23))
        self.applyB.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.cancelB = QPushButton(changeprofile)
        self.cancelB.setObjectName(u"cancelB")
        self.cancelB.setGeometry(QRect(230, 340, 75, 23))
        self.cancelB.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.cpwL = QLabel(changeprofile)
        self.cpwL.setObjectName(u"cpwL")
        self.cpwL.setGeometry(QRect(40, 70, 209, 35))
        self.cpwL.setFont(font)
        self.cpwL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.currentpwF = QLineEdit(changeprofile)
        self.currentpwF.setObjectName(u"currentpwF")
        self.currentpwF.setGeometry(QRect(260, 80, 116, 20))
        self.currentpwF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.instructionsL = QLabel(changeprofile)
        self.instructionsL.setObjectName(u"instructionsL")
        self.instructionsL.setGeometry(QRect(20, 110, 661, 81))
        self.instructionsL.setFont(font)
        self.instructionsL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.error = QLabel(changeprofile)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(390, 70, 201, 31))
        self.error.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:red;")
        self.error_2 = QLabel(changeprofile)
        self.error_2.setObjectName(u"error_2")
        self.error_2.setGeometry(QRect(400, 280, 201, 31))
        self.error_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground);\n"
"color:red;")

        self.retranslateUi(changeprofile)

        QMetaObject.connectSlotsByName(changeprofile)
    # setupUi

    def retranslateUi(self, changeprofile):
        changeprofile.setWindowTitle(QCoreApplication.translate("changeprofile", u"Change Info", None))
        self.pLabel.setText(QCoreApplication.translate("changeprofile", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Personal Info</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\"><br/></span></p></body></html>", None))
        self.newemailF.setPlaceholderText(QCoreApplication.translate("changeprofile", u"New Email", None))
        self.newpwF.setText("")
        self.newpwF.setPlaceholderText(QCoreApplication.translate("changeprofile", u"New Password", None))
        self.confirmnewpwF.setPlaceholderText(QCoreApplication.translate("changeprofile", u"Confirm new Password", None))
        self.newemailL.setText(QCoreApplication.translate("changeprofile", u"Enter your new Email :", None))
        self.newpwL.setText(QCoreApplication.translate("changeprofile", u"Enter you'r new Password :", None))
        self.cnewpwL.setText(QCoreApplication.translate("changeprofile", u"Confirm Your New Password :", None))
        self.applyB.setText(QCoreApplication.translate("changeprofile", u"Apply", None))
        self.cancelB.setText(QCoreApplication.translate("changeprofile", u"Cancel", None))
        self.cpwL.setText(QCoreApplication.translate("changeprofile", u"Enter your current Password :", None))
        self.currentpwF.setPlaceholderText(QCoreApplication.translate("changeprofile", u"Current Password", None))
        self.instructionsL.setText(QCoreApplication.translate("changeprofile", u"<html><head/><body><p><span style=\" font-weight:600;\">Fill in your new email and password if you want them changed, leave them blank if not </span></p></body></html>", None))
        self.error.setText("")
        self.error_2.setText("")
    # retranslateUi

