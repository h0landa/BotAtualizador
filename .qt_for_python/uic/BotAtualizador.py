# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BotAtualizador.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_BotAtualizador(object):
    def setupUi(self, BotAtualizador):
        if not BotAtualizador.objectName():
            BotAtualizador.setObjectName(u"BotAtualizador")
        BotAtualizador.resize(324, 240)
        BotAtualizador.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.gridLayoutWidget = QWidget(BotAtualizador)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 301, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.buscar_exe = QPushButton(self.gridLayoutWidget)
        self.buscar_exe.setObjectName(u"buscar_exe")
        self.buscar_exe.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.buscar_exe, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.caminho_ns = QLineEdit(self.gridLayoutWidget)
        self.caminho_ns.setObjectName(u"caminho_ns")
        self.caminho_ns.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.caminho_ns, 3, 1, 1, 1)

        self.caminho_executavel = QLineEdit(self.gridLayoutWidget)
        self.caminho_executavel.setObjectName(u"caminho_executavel")
        self.caminho_executavel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.caminho_executavel, 1, 1, 1, 1)

        self.buscar_ns = QPushButton(self.gridLayoutWidget)
        self.buscar_ns.setObjectName(u"buscar_ns")
        self.buscar_ns.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.buscar_ns, 4, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(BotAtualizador)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 150, 289, 59))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.numero_siserps = QLineEdit(self.gridLayoutWidget_2)
        self.numero_siserps.setObjectName(u"numero_siserps")
        self.numero_siserps.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.numero_siserps, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.confirmar = QPushButton(self.gridLayoutWidget_2)
        self.confirmar.setObjectName(u"confirmar")

        self.gridLayout_2.addWidget(self.confirmar, 1, 1, 1, 1)


        self.retranslateUi(BotAtualizador)

        QMetaObject.connectSlotsByName(BotAtualizador)
    # setupUi

    def retranslateUi(self, BotAtualizador):
        BotAtualizador.setWindowTitle(QCoreApplication.translate("BotAtualizador", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("BotAtualizador", u"Executavel ", None))
        self.buscar_exe.setText(QCoreApplication.translate("BotAtualizador", u"Buscar Exe", None))
        self.label_2.setText(QCoreApplication.translate("BotAtualizador", u" Pasta NS", None))
        self.caminho_ns.setPlaceholderText(QCoreApplication.translate("BotAtualizador", u"C:/", None))
        self.caminho_executavel.setPlaceholderText(QCoreApplication.translate("BotAtualizador", u"C:/", None))
        self.buscar_ns.setText(QCoreApplication.translate("BotAtualizador", u"Buscar NS", None))
        self.numero_siserps.setPlaceholderText(QCoreApplication.translate("BotAtualizador", u"1 2  3 4 5 6 7 8", None))
        self.label_3.setText(QCoreApplication.translate("BotAtualizador", u"Numero dos Siserps", None))
        self.confirmar.setText(QCoreApplication.translate("BotAtualizador", u"Confirmar dados", None))
    # retranslateUi

