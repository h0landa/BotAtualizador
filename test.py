import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from BotAtualizador import Ui_BotAtualizador
import os
from PyQt5.uic import loadUi
import shutil

class MainWindow(QDialog, Ui_BotAtualizador):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("BotAtualizador.ui", self)
        self.confirmar.clicked.connect(self.siserp)
    def siserp(self):
        lista_siserps = self.numero_siserps.text()
        lista_siserps = lista_siserps.split()
        quantidade = len(lista_siserps)
        for c in range(0, quantidade):
            print(lista_siserps[c])
    
    
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = mainwindow
widget.show()
sys.exit(app.exec_())