tel1 = input('Telefone: ')
tel2 = tel1.replace('-', '')

if len(tel2) == 8:
    print('9'+tel2[0:4]+'-'+tel2[4:])
elif len(tel2) == 9:
    print(tel2[0:5]+'-'+tel2[5:])
else:
    print('Valor inválido...')
