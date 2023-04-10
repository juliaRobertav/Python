from SQL.read import listar_filmes, listar_usuarios
from netflix import Cliente
import os

#jogar o menu dentro de um objeto(Cliente)


def menu():
    usuario = []
    usuarios = []
    escolhido = ['###', '###', '###', '###']
    planos = ["basic", "medium", "premium"]
    tipos = ["user", "admin"]

    filme = []
    filmes = []
    generos = ['comédia', 'aventura', 'drama']
    while True:
        print("-------------------",
              f"\n Usuário: {escolhido[0]} "
              f"\n Tipo: {escolhido[3]} "
              f"\n [0] - Sair ",
              f"\n [1] - Cadastrar Usuário ",
              f"\n [2] - Cadastrar Filme ",
              f"\n [3] - Login ",
              f"\n [4] - Listar filmes ",
              f"\n [5] - Assistir filmes ",
              f"\n ------------------- ")
        os.system('pause')

        op = int(input("Digite uma opção: "))

        if op == 0:
            break
        elif op == 1:
            nome = input("Nome: ").upper().strip()
            usuario.append(nome)
            email = input("Email: ")
            usuario.append(email)
            while True:
                print(f"planos disponíveis: |basic| |medium| |premium|")
                plano = input("Plano: ")
                if plano in planos:
                    usuario.append(plano)
                    break
                else:
                    print(f"\33[31mPlano Invalido, tente novamente\33[m")

            while True:
                print("Tipo: |user| |admin|")
                tipo = input("Tipo: ")
                if tipo in tipos:
                    usuario.append(tipo)
                    break
                else:
                    print(f"\33[31mPlano Invalido, tente novamente\33[m")

            usuarios.append(usuario[:])
            usuario.clear()

        elif op == 2:
            if escolhido[3] == 'user' or escolhido[3] == '###':
                print("\033[31mAPENAS ADMINS PODEM CADASTRAR FILMES\33[m")
            else:
                nome_filme = input("Digite o nome do filme: ").upper()
                filme.append(nome_filme)
                while True:
                    print(f"Gêneros: {generos}")
                    genero_filme = input("Digite o genero do filme: ").capitalize()
                    if genero_filme in planos:
                        filme.append(genero_filme)
                        break
                    else:
                        print(f"\33[31mPlano Invalido, tente novamente\33[m")
                while True:
                    print(f"Planos: {planos}")
                    plano_necessario = input("Digite o plano necessario para assisti-lo: ")
                    if plano_necessario in planos:
                        filme.append(plano_necessario)
                        break
                    else:
                        print(f"\33[31mPlano Invalido, tente novamente\33[m")

                filmes.append(filme[:])
                filme.clear()

        elif op == 3:
            escolhido.clear()
            cliente = input("Nome: ").upper().strip()
            for i in range(len(usuarios)):
                if cliente == usuarios[i][0]:
                    escolhido.append(usuarios[i][0])
                    escolhido.append(usuarios[i][1])
                    escolhido.append(usuarios[i][2])
                    escolhido.append(usuarios[i][3])

            print(escolhido)

        elif op == 4:
            listar_filmes()

        elif op == 5:
            add_filme = input("Digite o filme que deseja assistir:")
            filmes.append(add_filme)
            print(filmes)
