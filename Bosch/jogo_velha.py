##comandos##
# while para resposta
# for para posições
# while true para jogadas
# jogadores
# ganhador
# exibir tabela
# MQTT(pesquisar mais)
# não esquecer de aplicar no main
# jogador escolher a posição e "X" ou "O"


def tabuleiro():
    tab = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
           ]

    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(tab)


def jogadas():
    while True:
        try:
            jogada = int(input("Digite a posição em que deseja jogar:"))
            for jogada in range(1, 10):
                return jogada
        except ValueError:
            print("Verifique novamente, o número não está no tabuleiro ou isto não é um número...")
            continue


def posicao(posicao_jogador):
    pos = jogadas() - 1
    tabuleiro[pos] = posicao_jogador
    if tabuleiro[pos] == "X" or tabuleiro[pos] == "O":
        print("\nEspaço já ocupado. Tente colocar em outro.")
    else:



if __name__ == "__main__":
    tabuleiro()
    jogadas()
    posicao()

