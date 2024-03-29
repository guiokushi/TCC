# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alerta_prod_venc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prod_venc_titulo = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_titulo.setGeometry(QtCore.QRect(320, 40, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.prod_venc_titulo.setFont(font)
        self.prod_venc_titulo.setStyleSheet("color: rgb(255, 0, 0);")
        self.prod_venc_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.prod_venc_titulo.setObjectName("prod_venc_titulo")
        self.prod_venc_texto = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_texto.setGeometry(QtCore.QRect(80, 90, 761, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prod_venc_texto.setFont(font)
        self.prod_venc_texto.setAlignment(QtCore.Qt.AlignCenter)
        self.prod_venc_texto.setWordWrap(True)
        self.prod_venc_texto.setObjectName("prod_venc_texto")
        self.prod_venc_prod = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_prod.setGeometry(QtCore.QRect(220, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prod_venc_prod.setFont(font)
        self.prod_venc_prod.setObjectName("prod_venc_prod")
        self.prod_venc_marca = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_marca.setGeometry(QtCore.QRect(220, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prod_venc_marca.setFont(font)
        self.prod_venc_marca.setObjectName("prod_venc_marca")
        self.prod_venc_data = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_data.setGeometry(QtCore.QRect(220, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.prod_venc_data.setFont(font)
        self.prod_venc_data.setObjectName("prod_venc_data")
        self.res_prod_venc_prod = QtWidgets.QLabel(self.centralwidget)
        self.res_prod_venc_prod.setGeometry(QtCore.QRect(320, 200, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_prod_venc_prod.setFont(font)
        self.res_prod_venc_prod.setObjectName("res_prod_venc_prod")
        self.res_prod_venc_marca = QtWidgets.QLabel(self.centralwidget)
        self.res_prod_venc_marca.setGeometry(QtCore.QRect(300, 230, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_prod_venc_marca.setFont(font)
        self.res_prod_venc_marca.setObjectName("res_prod_venc_marca")
        self.res_prod_venc_data = QtWidgets.QLabel(self.centralwidget)
        self.res_prod_venc_data.setGeometry(QtCore.QRect(410, 260, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.res_prod_venc_data.setFont(font)
        self.res_prod_venc_data.setObjectName("res_prod_venc_data")
        self.prod_venc_ok = QtWidgets.QPushButton(self.centralwidget)
        self.prod_venc_ok.setGeometry(QtCore.QRect(720, 310, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prod_venc_ok.setFont(font)
        self.prod_venc_ok.setStyleSheet("color: rgb(0, 0, 127);")
        self.prod_venc_ok.setObjectName("prod_venc_ok")
        self.prod_venc_texto_2 = QtWidgets.QLabel(self.centralwidget)
        self.prod_venc_texto_2.setGeometry(QtCore.QRect(70, 310, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.prod_venc_texto_2.setFont(font)
        self.prod_venc_texto_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.prod_venc_texto_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.prod_venc_texto_2.setWordWrap(True)
        self.prod_venc_texto_2.setObjectName("prod_venc_texto_2")
        self.fundo_branco = QtWidgets.QLabel(self.centralwidget)
        self.fundo_branco.setGeometry(QtCore.QRect(-100, -160, 1081, 731))
        self.fundo_branco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fundo_branco.setText("")
        self.fundo_branco.setObjectName("fundo_branco")
        self.fundo_branco.raise_()
        self.prod_venc_titulo.raise_()
        self.prod_venc_texto.raise_()
        self.prod_venc_prod.raise_()
        self.prod_venc_marca.raise_()
        self.prod_venc_data.raise_()
        self.res_prod_venc_prod.raise_()
        self.res_prod_venc_marca.raise_()
        self.res_prod_venc_data.raise_()
        self.prod_venc_ok.raise_()
        self.prod_venc_texto_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
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
        self.prod_venc_titulo.setText(_translate("MainWindow", "Produto Vencido"))
        self.prod_venc_texto.setText(_translate("MainWindow", "Atenção: O produto abaixo encontra-se vencido! Por favor, retire-o do carrinho e retorne-o a um de nossos logistas."))
        self.prod_venc_prod.setText(_translate("MainWindow", "Produto:"))
        self.prod_venc_marca.setText(_translate("MainWindow", "Marca:"))
        self.prod_venc_data.setText(_translate("MainWindow", "Data de Validade:"))
        self.res_prod_venc_prod.setText(_translate("MainWindow", "a"))
        self.res_prod_venc_marca.setText(_translate("MainWindow", "a"))
        self.res_prod_venc_data.setText(_translate("MainWindow", "a"))
        self.prod_venc_ok.setText(_translate("MainWindow", "OK"))
        self.prod_venc_texto_2.setText(_translate("MainWindow", "Você não poderá finalizar a compra com este produto dentro do carrinho."))
