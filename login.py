# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3
from Person import *

from PyQt6 import QtCore, QtGui, QtWidgets
from volunteer import Ui_volunteerprofile
from consumerrprofile import Ui_Costumerprofile


class Ui_login(object):
    def openvolunteer(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_volunteerprofile()
        self.ui.setupUi(self.window)
        login.close()
        self.window.show()

    def openconsumer(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Costumerprofile()
        self.ui.setupUi(self.window)
        login.close()
        self.window.show()

    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(375, 236)
        self.loginL = QtWidgets.QPushButton(login)
        self.loginL.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.loginL.setObjectName("loginL")
        self.unL = QtWidgets.QLabel(login)
        self.unL.setGeometry(QtCore.QRect(80, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unL.setFont(font)
        self.unL.setObjectName("unL")
        self.pwL = QtWidgets.QLabel(login)
        self.pwL.setGeometry(QtCore.QRect(80, 130, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pwL.setFont(font)
        self.pwL.setObjectName("pwL")
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(130, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 171, 20))
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(169, 90, 151, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.usernameLF = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.usernameLF.setObjectName("usernameLF")
        self.verticalLayout.addWidget(self.usernameLF)
        self.passwordLF = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordLF.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.passwordLF.setObjectName("passwordLF")
        self.verticalLayout.addWidget(self.passwordLF)
        self.retranslateUi(login)
        self.error = QtWidgets.QLabel(login)
        self.error.setGeometry(QtCore.QRect(120, 233, 261, 20))
        self.label.setFont(font)
        self.error.setObjectName("error")
        QtCore.QMetaObject.connectSlotsByName(login)
        self.loginL.clicked.connect(self.loginfunc)

    def loginfunc(self):
        user=self.usernameLF.text()
        password=self.passwordLF.text()


        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")

        else:
            conn = sqlite3.connect("hAppDB.db")
            cur = conn.cursor()
            query = 'SELECT Password,Profile FROM users WHERE Username =\'' + user + "\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                print("Successfully logged in.")
                cur.execute(query)
                result_pass=cur.fetchone()[1]
                print(result_pass)
                if result_pass=='Volunteer':
                    self.openvolunteer()
                 #  v1=volunteer(result[0],result[1],result[2],result[3],result[4])
                if result_pass=='Consumer':
                    self.openconsumer()


                #self.error.setText("")
            else:
                #self.error.setText("Invalid username or password")
                print("Invalid username or password")









    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "login"))
        self.loginL.setToolTip(_translate("login", "Press To Login "))
        self.loginL.setText(_translate("login", "Login"))
        self.unL.setText(_translate("login", "User Name"))
        self.pwL.setText(_translate("login", "Password"))
        self.label.setText(_translate("login", "Login"))
        self.label_2.setText(_translate("login", "Sign in to your existing account"))
        self.usernameLF.setPlaceholderText(_translate("login", "User name "))
        self.passwordLF.setPlaceholderText(_translate("login", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec())
