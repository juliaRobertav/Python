nome = input('Digite seu nome:').strip().upper()

for x in range(len(nome)):
 print(nome[0:x+1])