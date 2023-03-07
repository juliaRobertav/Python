K = { 'nome': 'Lindomar', 'idade': 20}    ###K:items  nome/idade:key   lindomar/20:value

nomes = {}
valores = []
for i in range(2):
    nomes['nome']= input('Nome:')
    nomes['idade'] = int(input('Idade:'))
    nomes['sexo'] = input('Sexo:')
    valores.append(nomes.copy())
    del nomes['idade']          ###apaga idade

print(valores[0]['nome'])


from random import randint   ###randint: sorteio
from time import sleep      ###quando sortear mostra devagar(tempo)--pausa
from operator import itemgetter   ###ordem crescente em dicionário
###sorted:ordem crescente  decrescente:reverse
for pos, val in valores.items():   ###enumeratte dicionario

from random import randint
from time import sleep
from operator import itemgetter

ordem = {}

valores = {
    'V1': randint(1, 9),
    'V2': randint(1, 9),
    'V3': randint(1, 9),
    'V4': randint(1, 9)
}

for pos, val in valores.items():
    print(val, end='')
    sleep(1)

ordem = sorted(valores.items(), key=itemgetter(1))   ###items:transforma em tupla
print('')
for i in range(4):
    print(ordem[i][1], end='')
    
    ou:
    
ordem = sorted(valores.values(), reverse =True)
print('')
print(ordem)
for i in range (len(ordem)):
    print(ordem[i], end=' ')
    
    
