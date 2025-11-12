# ---------------------------------------------------------------
# Project : UE2 Converter (PyQt5)
# Author  : Marco Gernet
# Date    : 2025-11-06
# Purpose : Miles ↔ Kilometer converter with PyQt5
# ---------------------------------------------------------------

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ue2_widget.ui', self)
        self.comboBox.activated.connect(self.textSetting)
        self.lineEdit.textChanged.connect(self.textSetting)
        self.resize(800, 600)
        self.setWindowTitle("UE2:Converter")
        self.show()



    def textSetting(self):
        index = self.comboBox.currentIndex()
        value = self.lineEdit.text()
        unit = self.comboBox.itemText((index+1) % 2)

        print('Input:', value, self.comboBox.itemText(index))

        try:
            conv_value = float(value)


            if index == 1:
                conv_value *= 1.609344

            elif index == 0:
                conv_value /= 1.609344

            print('Output:', str(conv_value) + ' ' + unit + '\n')
            self.label.setText(str(conv_value) + ' ' + unit)

        except ValueError:
            print("Rechnung nicht möglich!")
            self.label.setText("Rechnung nicht möglich!")




app = QApplication([])
window = MainWindow()
app.exec_()