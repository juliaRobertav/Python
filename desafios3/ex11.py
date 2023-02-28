n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

opcao = 0

while opcao != 5:

    print('''    [1]-Somar
    [2]-Multiplicar
    [3]-Maior
    [4]-Novos numeros
    [5]-Fim do progama''')
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("A soma é:",n1+n2)
    elif opcao == 2:
        print("A multiplicação é:",n2*n1)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior entre {} e {} é {}: ".format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero: "))
    elif opcao == 5:
        print("Fim")
    else:
        print("Erro, tente novamente")
print("Fim do progama")