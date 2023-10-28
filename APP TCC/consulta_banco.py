import mysql.connector
import tela_id_etiqueta

con = mysql.connector.connect(host='localhost',database='db_ProdutosTCC',user='root',password='lele77608')

if con.is_connected():
    db_info = con.get_server_info()
    print("conectado ao servidor mysql versão", db_info)
    cursor = con.cursor()
    id = '1'
    consulta_preco = """SELECT Preco FROM tbl_Produtos WHERE ID_RFID = '{}'""".format(id)
    cursor.execute(consulta_preco)
    preco = cursor.fetchall()[0][0]
    print(preco)

if con.is_connected():
    cursor.close()
    con.close()
    print("conexão ao mysql foi encerrada")