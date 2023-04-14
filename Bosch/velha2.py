import self


class Jogo():
    """
    Classe onde engloba todos os processos do jogo da velha
    """
    jogo1 = None


tabuleiro = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
             ]


def __init__(self, jogador_inicial):
    """
    Função para iniciar o jogo e acrescentar todas
    as outras funções
    :param self:
    :param jogador_inicial: inicia o jogo ja com o primeiro jogador
    :return:
    """
    self.__tabuleiro = tabuleiro
    self.jogo1 = jogador_inicial
    self.imprimir_tabuleiro()
    self.icone1()
    self.icone2()
    self.jogadas()
    self.verificar_jogadas()
    self.verificar_tabuleiro()
    self.joga()
    self.erros()


def imprimir_tabuleiro(self):
    """
    Nesta função é onde exibe o tabuleiro
    :param self:
    :return:
    """
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
    print("└───┴───┴───┘")
    print(tabuleiro)


@property
def icone1(self):
    """
    Função para o getter 1, onde irá ser retornado o ícone
    :param self:
    :return:
    """
    print(icone1())
    self._icone1 = icone1


@icone1.setter
def icone1(self, icone1):
    """
    Função para o setter 1, onde informará o ícone escolhido
    :param self:
    :param icone1:
    :return:
    """
    icon = input("Digite o icone que deseja [X or O]:")
    if icon == "X":
        print(icone1)
        self._icone1 = icone1
    else:
        print("Erro!")


@property
def icone2(self):
    """
    Função para o getter 2,
    onde será retornado o segundo ícone escolhido
    :param self:
    :return:
    """
    print(icone2())
    self._icone2 = icone2


@icone2.setter
def icone1(self, icone1):
    """
    Função para o setter 2, onde sera escolhido outro ícone
    :param self:
    :param icone1:
    :return:
    """
    icon = input("Digite o icone que deseja [X or O]:")
    if icon == "X":
        print(icone2)
        self._icone2 = icone2
    else:
        print("Erro!")


def jogadas():
    """
    Inicia as jogadas e verifica os ícones escolhidos
    :return:
    """
    icone1()
    icone2()
    icone = 0
    jogar = input("Digite a posição que deseja jogar:")
    for pos in jogar(1, 10):
        if icone == icone1():
            tabuleiro[pos] = "X"
        elif icone == icone2():
            tabuleiro[pos] = "O"


def verificar_jogadas(self, jogada):
    """
    Verifica se as jogadas estão corretas
    :param self:
    :param jogada:
    :return:
    """
    if jogada in self.tabuleiro.keys():
        if self.tabuleiro[jogada] == " ":
            return True
    return False


def verificar_tabuleiro(self):
    """
    Verifica o tabuleiro para saber quem ganhou ou
    caso dê empate
    :param self:
    :return:
    """
    # Verificações das 3 verticais
    if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
        return self.tabuleiro['7']
    elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
        return self.tabuleiro['8']
    elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
        return self.tabuleiro['9']


    # Verificações das 3 horizontais
    elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
        return self.tabuleiro['7']
    elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
        return self.tabuleiro['8']
    elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
        return self.tabuleiro['1']

    # Verificações das 2 diagonais
    elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
        return self.tabuleiro['7']
    elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
        return self.tabuleiro['1']

    # Verificando empate
    if [*self.tabuleiro.values()].count(' ') == 0:
        return "empate"
    else:
        return [*self.tabuleiro.values()].count(' ')


def joga():
    """
    Função apenas para jogada
    :return:
    """
    while True:
        self.imprimir_tabuleiro()

        print(f"Turno do {self.jogo1}, qual sua jogada?")

        # Enquanto o jogador não fizer uma jogada válida
        while True:
            jogar = input("Jogada: ")

            if self.verificar_jogada(jogar):  # Se a jogada for válida...
                break  # Encerra o loop
            else:
                print(f"jogado do {self.jogo1} inválida, jogue novamente.")

        self.tabuleiro[jogar] = self.jogo1

        verificar_jogo = self.verificar_tabuleiro()

        if verificar_jogo == "X":
            print("X é o vencedor!!!")
            break

        elif verificar_jogo == "O":
            print("O é o vencedor!!!")
            break

        if verificar_jogo == "empate":
            print("EMPATE!!!")
            break

        # Troca o jogador do próximo turno
        self.jogo1 = "X" if self.jogo1 == "O" else "O"

def erros():
    """
    Função caso de erros
    :return: 
    """
    try:
        for jogada in range(1, 10):
            return jogada
    except ValueError:
        print("Verifique novamente, o número não está no tabuleiro ou isto não é um número...")


if __name__ == '__main__':
    joga()
