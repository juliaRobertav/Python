import random


def forca2():
    print('=' * 20)
    print("  JOGO DA FORCA! \n SEJA BEM VINDO!  ")
    print('=' * 20)

    digitadas = []
    palavras = ["livro", "pitbull", "cerejeira", "mão", "sobrinho", "Mercedes-Benz"]
    secreto = random.choice(palavras)
    dicas = []
    letras_corretas = []
    letras_erradas = []
    corpo = 6
    modos_do_jogo = {
        "Nutela",
        "Café com Leite",
        "Raiz"
    }

    for j in digitadas:  ##j=jogo
        jogo = input(f"Escolha em qual modo você quer jogar: {modos_do_jogo}")
        if modos_do_jogo == "Nutela":
            tentativa = str(input("Digite uma letra: \n"))
            if digitadas == secreto:
                print("Você acertou!!!PARABÉNS!!!")
            elif len(tentativa) > 1:
                print("DIGITE APENAS 1 LETRA POR VEZ!!!ERRO!!!")
                corpo -= 1
            else:
                print("Deseja uma Dica?(S/N)")
                if "S":
                    print(dicas)
                if "N":
                    continue
        elif digitadas != palavras:
            print("Errou!!Tente Novamente!")
            corpo -= 1
        break


def modo2():
    return forca2()


if __name__ == "__main__":
    forca2()
    modo2()
