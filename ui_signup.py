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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_create(object):
    def setupUi(self, create):
        if not create.objectName():
            create.setObjectName(u"create")
        create.resize(789, 468)
        create.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(20, 181, 255), stop:1 rgba(255, 255, 255, 255))")
        self.gridLayout = QGridLayout(create)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 1, 1, 1)

        self.signupL = QLabel(create)
        self.signupL.setObjectName(u"signupL")
        font = QFont()
        font.setPointSize(22)
        self.signupL.setFont(font)
        self.signupL.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.signupL, 2, 1, 1, 1)

        self.frame = QFrame(create)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.usernameRF = QLineEdit(self.frame)
        self.usernameRF.setObjectName(u"usernameRF")
        font1 = QFont()
        font1.setPointSize(10)
        self.usernameRF.setFont(font1)
        self.usernameRF.setStyleSheet(u"")
        self.usernameRF.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.verticalLayout_2.addWidget(self.usernameRF)

        self.emailRF = QLineEdit(self.frame)
        self.emailRF.setObjectName(u"emailRF")
        self.emailRF.setFont(font1)

        self.verticalLayout_2.addWidget(self.emailRF)

        self.pwRF = QLineEdit(self.frame)
        self.pwRF.setObjectName(u"pwRF")
        self.pwRF.setFont(font1)
        self.pwRF.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.pwRF)

        self.pwcRF = QLineEdit(self.frame)
        self.pwcRF.setObjectName(u"pwcRF")
        self.pwcRF.setFont(font1)
        self.pwcRF.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.pwcRF)

        self.profboxR = QComboBox(self.frame)
        self.profboxR.addItem("")
        self.profboxR.addItem("")
        self.profboxR.setObjectName(u"profboxR")
        self.profboxR.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(12)
        self.profboxR.setFont(font2)
        self.profboxR.setEditable(False)
        self.profboxR.setFrame(True)

        self.verticalLayout_2.addWidget(self.profboxR)


        self.gridLayout.addWidget(self.frame, 3, 2, 1, 1)

        self.widget = QWidget(create)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.unR = QLabel(self.widget)
        self.unR.setObjectName(u"unR")
        self.unR.setFont(font1)
        self.unR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.unR)

        self.emailR = QLabel(self.widget)
        self.emailR.setObjectName(u"emailR")
        self.emailR.setFont(font1)
        self.emailR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.emailR)

        self.pwR = QLabel(self.widget)
        self.pwR.setObjectName(u"pwR")
        self.pwR.setFont(font1)
        self.pwR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.pwR)

        self.pwcR = QLabel(self.widget)
        self.pwcR.setObjectName(u"pwcR")
        self.pwcR.setFont(font1)
        self.pwcR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.pwcR)

        self.profR = QLabel(self.widget)
        self.profR.setObjectName(u"profR")
        self.profR.setFont(font1)
        self.profR.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.profR)


        self.gridLayout.addWidget(self.widget, 3, 1, 1, 1)

        self.back2 = QPushButton(create)
        self.back2.setObjectName(u"back2")
        self.back2.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.back2, 0, 0, 1, 1)

        self.signupR = QPushButton(create)
        self.signupR.setObjectName(u"signupR")
        self.signupR.setFont(font2)
        self.signupR.setCursor(QCursor(Qt.ArrowCursor))
        self.signupR.setAutoDefault(False)

        self.gridLayout.addWidget(self.signupR, 4, 2, 1, 1)

        self.error = QLabel(create)
        self.error.setObjectName(u"error")
        self.error.setFont(font1)
        self.error.setStyleSheet(u"color: red;\n"
"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.gridLayout.addWidget(self.error, 2, 2, 1, 1)


        self.retranslateUi(create)

        QMetaObject.connectSlotsByName(create)
    # setupUi

    def retranslateUi(self, create):
        create.setWindowTitle(QCoreApplication.translate("create", u"signup", None))
        self.signupL.setText(QCoreApplication.translate("create", u"Signup", None))
        self.usernameRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your Name ", None))
        self.emailRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your  Email", None))
        self.pwRF.setPlaceholderText(QCoreApplication.translate("create", u"Enter Your Password", None))
        self.pwcRF.setPlaceholderText(QCoreApplication.translate("create", u"Password Confirm ", None))
        self.profboxR.setItemText(0, QCoreApplication.translate("create", u"Volunteer", None))
        self.profboxR.setItemText(1, QCoreApplication.translate("create", u"Consumer", None))

        self.profboxR.setCurrentText(QCoreApplication.translate("create", u"Volunteer", None))
        self.unR.setText(QCoreApplication.translate("create", u"User Name", None))
        self.emailR.setText(QCoreApplication.translate("create", u"Email", None))
        self.pwR.setText(QCoreApplication.translate("create", u"Password", None))
        self.pwcR.setText(QCoreApplication.translate("create", u"Password Confirm ", None))
        self.profR.setText(QCoreApplication.translate("create", u"Profile", None))
        self.back2.setText(QCoreApplication.translate("create", u"Back", None))
#if QT_CONFIG(tooltip)
        self.signupR.setToolTip(QCoreApplication.translate("create", u"Press To Signup", None))
#endif // QT_CONFIG(tooltip)
        self.signupR.setText(QCoreApplication.translate("create", u"Signup", None))
        self.error.setText("")
    # retranslateUi

