p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))
t = p
cont = 1
while cont <= 10:
    print(' {}'.format(t), end="")
    t += r
    cont += 1