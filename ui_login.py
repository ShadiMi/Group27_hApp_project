# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import loginqrc_rc

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(1280, 768)
        login.setWindowOpacity(1.000000000000000)
        login.setStyleSheet(u"*{\n"
"font-family:century gothic;\n"
"fomt-size:24px;\n"
"background:url(:/loginimgs/loginBG.jpg) \n"
"}\n"
"QFrame\n"
"{\n"
"background:rgba(6, 16, 28, 0.8);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"\n"
"background:red;\n"
"border-radius:30px;\n"
"}\n"
"\n"
"\n"
"QToolButton\n"
"{\n"
"\n"
"background:white;\n"
"border-radius:30px;\n"
"}\n"
"QLable\n"
"{\n"
"background:rgba(0,0,0,0.8);	\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border_bottom:1px solid #717072;\n"
"\n"
"\n"
"}\n"
"")
        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(460, 190, 381, 321))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 40, 161, 61))
        font = QFont()
        font.setFamilies([u"century gothic"])
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.loginL = QPushButton(self.frame)
        self.loginL.setObjectName(u"loginL")
        self.loginL.setGeometry(QRect(10, 269, 361, 31))
        font1 = QFont()
        font1.setFamilies([u"century gothic"])
        font1.setPointSize(12)
        self.loginL.setFont(font1)
        self.loginL.setStyleSheet(u"QPushButton\n"
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
        self.usernameLF = QLineEdit(self.frame)
        self.usernameLF.setObjectName(u"usernameLF")
        self.usernameLF.setGeometry(QRect(20, 100, 341, 31))
        font2 = QFont()
        font2.setFamilies([u"century gothic"])
        font2.setPointSize(14)
        self.usernameLF.setFont(font2)
        self.usernameLF.setStyleSheet(u"QLineEdit\n"
"{\n"
"\n"
"bachground:transparent;\n"
"border-bottom:1px solid #717072;\n"
"color:#717072;\n"
"\n"
"}\n"
"\n"
"")
        self.passwordLF = QLineEdit(self.frame)
        self.passwordLF.setObjectName(u"passwordLF")
        self.passwordLF.setGeometry(QRect(20, 180, 341, 31))
        self.passwordLF.setFont(font2)
        self.passwordLF.setAcceptDrops(True)
        self.passwordLF.setStyleSheet(u"QLineEdit\n"
"{\n"
"\n"
"bachground:transparent;\n"
"border-bottom:1px solid #717072;\n"
"color:#717072;\n"
"\n"
"}")
        self.passwordLF.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 220, 201, 41))
        self.label_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.loginIcon = QPushButton(login)
        self.loginIcon.setObjectName(u"loginIcon")
        self.loginIcon.setGeometry(QRect(600, 110, 101, 101))
        self.loginIcon.setStyleSheet(u"QPushButton\n"
"\n"
"\n"
"{\n"
"background:skyblue;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/loginimgs/usericon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.loginIcon.setIcon(icon)
        self.loginIcon.setIconSize(QSize(42, 79))
        self.back = QPushButton(login)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(20, 30, 101, 31))
        self.back.setFont(font1)
        self.back.setStyleSheet(u"QPushButton\n"
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

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\">LOGIN HERE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">LOGIN HERE</span></p></body></html>", None))
        self.loginL.setText(QCoreApplication.translate("login", u"CONFIRM", None))
#if QT_CONFIG(tooltip)
        self.usernameLF.setToolTip(QCoreApplication.translate("login", u"<html><head/><body><p><span style=\" color:#ffffff;\">ySERNAME</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.usernameLF.setText("")
        self.usernameLF.setPlaceholderText(QCoreApplication.translate("login", u"Username", None))
#if QT_CONFIG(whatsthis)
        self.passwordLF.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.passwordLF.setText("")
        self.passwordLF.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("login", u"<html><head/><body><p><span style=\" color:#ffffff;\">Sign in to your existing account</span></p></body></html>", None))
        self.loginIcon.setText("")
        self.back.setText(QCoreApplication.translate("login", u"Back", None))
    # retranslateUi

