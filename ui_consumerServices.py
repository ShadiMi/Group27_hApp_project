# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consumerServices.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QWidget)
import stChoices_rc

class Ui_stChoices(object):
    def setupUi(self, stChoices):
        if not stChoices.objectName():
            stChoices.setObjectName(u"stChoices")
        stChoices.resize(1280, 768)
        stChoices.setStyleSheet(u"\n"
"QFrame\n"
"{\n"
"background:rgba(99, 0, 0,0.7);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame = QFrame(stChoices)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 160, 261, 491))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.spectate = QPushButton(self.frame)
        self.spectate.setObjectName(u"spectate")
        self.spectate.setGeometry(QRect(90, 50, 81, 71))
        self.spectate.setStyleSheet(u"QPushButton\n"
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
"background:skyblue\n"
"}")
        icon = QIcon()
        icon.addFile(u":/consumerChoicesimgs/hos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.spectate.setIcon(icon)
        self.spectate.setIconSize(QSize(53, 47))
        self.consultation = QPushButton(self.frame)
        self.consultation.setObjectName(u"consultation")
        self.consultation.setGeometry(QRect(90, 170, 81, 71))
        self.consultation.setStyleSheet(u"QPushButton\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/consumerChoicesimgs/consulatin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.consultation.setIcon(icon1)
        self.consultation.setIconSize(QSize(62, 67))
        self.consultation.setCheckable(True)
        self.lecture = QPushButton(self.frame)
        self.lecture.setObjectName(u"lecture")
        self.lecture.setGeometry(QRect(90, 290, 81, 71))
        self.lecture.setStyleSheet(u"QPushButton\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/consumerChoicesimgs/lec2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lecture.setIcon(icon2)
        self.lecture.setIconSize(QSize(50, 59))
        self.consultationL = QLabel(self.frame)
        self.consultationL.setObjectName(u"consultationL")
        self.consultationL.setGeometry(QRect(60, 120, 141, 51))
        font = QFont()
        font.setFamilies([u"century gothic"])
        font.setBold(True)
        self.consultationL.setFont(font)
        self.consultationL.setStyleSheet(u"QLabel\n"
"{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.spectateL = QLabel(self.frame)
        self.spectateL.setObjectName(u"spectateL")
        self.spectateL.setGeometry(QRect(60, 0, 141, 51))
        self.spectateL.setFont(font)
        self.spectateL.setStyleSheet(u"QLabel\n"
"{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.lectureL = QLabel(self.frame)
        self.lectureL.setObjectName(u"lectureL")
        self.lectureL.setGeometry(QRect(60, 240, 141, 51))
        self.lectureL.setFont(font)
        self.lectureL.setStyleSheet(u"QLabel\n"
"{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.all = QPushButton(self.frame)
        self.all.setObjectName(u"all")
        self.all.setGeometry(QRect(90, 400, 81, 71))
        self.all.setStyleSheet(u"QPushButton\n"
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
        self.all.setIcon(icon2)
        self.all.setIconSize(QSize(50, 59))
        self.allL = QLabel(self.frame)
        self.allL.setObjectName(u"allL")
        self.allL.setGeometry(QRect(60, 360, 141, 51))
        self.allL.setFont(font)
        self.allL.setStyleSheet(u"QLabel\n"
"{\n"
"\n"
"background:transparent;\n"
"\n"
"}")
        self.pushButton = QPushButton(stChoices)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 130, 161, 31))
        font1 = QFont()
        font1.setFamilies([u"century gothic"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/img/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(42, 79))
        self.nameL = QLabel(stChoices)
        self.nameL.setObjectName(u"nameL")
        self.nameL.setGeometry(QRect(380, 20, 171, 71))
        font2 = QFont()
        font2.setFamilies([u"century gothic"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.nameL.setFont(font2)
        self.nameL.setStyleSheet(u"color:rgb(194, 194, 194)")
        self.ptsL = QLabel(stChoices)
        self.ptsL.setObjectName(u"ptsL")
        self.ptsL.setGeometry(QRect(640, 20, 161, 71))
        self.ptsL.setFont(font2)
        self.ptsL.setStyleSheet(u"color:rgb(194, 194, 194)")
        self.frame_2 = QFrame(stChoices)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(280, 160, 661, 491))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(9, 10, 641, 471))
        self.stackedWidget.setStyleSheet(u"background:transparent;")
        self.allP = QWidget()
        self.allP.setObjectName(u"allP")
        self.allTable = QTableWidget(self.allP)
        if (self.allTable.columnCount() < 7):
            self.allTable.setColumnCount(7)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.allTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.allTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.allTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.allTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.allTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.allTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.allTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.allTable.rowCount() < 20):
            self.allTable.setRowCount(20)
        self.allTable.setObjectName(u"allTable")
        self.allTable.setGeometry(QRect(0, 0, 641, 441))
        self.allTable.setStyleSheet(u"background:rgb(194, 194, 194)")
        self.allTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.allTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.allTable.setRowCount(20)
        self.stackedWidget.addWidget(self.allP)
        self.sp = QWidget()
        self.sp.setObjectName(u"sp")
        self.spectateTable = QTableWidget(self.sp)
        if (self.spectateTable.columnCount() < 7):
            self.spectateTable.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font3);
        self.spectateTable.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        if (self.spectateTable.rowCount() < 20):
            self.spectateTable.setRowCount(20)
        self.spectateTable.setObjectName(u"spectateTable")
        self.spectateTable.setGeometry(QRect(0, 0, 641, 441))
        self.spectateTable.setStyleSheet(u"background:rgb(194, 194, 194)")
        self.spectateTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.spectateTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.spectateTable.setRowCount(20)
        self.stackedWidget.addWidget(self.sp)
        self.cp = QWidget()
        self.cp.setObjectName(u"cp")
        self.consultationTable = QTableWidget(self.cp)
        if (self.consultationTable.columnCount() < 7):
            self.consultationTable.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font3);
        self.consultationTable.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        if (self.consultationTable.rowCount() < 20):
            self.consultationTable.setRowCount(20)
        self.consultationTable.setObjectName(u"consultationTable")
        self.consultationTable.setGeometry(QRect(0, 0, 641, 441))
        self.consultationTable.setStyleSheet(u"background:rgb(194, 194, 194)")
        self.consultationTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.consultationTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.consultationTable.setRowCount(20)
        self.stackedWidget.addWidget(self.cp)
        self.lp = QWidget()
        self.lp.setObjectName(u"lp")
        self.lectureTable = QTableWidget(self.lp)
        if (self.lectureTable.columnCount() < 7):
            self.lectureTable.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font3);
        self.lectureTable.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        if (self.lectureTable.rowCount() < 20):
            self.lectureTable.setRowCount(20)
        self.lectureTable.setObjectName(u"lectureTable")
        self.lectureTable.setGeometry(QRect(0, 0, 641, 441))
        self.lectureTable.setStyleSheet(u"background:rgb(194, 194, 194)")
        self.lectureTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.lectureTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lectureTable.setRowCount(20)
        self.stackedWidget.addWidget(self.lp)
        self.frame_3 = QFrame(stChoices)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(560, 630, 381, 61))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.signupButton = QPushButton(self.frame_3)
        self.signupButton.setObjectName(u"signupButton")
        self.signupButton.setGeometry(QRect(270, 20, 101, 31))
        font4 = QFont()
        font4.setFamilies([u"century gothic"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.signupButton.setFont(font4)
        self.signupButton.setStyleSheet(u"QPushButton\n"
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
        self.error = QLabel(self.frame_3)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(30, 30, 221, 20))
        self.error.setStyleSheet(u"background:transparent;\n"
"color:red;")
        self.frame_4 = QFrame(stChoices)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 20, 121, 51))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.back = QPushButton(self.frame_4)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(10, 10, 101, 31))
        self.back.setFont(font4)
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
"background:rgba(6, 16, 28,1);\n"
"}")
        self.frame_5 = QFrame(stChoices)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(950, 160, 311, 491))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.listWidget = QListWidget(self.frame_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 20, 291, 431))
        self.listWidget.setStyleSheet(u"background:rgb(194, 194, 194)")
        self.pushButton_2 = QPushButton(stChoices)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(480, 130, 241, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(42, 79))
        self.pushButton_3 = QPushButton(stChoices)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1030, 130, 161, 31))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton\n"
