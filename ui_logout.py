# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmlogout.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_confirmlogout(object):
    def setupUi(self, confirmlogout):
        if not confirmlogout.objectName():
            confirmlogout.setObjectName(u"confirmlogout")
        confirmlogout.resize(224, 111)
        confirmlogout.setStyleSheet(u"")
        self.label = QLabel(confirmlogout)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 196, 16))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")
        self.layoutWidget = QWidget(confirmlogout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 40, 77, 54))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.confirmlogout_2 = QPushButton(self.layoutWidget)
        self.confirmlogout_2.setObjectName(u"confirmlogout_2")
        self.confirmlogout_2.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.confirmlogout_2)

        self.cancellogout = QPushButton(self.layoutWidget)
        self.cancellogout.setObjectName(u"cancellogout")
        self.cancellogout.setStyleSheet(u"background:setAttribute(Qt::WA_TranslucentBackground)")

        self.verticalLayout.addWidget(self.cancellogout)


        self.retranslateUi(confirmlogout)

        QMetaObject.connectSlotsByName(confirmlogout)
    # setupUi

    def retranslateUi(self, confirmlogout):
        confirmlogout.setWindowTitle(QCoreApplication.translate("confirmlogout", u"confirmlogout", None))
        self.label.setText(QCoreApplication.translate("confirmlogout", u"Are you sure you want to log out :", None))
#if QT_CONFIG(tooltip)
        self.confirmlogout_2.setToolTip(QCoreApplication.translate("confirmlogout", u"<html><head/><body><p><span style=\" color:#ff0000;\">Logout</span></p><p><span style=\" color:#ff0000;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.confirmlogout_2.setText(QCoreApplication.translate("confirmlogout", u"Logout", None))
        self.cancellogout.setText(QCoreApplication.translate("confirmlogout", u"Cancel", None))
    # retranslateUi

