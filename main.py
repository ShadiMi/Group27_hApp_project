import sqlite3
import sys

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget
from ui_welcome import Ui_MainWindow
from ui_login import Ui_login
from ui_signup import Ui_create
from ui_volunteer import Ui_volunteerprofile
from ui_consumer import Ui_conumerprofile
from ui_logout import Ui_confirmlogout
import Person

uv=Person.volunteer()
uc=Person.consumer()


def database(user):
    conn = sqlite3.connect("hAppDB.db")
    cur = conn.cursor()
    query = 'SELECT * FROM users WHERE Username =\'' + user + "\'"
    cur.execute(query)
    result = cur.fetchone()
    if result[3]=='Volunteer':
        uv.username=result[0]
        uv.email=result[1]
        uv.password=result[2]
        uv.profile=result[3]
        uv.points=result[4]
        return uv
    else:
        uc.username=result[0]
        uc.email=result[1]
        uc.password=result[2]
        uc.profile=result[3]
        uc.points=result[4]
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
            self.label_2.setText("Please input all fields.")

        else:
            person=database(user)
            result_pass=person.password
            result_prof=person.profile

            if result_pass == password:
                print("Successfully logged in.")
                self.label_2.setText("Successfully logged in.")


                print(result_pass)
                if result_prof=='Volunteer':
                    self.goVolunteer()

                if result_prof=='Consumer':
                    self.goConsumer()
            else:

                print("Invalid username or password")
                self.label_2.setText("Invalid username or password")

class volunteerWindow(QWidget, Ui_volunteerprofile):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

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
        self.progressBar.setValue(uv.points)
        self.pushlogout.clicked.connect()

    def gologout(self):
        self.windowLogout=volunteerWindow()
        self.close()
        self.windowLogout.show()


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

    def createaccount(self):
        u = self.usernameRF.text()
        mail = self.emailRF.text()
        pw = self.pwRF.text()
        pwc = self.pwcRF.text()
        prof = self.profboxR.currentText()
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
            user=cursor.fetchone()[0]
            cursor = db.cursor()
            print(user)
            if user==u:
                self.error.setText("Username is not available.")


            elif prof=='Volunteer' or prof=='Consumer':
                cursor.execute("INSERT INTO users (Username,Email,Password,Profile,Points) VALUES (?,?,?,?,0)",(u, mail, pw, prof))
                db.commit()
                print("Records created successfully")
                self.gohome()
            else:
                cursor.execute("INSERT INTO users (Username,Email,Password,Profile) VALUES (?,?,?,?)",(u, mail, pw, prof))
                db.commit()
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
