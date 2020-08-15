from PyQt5.QtWidgets import QMessageBox, QWidget

MainClass(QWidget):
    def __init__(self):
        super().__init__()

    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")
