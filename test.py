from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widget.ui', self)
        self.resize(800, 600)
        self.setWindowTitle("Mein erstes Fenster")
        self.pb_1.clicked.connect(self.button_click)
        self.show()


    def button_click(self):
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setText("Hello World")
        msg.exec_()

app = QApplication([])
window = MainWindow()
app.exec_()

#test
