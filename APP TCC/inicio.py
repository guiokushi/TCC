# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inicio.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 472)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bem_vindo = QtWidgets.QLabel(self.centralwidget)
        self.bem_vindo.setGeometry(QtCore.QRect(150, 110, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(40)
        self.bem_vindo.setFont(font)
        self.bem_vindo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bem_vindo.setObjectName("bem_vindo")
        self.comecar = QtWidgets.QPushButton(self.centralwidget)
        self.comecar.setGeometry(QtCore.QRect(590, 320, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comecar.setFont(font)
        self.comecar.setStyleSheet("color: rgb(0, 0, 127);")
        self.comecar.setCheckable(True)
        self.comecar.setAutoExclusive(True)
        self.comecar.setObjectName("comecar")
        self.logo_maua = QtWidgets.QLabel(self.centralwidget)
        self.logo_maua.setGeometry(QtCore.QRect(10, 10, 201, 91))
        self.logo_maua.setStyleSheet("background-image: url(:/newPrefix/logo_maua.png);")
        self.logo_maua.setText("")
        self.logo_maua.setPixmap(QtGui.QPixmap(":/newPrefix/logo_maua.png"))
        self.logo_maua.setScaledContents(True)
        self.logo_maua.setObjectName("logo_maua")
        self.logo_eureaka = QtWidgets.QLabel(self.centralwidget)
        self.logo_eureaka.setGeometry(QtCore.QRect(580, 30, 211, 71))
        self.logo_eureaka.setStyleSheet("background-image: url(:/newPrefix/logo_eureka.png);")
        self.logo_eureaka.setText("")
        self.logo_eureaka.setPixmap(QtGui.QPixmap(":/newPrefix/logo_eureka.png"))
        self.logo_eureaka.setScaledContents(True)
        self.logo_eureaka.setObjectName("logo_eureaka")
        self.fundo_branco = QtWidgets.QLabel(self.centralwidget)
        self.fundo_branco.setGeometry(QtCore.QRect(0, -10, 1171, 701))
        self.fundo_branco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fundo_branco.setText("")
        self.fundo_branco.setObjectName("fundo_branco")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(210, 20, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: rgb(0, 0, 127);")
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setWordWrap(True)
        self.titulo.setObjectName("titulo")
        self.mini_capa = QtWidgets.QLabel(self.centralwidget)
        self.mini_capa.setGeometry(QtCore.QRect(300, 190, 221, 191))
        self.mini_capa.setStyleSheet("background-image: url(:/newPrefix/mini_capa.png);")
        self.mini_capa.setText("")
        self.mini_capa.setPixmap(QtGui.QPixmap(":/newPrefix/mini_capa.png"))
        self.mini_capa.setScaledContents(True)
        self.mini_capa.setObjectName("mini_capa")
        self.fundo_branco.raise_()
        self.mini_capa.raise_()
        self.comecar.raise_()
        self.bem_vindo.raise_()
        self.logo_maua.raise_()
        self.logo_eureaka.raise_()
        self.titulo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 26))
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
        self.bem_vindo.setText(_translate("MainWindow", "Seja bem-vindo(a)!"))
        self.comecar.setText(_translate("MainWindow", "COMEÇAR"))
        self.titulo.setText(_translate("MainWindow", "Carrinho de Supermercado Inteligente"))
import imagens_rc