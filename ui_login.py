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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(789, 469)
        login.setBaseSize(QSize(1024, 768))
        login.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.gridLayout = QGridLayout(login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.back = QPushButton(login)
        self.back.setObjectName(u"back")
        self.back.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.back, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.label = QLabel(login)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.label, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 2, 1)

        self.label_2 = QLabel(login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.label_2, 3, 2, 1, 1)

        self.frame = QFrame(login)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.unL = QLabel(self.frame)
        self.unL.setObjectName(u"unL")
        font1 = QFont()
        font1.setPointSize(10)
        self.unL.setFont(font1)
        self.unL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.horizontalLayout_3.addWidget(self.unL)

        self.usernameLF = QLineEdit(self.frame)
        self.usernameLF.setObjectName(u"usernameLF")
        self.usernameLF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.horizontalLayout_3.addWidget(self.usernameLF)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pwL = QLabel(self.frame)
        self.pwL.setObjectName(u"pwL")
        self.pwL.setFont(font1)
        self.pwL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.horizontalLayout_4.addWidget(self.pwL)

        self.passwordLF = QLineEdit(self.frame)
        self.passwordLF.setObjectName(u"passwordLF")
        self.passwordLF.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.passwordLF.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.passwordLF)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.frame, 4, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(214, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 4, 1, 1)

        self.loginL = QPushButton(login)
        self.loginL.setObjectName(u"loginL")
        self.loginL.setCursor(QCursor(Qt.ArrowCursor))
        self.loginL.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.loginL, 5, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 3, 1, 1)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"login", None))
        self.back.setText(QCoreApplication.translate("login", u"Back", None))
        self.label.setText(QCoreApplication.translate("login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("login", u"Sign in to your existing account", None))
        self.unL.setText(QCoreApplication.translate("login", u"Username", None))
        self.usernameLF.setPlaceholderText(QCoreApplication.translate("login", u"User name ", None))
        self.pwL.setText(QCoreApplication.translate("login", u"Password ", None))
        self.passwordLF.setPlaceholderText(QCoreApplication.translate("login", u"Password", None))
#if QT_CONFIG(tooltip)
        self.loginL.setToolTip(QCoreApplication.translate("login", u"Press To Login ", None))
#endif // QT_CONFIG(tooltip)
        self.loginL.setText(QCoreApplication.translate("login", u"Login", None))
    # retranslateUi

