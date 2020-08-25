from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QGridLayout)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets, uic
import sys



class Button(QPushButton):
    def __init__(self, win, num):
        super(Button, self).__init__(win)
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
        super().__init__()
        self.initUI()

        self.setGeometry(100, 100, 1153, 600)
        self.setWindowTitle("Digital Test")

    def initUI(self):
        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box

        grid_layout = QGridLayout()

        self.button_list=[]
        for x in range(100):
            for y in range(6):
                button = Button(self, str(str(3*x+y)))
                self.button_list.append(button)
                button.setFixedWidth(40)
                button.setFixedHeight(40)
                grid_layout.addWidget(button, x, y)

        self.widget.setLayout(grid_layout)


        self.pallet_area = QtWidgets.QScrollArea(self)
        self.pallet_area.setGeometry(QtCore.QRect(839, 50, 311, 541))
        self.pallet_area.setWidgetResizable(True)

        # self.pallet_area.setWidget(self.scrollAreaWidgetContents)
        self.pallet_area.setWidget(self.widget)

        #Scroll Area Properties
        # self.scroll = QScrollArea()             # Scroll Area which contains the widgets, set as the centralWidget
        # self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self.widget)

        # self.setCentralWidget(self.scroll)

        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()