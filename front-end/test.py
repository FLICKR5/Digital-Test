import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class button(QPushButton):
    def __init__(self, win, num):
        super(button, self).__init__(win)
        self.clicked.connect(self.call)
        self.number=num
        self.setText(str(self.number))
        button_font = QtGui.QFont()
        button_font.setPointSize(16)
        self.setFont(button_font)
    
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
        self.button_no=1
        self.row = 1
        self.coul = 1 

        self.new_button = QPushButton(self)
        self.new_button.setText("Click Me")
        self.new_button.setGeometry(QtCore.QRect(100, 500, 100, 100))
        self.new_button.clicked.connect(self.clicked)

        self.pallet_area = QtWidgets.QScrollArea(self)
        self.pallet_area.setGeometry(QtCore.QRect(839, 50, 311, 541))
        self.pallet_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 509))
        self.pallet_area.setWidget(self.scrollAreaWidgetContents)
        

        # self.cl_button = button(self, 12)
        # self.cl_button.setGeometry(QtCore.QRect(100, 100, 100, 100))


    def clicked(self):
        self.button_list.append(button(self, self.button_no))
        self.button_list[self.button_no-1].setGeometry(QtCore.QRect((self.coul*42-42)+850, (self.row*42-42)+60, 35, 35))
        self.coul+=1
        if self.button_no % 7==0:
            print("inre")
            self.row+=1
            self.coul = 1 
        self.button_no+=1
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
