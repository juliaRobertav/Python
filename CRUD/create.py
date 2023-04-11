import mysql.connector
from prettytable import PrettyTable

def criar():
    try:        #conecta ao banco
        conexao = mysql.connector.connect(
            host='localhost',
            database='netflix',
            user='root',
            password=''
        )
        cursor.close()
        conexao.close()
    

    except:
        pass

    finally:

       

        def inserir_filmes(add_filmes, usuario, filme, plano, tipo, idade):
             planos = ['basic', 'medium', 'premium']
        filme = input("Filme: ")
        print(planos)
        while True:
            plano = input("Plano: ")
            if plano not in planos:
                print("Plano inválido...")
            else:
                break
        desc = input("Descrição: ")
        classif = int(input("Classificação: "))

        
        add_filmes ="""insert into filmes(filme,plano,descricao,class) 
                values 
                ('Vovózona', 'basic', 'CCC', 12),
                ('The ridiculous 6', 'medium', 'DDD', 14);"""
            
        inserir_filmes = f"""INSERT INTO filmes(usuario, filme, plano, tipo, idade)
        values 
        ('{usuario}', '{filme}', '{plano}', '{tipo}', '{idade}');"""
        cursor = conexao.cursor()
        cursor.execute(inserir_filmes)
        conexao.commit()
        # (""") = várias linhas-uma String

        cursor = conexao.cursor()
        cursor.execute(add_filmes)
        conexao.commit()

        sql = 'select * from filmes'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)

        print(tabela)

        for i in linhas:
            print(i[0], end='\t')
            print(i[1], ' ' * (10 - len(i[1])), end='\t')
            print(i[2], ' ' * (20 - len(i[1])), end='\t')
            print(i[3], ' ' * (10 - len(i[1])), end='\t')
            print(i[4])


        def inserir_usuário(usuario, email, plano, tipo, idade):
           
            inserir_usuário = f"""INSERT INTO usuario(usuario, email, plano, tipo, idade)
            values 
            ('{usuario}', '{email}', '{plano}', '{tipo}', '{idade}');"""
            cursor = conexao.cursor()
            cursor.execute(inserir_usuário)
            conexao.commit()

            sql = "SELECT * from usuarios"
            cursor.execute(sql)
            linhas = cursor.fetchall() # fetchall() => TRAGA TODAS AS LINHAS
            tabela = PrettyTable()
            tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

        for linha in linhas:
            tabela.add_row(linha)

        print(tabela)



    cursor = conexao.cursor()
    return conexao, cursor

