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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QTimeEdit,
    QWidget)

class Ui_vServices(object):
    def setupUi(self, vServices):
        if not vServices.objectName():
            vServices.setObjectName(u"vServices")
        vServices.resize(1280, 768)
        self.servicesTable = QTableWidget(vServices)
        if (self.servicesTable.columnCount() < 6):
            self.servicesTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.servicesTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.servicesTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.servicesTable.rowCount() < 10):
            self.servicesTable.setRowCount(10)
        self.servicesTable.setObjectName(u"servicesTable")
        self.servicesTable.setGeometry(QRect(320, 240, 531, 331))
        self.servicesTable.setFrameShadow(QFrame.Sunken)
        self.servicesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.servicesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.servicesTable.setSortingEnabled(True)
        self.servicesTable.setRowCount(10)
        self.addService = QPushButton(vServices)
        self.addService.setObjectName(u"addService")
        self.addService.setGeometry(QRect(170, 420, 75, 23))
        self.serviceboxR = QComboBox(vServices)
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.setObjectName(u"serviceboxR")
        self.serviceboxR.setEnabled(True)
        self.serviceboxR.setGeometry(QRect(70, 260, 191, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.serviceboxR.setFont(font1)
        self.serviceboxR.setEditable(False)
        self.serviceboxR.setFrame(True)
        self.serviceName = QLineEdit(vServices)
        self.serviceName.setObjectName(u"serviceName")
        self.serviceName.setGeometry(QRect(70, 290, 191, 22))
        font2 = QFont()
        font2.setPointSize(10)
        self.serviceName.setFont(font2)
        self.serviceName.setStyleSheet(u"")
        self.serviceName.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.backv = QPushButton(vServices)
        self.backv.setObjectName(u"backv")
        self.backv.setGeometry(QRect(30, 20, 75, 23))
        self.vdate = QDateEdit(vServices)
        self.vdate.setObjectName(u"vdate")
        self.vdate.setGeometry(QRect(150, 320, 91, 20))
        self.vdate.setCalendarPopup(True)
        self.vtime = QTimeEdit(vServices)
        self.vtime.setObjectName(u"vtime")
        self.vtime.setGeometry(QRect(150, 350, 71, 20))
        self.vtime.setCalendarPopup(False)
        self.label = QLabel(vServices)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(111, 321, 27, 16))
        self.label_2 = QLabel(vServices)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(111, 351, 26, 16))
        self.label_3 = QLabel(vServices)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 380, 41, 21))
        self.spinBox = QSpinBox(vServices)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(160, 380, 42, 22))
        self.label_4 = QLabel(vServices)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 400, 61, 21))
        self.label_5 = QLabel(vServices)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 30, 401, 211))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.studentList = QListWidget(vServices)
        self.studentList.setObjectName(u"studentList")
        self.studentList.setGeometry(QRect(1020, 270, 181, 291))
        self.studentList.setFont(font)
        self.studentList.setFocusPolicy(Qt.StrongFocus)
        self.studentList.setFrameShape(QFrame.NoFrame)
        self.studentList.setSpacing(1)
        self.label_6 = QLabel(vServices)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(920, 230, 181, 31))
        self.numStudents = QLabel(vServices)
        self.numStudents.setObjectName(u"numStudents")
        self.numStudents.setGeometry(QRect(890, 230, 51, 31))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.numStudents.setFont(font4)

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
        ___qtablewidgetitem4 = self.servicesTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("vServices", u"Length", None));
        ___qtablewidgetitem5 = self.servicesTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("vServices", u"Service ID", None));
        self.addService.setText(QCoreApplication.translate("vServices", u"Add Service", None))
        self.serviceboxR.setItemText(0, QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceboxR.setItemText(1, QCoreApplication.translate("vServices", u"Advice", None))
        self.serviceboxR.setItemText(2, QCoreApplication.translate("vServices", u"Operation", None))

        self.serviceboxR.setCurrentText(QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceName.setPlaceholderText(QCoreApplication.translate("vServices", u"Enter Service Name ", None))
        self.backv.setText(QCoreApplication.translate("vServices", u"Back", None))
        self.vtime.setDisplayFormat(QCoreApplication.translate("vServices", u"HH:mm", None))
        self.label.setText(QCoreApplication.translate("vServices", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("vServices", u"Time:", None))
        self.label_3.setText(QCoreApplication.translate("vServices", u"Length:", None))
        self.label_4.setText(QCoreApplication.translate("vServices", u"(in hours)", None))
        self.label_5.setText(QCoreApplication.translate("vServices", u"<html><head/><body><p>Services Cost:</p><p align=\"center\">Advice: 50 points per hour</p><p align=\"center\">   Lecture: 150 points per hour</p><p align=\"center\">     Spectate: 200 points per hour</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("vServices", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Students interested:</span></p></body></html>", None))
        self.numStudents.setText(QCoreApplication.translate("vServices", u"0", None))
    # retranslateUi

