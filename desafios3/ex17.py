resp = "Ss"
soma = 0
quantidade = 0
n = 0
maior = menor = 0

while resp in "Ss":
    soma += n
    quantidade += 1
    n = int(input("Digite um numero: "))
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if quantidade == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / quantidade
print("A media de seus numeros foi: {}".format(media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))