# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSplitter,
    QWidget)

class Ui_create(object):
    def setupUi(self, create):
        if not create.objectName():
            create.setObjectName(u"create")
        create.resize(1280, 768)
        create.setStyleSheet(u"QFrame\n"
"{\n"
"background:rgba(6, 16, 28, 0.8);\n"
"border-radius:15px;\n"
"}")
        self.bgframe = QFrame(create)
        self.bgframe.setObjectName(u"bgframe")
        self.bgframe.setGeometry(QRect(490, 200, 381, 321))
        self.bgframe.setFrameShape(QFrame.StyledPanel)
        self.bgframe.setFrameShadow(QFrame.Raised)
        self.error = QLabel(self.bgframe)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(140, 80, 181, 16))
        font = QFont()
        font.setPointSize(10)
        self.error.setFont(font)
        self.error.setStyleSheet(u"color: red;\n"
"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.signupL = QLabel(self.bgframe)
        self.signupL.setObjectName(u"signupL")
        self.signupL.setGeometry(QRect(30, 30, 87, 41))
        font1 = QFont()
        font1.setPointSize(22)
        self.signupL.setFont(font1)
        self.signupL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.frame = QFrame(self.bgframe)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(160, 99, 151, 155))
        self.frame.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.usernameRF = QLineEdit(self.frame)
        self.usernameRF.setObjectName(u"usernameRF")
        self.usernameRF.setGeometry(QRect(9, 9, 133, 22))
        self.usernameRF.setFont(font)
        self.usernameRF.setStyleSheet(u"")
        self.usernameRF.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.emailRF = QLineEdit(self.frame)
        self.emailRF.setObjectName(u"emailRF")
        self.emailRF.setGeometry(QRect(9, 37, 133, 22))
        self.emailRF.setFont(font)
        self.pwRF = QLineEdit(self.frame)
        self.pwRF.setObjectName(u"pwRF")
        self.pwRF.setGeometry(QRect(9, 65, 133, 22))
        self.pwRF.setFont(font)
        self.pwRF.setEchoMode(QLineEdit.Password)
        self.pwcRF = QLineEdit(self.frame)
        self.pwcRF.setObjectName(u"pwcRF")
        self.pwcRF.setGeometry(QRect(9, 93, 133, 22))
        self.pwcRF.setFont(font)
        self.pwcRF.setEchoMode(QLineEdit.Password)
        self.profboxR = QComboBox(self.frame)
        self.profboxR.addItem("")
        self.profboxR.addItem("")
        self.profboxR.setObjectName(u"profboxR")
        self.profboxR.setEnabled(True)
        self.profboxR.setGeometry(QRect(9, 121, 98, 25))
        font2 = QFont()
        font2.setPointSize(12)
        self.profboxR.setFont(font2)
        self.profboxR.setEditable(False)
        self.profboxR.setFrame(True)
        self.widget = QWidget(self.bgframe)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(28, 99, 141, 151))
        self.widget.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.unR = QLabel(self.widget)
        self.unR.setObjectName(u"unR")
        self.unR.setGeometry(QRect(9, 9, 81, 16))
        self.unR.setFont(font)
        self.unR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.emailR = QLabel(self.widget)
        self.emailR.setObjectName(u"emailR")
        self.emailR.setGeometry(QRect(10, 40, 51, 16))
        self.emailR.setFont(font)
        self.emailR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.pwR = QLabel(self.widget)
        self.pwR.setObjectName(u"pwR")
        self.pwR.setGeometry(QRect(10, 70, 71, 16))
        self.pwR.setFont(font)
        self.pwR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.pwcR = QLabel(self.widget)
        self.pwcR.setObjectName(u"pwcR")
        self.pwcR.setGeometry(QRect(10, 100, 111, 16))
        self.pwcR.setFont(font)
        self.pwcR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.profR = QLabel(self.widget)
        self.profR.setObjectName(u"profR")
        self.profR.setGeometry(QRect(10, 130, 36, 16))
        self.profR.setFont(font)
        self.profR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.signupR = QPushButton(self.bgframe)
        self.signupR.setObjectName(u"signupR")
        self.signupR.setGeometry(QRect(70, 260, 261, 31))
        font3 = QFont()
        font3.setFamilies([u"century gothic"])
        font3.setPointSize(12)
        self.signupR.setFont(font3)
        self.signupR.setStyleSheet(u"QPushButton\n"
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
        self.splitter = QSplitter(create)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 0, 0))
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(create)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_3 = QSplitter(create)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_4 = QSplitter(create)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.splitter_5 = QSplitter(create)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.splitter_6 = QSplitter(create)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(0, 0, 0, 0))
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.back2 = QPushButton(create)
        self.back2.setObjectName(u"back2")
        self.back2.setGeometry(QRect(0, 10, 101, 31))
        self.back2.setFont(font3)
        self.back2.setStyleSheet(u"QPushButton\n"
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

        self.retranslateUi(create)

        QMetaObject.connectSlotsByName(create)
    # setupUi

    def retranslateUi(self, create):
        create.setWindowTitle(QCoreApplication.translate("create", u"signup", None))
        self.error.setText("")
        self.signupL.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Signup</span></p></body></html>", None))
        self.usernameRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your Name ", None))
        self.emailRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your  Email", None))
        self.pwRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your Password", None))
        self.pwcRF.setPlaceholderText(QCoreApplication.translate("create", u"Password Confirm ", None))
        self.profboxR.setItemText(0, QCoreApplication.translate("create", u"Volunteer", None))
        self.profboxR.setItemText(1, QCoreApplication.translate("create", u"Consumer", None))

        self.profboxR.setCurrentText(QCoreApplication.translate("create", u"Volunteer", None))
        self.unR.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">User Name</span></p></body></html>", None))
        self.emailR.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Email</span></p></body></html>", None))
        self.pwR.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Password</span></p></body></html>", None))
        self.pwcR.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Password Confirm </span></p></body></html>", None))
        self.profR.setText(QCoreApplication.translate("create", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Profile</span></p></body></html>", None))
        self.signupR.setText(QCoreApplication.translate("create", u"Sign-up", None))
        self.back2.setText(QCoreApplication.translate("create", u"Back", None))
    # retranslateUi

