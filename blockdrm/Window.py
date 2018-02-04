import sys
import qdarkstyle
from PyQt5 import QtWidgets, QtGui
from .GenerateUser import GenerateUser
from .Settings import Settings

class Window (QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # call parent ctor
        self.init_ui()
    
    def init_ui(self):
        self.label = QtWidgets.QLabel()
        self.label.setText("Add a user: ID FirstName LastName")
        self.lineEntry = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton('Submit')
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label)
        v_box.addWidget(self.lineEntry)
        v_box.addWidget(self.button)
        self.setLayout(v_box)
        # set superior dark colors.
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.setWindowTitle("BlockChain Dermatology, LLC")
        self.button.clicked.connect(self.btn_click)
        self.show()




    def old_init_ui(self):
        self.b = QtWidgets.QPushButton('Push Me!')
        self.l = QtWidgets.QLabel('I have not been clicked yet')
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        # set superior dark colors.
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        h_box.addWidget(self.l)
        h_box.addStretch()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.b)
        v_box.addLayout(h_box)
        self.setLayout(v_box)
        self.setWindowTitle("Block Dermatologist")
        self.b.clicked.connect(self.btn_click)
        self.show()

    
    def btn_click(self):
        sender = self.sender()
        if sender.text() == 'Submit':
            stringFromButton = self.lineEntry.text()
            print(stringFromButton)
            vectorFromButton = stringFromButton.split()
            settings = Settings()
            newUser = GenerateUser(settings)
            newUser.addUser(vectorFromButton[0], vectorFromButton[1], vectorFromButton[2])
            