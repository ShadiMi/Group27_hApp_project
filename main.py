import datetime
import sqlite3
import sys

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QListWidgetItem, QCheckBox, \
    QMessageBox
from ui_welcome import Ui_MainWindow
from ui_login import Ui_login
from ui_signup import Ui_create
from ui_volunteer import Ui_volunteerprofile
from ui_consumer import Ui_conumerprofile
from ui_logout import Ui_confirmlogout
from ui_vServices import Ui_vServices
import Person


uv=Person.volunteer()
uc=Person.consumer()


def database(user):
    conn = sqlite3.connect("hAppDB.db")
    cur = conn.cursor()
    query = 'SELECT * FROM users WHERE Username =\'' + user + "\'"
    cur.execute(query)
    result = cur.fetchone()
    print(result)
    if result != None:
        if result[3]=='Volunteer':
            uv.username=result[0]
            uv.email=result[1]
            uv.password=result[2]
            uv.profile=result[3]
            uv.points=result[4]
            conn.close()
            return uv
        else:
            uc.username=result[0]
            uc.email=result[1]
            uc.password=result[2]
            uc.profile=result[3]
            uc.points=result[4]
            conn.close()
            return uc


class loginWindow(QWidget, Ui_login):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.back.clicked.connect(self.gohome)
        self.loginL.clicked.connect(self.loginfunc)

    def gohome(self):
        self.close()
        window.show()

    def goVolunteer(self):
        self.windowV=volunteerWindow()
        self.close()
        self.windowV.show()

    def goConsumer(self):
        self.windowC=consumerWindow()
        self.close()
        self.windowC.show()


    def loginfunc(self):
        user=self.usernameLF.text()
        password=self.passwordLF.text()


        if len(user) == 0 or len(password) == 0:
            self.label_2.setStyleSheet(u"color: red;\n"
                                     "background:setAttribute(Qt::WA_TranslucentBackground)")
            self.label_2.setText("Please input all fields.")

        else:
            person=database(user)
            if person!=None:
                result_pass=person.password
                result_prof=person.profile

            else:
                result_pass = 'NULL'
                result_prof = 'NULL'

            if result_pass == password:
                print("Successfully logged in.")
                self.label_2.setText("Successfully logged in.")


                print(result_pass)
                if result_prof=='Volunteer':
                    self.goVolunteer()

                if result_prof=='Consumer':
                    self.goConsumer()
            else:

                print("Invalid password")
                self.label_2.setStyleSheet(u"color: red;\n"
                                           "background:setAttribute(Qt::WA_TranslucentBackground)")
                self.label_2.setText("Invalid username or password")

class volunteerServicesWindow(QWidget, Ui_vServices):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.addService.clicked.connect(self.addvServiceFunc)
        self.sTable()
        self.backv.clicked.connect(self.goVolunteer)
        self.vdate.setMinimumDate(QDate.currentDate())


    def goVolunteer(self):
        self.windowV=volunteerWindow()
        self.close()
        self.windowV.show()
    def addvServiceFunc(self):
        servicetype=self.serviceboxR.currentText()
        servicesName=self.serviceName.text()
        servicesDate=self.vdate.date()
        serviceTime=self.vtime.time()
        if servicetype=="Advice":cost=50
        elif servicetype=="Lecture":cost=150
        else:cost=200
        print(servicesDate)
        sDate=servicesDate.toPython()
        sTime=serviceTime.toString()
        print(sDate,'  ',sTime)
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        cursor.execute("INSERT INTO servicesTB (Username,servicetype,servicename,Date,Time,Cost) VALUES (?,?,?,?,?,?)",(uv.username,servicetype,servicesName,sDate,sTime,cost))
        db.commit()
        cursor.close()
        print("Records created successfully")

    def sTable(self):
            conn = sqlite3.connect("hAppDB.db")
            cur = conn.cursor()
            query = 'SELECT servicetype,servicename,Date,Time FROM servicesTB WHERE Username =\'' + uv.username + "\'"
            tablerow=0
            for row in cur.execute(query):
                self.servicesTable.setItem(tablerow,0,QTableWidgetItem(row[0]))
                self.servicesTable.setItem(tablerow,1,QTableWidgetItem(row[1]))
                self.servicesTable.setItem(tablerow,2,QTableWidgetItem(row[2]))
                self.servicesTable.setItem(tablerow,3, QTableWidgetItem(row[3]))
                tablerow+=1

