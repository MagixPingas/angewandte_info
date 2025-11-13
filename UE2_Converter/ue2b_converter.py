# ---------------------------------------------------------------
# Project : UE2b Converter (PyQt5)
# Author  : Marco Gernet
# Date    : 2025-11-13
# Purpose : Miles ↔ Kilometer converter with PyQt5
# ---------------------------------------------------------------
from operator import index

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ue2b_widget.ui', self)
        self.comboBox.activated.connect(self.textSetting)
        self.lineEdit.textChanged.connect(self.textSetting)
        self.rb_km.toggled.connect(self.toggleTest)
        self.rb_mi.toggled.connect(self.toggleTest)
        self.resize(800, 600)
        self.setWindowTitle("UE2b:Converter")
        self.show()



    def textSetting(self):
        index = self.comboBox.currentIndex()
        value = self.lineEdit.text()



        self.calc(value, index)




    def toggleTest(self):
        rb = self.sender()
        if rb.isChecked():
            value = self.lineEdit.text()
            index = rb.objectName()


            self.calc(value, index)




    def calc(self, value, index):

        try:
            conv_value = float(value)

            print('Input:', str(conv_value), index)

            unit = ''

            if index == 'rb_km':
                conv_value /= 1.609344
                self.comboBox.blockSignals(True)
                self.comboBox.setCurrentIndex(0)
                self.comboBox.blockSignals(False)
                unit = 'Meilen [mi]'


            elif index == 'rb_mi':
                conv_value *= 1.609344
                self.comboBox.blockSignals(True)
                self.comboBox.setCurrentIndex(1)
                self.comboBox.blockSignals(False)
                unit = 'Kilometer [km]'


            elif index == 1:
                conv_value *= 1.609344
                self.rb_mi.blockSignals(True)
                self.rb_mi.setChecked(True)
                unit = self.comboBox.itemText((index + 1) % 2)
                self.rb_mi.blockSignals(False)


            elif index == 0:
                conv_value /= 1.609344
                self.rb_km.blockSignals(True)
                self.rb_km.setChecked(True)
                unit = self.comboBox.itemText((index + 1) % 2)
                self.rb_km.blockSignals(False)


            self.outputText(conv_value, unit)

        except ValueError:
            if value == '' or value == '.' or value == ',':
                self.errorText()
                return
            else:
                adder = 0
                for i in value:
                    if i.isnumeric():
                        continue
                    elif i == ',':
                        adder += 1
                        continue
                    elif adder == 2:
                        self.errorText()
                        break
                    else:
                        self.errorText()
                        return
                value = value.replace(',', '.', 1)
                self.calc(value, index)

    def errorText(self):
        self.lineEdit.blockSignals(True)
        self.lineEdit.clear()
        self.lineEdit.blockSignals(False)
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText("Bitte Dezimalzahl eingeben")
        msg.exec_()
        print("Rechnung nicht möglich! \n")
        self.label.setText("Rechnung nicht möglich!")

    def outputText(self, conv_value, unit):
        val = round(conv_value, 3)
        print('Output:', str(val), unit, '\n')
        self.label.setText(str(val) + ' ' + unit)

app = QApplication([])
window = MainWindow()
app.exec_()