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
        self.servicesTable.setGeometry(QRect(370, 250, 531, 331))
        self.servicesTable.setFrameShadow(QFrame.Sunken)
        self.servicesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.servicesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.servicesTable.setSortingEnabled(True)
        self.servicesTable.setRowCount(10)
        self.serviceboxR = QComboBox(vServices)
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.addItem("")
        self.serviceboxR.setObjectName(u"serviceboxR")
        self.serviceboxR.setEnabled(True)
        self.serviceboxR.setGeometry(QRect(190, 220, 121, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.serviceboxR.setFont(font1)
        self.serviceboxR.setEditable(False)
        self.serviceboxR.setFrame(True)
        self.serviceName = QLineEdit(vServices)
        self.serviceName.setObjectName(u"serviceName")
        self.serviceName.setGeometry(QRect(160, 270, 191, 22))
        font2 = QFont()
        font2.setPointSize(10)
        self.serviceName.setFont(font2)
        self.serviceName.setStyleSheet(u"")
        self.serviceName.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.vdate = QDateEdit(vServices)
        self.vdate.setObjectName(u"vdate")
        self.vdate.setGeometry(QRect(160, 320, 91, 20))
        self.vdate.setCalendarPopup(True)
        self.vtime = QTimeEdit(vServices)
        self.vtime.setObjectName(u"vtime")
        self.vtime.setGeometry(QRect(160, 370, 71, 20))
        self.vtime.setCalendarPopup(False)
        self.spinBox = QSpinBox(vServices)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(160, 420, 42, 22))
        self.label_5 = QLabel(vServices)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 40, 401, 141))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.studentList = QListWidget(vServices)
        self.studentList.setObjectName(u"studentList")
        self.studentList.setGeometry(QRect(1040, 280, 181, 291))
        self.studentList.setFont(font)
        self.studentList.setFocusPolicy(Qt.StrongFocus)
        self.studentList.setFrameShape(QFrame.NoFrame)
        self.studentList.setSpacing(1)
        self.label_6 = QLabel(vServices)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(920, 240, 181, 31))
        self.label_6.setStyleSheet(u"color:white;\n"
"text-align:center;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;")
        self.numStudents = QLabel(vServices)
        self.numStudents.setObjectName(u"numStudents")
        self.numStudents.setGeometry(QRect(1110, 240, 51, 31))
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.numStudents.setFont(font4)
        self.numStudents.setStyleSheet(u"color:white;\n"
"text-align:center;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;")
        self.backv = QPushButton(vServices)
        self.backv.setObjectName(u"backv")
        self.backv.setGeometry(QRect(10, 10, 91, 31))
        font5 = QFont()
        font5.setFamilies([u"century gothic"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.backv.setFont(font5)
        self.backv.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")
        self.pushButton = QPushButton(vServices)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 220, 161, 31))
        font6 = QFont()
        font6.setFamilies([u"century gothic"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.pushButton.setFont(font6)
        self.pushButton.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/newPrefix/img/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(42, 79))
        self.pushButton_2 = QPushButton(vServices)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 260, 131, 41))
        self.pushButton_2.setFont(font6)
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(42, 79))
        self.pushButton_3 = QPushButton(vServices)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 310, 131, 41))
        self.pushButton_3.setFont(font6)
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(42, 79))
        self.pushButton_4 = QPushButton(vServices)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 360, 131, 41))
        self.pushButton_4.setFont(font6)
        self.pushButton_4.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(42, 79))
        self.pushButton_5 = QPushButton(vServices)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 410, 131, 41))
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(42, 79))
        self.addService = QPushButton(vServices)
        self.addService.setObjectName(u"addService")
        self.addService.setGeometry(QRect(140, 470, 151, 41))
        self.addService.setFont(font5)
        self.addService.setStyleSheet(u"QPushButton\n"
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
"background:rgb(0, 140, 227);\n"
"}")

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
        self.serviceboxR.setItemText(0, QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceboxR.setItemText(1, QCoreApplication.translate("vServices", u"Advice", None))
        self.serviceboxR.setItemText(2, QCoreApplication.translate("vServices", u"Operation", None))

        self.serviceboxR.setCurrentText(QCoreApplication.translate("vServices", u"Lecture", None))
        self.serviceName.setPlaceholderText(QCoreApplication.translate("vServices", u"Enter Service Name ", None))
        self.vtime.setDisplayFormat(QCoreApplication.translate("vServices", u"HH:mm", None))
        self.label_5.setText(QCoreApplication.translate("vServices", u"<html><head/><body><p>-Services Cost:</p><p align=\"center\">Advice: 50 points per hour</p><p align=\"center\">Lecture: 150 points per hour</p><p align=\"center\">Spectate: 200 points per hour</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("vServices", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Students interested:</span></p></body></html>", None))
        self.numStudents.setText(QCoreApplication.translate("vServices", u"<html><head/><body><p align=\"center\">0</p></body></html>", None))
        self.backv.setText(QCoreApplication.translate("vServices", u"Back", None))
        self.pushButton.setText(QCoreApplication.translate("vServices", u"Choose service type:", None))
        self.pushButton_2.setText(QCoreApplication.translate("vServices", u"Service name:", None))
        self.pushButton_3.setText(QCoreApplication.translate("vServices", u"Date:", None))
        self.pushButton_4.setText(QCoreApplication.translate("vServices", u"Time:", None))
        self.pushButton_5.setText(QCoreApplication.translate("vServices", u"Length:\n"
"(in hrs)", None))
        self.addService.setText(QCoreApplication.translate("vServices", u"Add Service", None))
    # retranslateUi

