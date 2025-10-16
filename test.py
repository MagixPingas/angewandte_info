from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('widget.ui', self)
        self.resize(800, 600)
        self.setWindowTitle("Mein erstes Fenster")
        self.show()




app = QApplication([])
window = MainWindow()
app.exec_()


