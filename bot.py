from time import sleep
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
        caminho_arquivo_exe = QFileDialog.getOpenFileName(self)
        self.caminho_executavel.setText(caminho_arquivo_exe[0])
    
    def line_edit_ns(self):
        caminho_pasta_ns = QtWidgets.QFileDialog.getExistingDirectory(self, 'Open file', '/')
        self.caminho_ns.setText(caminho_pasta_ns)

    def copiar_renomear_renomear(self):
        lista_siserps = self.numero_siserps.text()
        lista_siserps = lista_siserps.split()
        quantidade = len(lista_siserps)
        for c in range(0, quantidade):
            diretorio_entrada_executavel = self.caminho_executavel.text()
            diretorio_saida01 = self.caminho_ns.text() + '/siserp' + lista_siserps[c]
            diretorio_entrada_PastaNs = self.caminho_ns.text() + '/siserp' + lista_siserps[c] + '/' + lista_siserps[c]
            diretorio_saida02 = self.caminho_ns.text() + '/siserp' + lista_siserps[c] + '/' + lista_siserps[c] + '-copia'
            diretorio_entrada_PastaNs02 = self.caminho_ns.text() + '/siserp' + lista_siserps[c] + '/att'
            diretorio_saida03 = self.caminho_ns.text() + '/siserp' + lista_siserps[c] + '/' + lista_siserps[c]
            shutil.copy(diretorio_entrada_executavel, diretorio_saida01)
            os.rename(diretorio_entrada_PastaNs, diretorio_saida02)
            os.rename(diretorio_entrada_PastaNs02, diretorio_saida03)

app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = mainwindow
widget.show()
sys.exit(app.exec_())