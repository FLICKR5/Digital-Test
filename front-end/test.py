import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class button(QPushButton):
    def __init__(self, win, num):
        super(button, self).__init__(win)
        self.clicked.connect(self.call)
        self.number=num
        self.setText(str(self.number))
        self.show()
    
    def call(self):
        print(self.number)

    

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

        self.setGeometry(100, 100, 1153, 600)

    def initUI(self):
        self.button_list=[]
        self.new_button = QPushButton(self)
        self.new_button.setText("Click Me")
        self.new_button.setGeometry(QtCore.QRect(500, 500, 100, 100))
        self.new_button.clicked.connect(self.clicked)
        self.button_no=1

        # self.cl_button = button(self, 12)
        # self.cl_button.setGeometry(QtCore.QRect(100, 100, 100, 100))

    def clicked(self):
        print("called")
        self.button_list.append(button(self, self.button_no))
        self.button_list[self.button_no-1].setGeometry(QtCore.QRect(self.button_no*50, 0, 50, 50))

        self.button_no+=1
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
