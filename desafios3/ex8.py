mediaidade = 0
somaidade = 0
mdih = 0
nomex = ''
totalm20 = 0
for p in range(1, 5):
    print('-------- {}°Pessoa-------- '.format(p))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    mediaidade = somaidade / p
    print("A media de idade é {}".format(mediaidade))

    if p == 1 and sexo in 'Mm':
        mdih = idade
        nomex = nome
    if sexo in "Mm" and idade > mdih:
        mdih = idade
        nomex = nome

    print(" O homem mais velho tem {} anos e seu nome é {}".format(mdih, nomex))
    if sexo in "Ff" and idade < 20:
        totalm20 += 1
    print("São {} mulheres com menos de 20 anos".format(totalm20))