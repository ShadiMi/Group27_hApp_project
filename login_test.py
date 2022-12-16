import pytest
from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel
import login

@pytest.fixture()
def app2(qtbot):
    test_login_app=login.Ui_login()
    qtbot.addWidget(test_login_app)
    return test_login_app

def test_app2(app2):
    assert app2.label.text()=='Login'
    assert app2.label_2.text()=='Sign in to your existing account'



def test_signal_after_click(app2, qtbot):
    qtbot.mouseClick(app2.button, QtCore.Qt.LeftButton)
    assert app2.loginL.isSignalConnected(app2.loginfunc())


if __name__ == '__main__':
    pytest.main()