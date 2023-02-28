maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("Digite o peso da pessoa {}: ".format(p)))
    if peso == 1:
        menor = p
        maior = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}".format(maior))
print("O menor peso lido foi de {}".format(menor))