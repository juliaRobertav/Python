class Who():

	def __init__(self, sorteio, jogador, dicas, palavras) -> None:
		self.inicio()
		self.sorteio = sorteio
		self.jogador = jogador
		self.__dicas = dicas
		self.__palavras = palavras
		dicas = []
		palavras = []

	@property
	def sorteioGet(self):
		return self.sorteio

	@sorteioGet.setter
	def sorteio_palavrasSet(self):
		self.sorteio = self.__palavras

	def inicio(self):
		print("=*=*=*=*=*=*=*=*=*=*")
		print("Bem vindo ao jogo!!!")
		print("=*=*=*=*=*=*=*=*=*=*")
		print("QUEM SOU EU??")
		print("Regras do jogo:")
		print("Cada palavra haverá 5 dicas e você deve adivinhar qual é, por isso, preste atenção!\n")
		print("=*=*=")
		print("Menu:")
		print("[1]Jogar")
		print("[2]Ver Ranking")
		print("[3]Sair")

	# def Pessoas(self):

	# def Menu(self):
