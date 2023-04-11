import csv
import pyglet

window = pyglet.window.window(width=1200, height=720, coption="Jogo da forca" )


##falta:tempo e menu

def imprimir_mensagem():
    print('-' * 35)
    print("SEJA BEM VINDO AO JOGO DA FORCA!!!")
    print('-' * 35)


def main():
    imprimir_mensagem()

    palavras = ["livro", "pitbull", "cerejeira", "mão"]
    digitadas = []
    letrasErradas = []
    letrasCertas = []

    jogar = True

    while jogar:
        letra = str(input("Digite uma letra:"))

        if len(letra) > 1:
            print("DIGITE UMA LETRA DE CADA VEZ")
            continue
        digitadas.append(letra)
        secreto = ''
        for letra in palavras:
            if letra in digitadas:
                secreto += letra
                digitadas.append(letrasCertas)

            else:
                digitadas.append(letrasErradas)
                print("Tente novamente!")

            if secreto == palavras:
                print("Parabéns!!Você ganhou!")
                break
            else:
                print(f"A palavra está assim: {secreto}")


def vidas(letra, secreto):
    main()

    chances = 6

    if letra not in secreto:
        chances -= 1

    if chances <= 0:
        print("Poxa, acabaram suas chances! :(")

    print(f"Você tem {chances} chances.")
    print()


def nutela(letrasErradas, letrasCertas, digitadas):
    dicas = ["ler", "raça de cachorro", "árvore", "parte do corpo"]
    dicas.index("ler", "raça de cachorro", "árvore", "parte do corpo")

    print(f"A palavra está assim:{digitadas}")
    print(f"Letras erradas:{letrasErradas}")
    print(f"Letras Corretas:{letrasCertas}")


def cafe_com_leite():
    main()
    chances = -3
    palavras = ["livro", "pitbull", "cerejeira", "mão"]
    dicas = ["ler", "raça de cachorro", "árvore", "parte do corpo"]

    palavras.append("sobrinho")
    dicas.append("parente")
    palavras.pop(4)
    dicas.pop(4)
    palavras.remove("livro")
    dicas.remove("ler")


def raiz(texto=None):
    with open('readme.txt', 'w', encoding='utf-8') as f:
        f.write('readme')
        x = csv.writer(f)
        for f in texto:
            "livro";
            "ler\n"
            "pitbull";
            "raça de cachorro\n"
            "cerejeira";
            "árvore\n"
            "mão";
            "parte do corpo\n"
            print(f)
    f.close()


def imprimir_jogo(letrasErradas, letrasCertas, palavras):
    print(len(letrasErradas))
    print("Letras Erradas:", end=' ')

    v = '-' * len(letrasCertas)
    for x in range(len(palavras)):
        if palavras[x] in letrasCertas:
            v = v[:x] + palavras[x] + v[x + 1:]
            print(v)


def erros():
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    main()
    pyglet.app.run()
