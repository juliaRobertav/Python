sexo = str(input("Digite seu sexo: [F/M]")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Error, sexo invalido! informe novamente corretamente: ")).strip().upper()
print("Sexo {} resgistrado corretamante".format(sexo))