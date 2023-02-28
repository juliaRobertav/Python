from random import randint

a = False
x = 0
while not a:
    comp = randint(0, 10)
    palpite = int(input("Chuta um numero de 0 á 10:"))
    x += 1
    if palpite == comp:
        a = True
        print("Acertou!!")
        print("Voce tentou {} vezes ".format(x))
    else:
        print("tente novamente")