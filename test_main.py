import sys
import unittest
from unittest import mock, TestCase
import PySide6
from PySide6 import QtGui
from PySide6.QtGui import QGuiApplication
from PySide6.QtTest import QTest
from PySide6.QtTest import QSignalSpy
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtWidgets import QWidget

import main
import ui_welcome

"""
_instance = None
class UsesQApplication(unittest.TestCase):
    '''Helper class to provide QApplication instances'''

    qapplication = True

    def setUp(self):
        '''Creates the QApplication instance'''

        # Simple way of making instance a singleton
        super().setUp()
        global _instance
        if _instance is None:
            _instance =main.MainWindow()

        self.app = _instance

    def tearDown(self):
        '''Deletes the reference owned by self'''
        del self.app
        super().tearDown()

class Test(UsesQApplication):

    def setUp(self):
        #If you override setup, tearDown, make sure
        #to have a super call
        super().__init__()

    def tearDown(self):
        super().__init__()

    def testWelcome(self):
        welcomeLabel=main.MainWindow.
"""

app = QApplication(sys.argv)
window = main.MainWindow()


class test_main_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.MainWindow()

    def test_WelcomeWindow(self):
        self.assertEqual(self.form.welcomeFlag,True)

    def test_WelcomeText(self):
        self.assertEqual(self.form.ui.welcomeL.text(),
                         '<html><head/><body><p align="center">Welcome to hApp</p></body></html>')

    def test_LoginBtnText(self):
        self.assertEqual(self.form.ui.login.text(),
                         'Login')

    def test_LoginSignal(self):
        loginButton = self.form.ui.login
        spy = QSignalSpy(loginButton, QPushButton.click(loginButton))
        QTest.mouseClick(loginButton, Qt.MouseButton.LeftButton)

    def test_signupBtnText(self):
        self.assertEqual(self.form.ui.createacc.text(),
                         'Signup')

    def test_signupSignal(self):
        signupButton = self.form.ui.createacc
        spy=QSignalSpy(signupButton,QPushButton.click(signupButton))
        QTest.mouseClick(signupButton, Qt.MouseButton.LeftButton)


class test_login_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.loginWindow()

    def test_loginWindow(self):
        self.assertEqual(self.form.loginFlag,True)

    def test_loginText(self):
        self.assertEqual(self.form.ui.label.text(),
                         '<html><head/><body><p align="center">LOGIN HERE</p></body></html>')

    def test_LoginBtnText(self):
        self.assertEqual(self.form.ui.loginL.text(),
                         'CONFIRM')

    def test_LoginSignal(self):
        confirmButton = self.form.ui.login
        spy = QSignalSpy(confirmButton, QPushButton.click(confirmButton))
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)






class test_databse(unittest.main):
    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc


if __name__ == '__main__':
    unittest.main(argv=['', '-v'])
    window = main.MainWindow()



