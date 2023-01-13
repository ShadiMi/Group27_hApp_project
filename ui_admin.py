# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(1260, 778)
        Admin.setStyleSheet(u"\n"
"QFrame\n"
"{\n"
"background:rgba(99, 0, 0,0.7);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.stackedWidget = QStackedWidget(Admin)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(280, 30, 871, 651))
        self.stackedWidget.setStyleSheet(u"background:rgba(99, 0, 0,0.3);")
        self.stackedWidget.setFrameShape(QFrame.Panel)
        self.stackedWidget.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.setLineWidth(5)
        self.spage = QWidget()
        self.spage.setObjectName(u"spage")
        self.sTable = QTableWidget(self.spage)
        if (self.sTable.columnCount() < 7):
            self.sTable.setColumnCount(7)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setForeground(brush);
        self.sTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.sTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.sTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.sTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.sTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.sTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.sTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.sTable.rowCount() < 100):
            self.sTable.setRowCount(100)
        self.sTable.setObjectName(u"sTable")
        self.sTable.setGeometry(QRect(0, 40, 861, 561))
        self.sTable.setStyleSheet(u"QTableWidget{\n"
"border: 0px solid blue\n"
"}")
        self.sTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sTable.setSortingEnabled(True)
        self.sTable.setRowCount(100)
        self.servicesL = QLabel(self.spage)
        self.servicesL.setObjectName(u"servicesL")
        self.servicesL.setGeometry(QRect(170, 10, 81, 21))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.servicesL.setFont(font1)
        self.servicesL.setStyleSheet(u"background:transparent")
        self.complete = QPushButton(self.spage)
        self.complete.setObjectName(u"complete")
        self.complete.setGeometry(QRect(180, 610, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"century gothic"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.complete.setFont(font2)
        self.complete.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.decline = QPushButton(self.spage)
        self.decline.setObjectName(u"decline")
        self.decline.setGeometry(QRect(300, 610, 101, 31))
        self.decline.setFont(font2)
        self.decline.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.stackedWidget.addWidget(self.spage)
        self.upage = QWidget()
        self.upage.setObjectName(u"upage")
        self.uTable = QTableWidget(self.upage)
        if (self.uTable.columnCount() < 5):
            self.uTable.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.uTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.uTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.uTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.uTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.uTable.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        if (self.uTable.rowCount() < 100):
            self.uTable.setRowCount(100)
        self.uTable.setObjectName(u"uTable")
        self.uTable.setGeometry(QRect(0, 40, 861, 561))
        self.uTable.setStyleSheet(u"background:rgba(99, 0, 0,0.3);")
        self.uTable.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.uTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.uTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.uTable.setShowGrid(True)
        self.uTable.setGridStyle(Qt.SolidLine)
        self.uTable.setSortingEnabled(True)
        self.uTable.setRowCount(100)
        self.usersL = QLabel(self.upage)
        self.usersL.setObjectName(u"usersL")
        self.usersL.setGeometry(QRect(190, 10, 48, 21))
        self.usersL.setFont(font1)
        self.usersL.setStyleSheet(u"background:transparent")
        self.deleteU = QPushButton(self.upage)
        self.deleteU.setObjectName(u"deleteU")
        self.deleteU.setGeometry(QRect(380, 610, 111, 31))
        self.deleteU.setFont(font2)
        self.deleteU.setStyleSheet(u"QPushButton\n"
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
"background:rgba(99, 0, 0,0.7);\n"
"}")
        self.addPointsPB = QPushButton(self.upage)
        self.addPointsPB.setObjectName(u"addPointsPB")
        self.addPointsPB.setGeometry(QRect(160, 610, 111, 31))
        self.addPointsPB.setFont(font2)
        self.addPointsPB.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.pointsF = QLineEdit(self.upage)
        self.pointsF.setObjectName(u"pointsF")
        self.pointsF.setGeometry(QRect(70, 610, 81, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pointsF.setFont(font3)
        self.pointsF.setStyleSheet(u"color:rgb(194, 194, 194);\n"
"background:rgba(6, 16, 28,1);")
        self.stackedWidget.addWidget(self.upage)
        self.frame_4 = QFrame(Admin)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(160, 280, 121, 111))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.servicesPB = QPushButton(self.frame_4)
        self.servicesPB.setObjectName(u"servicesPB")
        self.servicesPB.setGeometry(QRect(10, 60, 101, 31))
        self.servicesPB.setFont(font2)
        self.servicesPB.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.usersPB = QPushButton(self.frame_4)
        self.usersPB.setObjectName(u"usersPB")
        self.usersPB.setGeometry(QRect(10, 10, 101, 31))
        self.usersPB.setFont(font2)
        self.usersPB.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.frame = QFrame(Admin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(90, 630, 141, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logoutPB = QPushButton(self.frame)
        self.logoutPB.setObjectName(u"logoutPB")
        self.logoutPB.setGeometry(QRect(20, 10, 101, 31))
        self.logoutPB.setFont(font2)
        self.logoutPB.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.frame_2 = QFrame(Admin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(80, 80, 151, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.userR = QLineEdit(self.frame_2)
        self.userR.setObjectName(u"userR")
        self.userR.setGeometry(QRect(20, 10, 101, 20))
        self.resetPw = QPushButton(self.frame_2)
        self.resetPw.setObjectName(u"resetPw")
        self.resetPw.setGeometry(QRect(10, 40, 131, 31))
        self.resetPw.setFont(font2)
        self.resetPw.setStyleSheet(u"QPushButton\n"
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
"background:rgba(6, 16, 28,1);\n"
"}")

        self.retranslateUi(Admin)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(QCoreApplication.translate("Admin", u"Admin", None))
        ___qtablewidgetitem = self.sTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Admin", u"serviceID", None));
        ___qtablewidgetitem1 = self.sTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Admin", u"User", None));
        ___qtablewidgetitem2 = self.sTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Admin", u"Type", None));
        ___qtablewidgetitem3 = self.sTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Admin", u"Name", None));
        ___qtablewidgetitem4 = self.sTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Admin", u"Date", None));
        ___qtablewidgetitem5 = self.sTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Admin", u"Length", None));
        ___qtablewidgetitem6 = self.sTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Admin", u"Status", None));
        self.servicesL.setText(QCoreApplication.translate("Admin", u"<html><head/><body><p><span style=\" color:#c2c2c2;\">Services</span></p></body></html>", None))
        self.complete.setText(QCoreApplication.translate("Admin", u"Approve", None))
        self.decline.setText(QCoreApplication.translate("Admin", u"Decline", None))
        ___qtablewidgetitem7 = self.uTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Admin", u"ID", None));
        ___qtablewidgetitem8 = self.uTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Admin", u"Name", None));
        ___qtablewidgetitem9 = self.uTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Admin", u"Profile", None));
        ___qtablewidgetitem10 = self.uTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Admin", u"Points", None));
        ___qtablewidgetitem11 = self.uTable.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Admin", u"Hours", None));
        self.usersL.setText(QCoreApplication.translate("Admin", u"Users", None))
        self.deleteU.setText(QCoreApplication.translate("Admin", u"Delete User", None))
        self.addPointsPB.setText(QCoreApplication.translate("Admin", u"Add Points", None))
        self.pointsF.setText("")
        self.pointsF.setPlaceholderText(QCoreApplication.translate("Admin", u"Points", None))
        self.servicesPB.setText(QCoreApplication.translate("Admin", u"Services", None))
        self.usersPB.setText(QCoreApplication.translate("Admin", u"Users", None))
        self.logoutPB.setText(QCoreApplication.translate("Admin", u"Logout", None))
        self.userR.setPlaceholderText(QCoreApplication.translate("Admin", u"Username", None))
        self.resetPw.setText(QCoreApplication.translate("Admin", u"Reset Password", None))
    # retranslateUi

