from ast import Break
from audioop import add
from multiprocessing.sharedctypes import Value
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtTest
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel, QSizeGrip, QSizePolicy
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from functools import partial
from gerar_qrcode import Payload
import mysql.connector
import re
import datetime
import mercury
import time

import lista_compras
import inicio
import instrucoes
import tela_pagamento
import tela_inf_prod
import alerta_prod_venc
import tela_final
import tela_busca_produtos
import mapa_do_mercado

con = mysql.connector.connect(host='localhost',database='db_ProdutosTCC',user='root',password='lele77608')
cursor = con.cursor()

class controller(QMainWindow):
    def __init__(self):
        super().__init__()

        self.contagem = 1
        self.indicador = 0
        self.contagem_busca = 1

        self.lista_compras_Window = QtWidgets.QMainWindow()
        self.lista_compras_ui = lista_compras.Ui_MainWindow()
        self.lista_compras_ui.setupUi(self.lista_compras_Window)

        self.inicio_Window = QtWidgets.QMainWindow()
        self.inicio_ui = inicio.Ui_MainWindow()
        self.inicio_ui.setupUi(self.inicio_Window)

        self.instrucoes_Window = QtWidgets.QMainWindow()
        self.instrucoes_ui = instrucoes.Ui_MainWindow()
        self.instrucoes_ui.setupUi(self.instrucoes_Window)

        self.tela_pagamento_Window = QtWidgets.QMainWindow()
        self.tela_pagamento_ui = tela_pagamento.Ui_MainWindow()
        self.tela_pagamento_ui.setupUi(self.tela_pagamento_Window)

        self.tela_final_Window = QtWidgets.QMainWindow()
        self.tela_final_ui = tela_final.Ui_MainWindow()
        self.tela_final_ui.setupUi(self.tela_final_Window)

        #self.tela_id_etiqueta_Window = QtWidgets.QMainWindow()
        #self.tela_id_etiqueta_ui = tela_id_etiqueta.Ui_MainWindow()
        #self.tela_id_etiqueta_ui.setupUi(self.tela_id_etiqueta_Window)

        #self.tela_id_etiqueta_retirar_Window = QtWidgets.QMainWindow()
        #self.tela_id_etiqueta_retirar_ui = tela_id_etiqueta_retirar.Ui_MainWindow()
        #self.tela_id_etiqueta_retirar_ui.setupUi(self.tela_id_etiqueta_retirar_Window)

        self.tela_inf_prod_Window = QtWidgets.QMainWindow()
        self.tela_inf_prod_ui = tela_inf_prod.Ui_MainWindow()
        self.tela_inf_prod_ui.setupUi(self.tela_inf_prod_Window)

        self.alerta_prod_venc_Window = QtWidgets.QMainWindow()
        self.alerta_prod_venc_ui = alerta_prod_venc.Ui_MainWindow()
        self.alerta_prod_venc_ui.setupUi(self.alerta_prod_venc_Window)

        self.tela_busca_produtos_Window = QtWidgets.QMainWindow()
        self.tela_busca_produtos_ui = tela_busca_produtos.Ui_MainWindow()
        self.tela_busca_produtos_ui.setupUi(self.tela_busca_produtos_Window)

        self.mapa_do_mercado_Window = QtWidgets.QMainWindow()
        self.mapa_do_mercado_ui = mapa_do_mercado.Ui_MainWindow()
        self.mapa_do_mercado_ui.setupUi(self.mapa_do_mercado_Window)

        self.inicio_ui.comecar.clicked.connect(self.show_instrucoes)
        self.inicio_ui.comecar.clicked.connect(self.inicio_Window.close)

        self.lista_compras_ui.pagar.clicked.connect(self.alerta_prod_venc_finalizar_compra)
        #self.lista_compras_ui.pagar.clicked.connect(self.pagamento)
        #self.lista_compras_ui.pagar.clicked.connect(self.show_tela_pagamento)
        #self.lista_compras_ui.pagar.clicked.connect(self.lista_compras_Window.close)

        self.lista_compras_ui.localizar_item.clicked.connect(self.show_tela_busca_produtos)
        self.tela_busca_produtos_ui.botao_voltar.clicked.connect(self.tela_busca_produtos_Window.close)

        self.instrucoes_ui.botao_instrucoes_continuar.clicked.connect(self.show_lista_compras)
        self.instrucoes_ui.botao_instrucoes_continuar.clicked.connect(self.instrucoes_Window.close)
        self.instrucoes_ui.botao_instrucoes_continuar.clicked.connect(self.compara_lista)

        self.tela_pagamento_ui.finalizar.clicked.connect(self.show_tela_final)
        self.tela_pagamento_ui.finalizar.clicked.connect(self.tela_pagamento_Window.close)

        self.tela_busca_produtos_ui.botao_buscar.clicked.connect(lambda: self.tela_busca_produtos_ui.criar_linha_busca(self, self.contagem_busca))
        self.tela_busca_produtos_ui.botao_buscar.clicked.connect(self.incrementa_busca)

        #self.lista_compras_ui.inserir_item.clicked.connect(self.show_tela_id_etiqueta)

        #self.lista_compras_ui.remover_item.clicked.connect(self.show_tela_id_etiqueta_retirar)


        #self.tela_id_etiqueta_ui.pushButton.clicked.connect(lambda: self.lista_compras_ui.criar_linha(self, self.contagem, str(self.tela_id_etiqueta_ui.textEdit.toPlainText())))
        #self.tela_id_etiqueta_ui.pushButton.clicked.connect(self.tela_id_etiqueta_Window.close)

        self.alerta_prod_venc_ui.prod_venc_ok.clicked.connect(self.alerta_prod_venc_Window.close)

        self.mapa_do_mercado_ui.botao_voltar.clicked.connect(self.mapa_do_mercado_Window.close)

        #self.lista_compras_ui_
        #getattr(self.lista_compras_ui, f'saiba_mais{self.pegar_sender}').clicked.connect(self.show_tela_inf_prod)

        #self.tela_id_etiqueta_retirar_ui.pushButton.clicked.connect(lambda: self.remover_linha_teste(str(self.tela_id_etiqueta_retirar_ui.textEdit.toPlainText())))

        #self.lista_compras_ui.inserir_item.clicked.connect(lambda: self.lista_compras_ui.criar_linha(self, self.contagem))
        #self.lista_compras_ui.inserir_item.clicked.connect(self.incrementa)

        self.tela_busca_produtos_ui.A.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.B.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.C.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.D.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.E.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.F.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.G.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.H.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.I.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.J.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.K.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.L.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.M.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.N.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.O.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.P.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.Q.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.R.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.S.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.T.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.U.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.V.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.W.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.X.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.Y.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.Z.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.cedilha.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.espaco.clicked.connect(self.escrever)
        self.tela_busca_produtos_ui.apagar.clicked.connect(self.apagar)

    def remover_linha_teste(self, id_etiqueta=str):

        consulta_preco = """SELECT Preco FROM tbl_Produtos WHERE ID_RFID = '{}'""".format(id_etiqueta)
        consulta_id = """SELECT ID_Produto FROM tbl_Produtos WHERE ID_RFID = '{}'""".format(id_etiqueta)
        consulta_data = """SELECT Data_Validade FROM tbl_Produtos WHERE ID_RFID = '{}'""".format(id_etiqueta)

        #cursor.reset()
        cursor.execute(consulta_preco)
        resultado_preco = cursor.fetchall()[0][0]
        #cursor.reset()

        cursor.execute(consulta_id)
        resultado_id = str(cursor.fetchall()[0][0])
        #cursor.reset()

        cursor.execute(consulta_data)
        resultado_data = str(cursor.fetchall()[0][0])
        #cursor.reset()

        self.lista_compras_ui.produtos.clear()
        self.lista_compras_ui.produtos.append(resultado_id)
        self.lista_compras_ui.produtos.append(resultado_preco)
        self.lista_compras_ui.produtos.append(resultado_data)

        getattr(self.lista_compras_ui, f'nome{resultado_id}').deleteLater()
        getattr(self.lista_compras_ui, f'qtde{resultado_id}').deleteLater()
        getattr(self.lista_compras_ui, f'preco{resultado_id}').deleteLater()
        getattr(self.lista_compras_ui, f'saiba_mais{resultado_id}').deleteLater()
        self.lista_compras_ui.produtos_na_lista.remove(self.lista_compras_ui.produtos)

        self.lista_compras_ui.atualizar_preco()

    def compara_lista(self):
        
        reader = mercury.Reader("llrp://169.254.63.150")
        while True:

            reader.set_read_plan([1],"GEN2")

            lista=reader.read()
            lista_epc=[]
            for item in lista:
                string = str(item)
                lista_epc.append(string)
            lista_epc2=[]
            for epc_2 in lista_epc:
                epc=epc_2[2:26]
                lista_epc2.append(epc)

            for item in lista_epc2:
                if item not in self.lista_compras_ui.epcs_na_lista:
                    self.incrementa
                    self.lista_compras_ui.epcs_na_lista.append(item)
                    self.lista_compras_ui.criar_linha(self, self.contagem, item)
            for item in self.lista_compras_ui.epcs_na_lista:
                if item not in lista_epc2:
                    self.lista_compras_ui.epcs_na_lista.remove(item)
                    self.remover_linha_teste(self, item)
            if self.indicador == 1:
                break
            time.sleep(3)

    def escrever(self):
        sender = self.tela_busca_produtos_Window.sender()
        letra = sender.text()
        texto_atual = str(self.tela_busca_produtos_ui.barra_de_busca.toPlainText())
        texto_novo = texto_atual+letra
        _translate = QtCore.QCoreApplication.translate
        self.tela_busca_produtos_ui.barra_de_busca.setText(_translate("MainWindow", "{}").format(texto_novo))

    def apagar(self):
        texto_atual = str(self.tela_busca_produtos_ui.barra_de_busca.toPlainText())
        texto_novo = texto_atual[:-1]
        _translate = QtCore.QCoreApplication.translate
        self.tela_busca_produtos_ui.barra_de_busca.setText(_translate("MainWindow", "{}").format(texto_novo))

    def incrementa(self):
        self.contagem = self.contagem+1

    def incrementa_busca(self):
        self.contagem_busca = self.contagem_busca+1
    
    def show_lista_compras(self):
        self.lista_compras_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.lista_compras_Window.setWindowState(Qt.WindowFullScreen)
        self.lista_compras_Window.show()

    def show_instrucoes(self):
        self.instrucoes_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.instrucoes_Window.setWindowState(Qt.WindowFullScreen)
        self.instrucoes_Window.show()

    def show_tela_final(self):
        self.tela_final_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.tela_final_Window.setWindowState(Qt.WindowFullScreen)
        self.tela_final_Window.show()
        QtTest.QTest.qWait(5000)
        self.tela_final_Window.close()
        self.show_inicio

    
    def show_inicio(self):
        self.inicio_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.inicio_Window.setWindowState(Qt.WindowFullScreen)
        self.inicio_Window.show()

    def show_tela_busca_produtos(self):
        self.tela_busca_produtos_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.tela_busca_produtos_Window.setWindowState(Qt.WindowFullScreen)
        self.tela_busca_produtos_Window.show()

    def show_tela_pagamento(self):
        self.indicador=1
        self.tela_pagamento_Window.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.tela_pagamento_Window.setWindowState(Qt.WindowFullScreen)
        self.tela_pagamento_Window.show()
    
    def alerta_prod_venc_finalizar_compra(self):

        dia_de_hoje = datetime.date.today()
        dia_de_hoje_br = dia_de_hoje.strftime("%d/%m/%Y")

        date_format = "%d/%m/%Y"

        date_hoje = datetime.datetime.strptime(dia_de_hoje_br, date_format).date()

        for i in self.lista_compras_ui.produtos_na_lista:
            data_produto = i[2]
            if data_produto != 'N/A':
                data_produto = datetime.datetime.strptime(data_produto, date_format).date()
                if data_produto < date_hoje:

                    id = i[0]

                    consulta_nome_marca = """SELECT Nome, Marca FROM tbl_Produtos WHERE ID_Produto = '{}'""".format(id)
                    cursor.execute(consulta_nome_marca)
                    resultado_nome_marca = cursor.fetchall()
                    #cursor.reset()

                    resultado_nome = resultado_nome_marca[0][0]
                    resultado_marca = resultado_nome_marca[0][1]

                    _translate = QtCore.QCoreApplication.translate
                    self.alerta_prod_venc_ui.res_prod_venc_prod.setText(_translate("MainWindow", "{}").format(resultado_nome))
                    self.alerta_prod_venc_ui.res_prod_venc_marca.setText(_translate("MainWindow", "{}").format(resultado_marca))
                    self.alerta_prod_venc_ui.res_prod_venc_data.setText(_translate("MainWindow", "{}").format(data_produto))
                    self.lista_compras_ui.show_tela_alerta_prod_venc()
                    break
        else:
            self.pagamento()
            self.show_tela_pagamento()
            self.lista_compras_Window.close()

    def pagamento(self):

        self.lista_compras_ui.atualizar_preco()
        payload = Payload('Leticia Gomes Ferreira', '51201553830', str(self.lista_compras_ui.preco_total), 'Sao Paulo', 'TCCCarrinhoInteligente')

        payload.gerarPayload()
        self.tela_pagamento_ui.imagem_qrcode.setPixmap(QtGui.QPixmap("pixqrcodegen.png"))
        self.tela_pagamento_ui.imagem_qrcode.setScaledContents(True)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_inicio()
    sys.exit(app.exec_())