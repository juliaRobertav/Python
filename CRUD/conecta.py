import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='conecta',
    )
    cursor = conexao.cursor()
    return conexao, cursor

# CRUD

    #nome_produto   #variáveis dentro de um texto
    #comando = 'INSERT INTO'    #importante saber o nome dos produtos
    #cursor.execute(comando)
    #conexao.commit()    #edita o banco de dados
    #resultado = cursor.fechtall()   #ler o banco de dados


    cursor.close()
    conexao.close()
