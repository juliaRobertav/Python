import random
import time

tempo_inicio = time.time()

mult = 0
x = 0
vida = 1000
chance = 2
sorteio = 0

while x == 0:
    mult = 0
    sorteio = random.randint(1, 1000)
    for count in range(2, sorteio):
        if (sorteio%count==0):
            mult += 1
        if mult == 0:
            x += 1
n = 0

while n != sorteio:
    n = int(input('Digite um número:'))
    tempo_resposta = time.time()


    if tempo_resposta -tempo_inicio > 60:
        print('Seu tempo acabou!')
        break

    if chance >=0 and vida >= 0:
        if n % 2 == 0:
            vida = vida - abs(n)
            print(f'Errou! Você digitou um número par! \n  \33[34m Vidas:{vida}\33[m')
        if n > sorteio:
            print(f'O número é menor!\33[31m \n  \33[34m Vidas:{vida}\33[m')
            chance -= 1
        else:
            print(f'O número é maior!\33[31m \n   \33[34m Vidas:{vida}\33[m')
            chance -= 1
        if chance <= 0 or vida <=0:
            print(f'Suas chances acabaram!\33[31m O número era: {sorteio}')
            print('FIM DE JOGO!')
            break
        if n == sorteio:
            print('Você acertou, Parabéns!')
