# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_pagamento.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 526)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagem_qrcode = QtWidgets.QLabel(self.centralwidget)
        self.imagem_qrcode.setGeometry(QtCore.QRect(340, 40, 261, 231))
        self.imagem_qrcode.setText("")
        self.imagem_qrcode.setObjectName("imagem_qrcode")
        self.realize_o_pagamento = QtWidgets.QLabel(self.centralwidget)
        self.realize_o_pagamento.setGeometry(QtCore.QRect(200, 310, 531, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.realize_o_pagamento.setFont(font)
        self.realize_o_pagamento.setAlignment(QtCore.Qt.AlignCenter)
        self.realize_o_pagamento.setWordWrap(True)
        self.realize_o_pagamento.setObjectName("realize_o_pagamento")
        self.finalizar = QtWidgets.QPushButton(self.centralwidget)
        self.finalizar.setGeometry(QtCore.QRect(710, 380, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.finalizar.setFont(font)
        self.finalizar.setStyleSheet("color: rgb(0, 0, 127);")
        self.finalizar.setObjectName("finalizar")
        self.fundo_branco = QtWidgets.QLabel(self.centralwidget)
        self.fundo_branco.setGeometry(QtCore.QRect(-120, -100, 1241, 781))
        self.fundo_branco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fundo_branco.setText("")
        self.fundo_branco.setObjectName("fundo_branco")
        self.fundo_branco.raise_()
        self.imagem_qrcode.raise_()
        self.realize_o_pagamento.raise_()
        self.finalizar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.realize_o_pagamento.setText(_translate("MainWindow", "Aponte a câmera para o QR code e realize o pagamento"))
        self.finalizar.setText(_translate("MainWindow", "FINALIZAR"))
