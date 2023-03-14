class Cliente:
    def __init__(self, nome='', email='', planoX='', tipo='user'):
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        if planoX in self.planos:
            self.plano = planoX
        else:
            print('Plano Inválido.')
            self.plano = ''

        self.tipos = ['user', 'admin']
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print('Tipo de usuário inválido.')
            self.tipo = ''
            
            
            
    def mudar_plano(self, novoPlano):
        if novoPlano in self.planos:
            self.plano = novoPlano
        else:
            print('Plano Inválido')
            
            
     def ver_filme(self, filme, planoFilme):
        if self.plano == 'premium' or self.plano == planoFilme:
            print(f'o cliente {self.nome} pode assistir {filme}')
        elif self.plano == 'medium' and planoFilme == 'basic':
            print()
        else:
            print(f'o cliente {self.nome} \33[31mNÃO pode \33[m assistir {filme}')
            
            
                  
from netflix import Cliente

b1 = Cliente('Julia', 'jj@ggi', 'premium', 'admin')
print(f'Plano Velho: \33[31m{b1.plano.upper()}\33[m')
b1.mudar_plano('basic')
print(f'Plano Novo: \33[34m{b1.plano.upper()}\33[m')
