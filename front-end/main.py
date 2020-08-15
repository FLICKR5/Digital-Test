from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

        self.setGeometry(200, 100, 880, 565)
        self.setWindowTitle("Digital Test")

    def initUI(self):

        qst_label_font = QtGui.QFont()
        qst_label_font.setFamily("Nimbus Sans [urw]")
        qst_label_font.setPointSize(14)
        qst_label_font.setBold(True)
        qst_label_font.setWeight(75)
        self.qst_lable = QtWidgets.QLabel(self)
        self.qst_lable.move(0, 20)
        self.qst_lable.setFont(qst_label_font)
        self.qst_lable.setText("Q.No")


        question_entry_font = QtGui.QFont()
        question_entry_font.setFamily("Nimbus Mono PS [UKWN]")
        question_entry_font.setPointSize(14)
        self.question_entry = QtWidgets.QTextEdit(self)
        self.question_entry.setGeometry(QtCore.QRect(60, 20, 801, 61))
        self.question_entry.setFont(question_entry_font)

        self.opt_radio_1 = QtWidgets.QRadioButton(self)
        self.opt_radio_1.setGeometry(QtCore.QRect(30, 150, 21, 31))

        self.opt_radio_2 = QtWidgets.QRadioButton(self)
        self.opt_radio_2.setGeometry(QtCore.QRect(30, 210, 21, 31))

        self.opt_radio_3 = QtWidgets.QRadioButton(self)
        self.opt_radio_3.setGeometry(QtCore.QRect(30, 270, 21, 31))

        self.opt_radio_4 = QtWidgets.QRadioButton(self)
        self.opt_radio_4.setGeometry(QtCore.QRect(30, 330, 21, 31))


        self.opt_entry_1 = QtWidgets.QTextEdit(self)
        self.opt_entry_1.setGeometry(QtCore.QRect(60, 150, 441, 31))

        self.opt_entry_2 = QtWidgets.QTextEdit(self)
        self.opt_entry_2.setGeometry(QtCore.QRect(60, 210, 441, 31))

        self.opt_entry_3 = QtWidgets.QTextEdit(self)
        self.opt_entry_3.setGeometry(QtCore.QRect(60, 270, 441, 31))

        self.opt_entry_4 = QtWidgets.QTextEdit(self)
        self.opt_entry_4.setGeometry(QtCore.QRect(60, 330, 441, 31))


        done_button_font = QtGui.QFont()
        done_button_font.setPointSize(14)
        self.done_button = QtWidgets.QPushButton(self)
        self.done_button.setGeometry(QtCore.QRect(770, 470, 101, 41))
        self.done_button.setFont(done_button_font)
        self.done_button.setText("Done")

        next_button_font = QtGui.QFont()
        next_button_font.setPointSize(14)
        self.next_button = QtWidgets.QPushButton(self)
        self.next_button.setGeometry(QtCore.QRect(650, 470, 101, 41))
        self.next_button.setFont(next_button_font)
        self.next_button.setText("Next")

        back_button_font = QtGui.QFont()
        back_button_font.setPointSize(14)
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(QtCore.QRect(530, 470, 101, 41))
        self.back_button.setFont(back_button_font)
        self.back_button.setText("Back")

        # self.next_button.clicked.connect(self.clicked)


    def clicked(self):
        print("Clicked")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
