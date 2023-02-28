from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    nasc = int(input("Em que ano {} pessoa nasceu: ".format(pess)))
    ida = atual - nasc
    if ida >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print("São {} menores de idade".format(totalmenor))
print("São {} maiores de idade".format(totalmaior))