"\n"
"{\n"
"color:white;\n"
"background:rgba(6, 16, 28,1);\n"
"border-radius:15px;\n"
"}")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(42, 79))

        self.retranslateUi(stChoices)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(stChoices)
    # setupUi

    def retranslateUi(self, stChoices):
        stChoices.setWindowTitle(QCoreApplication.translate("stChoices", u"Form", None))
        self.spectate.setText("")
        self.consultation.setText("")
#if QT_CONFIG(tooltip)
        self.lecture.setToolTip(QCoreApplication.translate("stChoices", u"lecture", None))
#endif // QT_CONFIG(tooltip)
        self.lecture.setText("")
#if QT_CONFIG(tooltip)
        self.consultationL.setToolTip(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\">LOGIN HERE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.consultationL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Cosultation</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.spectateL.setToolTip(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\">LOGIN HERE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spectateL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Spectate</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.lectureL.setToolTip(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\">LOGIN HERE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lectureL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">Lecture</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.all.setToolTip(QCoreApplication.translate("stChoices", u"lecture", None))
#endif // QT_CONFIG(tooltip)
        self.all.setText("")
#if QT_CONFIG(tooltip)
        self.allL.setToolTip(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\">LOGIN HERE</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.allL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; color:#ffffff;\">All</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("stChoices", u"choices:", None))
        self.nameL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" color:#c2c2c2;\">Name</span></p></body></html>", None))
        self.ptsL.setText(QCoreApplication.translate("stChoices", u"<html><head/><body><p align=\"center\"><span style=\" color:#c2c2c2;\">Points</span></p></body></html>", None))
        ___qtablewidgetitem = self.allTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stChoices", u"Name", None));
        ___qtablewidgetitem1 = self.allTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stChoices", u"Volunteer", None));
        ___qtablewidgetitem2 = self.allTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stChoices", u"Length", None));
        ___qtablewidgetitem3 = self.allTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("stChoices", u"Type", None));
        ___qtablewidgetitem4 = self.allTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("stChoices", u"Cost", None));
        ___qtablewidgetitem5 = self.allTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("stChoices", u"Date", None));
        ___qtablewidgetitem6 = self.allTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("stChoices", u"ID", None));
        ___qtablewidgetitem7 = self.spectateTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("stChoices", u"Name", None));
        ___qtablewidgetitem8 = self.spectateTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("stChoices", u"Volunteer", None));
        ___qtablewidgetitem9 = self.spectateTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("stChoices", u"Length", None));
        ___qtablewidgetitem10 = self.spectateTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("stChoices", u"Type", None));
        ___qtablewidgetitem11 = self.spectateTable.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("stChoices", u"Cost", None));
        ___qtablewidgetitem12 = self.spectateTable.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("stChoices", u"Date", None));
        ___qtablewidgetitem13 = self.spectateTable.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("stChoices", u"ID", None));
        ___qtablewidgetitem14 = self.consultationTable.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("stChoices", u"Name", None));
        ___qtablewidgetitem15 = self.consultationTable.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("stChoices", u"Volunteer", None));
        ___qtablewidgetitem16 = self.consultationTable.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("stChoices", u"Length", None));
        ___qtablewidgetitem17 = self.consultationTable.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("stChoices", u"Type", None));
        ___qtablewidgetitem18 = self.consultationTable.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("stChoices", u"Cost", None));
        ___qtablewidgetitem19 = self.consultationTable.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("stChoices", u"Date", None));
        ___qtablewidgetitem20 = self.consultationTable.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("stChoices", u"ID", None));
        ___qtablewidgetitem21 = self.lectureTable.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("stChoices", u"Name", None));
        ___qtablewidgetitem22 = self.lectureTable.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("stChoices", u"Volunteer", None));
        ___qtablewidgetitem23 = self.lectureTable.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("stChoices", u"Length", None));
        ___qtablewidgetitem24 = self.lectureTable.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("stChoices", u"Type", None));
        ___qtablewidgetitem25 = self.lectureTable.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("stChoices", u"Cost", None));
        ___qtablewidgetitem26 = self.lectureTable.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("stChoices", u"Date", None));
        ___qtablewidgetitem27 = self.lectureTable.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("stChoices", u"ID", None));
        self.signupButton.setText(QCoreApplication.translate("stChoices", u"Signup", None))
        self.error.setText("")
        self.back.setText(QCoreApplication.translate("stChoices", u"Back", None))
        self.pushButton_2.setText(QCoreApplication.translate("stChoices", u"Available Services", None))
        self.pushButton_3.setText(QCoreApplication.translate("stChoices", u"Schedule", None))
    # retranslateUi

