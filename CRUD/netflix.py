import mysql.connector

class Cliente:
    def __init__(self, nome="", email="", plano="", tipo=""):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']

        def criar_usuario():
            comando = f'INSERT usuario FROM usuarios = 10 WHERE nome_usuario = "{usuario}"'

        if plano in self.planos:
            self.plano = plano
        else:
            print("Plano Invalido")
            self.plano = ""

        self.tipos = ['user', 'admin']
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print("tipo invalido")
            self.tipo = ""


    def mudar_plano(self, novoPlano):
        if novoPlano in self.planos:
            self.plano = novoPlano
        else:
            print("Plano não existente")

    def ver_filme(self, filme, planoFilme):
        if self.plano == "premium" or self.plano == planoFilme:
            print(f"O cliente {self.nome} \33[34mpode\33[m assistir {filme}")
        elif self.plano == "medium" and planoFilme == "basic":
            print(f"O cliente {self.nome} \33[31mNÃO\33[m pode assistir {filme}")
        else:
            print(f"O cliente {self.nome} \33[31mNÃO\33[m pode assistir {filme}")
