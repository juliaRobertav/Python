import random


def forca():
    secreto = random.choice
    digitadas = []
    chances = 3

    print('=' * 20)
    print("  JOGO DA FORCA! \n SEJA BEM VINDO!  ")
    print('=' * 20)

    while True:
        palavra = str(input("Digite uma letra: \n"))
        if len(palavra) > 1:
            print("DIGITE APENAS 1 LETRA POR VEZ!!!ERRO!!!")
            digitadas.append(palavra)
            chances -= 2
            continue

    digitado_temporário = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            digitado_temporário += letra_secreta
        else:
            digitado_temporário += '*'
            break

    if digitado_temporário == secreto:
        print(" PARABÉNS VOCÊ ACERTOU!!!")

    else:
        print(f"A palavra está assim: {digitado_temporário}")

    if palavra not in secreto:
        chances -= 1
    breakpoint()
    print(f"Você tem {chances} chances.")
    print()


if __name__ == "__main__":
    forca()