class volunteerWindow(QWidget, Ui_volunteerprofile):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.welcomemsg_3.setText(uv.username+'!')
        self.welcomemsg_2.setText('nice to see you again!')
        self.filler1.setText(str(uv.points))
        self.filler2.setText(str(uv.points//20))
        self.ptsIcd.display((uv.points))
        self.hrsIcd.display(uv.points//20)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(200)
        self.progressBar.setValue(uv.points%200)
        self.pushlogout.clicked.connect(self.gologout)
        self.services.clicked.connect(self.goservices)
        self.svCalendar.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.updateService)
        self.completeButton.clicked.connect(self.updatePoints)

    def updatePoints(self):
        conn = sqlite3.connect("hAppDB.db")
        cur = conn.cursor()
        print(uv.username)

        query = 'SELECT Cost FROM servicesTB WHERE Username = ? AND Status = ? '
        cur.execute(query,(uv.username,"Complete"),)
        result = cur.fetchall()[0]
        pts=result[0]+uv.points
        uv.points=pts
        cur.close()


        cur = conn.cursor()
        query = "UPDATE users SET Points = ? WHERE Username=?"
        print('Updated')
        row = (pts, uv.username,)
        cur.execute(query, row)
        conn.commit()

        query = 'DELETE FROM servicesTB WHERE Username = ? AND Status = ? '
        cur.execute(query, (uv.username, 'Complete'), )
        conn.commit()
        print('Deleted')
        cur.close()



    def updateService(self):
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        Date=self.svCalendar.selectedDate().toPython()

        for i in range(self.svListWidget.count()):
            item=self.svListWidget.item(i)
            task=item.text()
            if item.checkState()==Qt.CheckState.Checked:
                query="UPDATE servicesTB SET Status='Complete' WHERE Date=? AND Username=?"
            else:
                query = "UPDATE servicesTB SET Status='Incomplete' WHERE Date=? AND Username=?"
            row=(Date,uv.username,)
            cursor.execute(query,row)
        db.commit()
        cursor.close()
        msgBox=QMessageBox()
        msgBox.setText("Changes saved.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def gologout(self):
        self.windowLogout=logoutWindow()
        self.close()
        self.windowLogout.show()
    def goservices(self):
        self.windowvServices=volunteerServicesWindow()
        self.close()
        self.windowvServices.show()

    def calendarDateChanged(self):
        print("The calendar date was changed.")
        dateSelected=self.svCalendar.selectedDate().toPython()
        print("Date selected: ",dateSelected)
        self.updateCalendar(dateSelected)

    def updateCalendar(self,Date):
        self.svListWidget.clear()
        db = sqlite3.connect('hAppDB.db')
        print("Opened database successfully")
        cursor = db.cursor()
        query='SELECT servicename,Date,Time,Status FROM servicesTB WHERE Date =? AND Username=?'
        row=(Date,uv.username,)
        results=cursor.execute(query,row).fetchall()
        for result in results:
            print(result[0])
            item=QListWidgetItem(str(result[0])+'     '+str(result[1])+' '+str(result[2]))
            item.setCheckState(Qt.CheckState.Unchecked)
            self.svListWidget.addItem(item)






class consumerWindow(QWidget, Ui_conumerprofile):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


class signupWindow(QWidget, Ui_create):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.back2.clicked.connect(self.gohome)
        self.signupR.clicked.connect(self.createaccount)

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
            user=cursor.fetchone()
            cursor.close()

            if user!=None:
                self.error.setText("Username is not available.")
                cursor.close()


            else:
                cursor = db.cursor()
                cursor.execute("INSERT INTO users (Username,Email,Password,Profile,Points) VALUES (?,?,?,?,0)",(u, mail, pw, prof))
                db.commit()
                cursor.close()
                print("Records created successfully")
                self.gohome()




    def gohome(self):
        self.close()
        window.show()


class logoutWindow(QWidget,Ui_confirmlogout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.confirmlogout_2.clicked.connect(exit)


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.login.clicked.connect(self.gotologin)
        self.createacc.clicked.connect(self.gotoSignup)

    def gotologin(self):
        self.window2 = loginWindow()
        window.close()
        self.window2.show()


    def gotoSignup(self):
        self.window3 = signupWindow()
        window.close()
        self.window3.show()




if __name__ == "__main__":
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = MainWindow()
    window.show()
    app.exec_()
