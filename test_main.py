import sys
import unittest
from unittest import mock
from PySide6.QtTest import QTest
from PySide6.QtTest import QSignalSpy
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton
import main



app = QApplication(sys.argv)


class test_main_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.MainWindow()

    def test_WelcomeWindow(self):
        self.assertNotEqual(self.form.welcomeFlag,False)

    def test_WelcomeText(self):
        self.assertEqual(self.form.welcomeL.text(),
                         '<html><head/><body><p align="center">Welcome to hApp</p></body></html>')

    def test_LoginBtnText(self):
        self.assertEqual(self.form.login.text(),
                         'Login')

    def test_LoginSignal(self):
        loginButton = self.form.login
        spy = QSignalSpy(loginButton, QPushButton.click(loginButton))
        QTest.mouseClick(loginButton, Qt.MouseButton.LeftButton)

    def test_signupBtnText(self):
        self.assertEqual(self.form.createacc.text(),
                         'Signup')

    def test_signupSignal(self):
        signupButton = self.form.createacc
        spy=QSignalSpy(signupButton,QPushButton.click(signupButton))
        QTest.mouseClick(signupButton, Qt.MouseButton.LeftButton)


class test_login_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.loginWindow()

    def test_loginWindow(self):
        self.assertNotEqual(self.form.loginFlag,False)

    def test_loginText(self):
        self.assertEqual(self.form.label.text(),
                         '<html><head/><body><p align="center"><span style=" font-size:16pt; color:#ffffff;">LOGIN HERE</span></p></body></html>')

    def test_LoginBtnText(self):
        self.assertEqual(self.form.loginL.text(),
                         'CONFIRM')


    """Tests if the error msg changes to 'Please input all fields.' if not all fields are filled """
    def test_LoginFields(self):
        self.form.label_2.setText('Signin')
        self.assertEqual(self.form.label_2.text(),'Signin')
        confirmButton = self.form.loginL
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.label_2.text(),'Please input all fields.')

    """Tests if login function checks the username and password entered matches the ones in the database and directs to the appropriate window """
    def test_LoginFunction(self):
        self.form.usernameLF.setText('shadi')
        self.form.passwordLF.setText('123')
        self.assertEqual(self.form.loginSucessFlag,False)
        confirmButton = self.form.loginL
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.loginSucessFlag,True)

class test_signup_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.signupWindow()

    def test_signupWindow(self):
        self.assertNotEqual(self.form.signupFlag,False)

    def test_signupText(self):
        self.assertEqual(self.form.signupL.text(),
                         '<html><head/><body><p><span style=" color:#c2c2c2;">Signup</span></p></body></html>')

    def test_signupBtnText(self):
        self.assertEqual(self.form.signupR.text(),
                         'Sign-up')

    """Tests if error field changes to 'Please fill in all inputs.' if one of the fields are empty and you click the 'confirm Button'"""
    def test_signupFieldsFilled(self):
        self.assertEqual(self.form.error.text(),'')
        confirmButton = self.form.signupR
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.error.text(),'Please fill in all inputs.')


    """Tests if error field changes to 'Username is not available.' if username already exists in the database'"""
    def test_signupFieldsIfUserexists(self):
        self.assertEqual(self.form.error.text(),'')
        self.form.usernameRF.setText('shadi')
        self.form.pwRF.setText('1')
        self.form.pwcRF.setText('1')
        confirmButton = self.form.signupR
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.error.text(),'Username is not available.')


    """Tests if error field changes to 'Passwords do not match.' if password and confirm password fields do not match'"""

    def test_signupFieldsIfPasswordsMatch(self):
        self.assertEqual(self.form.error.text(), '')
        self.form.usernameRF.setText('shadi')
        self.form.pwRF.setText('1')
        self.form.pwcRF.setText('3')
        confirmButton = self.form.signupR
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.error.text(), 'Passwords do not match.')

class test_consumer_window(unittest.TestCase):
    def setUp(self):
        '''Create the GUI'''
        self.form = main.consumerWindow()

    def test_consumerWindow(self):
        self.assertNotEqual(self.form.consumerFlag,False)

    def test_consumerText(self):
        self.assertEqual(self.form.welcomelabel.text(),
                         '<html><head/><body><p><span style=" font-size:22pt; font-style:italic; color:#000000;">Welcome, </span></p></body></html>')

    def test_confirmBtnText(self):
        self.assertEqual(self.form.confirmBtn.text(),
                         'Confirm')


    """Tests if the error msg changes to 'Coupon does not exist!' if the coupon entered doesn't exist in the database """
    def test_consumerCouponInvalid(self):
        self.form.cpnInstructionL.setText('test')
        self.assertEqual(self.form.cpnInstructionL.text(),'test')
        confirmButton = self.form.confirmBtn
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.cpnInstructionL.text(),'Coupon does not exist!')

    """Tests if the error msg changes to 'Coupon already been redeemed!' if the coupon entered has already been redeemed and its status in the database changed to 'Unavailable' """
    def test_consumerCouponUnavailable(self):
        self.form.cpnInstructionL.setText('test')
        self.assertEqual(self.form.cpnInstructionL.text(),'test')
        confirmButton = self.form.confirmBtn
        QTest.mouseClick(confirmButton, Qt.MouseButton.LeftButton)
        self.assertEqual(self.form.cpnInstructionL.text(),'Coupon already been redeemed!')





def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [test_signup_window,test_login_window,test_main_window,test_databse]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)




class test_databse(unittest.main):
    def fix_dbc(self):
        dbc = mock.MagicMock(spec=['cursor'])
        dbc.autocommit = True
        return dbc


if __name__ == '__main__':
    run_some_tests()
    window = main.MainWindow()



