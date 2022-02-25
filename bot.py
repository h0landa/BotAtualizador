from calendar import c
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
        self.buscar_exe.clicked.connect(self.line_edit_exe)
        self.buscar_ns.clicked.connect(self.line_edit_ns)
        self.confirmar.clicked.connect(self.copiar_renomear_renomear)
    def line_edit_exe(self):
        caminho_arquivo_exe = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self.caminho_executavel.setText(caminho_arquivo_exe[0])
    def line_edit_ns(self):
        caminho_pasta_ns = QFileDialog.getOpenFileName(self, 'Open file', '/')
        self.caminho_ns.setText(caminho_pasta_ns)                
    def copiar_renomear_renomear(self):
        contador = self.numero_siserps.text()
        contador = int(contador)
        for c in range(1, contador + 1):
            diretorio_entrada = self.caminho_executavel.text()
            diretorio_saida = self.caminho_ns.text() + 'siserp0' + c
            shutil.copy(diretorio_entrada, diretorio_saida)
        for c in range(1, contador):
            diretorio_entrada = self.caminho_ns.text() + '/siserp0' + c + '/0' + c
            diretorio_saida = self.caminho_ns.text() + '/siserp0' + c + '/0' + c + '-copia'
            os.rename(diretorio_entrada, diretorio_saida)
        for c in range(1, contador):
            diretorio_entrada = self.caminho_ns.text() + '/siserp0' + c + '/att'
            diretorio_saida = self.caminho_ns.text() + '/siserp0' + c + '/0' + c
            os.rename(diretorio_entrada, diretorio_saida)


#Adicionar os numeros dos siserps em uma lista, separalos com o comando split e fazer o laço de repetição percorrer todos os numeros dessa lista.
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = mainwindow
widget.show()
sys.exit(app.exec_())