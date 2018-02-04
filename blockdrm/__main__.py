import sys
from .Settings import Settings
from .GenerateUser import GenerateUser
from PyQt5 import QtWidgets, QtGui
from .Window import Window

"""
def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()



    # we make a button also with a label:
    button = QtWidgets.QPushButton(w)
    labelButton = QtWidgets.QLabel(w)

    button.setText("sample button")
    labelButton.setText("button label")

    # horizontal box
    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(labelButton)
    h_box.addStretch()

    # stretches above and below button label..
    # reminds me of HTML

    # vertical box
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(button)
    v_box.addLayout(h_box)

    w.setLayout(v_box)


    w.setWindowTitle("Block Dermatologist")
    w.show()
    sys.exit(app.exec())
"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec())

    settingPack = Settings()
    userGenerator = GenerateUser(settingPack)
    userGenerator.addUser("212341", "bryce", "smith")
    

if __name__ == '__main__':
    main()


"""

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    
    w.setGeometry(100, 100, 300, 200)

    # setting up a label
    l1 = QtWidgets.QLabel(w)
    l1.setText("hello0")
    l1.move(130, 20)

    l2 = QtWidgets.QLabel(w)
    # we could set an image from the project directory..
    # l2.setPixmap(QtGui.QPixmap('globe.png'))
    l2.move(120, 90)

    # we make a button also with a label:
    button = QtWidgets.QPushButton(w)
    labelButton = QtWidgets.QLabel(w)

    button.setText("sample button")
    labelButton.setText("button label")
    button.move(100,50)
    labelButton.move(110, 100)


    w.setWindowTitle("Block Dermatologist")
    w.show()
    sys.exit(app.exec())

"""