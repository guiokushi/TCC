# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_final.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.agradecimenti = QtWidgets.QLabel(self.centralwidget)
        self.agradecimenti.setGeometry(QtCore.QRect(160, 130, 501, 171))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.agradecimenti.setFont(font)
        self.agradecimenti.setScaledContents(False)
        self.agradecimenti.setAlignment(QtCore.Qt.AlignCenter)
        self.agradecimenti.setWordWrap(True)
        self.agradecimenti.setObjectName("agradecimenti")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 870, 211, 201))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix/imagem_rota_gps.png);")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/imagem_rota_gps.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.fundo_branco = QtWidgets.QLabel(self.centralwidget)
        self.fundo_branco.setGeometry(QtCore.QRect(0, -10, 1001, 661))
        self.fundo_branco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fundo_branco.setText("")
        self.fundo_branco.setObjectName("fundo_branco")
        self.logo_eureka = QtWidgets.QLabel(self.centralwidget)
        self.logo_eureka.setGeometry(QtCore.QRect(550, 40, 241, 91))
        self.logo_eureka.setStyleSheet("background-image: url(:/newPrefix/logo_eureka.png);")
        self.logo_eureka.setText("")
        self.logo_eureka.setPixmap(QtGui.QPixmap(":/newPrefix/logo_eureka.png"))
        self.logo_eureka.setScaledContents(True)
        self.logo_eureka.setObjectName("logo_eureka")
        self.logo_maua = QtWidgets.QLabel(self.centralwidget)
        self.logo_maua.setGeometry(QtCore.QRect(20, 20, 211, 101))
        self.logo_maua.setStyleSheet("background-image: url(:/newPrefix/logo_maua.png);")
        self.logo_maua.setText("")
        self.logo_maua.setPixmap(QtGui.QPixmap(":/newPrefix/logo_maua.png"))
        self.logo_maua.setScaledContents(True)
        self.logo_maua.setObjectName("logo_maua")
        self.patrocinado = QtWidgets.QLabel(self.centralwidget)
        self.patrocinado.setGeometry(QtCore.QRect(20, 280, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.patrocinado.setFont(font)
        self.patrocinado.setObjectName("patrocinado")
        self.logo_acura = QtWidgets.QLabel(self.centralwidget)
        self.logo_acura.setGeometry(QtCore.QRect(120, 340, 221, 81))
        self.logo_acura.setStyleSheet("background-image: url(:/newPrefix/logo_acura.png);")
        self.logo_acura.setText("")
        self.logo_acura.setPixmap(QtGui.QPixmap(":/newPrefix/logo_acura.png"))
        self.logo_acura.setScaledContents(True)
        self.logo_acura.setObjectName("logo_acura")
        self.logo_gs1 = QtWidgets.QLabel(self.centralwidget)
        self.logo_gs1.setGeometry(QtCore.QRect(510, 310, 141, 111))
        self.logo_gs1.setStyleSheet("background-image: url(:/newPrefix/logo_gs1.png);")
        self.logo_gs1.setText("")
        self.logo_gs1.setPixmap(QtGui.QPixmap(":/newPrefix/logo_gs1.png"))
        self.logo_gs1.setScaledContents(True)
        self.logo_gs1.setObjectName("logo_gs1")
        self.fundo_branco.raise_()
        self.agradecimenti.raise_()
        self.label_4.raise_()
        self.logo_eureka.raise_()
        self.logo_maua.raise_()
        self.patrocinado.raise_()
        self.logo_acura.raise_()
        self.logo_gs1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 26))
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
        self.agradecimenti.setText(_translate("MainWindow", "Obrigado(a) e volte sempre!"))
        self.patrocinado.setText(_translate("MainWindow", "Patrocinado por:"))
import imagens_rc
