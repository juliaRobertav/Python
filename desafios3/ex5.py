frase = input("escreva uma frase: ")
frase2 = frase.upper().replace(" ",'')
inverso = frase[::-1]

if frase == inverso:
    print(f"{frase} é um polindromo")
else:
    print(f'{frase} não é um polindromo')