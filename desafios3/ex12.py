x = int(input("Digite um numero para calculo fatorial: "))
c = x
f = 1
print('Calculando {}! ='.format(x),end=" ")
while c > 0:
    print("{}".format(c),end=" ")
    print(" X " if c > 1 else " = ", end="")
    f *= c
    c -= 1
print("{}".format(f))