import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize   



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.setMinimumSize(QSize(700, 700))    

        pybutton = QPushButton('Create a button', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(100,100)
        pybutton.move(100, 100)  
        self.x=0
        self.button_list = [] 
        self.list_index = 0     

    def clickMethod(self):
        print('Clicked')
        self.button_list.append(QPushButton('New Button', self))
        self.button_list[self.list_index].move(self.x, 0)
        self.button_list[self.list_index].show()
        # button_list[self.list_index].clicked.connect(self.back)
        self.x+=100
        self.list_index += 1
        print(self.button_list)
        # print(button_list)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )