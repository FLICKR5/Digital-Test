from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

        self.setGeometry(200, 100, 900, 600)
        self.setWindowTitle("Digital Test")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Digital-Test")
        self.label.move(400, 100)

        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setText("Next")
        self.next_button.clicked.connect(self.clicked)
        self.next_button.move(700, 500)

        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setText("Back")
        self.back_button.clicked.connect(self.clicked)
        self.back_button.move(600, 500)

        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setText("Done")
        self.done_button.clicked.connect(self.clicked)
        self.done_button.move(800, 500)
        

    def clicked(self):
        print("Clicked")





def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()