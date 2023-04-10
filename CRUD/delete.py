import mysql.connector
from conexao import conectar

def excluir():
    conexao, cursor = conectar()

    comando = f'DELETE FROM filmes WHERE nome_filme = "{filme}"'
    comando = f'DELETE FROM usuarios WHERE nome_usuario = "{usuario}"'

    cursor.execute(comando)
    conexao.commit()
    conexao.close()
