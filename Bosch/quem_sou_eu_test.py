import random

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

# Exemplo de uso do jogo
def main():
    # Criando personagens
    leao = Animal("Leão", 5, "Felino")
    shakespeare = PessoaFamosa("William Shakespeare", 456, "Escritor")
    superman = PersonagemFicticio("Superman", 30, "Quadrinhos")

    # Jogando com os personagens
    leao.jogar()
    print()

    shakespeare.jogar()
    print()

    superman.jogar()

if __name__ == "__main__":
    main()
