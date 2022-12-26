# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vServices.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTimeEdit,
    QWidget)

class Ui_vServices(object):
    def setupUi(self, vServices):
        if not vServices.objectName():
            vServices.setObjectName(u"vServices")
        vServices.resize(882, 695)
        self.servicesTable = QTableWidget(vServices)
        if (self.servicesTable.columnCount() < 4):
            self.servicesTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.servicesTable.rowCount() < 10):
            self.servicesTable.setRowCount(10)
        self.servicesTable.setObjectName(u"servicesTable")
        self.servicesTable.setGeometry(QRect(320, 190, 481, 331))
        self.servicesTable.setFrameShadow(QFrame.Sunken)
        self.servicesTable.setSortingEnabled(True)
        self.servicesTable.setRowCount(10)
        self.addService = QPushButton(vServices)
        self.addService.setObjectName(u"addService")
        self.addService.setGeometry(QRect(170, 340, 75, 23))
        self.serviceboxR = QComboBox(vServices)
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.setObjectName(u"serviceboxR")
        self.serviceboxR.setEnabled(True)
        self.serviceboxR.setGeometry(QRect(70, 210, 191, 25))
        font = QFont()
        font.setPointSize(12)
        self.serviceboxR.setFont(font)
        self.serviceboxR.setEditable(False)
        self.serviceboxR.setFrame(True)
        self.serviceName = QLineEdit(vServices)
        self.serviceName.setObjectName(u"serviceName")
        self.serviceName.setGeometry(QRect(70, 240, 191, 22))
        font1 = QFont()
        font1.setPointSize(10)
        self.serviceName.setFont(font1)
        self.serviceName.setStyleSheet(u"")
        self.serviceName.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.backv = QPushButton(vServices)
        self.backv.setObjectName(u"backv")
        self.backv.setGeometry(QRect(30, 20, 75, 23))
        self.vdate = QDateEdit(vServices)
        self.vdate.setObjectName(u"vdate")
        self.vdate.setGeometry(QRect(140, 270, 91, 20))
        self.vdate.setCalendarPopup(True)
        self.vtime = QTimeEdit(vServices)
        self.vtime.setObjectName(u"vtime")
        self.vtime.setGeometry(QRect(143, 301, 71, 20))
        self.vtime.setCalendarPopup(False)
        self.label = QLabel(vServices)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(111, 271, 27, 16))
        self.label_2 = QLabel(vServices)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(111, 301, 26, 16))

        self.retranslateUi(vServices)

        QMetaObject.connectSlotsByName(vServices)
    # setupUi

    def retranslateUi(self, vServices):
        vServices.setWindowTitle(QCoreApplication.translate("vServices", u"Services", None))
        ___qtablewidgetitem = self.servicesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("vServices", u"Service type", None));
        ___qtablewidgetitem1 = self.servicesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("vServices", u"Service name", None));
        ___qtablewidgetitem2 = self.servicesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("vServices", u"Date", None));
        ___qtablewidgetitem3 = self.servicesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("vServices", u"Time", None));
        self.addService.setText(QCoreApplication.translate("vServices", u"Add Service", None))
        self.serviceboxR.setItemText(0, QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceboxR.setItemText(1, QCoreApplication.translate("vServices", u"Advice", None))
        self.serviceboxR.setItemText(2, QCoreApplication.translate("vServices", u"OperationSpectate", None))

        self.serviceboxR.setCurrentText(QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceName.setPlaceholderText(QCoreApplication.translate("vServices", u"Enter Service Name ", None))
        self.backv.setText(QCoreApplication.translate("vServices", u"Back", None))
        self.vtime.setDisplayFormat(QCoreApplication.translate("vServices", u"HH:mm", None))
        self.label.setText(QCoreApplication.translate("vServices", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("vServices", u"Time:", None))
    # retranslateUi

