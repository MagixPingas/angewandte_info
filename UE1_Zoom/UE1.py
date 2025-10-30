from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ue1_widget.ui', self)
        self.resize(800, 600)
        self.setWindowTitle("UE1:Zoom")
        self.bigButton.clicked.connect(lambda: self.button_click(1.1))      #Damit dann etwas geschieht, muss das Signal der Komponente
        self.smallButton.clicked.connect(lambda: self.button_click(0.9))    #mit einer auszuführenden Funktion/Methode ("Slot") verknuepft werden.
        self.show()                                                         #slides_02_Qt5_basics_handout.pdf Folie 2


    def button_click(self, factor):

        self.resize(int(self.width() * factor), self.height())





app = QApplication([])
window = MainWindow()
app.exec_()