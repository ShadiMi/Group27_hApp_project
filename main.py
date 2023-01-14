import datetime
import os
import sqlite3
import sys

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QListWidgetItem, QCheckBox, \
    QMessageBox
from ui_welcome import Ui_MainWindow
from ui_login import Ui_login
from ui_signup import Ui_create
from ui_volunteer import Ui_volunteerprofile
from ui_consumer import Ui_conumerprofile
from ui_logout import Ui_confirmlogout
from ui_vServices import Ui_vServices
from ui_admin import Ui_Admin
from ui_coupon import Ui_coupons
from ui_changeinfo import Ui_changeprofile
from ui_consumerServices import Ui_stChoices

import Person
import random

uv = Person.volunteer()
uc = Person.consumer()
ua = Person.admin()
uv.profile = None
uc.profile = None
ua.profile = None
welcomeFlag=False
loginFlag=False
signupFlag=False
volunteerFlag=False
consumerFlag=False
adminFlag=False
volunteerServicesFlag=False
consumerServicesFlag=False
logoutFlag=False
changeinfoFlag=False
vCouponFlag=False




def database(user):
    conn = sqlite3.connect("hAppDB.db")
    cur = conn.cursor()
    query = 'SELECT * FROM users WHERE Username =\'' + user + "\'"
    cur.execute(query)
    result = cur.fetchone()
    print(result)
    if result != None:
        if result[3] == 'Admin':
            ua.username = result[0]
            ua.email = result[1]
            ua.password = result[2]
            ua.profile = result[3]
            ua.points = result[4]
            cur.close()
            return ua

        elif result[3] == 'Volunteer':
            uv.username = result[0]
            uv.email = result[1]
            uv.password = result[2]
            uv.profile = result[3]
            uv.points = result[4]
            uv.hours = result[5]
            cur.close()
            return uv
        else:
            uc.username = result[0]
            uc.email = result[1]
            uc.password = result[2]
            uc.profile = result[3]
            uc.points = result[4]
            cur.close()
            return uc


