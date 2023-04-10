import mysql.connector
def criar():
    try:        #conecta ao banco
        conexao = mysql.connector.connect(
            host='localhost',
            database='netflix',
            user='root',
            password=''
        )

    except:
        pass

    finally:

        def inserir_filmes(add_filmes):
            add_filmes ="""insert into filmes(filme,plano,descricao,class) 
                  values 
                  ('Vovózona', 'basic', 'CCC', 12),
                  ('The ridiculous 6', 'medium', 'DDD', 14);"""
            # (""") = várias linhas-uma String

            cursor = conexao.cursor()
            cursor.execute(add_filmes)
            conexao.commit()

            sql = 'select * from filmes'
            cursor.execute(sql)
            linhas = cursor.fetchall()

            for i in linhas:
                print(i[0], end='\t')
                print(i[1], ' ' * (10 - len(i[1])), end='\t')
                print(i[2], ' ' * (20 - len(i[1])), end='\t')
                print(i[3], ' ' * (10 - len(i[1])), end='\t')
                print(i[4])


        def inserir_usuário(add_user):
            add_user ="""insert into usuarios(nome, email, plano)
                    values
                    b1 = Cliente("Julia", "jugui@gmail.com", "premium", "admin", 18)
                    print(f"PLANO B1 {b1.plano}")
                    teste = vars(b1)   

                    b2 = Cliente("Luis", "lui@gmail.com", "basic", "user", 17)
                    b2.ver_filme("Titanic", "basic");"""
