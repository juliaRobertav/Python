num = int(input('Numero: '))

if num >= 1:
    for i in range(1, num ):
        if num % 1 == 0:
            print(num, 'é primo')
        else:
            print(num, 'não é primo')
            break