"""------------------------------------------------------------------------------------------------------------------------------------
Login Window"""
class loginWindow(QWidget, Ui_login):
    loginFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.loginSucessFlag = False
        self.setupUi(self)
        self.back.clicked.connect(self.gohome)
        self.loginL.clicked.connect(self.loginfunc)

    def paintEvent(self, event):
        self.tile = QPixmap("loginBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_login, self)

    def gohome(self):
        self.close()
        window.show()

    def goVolunteer(self):
        self.windowV = volunteerWindow()
        self.close()
        self.windowV.show()

    def goConsumer(self):
        self.windowC = consumerWindow()
        self.close()
        self.windowC.show()

    def goAdmin(self):
        self.windowA = adminWindow()
        self.close()
        self.windowA.show()

    def loginfunc(self):


        user = self.usernameLF.text()
        password = self.passwordLF.text()

        if len(user) == 0 or len(password) == 0:
            self.label_2.setStyleSheet(u"color: red;\n"
                                       "background:setAttribute(Qt::WA_TranslucentBackground)")
            self.label_2.setText("Please input all fields.")

        else:
            person = database(user)
            if person != None:
                result_pass = person.password
                result_prof = person.profile

            else:
                result_pass = 'NULL'
                result_prof = 'NULL'

            if result_pass == password:
                print("Successfully logged in.")
                self.label_2.setText("Successfully logged in.")
                self.loginSucessFlag=True
                print(result_pass)

                if result_prof == 'Admin':
                    self.goAdmin()

                if result_prof == 'Volunteer':
                    self.goVolunteer()

                if result_prof == 'Consumer':
                    self.goConsumer()
            else:

                print("Invalid password")
                self.label_2.setStyleSheet(u"color: red;\n"
                                           "background:setAttribute(Qt::WA_TranslucentBackground)")
                self.label_2.setText("Invalid username or password")


"""------------------------------------------------------------------------------------------------------------------------------------
Volunteer's Services Window"""
class volunteerServicesWindow(QWidget, Ui_vServices):
    volunteerServicesFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.addService.clicked.connect(self.addvServiceFunc)
        self.sTable()
        self.backv.clicked.connect(self.goVolunteer)
        self.vdate.setMinimumDate(QDate.currentDate())
        self.servicesTable.itemClicked.connect(self.serviceSelectedChanged)


    def paintEvent(self, event):
        self.tile = QPixmap("volunteerBG.png")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_vServices, self)


    def goVolunteer(self):
        self.windowV = volunteerWindow()
        self.close()
        self.windowV.show()

    def addvServiceFunc(self):
        servicetype = self.serviceboxR.currentText()
        servicesName = self.serviceName.text()
        servicesDate = self.vdate.date()
        serviceTime = self.vtime.time()
        if servicetype == "Advice":
            cost = 50
        elif servicetype == "Lecture":
            cost = 150
        else:
            cost = 200
        st = 'Incomplete'
        print(servicesDate)
        sDate = servicesDate.toPython()
        sTime = serviceTime.toString('hh:mm')
        sLength=self.spinBox.text()
        print(sDate, '  ', sTime)
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO servicesTB (Username,servicetype,servicename,Date,Time,Length,Cost,Status) VALUES (?,?,?,?,?,?,?,?)",
            (uv.username, servicetype, servicesName, sDate, sTime,sLength, cost, st))
        db.commit()
        cursor.close()
        print("Records created successfully")
        self.sTable()
        self.update()

    def sTable(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        query = 'SELECT servicetype,servicename,Date,Time,Length,serviceID FROM servicesTB WHERE Username =\'' + uv.username + "\'"
        tablerow = 0
        for row in cur.execute(query):
            self.servicesTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.servicesTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.servicesTable.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.servicesTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.servicesTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.servicesTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            tablerow += 1

    def serviceSelectedChanged(self):
        print("Service")
        servicetSelected = self.servicesTable.selectedItems().pop(5)
        print(servicetSelected.text())
        self.updateList(servicetSelected.text())

    def updateList(self, sID):
        self.studentList.clear()
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query = 'SELECT Username FROM consumerTB WHERE serviceID=?'

        counter=0
        results = cursor.execute(query, [sID]).fetchall()
        for result in results:
            item = QListWidgetItem(str(counter+1)+'.'+str(result[0]))
            self.studentList.addItem(item)
            counter=counter+1
        self.numStudents.setText(str(counter))



"""------------------------------------------------------------------------------------------------------------------------------------
Volunteer Window"""
class volunteerWindow(QWidget, Ui_volunteerprofile):
    volunteerFlag=True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.welcomemsg_3.setText(uv.username + '!')
        self.welcomemsg_2.setText('nice to see you again!')
        self.filler1.setText(str(uv.points))
        self.filler2.setText(str(uv.hours))
        self.ptsIcd.display((uv.points))
        self.hrsIcd.display(uv.hours)
        self.vlogout.clicked.connect(self.gologout)
        self.vservices.clicked.connect(self.goservices)
        self.svCalendar.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.updateService)
        self.vcoupon.clicked.connect(self.goCoupons)
        self.vprofile.clicked.connect(self.goprofile)

    def paintEvent(self, event):
        self.tile = QPixmap("volunteerBG.png")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_volunteerprofile, self)

    def updateService(self):
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        Date = self.svCalendar.selectedDate().toPython()

        for i in range(self.svListWidget.count()):
            item = self.svListWidget.item(i)
            task = item.text()
            if item.checkState() == Qt.CheckState.Checked:
                query = "UPDATE servicesTB SET Status='Complete' WHERE Date=? AND Username=?"
            else:
                query = "UPDATE servicesTB SET Status='Incomplete' WHERE Date=? AND Username=?"
            row = (Date, uv.username,)
            cursor.execute(query, row)
        db.commit()
        cursor.close()
        msgBox = QMessageBox()
        msgBox.setText("Changes saved.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def goCoupons(self):
        self.windowCoupon = couponWindow()
        self.close()
        self.windowCoupon.show()

    def gologout(self):
        self.windowLogout = logoutWindow()
        self.windowLogout.otherWindows(self)
        self.windowLogout.show()

    def goservices(self):
        self.windowvServices = volunteerServicesWindow()
        self.close()
        self.windowvServices.show()

    def goprofile(self):
        self.windowChangeinfo = changeInfoWindow()
        self.close()
        self.windowChangeinfo.show()

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.svCalendar.selectedDate().toPython()
        print("Date selected: ", dateSelected)
        self.updateCalendar(dateSelected)

    def updateCalendar(self, Date):
        self.svListWidget.clear()
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query = 'SELECT servicename,Date,Time,Status FROM servicesTB WHERE Date =? AND Username=?'
        row = (Date, uv.username,)
        results = cursor.execute(query, row).fetchall()
        for result in results:
            print(result[0])
            item = QListWidgetItem(str(result[0]) + '     ' + str(result[1]) + ' ' + str(result[2]))
            item.setCheckState(Qt.CheckState.Unchecked)
            self.svListWidget.addItem(item)


"""------------------------------------------------------------------------------------------------------------------------------------
Consumer Window"""
class consumerWindow(QWidget, Ui_conumerprofile):
    consumerFlag=True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cprofile.clicked.connect(self.goprofile)
        self.clogout.clicked.connect(self.gologout)
        self.scCalendar.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.cservicesB.clicked.connect(self.goCServices)
        self.welcomemsg.setText(uc.username)
        self.points.setText(str(uc.points))
        self.confirmBtn.clicked.connect(self.confirmCoupon)


    def paintEvent(self, event):
        self.tile = QPixmap("consumerBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_conumerprofile, self)

    def goCServices(self):
        self.cServicesWindow=consumerServicesWindow()
        self.close()
        self.cServicesWindow.show()

    def goprofile(self):
        self.windowChangeinfo = changeInfoWindow()
        self.close()
        self.windowChangeinfo.show()

    def gologout(self):
        self.windowLogout = logoutWindow()
        self.windowLogout.otherWindows(self)
        self.windowLogout.show()

    def confirmCoupon(self):
        couponField=self.couponF.text()
        print("TEST COUPONS:",couponField)
        couponField=couponField.upper()
        print("TEST COUPONS:", couponField)
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query = "SELECT Coupon,cStatus,Pts FROM couponsTB WHERE Coupon=?"
        result = cursor.execute(query,[couponField]).fetchone()
        print('result is: ', result)


        if result is None:
            self.cpnInstructionL.setStyleSheet('Color:red;\n Background:rgba(6, 16, 28,1)')
            self.cpnInstructionL.setText('  Coupon does not exist!')

        elif result[1]=='Available':
            uc.points=uc.points+result[2]
            query="UPDATE couponsTB SET cStatus='Unavailable' WHERE Coupon=?"
            cursor.execute(query,[couponField])
            db.commit()
            query="UPDATE users SET Points=? WHERE Username=?"
            row=(uc.points,uc.username)
            cursor.execute(query,row)
            db.commit()

            self.cpnInstructionL.setStyleSheet('Color:red;\n Background:rgba(6, 16, 28,1)')
            self.cpnInstructionL.setText(' Coupon redeemed, points added!')
            self.points.setText(str(uc.points))

        else:
            self.cpnInstructionL.setStyleSheet('Color:red;\n Background:rgba(6, 16, 28,1)')
            self.cpnInstructionL.setText(' Coupon already been redeemed!')









    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected = self.scCalendar.selectedDate().toPython()
        print("Date selected: ", dateSelected)
        self.updateCalendar(dateSelected)

    def updateCalendar(self, Date):
        self.scListWidget.clear()
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query = 'SELECT servicename,Date,Time,Length FROM servicesTB INNER JOIN consumerTB ON servicesTB.serviceID=consumerTB.serviceID WHERE consumerTB.Username = ? AND Date = ?'
        row=(uc.username,Date)
        results = cursor.execute(query, row).fetchall()
        print(results)
        for result in results:
            item = QListWidgetItem(str(result[0]) + '     ' + str(result[1]) + ' ' + str(result[2])+' '+str(result[3]))
            self.scListWidget.addItem(item)


"""------------------------------------------------------------------------------------------------------------------------------------
Conumers Services Window"""
class consumerServicesWindow(QWidget, Ui_stChoices):
    consumerServicesFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.cTable()
        self.updatecList()
        self.all.clicked.connect(self.goAll)
        self.consultation.clicked.connect(self.goConsult)
        self.lecture.clicked.connect(self.goLecture)
        self.spectate.clicked.connect(self.goSpectate)
        self.nameL.setText(uc.username)
        self.ptsL.setText('Points: '+str(uc.points))
        self.back.clicked.connect(self.goConsumer)
        self.stackedWidget.setCurrentIndex(0)
        self.signupButton.clicked.connect(self.signupService)

    def paintEvent(self, event):
        self.tile = QPixmap("consumerBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_stChoices, self)

    def goConsumer(self):
        self.windowC = consumerWindow()
        self.close()
        self.windowC.show()

    def goAll(self):
        self.stackedWidget.setCurrentIndex(0)
    def goConsult(self):
        self.stackedWidget.setCurrentIndex(2)
    def goLecture(self):
        self.stackedWidget.setCurrentIndex(3)
    def goSpectate(self):
        self.stackedWidget.setCurrentIndex(1)
    def cTable(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        query = 'SELECT servicename,Username,Length,servicetype,Cost,Date,serviceID FROM servicesTB'
        tablerow = 0
        for row in cur.execute(query):
            self.allTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.allTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.allTable.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.allTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.allTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.allTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.allTable.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            tablerow += 1

        query = 'SELECT servicename,Username,Length,servicetype,Cost,Date,serviceID FROM servicesTB WHERE servicetype="Operation"'
        tablerow = 0
        for row in cur.execute(query):
            self.spectateTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.spectateTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.spectateTable.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.spectateTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.spectateTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.spectateTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.spectateTable.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            tablerow += 1

        query = 'SELECT servicename,Username,Length,servicetype,Cost,Date,serviceID FROM servicesTB WHERE servicetype="Lecture"'
        tablerow = 0
        for row in cur.execute(query):
            self.lectureTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.lectureTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.lectureTable.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.lectureTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.lectureTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.lectureTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.lectureTable.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            tablerow += 1

        query = 'SELECT servicename,Username,Length,servicetype,Cost,Date,serviceID FROM servicesTB WHERE servicetype="Advice"'
        tablerow = 0
        for row in cur.execute(query):
            self.consultationTable.setItem(tablerow, 0, QTableWidgetItem(row[0]))
            self.consultationTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.consultationTable.setItem(tablerow, 2, QTableWidgetItem(str(row[2])))
            self.consultationTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.consultationTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            self.consultationTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.consultationTable.setItem(tablerow, 6, QTableWidgetItem(str(row[6])))
            tablerow += 1
    def updatecList(self):
        self.listWidget.clear()
        db = sqlite3.connect('hAppDB.db')
        cursor = db.cursor()
        query = 'SELECT servicename,Date,Time,Length FROM servicesTB INNER JOIN consumerTB ON servicesTB.serviceID=consumerTB.serviceID WHERE consumerTB.Username = ?'
        results = cursor.execute(query, [uc.username]).fetchall()
        for result in results:
            time=QTime.fromString(result[2])
            time=time.addSecs(result[3]*3600)
            item = QListWidgetItem(
                str(result[0]) + '     ' + str(result[1]) + '   ' + str(result[2]) + '-' + str(time.toString('hh:mm')))
            self.listWidget.addItem(item)
    def signupService(self):
        sID=0
        cost=0
        if self.stackedWidget.currentIndex()==0:
            sID = self.allTable.selectedItems().pop(6).text()
            cost=self.allTable.selectedItems().pop(4).text()
        elif self.stackedWidget.currentIndex()==1:
            sID = self.spectateTable.selectedItems().pop(6).text()
            cost = self.spectateTable.selectedItems().pop(4).text()
        elif self.stackedWidget.currentIndex()==2:
            sID = self.consultationTable.selectedItems().pop(6).text()
            cost = self.consultationTable.selectedItems().pop(4).text()
        else:
            sID = self.lectureTable.selectedItems().pop(6).text()
            cost = self.lectureTable.selectedItems().pop(4).text()
        print(sID)
        if uc.points>=int(cost):
            db = sqlite3.connect('hAppDB.db')
            print("Opened database successfully")
            cursor = db.cursor()
            query = "SELECT Username FROM consumerTB WHERE serviceID=? AND Username=?"
            row=(sID,uc.username)
            result=cursor.execute(query,row).fetchone()
            print('result is: ',result)

            if result is None:
                query = "INSERT INTO consumerTB  (Username,serviceID) VALUES (?,?)"
                row=(uc.username,sID)
                cursor.execute(query,row)

                uc.points=uc.points-int(cost)
                query = "UPDATE users SET Points = ? WHERE Username=?"
                row=(uc.points,uc.username)
                cursor.execute(query,row)
                db.commit()
                cursor.close()
                self.error.setStyleSheet("background:rgba(194, 194, 194,0.4);\n color:red;")
                self.error.setText("registration complete!")
            else:
                self.error.setStyleSheet("background:rgba(194, 194, 194,0.4);\n color:red;")
                self.error.setText("You're already resgistered to that service!")
        else:
            self.error.setStyleSheet("background:rgba(194, 194, 194,0.4);\n color:red;")
            self.error.setText("You dont have enough points!")
        self.cTable()
        self.ptsL.setText('Points: ' + str(uc.points))
        self.updatecList()
        self.update()



"""------------------------------------------------------------------------------------------------------------------------------------
Signup Window"""
class signupWindow(QWidget, Ui_create):
    signupFlag=True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.back2.clicked.connect(self.gohome)
        self.signupR.clicked.connect(self.createaccount)

    def paintEvent(self, event):
        self.tile = QPixmap("signupBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_create, self)

    '''SIGNUP'''

    def createaccount(self):
        u = self.usernameRF.text()
        mail = self.emailRF.text()
        pw = self.pwRF.text()
        pwc = self.pwcRF.text()
        prof = self.profboxR.currentText()
        print("start")
        if len(u) == 0 or len(pw) == 0 or len(pwc) == 0:
            self.error.setText("Please fill in all inputs.")
        elif pw != pwc:
            self.error.setText("Passwords do not match.")


        else:
            db = sqlite3.connect('hAppDB.db')
            print("Opened database successfully")
            cursor = db.cursor()
            query = 'SELECT * FROM users WHERE Username =\'' + u + "\'"
            cursor.execute(query)
            user = cursor.fetchone()
            cursor.close()

            if user != None:
                self.error.setText("Username is not available.")
                cursor.close()


            else:
                cursor = db.cursor()
                cursor.execute("INSERT INTO users (Username,Email,Password,Profile,Points,Hours) VALUES (?,?,?,?,0,0)",
                               (u, mail, pw, prof))
                db.commit()
                cursor.close()
                print("Records created successfully")
                self.gohome()

    def gohome(self):
        self.close()
        window.show()


"""------------------------------------------------------------------------------------------------------------------------------------
Logout Window"""
class logoutWindow(QWidget, Ui_confirmlogout):
    logoutFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.confirmlogout_2.clicked.connect(self.gohome)
        self.cancellogout.clicked.connect(self.gocancel)
        allWindows=None

    def otherWindows(self,x):
        self.allWindows=x

    def gocancel(self):
        self.close()

    def gohome(self):
        uv.profile = None
        uc.profile = None
        ua.profile = None
        self.close()
        self.allWindows.close()
        window.show()


"""------------------------------------------------------------------------------------------------------------------------------------
Welcome Window"""
class MainWindow(QMainWindow, Ui_MainWindow):
    welcomeFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.login.clicked.connect(self.gotologin)
        self.createacc.clicked.connect(self.gotoSignup)

    def paintEvent(self, event):
        self.tile = QPixmap("welcomeBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_MainWindow, self)

    def gotologin(self):
        self.window2 = loginWindow()
        window.close()
        self.window2.show()

    def gotoSignup(self):
        self.window3 = signupWindow()
        window.close()
        self.window3.show()


"""------------------------------------------------------------------------------------------------------------------------------------
Admin Window"""
class adminWindow(QWidget, Ui_Admin):
    adminFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.aTable()
        self.usersPB.clicked.connect(self.uWidget)
        self.servicesPB.clicked.connect(self.sWidget)
        self.complete.clicked.connect(self.updatePoints)
        self.decline.clicked.connect(self.declineService)
        self.logoutPB.clicked.connect(self.gologout)
        self.deleteU.clicked.connect(self.deleteUser)
        self.resetPw.clicked.connect(self.resetPassword)
        self.addPointsPB.clicked.connect(self.addPoints)

    def paintEvent(self, event):
        self.tile = QPixmap("consumerBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_Admin, self)

    def gologout(self):
        self.windowLogout = logoutWindow()
        self.windowLogout.otherWindows(self)
        self.windowLogout.show()

    def uWidget(self):
        self.stackedWidget.setCurrentIndex(1)

    def sWidget(self):
        self.stackedWidget.setCurrentIndex(0)

    def goAdmin(self):
        self.windowA = adminWindow()
        self.close()
        self.windowA.show()

    def aTable(self):
        self.sTable.setStyleSheet("font-weight:bold;\n color:rgb(132,132,132)")
        self.uTable.setStyleSheet("font-weight:bold;\n color:rgb(132,132,132)")
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        query = 'SELECT serviceID,Username,servicetype,servicename,Date,Length,Status FROM servicesTB'
        tablerow = 0
        for row in cur.execute(query):
            self.sTable.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.sTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.sTable.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.sTable.setItem(tablerow, 3, QTableWidgetItem(row[3]))
            self.sTable.setItem(tablerow, 4, QTableWidgetItem(row[4]))
            self.sTable.setItem(tablerow, 5, QTableWidgetItem(str(row[5])))
            self.sTable.setItem(tablerow, 6, QTableWidgetItem(row[6]))
            tablerow += 1

        query = 'SELECT rowid,Username,Profile,Points,Hours FROM users'
        tablerow = 0
        for row in cur.execute(query):
            self.uTable.setItem(tablerow, 0, QTableWidgetItem(str(row[0])))
            self.uTable.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.uTable.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.uTable.setItem(tablerow, 3, QTableWidgetItem(str(row[3])))
            self.uTable.setItem(tablerow, 4, QTableWidgetItem(str(row[4])))
            tablerow += 1

    def updatePoints(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        serviceId = self.sTable.selectedItems().pop(0).text()
        print(serviceId)
        status = self.sTable.selectedItems().pop().text()
        uname = self.sTable.selectedItems().pop(1).text()
        print(uname, ' ', status)

        query = 'SELECT Length,Cost FROM servicesTB WHERE serviceID = ?'
        cur.execute(query, [serviceId])
        result=cur.fetchone()
        length=result[0]
        cost=result[1]
        print(length,cost)

        query = 'SELECT Points,Hours FROM users WHERE Username = ?'
        print(uname)
        cur.execute(query, [uname])
        result=cur.fetchone()
        pts = result[0] + cost*length
        hrs=result[1]
        print(pts,hrs)

        hrs=hrs+length
        query = "UPDATE users SET Points = ?,Hours = ? WHERE Username=?"
        print('Updated')
        row = (pts,hrs, uname)
        cur.execute(query, row)
        conn.commit()
        cur.close()
        self.goAdmin()
        self.sWidget()

    def declineService(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        serviceId = self.sTable.selectedItems().pop(0).text()
        print(serviceId)

        query = 'DELETE FROM servicesTB WHERE serviceID=? '
        cur.execute(query, [serviceId])
        conn.commit()
        print('Deleted')
        cur.close()
        self.goAdmin()
        self.sWidget()

    def resetPassword(self):
        user = self.userR.text()
        pw = '0000'
        if user:
            conn = sqlite3.connect("hAppDB.db")
            cur = conn.cursor()
            query = "UPDATE users SET Password = ? WHERE Username=?"
            row = (pw, user)
            cur.execute(query, row)
            conn.commit()
            print(user, "'s password has been reset to 0000")
            cur.close()
            self.goAdmin()
            self.sWidget()
        else:
            print("Username is not found")

    def deleteUser(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        uname = self.uTable.selectedItems().pop(1).text()
        print(uname)

        query = 'DELETE FROM users WHERE Username=? '
        cur.execute(query, [uname])
        conn.commit()
        print('Deleted')
        cur.close()
        self.goAdmin()
        self.uWidget()

    def addPoints(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        uname = self.uTable.selectedItems().pop(1).text()
        pts= self.uTable.selectedItems().pop(3).text()
        addedPts=self.pointsF.text()
        pts=int(pts)+int(addedPts)
        print(uname)
        row=(pts,uname)

        query = 'UPDATE users SET Points=? WHERE Username=? '
        cur.execute(query, row)
        conn.commit()
        print('Deleted')
        cur.close()
        self.goAdmin()
        self.uWidget()


"""------------------------------------------------------------------------------------------------------------------------------------
User's infomation change Window"""
class changeInfoWindow(QWidget, Ui_changeprofile):
    changeinfoFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.applyB.clicked.connect(self.changeInfo)
        if self.currentProfile() == 'Consumer':
            self.cancelB.clicked.connect(self.goConsumer)

        elif self.currentProfile() == 'Volunteer':
            self.cancelB.clicked.connect(self.goVolunteer)

        else:
            self.cancelB.clicked.connect(self.goAdmin)

    def paintEvent(self, event):
        self.tile = QPixmap("infoBG.jpg")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_changeprofile, self)

    def currentProfile(self):

        if uc.profile == 'Consumer':
            return 'Consumer'
        elif uv.profile == 'Volunteer':
            return 'Volunteer'

        return 'Admin'

    def changeInfo(self):
        self.error.clear()
        self.error_2.clear()
        if self.currentProfile() == 'Consumer':
            if self.currentpwF.text() != uc.password:
                self.error.setText("Password is wrong")
            else:
                if self.newemailF.text() != '':
                    uc.email = self.newemailF.text()
                if self.newpwF.text() != '':
                    if self.newpwF.text() == self.confirmnewpwF.text():
                        uc.password = self.newpwF.text()
                    else:
                        self.error_2.setText("Passwords do not match")

                if self.newemailF.text() != '' or self.newpwF.text() != '':
                    conn = sqlite3.connect("hAppDB.db")
                    cur = conn.cursor()
                    query = "UPDATE users SET Password = ?,Email=? WHERE Username=?"
                    row = (uc.password, uc.email, uc.username)
                    cur.execute(query, row)
                    conn.commit()
                    cur.close()

        if self.currentProfile() == 'Volunteer':
            if self.currentpwF.text() != uv.password:
                self.error.setText("Password is wrong")
            else:
                if self.newemailF.text() != '':
                    uv.email = self.newemailF.text()
                if self.newpwF.text() != '':
                    if self.newpwF.text() == self.confirmnewpwF.text():
                        uv.password = self.newpwF.text()
                    else:
                        self.error_2.setText("Passwords do not match")

                if self.newemailF.text() != '' or self.newpwF.text() != '':
                    conn = sqlite3.connect("hAppDB.db")
                    cur = conn.cursor()
                    query = "UPDATE users SET Password = ?,Email=? WHERE Username=?"
                    row = (uv.password, uv.email, uv.username)
                    cur.execute(query, row)
                    conn.commit()

    def goVolunteer(self):
        self.windowV = volunteerWindow()
        self.close()
        self.windowV.show()

    def goConsumer(self):
        self.windowC = consumerWindow()
        self.close()
        self.windowC.show()

    def goAdmin(self):
        self.windowA = adminWindow()
        self.close()
        self.windowA.show()


"""------------------------------------------------------------------------------------------------------------------------------------
Volunteer's Coupons Window"""
class couponWindow(QWidget, Ui_coupons):
    vCouponFlag=True
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.filler1.setText(str(uv.points))
        self.History.clicked.connect(self.hWidget)
        self.infobtn.clicked.connect(self.iWidget)
        self.backv.clicked.connect(self.goVolunteer)
        self.initList()
        self.generate.clicked.connect(self.generateCoupon)
        self.error.setStyleSheet('color:red')

    def paintEvent(self, event):
        self.tile = QPixmap("volunteerBG.png")
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)
        super(Ui_coupons, self)

    def generateCoupon(self):
        couponStringBank = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        c = random.choice(couponStringBank)
        for i in range(5):
            c = c + random.choice(couponStringBank)

        pts = self.ptsF.text()
        if not pts.isnumeric():
            self.error.setText("invalid input")
            return
        elif (int)(pts) > uv.points:
            self.error.setText("You dont have that many points!")
            return

        stt = 'Available'

        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cur = db.cursor()
        cur.execute("INSERT INTO couponsTB (Coupon,Pts,Username,cStatus) VALUES (?,?,?,?)", (c, pts, uv.username, stt))
        db.commit()
        print("Records created successfully")

        query = "UPDATE users SET Points = ? WHERE Username=?"
        uv.points = uv.points - int(pts)
        row = (uv.points, uv.username)
        cur.execute(query, row)
        print('Updated')
        self.filler1.setText(str(uv.points))
        db.commit()
        self.initList()
        self.update()

    def goVolunteer(self):
        self.windowV = volunteerWindow()
        self.close()
        self.windowV.show()

    def hWidget(self):
        self.stackedWidget.setCurrentIndex(1)

    def iWidget(self):
        self.stackedWidget.setCurrentIndex(0)

    def initList(self):
        self.cList.clear()
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query = 'SELECT Coupon,Pts,cStatus FROM couponsTB WHERE Username=?'

        results = cursor.execute(query, [uv.username]).fetchall()
        for result in results:
            print(result[0])
            item = QListWidgetItem(
                "{:<30}".format(str(result[0])) + "{:<30}".format(str(result[1])) + "{:<15}".format(str(result[2])))
            self.cList.addItem(item)

        cursor.close()


if __name__ == "__main__":

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    window.show()
    app.exec_()
