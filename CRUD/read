import mysql.connector

from SQL.create import cursor
from SQL.create import conexao

def listar_usuarios():
    if conexao.is_connected():
        print(f'Conectou a {conexao.get_server_info()}')

    cursor = conexao.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print(f'Banco => {linha[0]}')

    sql = 'select * from usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall()  ##joga tudo dentro de uma lista(cada linha é uma tupla)
    sql = 'select * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall() 

    for i in linhas:
        print(i[0], end='\t')
        print(i[1], ' '*(10-len(i[1])), end='\t')
        print(i[2], ' '*(20-len(i[1])),end='\t')
        print(i[3], ' '*(10-len(i[1])),end='\t')
        print(i[4], ' '*(10-len(i[1])),end='\t')
        print(i[5])


def conexao():
    cursor = conexao.cursor()
    cursor.execute(inserir_filmes)
    conexao.commit()
    sql = 'select * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    cursor.close()
    conexao.close()
   

if (__name__ == '__main__'):
    listar_usuarios()
