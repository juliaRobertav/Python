import mysql.connector
from mysql import conecta

def atualizar():
   
    conexao, cursor = conectar() #fazendo a conexão

    comando = f'UPDATE filmes SET class_filme = 10 WHERE nome_filme = "{filme}"'
    comando = f'UPDATE usuario SET usuarios = 10 WHERE nome_usuario = "{usuario}"'

    cursor.execute(comando) #pedindo para executar o comando escrito
    conexao.commit() #edita o banco de dados

def atualizar_usuario():
    resp = input(f'Deseja atualizar o usuário? [S/N]').strip().upper()
    if resp == "S":
        sql = f"""UPDATE FROM usuarios WHERE id_usuario = '{id_usuario}';"""
        cursor.execute(sql)
        conexao.commit()

def atualizar_filme():
    resp = input(f'Deseja atualizar o filme? [S/N]').strip().upper()
    if resp == "S":
        sql = f"""UPDATE FROM filmes WHERE id_filme = '{id_filme}';"""
        cursor.execute(sql)
        conexao.commit()

def conectar():
    
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='conecta',
    )
    cursor = conexao.cursor()
    return conexao, cursor

    cursor.close()
    conexao.close()
