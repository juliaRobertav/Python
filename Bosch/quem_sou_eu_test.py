import random
import pandas as pd

class Personagem:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def __str__(self):
        return f"Nome: {self._nome}\nIdade: {self._idade}"

    def _fazer_pergunta(self):
        perguntas = [
            "Sou um animal?",
            "Sou uma pessoa famosa?",
            "Sou um personagem fictício?",
            "Sou conhecido(a) por minha profissão?"
        ]
        return random.choice(perguntas)

    def jogar(self):
        print(f"Adivinhe quem eu sou! Responda às perguntas:")
        resposta = input(self._fazer_pergunta() + " (s/n): ")
        self._verificar_resposta(resposta.lower())

    def _verificar_resposta(self, resposta):
        if resposta == "s":
            print("Você acertou!")
        else:
            print("Você errou!")

    # Getter e Setter para o atributo nome
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    # Classmethod para criar um personagem com base em uma string
    @classmethod
    def criar_personagem(cls, personagem_str):
        nome, idade = personagem_str.split(",")
        return cls(nome.strip(), int(idade.strip()))

    # Staticmethod para exibir uma mensagem de boas-vindas
    @staticmethod
    def boas_vindas():
        print("Bem-vindo ao jogo 'Quem sou eu?'!")

class Animal(Personagem):
    def __init__(self, nome, idade, especie):
        super().__init__(nome, idade)
        self._especie = especie

    def __str__(self):
        return super().__str__() + f"\nEspécie: {self._especie}"

class PessoaFamosa(Personagem):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self._profissao = profissao

    def __str__(self):
        return super().__str__() + f"\nProfissão: {self._profissao}"

class PersonagemFicticio(Personagem):
    def __init__(self, nome, idade, obra):
        super().__init__(nome, idade)
        self._obra = obra

    def __str__(self):
        return super().__str__() + f"\nObra: {self._obra}"

class PalavrasAnimais:
    _palavras = ["leão", "elefante", "girafa", "tigre", "macaco"]
    _dicas = [
        "Sou o rei da selva.",
        "Tenho uma tromba longa.",
        "Tenho um pescoço comprido.",
        "Sou um felino listrado.",
        "Sou conhecido por subir em árvores."
    ]

    @classmethod
    def obter_palavra(cls):
        indice = random.randint(0, len(cls._palavras) - 1)
        return cls._palavras[indice]

    @classmethod
    def obter_dica(cls):
        indice = random.randint(0, len(cls._dicas) - 1)
        return cls._dicas[indice]

class Palavras:
    # Adicione

