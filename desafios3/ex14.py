p = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razao: "))
t = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(' {}'.format(t), end="")
        t += r
        cont += 1
    print(" Pausa")
    mais = int(input("Quantos ternos voce quer mostrar a mais? "))