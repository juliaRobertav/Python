class ControleRemoto:

    caracteristicas:    #adjetivos
    - cor
    - largura
    - altura
    - comprimento

     métodos:       #ação
        - trocar de canal
        - ligar
        - desligar
        - alterar volume
        
class ControleRemoto:
        def __init__(self, corControle, larg, alt, compr):    #init: método construtor/
        self.cor = corControle     #self:obj-mesmo sistema obj diferentes/def carac. obj(propriedade)
        self.larg = larg
        self.alt = alt
        self.compr = compr
        
         def passar_canal(self, botao):
        if botao == '+':
            print('Próximo canal')
        elif botao == '-':
            print('Canal anterior')
  
  
  
  from controle import ControleRemoto

corX =input('Cor:')
j1 = ControleRemoto(corX, 2, 3, 4)      #instanciar obj(carregar todos elementos da classe)
j2 = ControleRemoto('branco', 8, 9, 10)
print(j1.cor)        #cada um como obj diferente
print(j2.cor)       #corControle: parâmetro temporário  
                    # cor:característica do obj que vem como parametro
                   
