import pytest
from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel
import welcome

@pytest.fixture()
def app(qtbot):
    test_welcome_app=welcome.Ui_welcomescreen()
    qtbot.addWidget(test_welcome_app)
    return test_welcome_app

def test_label(app):
    assert app.welcomeL.text()=="welcome"
    assert app.welcomeL.text() == "keke"
    assert app.signL.text()=="Sign in or make a new account"

def test_signal_after_click(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.login.isSignalConnected(app.loginfunc())



def label(qtbot):
    qlabel = QLabel()
    qlabel.setText("welcome")
    qtbot.addWidget(qlabel)
    return qlabel


def test_label(label):
    assert label.text() == "welcome"

if __name__ == '__main__':
    pytest.main()