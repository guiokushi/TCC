# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrucoes.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imagem_carrinho_instrucoes = QtWidgets.QLabel(self.centralwidget)
        self.imagem_carrinho_instrucoes.setGeometry(QtCore.QRect(20, 60, 61, 61))
        self.imagem_carrinho_instrucoes.setStyleSheet("")
        self.imagem_carrinho_instrucoes.setText("")
        self.imagem_carrinho_instrucoes.setPixmap(QtGui.QPixmap(":/newPrefix/add-to-cart.png"))
        self.imagem_carrinho_instrucoes.setScaledContents(True)
        self.imagem_carrinho_instrucoes.setObjectName("imagem_carrinho_instrucoes")
        self.imagem_celular_instrucoes = QtWidgets.QLabel(self.centralwidget)
        self.imagem_celular_instrucoes.setGeometry(QtCore.QRect(20, 320, 61, 61))
        self.imagem_celular_instrucoes.setStyleSheet("")
        self.imagem_celular_instrucoes.setText("")
        self.imagem_celular_instrucoes.setPixmap(QtGui.QPixmap(":/newPrefix/qr-code-scan.png"))
        self.imagem_celular_instrucoes.setScaledContents(True)
        self.imagem_celular_instrucoes.setObjectName("imagem_celular_instrucoes")
        self.instrucoes_1 = QtWidgets.QLabel(self.centralwidget)
        self.instrucoes_1.setGeometry(QtCore.QRect(100, 50, 691, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instrucoes_1.setFont(font)
        self.instrucoes_1.setScaledContents(False)
        self.instrucoes_1.setWordWrap(True)
        self.instrucoes_1.setObjectName("instrucoes_1")
        self.instrucoes_2 = QtWidgets.QLabel(self.centralwidget)
        self.instrucoes_2.setGeometry(QtCore.QRect(100, 130, 691, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instrucoes_2.setFont(font)
        self.instrucoes_2.setScaledContents(False)
        self.instrucoes_2.setWordWrap(True)
        self.instrucoes_2.setObjectName("instrucoes_2")
        self.imagem_lista_instrucoes = QtWidgets.QLabel(self.centralwidget)
        self.imagem_lista_instrucoes.setGeometry(QtCore.QRect(20, 230, 61, 61))
        self.imagem_lista_instrucoes.setStyleSheet("")
        self.imagem_lista_instrucoes.setText("")
        self.imagem_lista_instrucoes.setPixmap(QtGui.QPixmap(":/newPrefix/verification-of-delivery-list-clipboard-symbol.png"))
        self.imagem_lista_instrucoes.setScaledContents(True)
        self.imagem_lista_instrucoes.setObjectName("imagem_lista_instrucoes")
        self.instrucoes_3 = QtWidgets.QLabel(self.centralwidget)
        self.instrucoes_3.setGeometry(QtCore.QRect(100, 230, 691, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instrucoes_3.setFont(font)
        self.instrucoes_3.setScaledContents(False)
        self.instrucoes_3.setWordWrap(True)
        self.instrucoes_3.setObjectName("instrucoes_3")
        self.instrucoes_4 = QtWidgets.QLabel(self.centralwidget)
        self.instrucoes_4.setGeometry(QtCore.QRect(100, 310, 691, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instrucoes_4.setFont(font)
        self.instrucoes_4.setScaledContents(False)
        self.instrucoes_4.setWordWrap(True)
        self.instrucoes_4.setObjectName("instrucoes_4")
        self.botao_instrucoes_continuar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_instrucoes_continuar.setGeometry(QtCore.QRect(590, 400, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_instrucoes_continuar.setFont(font)
        self.botao_instrucoes_continuar.setStyleSheet("color: rgb(0, 0, 127);")
        self.botao_instrucoes_continuar.setCheckable(True)
        self.botao_instrucoes_continuar.setAutoExclusive(True)
        self.botao_instrucoes_continuar.setObjectName("botao_instrucoes_continuar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 870, 211, 201))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/imagem_rota_gps.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/imagem_rota_gps.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.imagem_mapa_instrucoes = QtWidgets.QLabel(self.centralwidget)
        self.imagem_mapa_instrucoes.setGeometry(QtCore.QRect(20, 140, 61, 61))
        self.imagem_mapa_instrucoes.setStyleSheet("")
        self.imagem_mapa_instrucoes.setText("")
        self.imagem_mapa_instrucoes.setPixmap(QtGui.QPixmap(":/newPrefix/gps-route.png"))
        self.imagem_mapa_instrucoes.setScaledContents(True)
        self.imagem_mapa_instrucoes.setObjectName("imagem_mapa_instrucoes")
        self.fonte_icones = QtWidgets.QLabel(self.centralwidget)
        self.fonte_icones.setGeometry(QtCore.QRect(10, 0, 131, 16))
        self.fonte_icones.setObjectName("fonte_icones")
        self.fundo_branco = QtWidgets.QLabel(self.centralwidget)
        self.fundo_branco.setGeometry(QtCore.QRect(-40, -30, 1151, 741))
        self.fundo_branco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fundo_branco.setText("")
        self.fundo_branco.setObjectName("fundo_branco")
        self.fundo_branco.raise_()
        self.botao_instrucoes_continuar.raise_()
        self.imagem_carrinho_instrucoes.raise_()
        self.imagem_celular_instrucoes.raise_()
        self.instrucoes_1.raise_()
        self.instrucoes_2.raise_()
        self.imagem_lista_instrucoes.raise_()
        self.instrucoes_3.raise_()
        self.instrucoes_4.raise_()
        self.label_4.raise_()
        self.imagem_mapa_instrucoes.raise_()
        self.fonte_icones.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
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
        self.instrucoes_1.setText(_translate("MainWindow", "Coloque os produtos no carrinho e acompanhe em tempo real a sua lista de compras na tela. O valor total da compra será atualizado automaticamente. Informações sobre o produto estão disponibilizadas na opção \"Saber mais\""))
        self.instrucoes_2.setText(_translate("MainWindow", "Caso não encontre algum item, clique em \"Localizar produto\" no canto inferior esquerdo e digite o nome do produto ou da marca. O carrinho irá guiá-lo(a) até a prateleira, ou informá-lo(a) da ausência em estoque."))
        self.instrucoes_3.setText(_translate("MainWindow", "Ao terminar sua compra, confira todos os itens na sua lista clique em \"Finalizar compra\" no canto inferior direito. Você será redirecionado(a) ao nosso sistema de pagamento por PIX."))
        self.instrucoes_4.setText(_translate("MainWindow", "Ao aparecer o QR Code, abra seu aplicativo de pagamento e aponte a câmera para a tela. O sistema irá detectar automaticamente seu pagamento quando realizado, e, após a confirmação, retire suas compras e boa viagem!"))
        self.botao_instrucoes_continuar.setText(_translate("MainWindow", "CONTINUAR"))
        self.fonte_icones.setText(_translate("MainWindow", "Fonte: Flaticons.com"))
import imagens_rc
