class CaraCara:
	def __init__(self, usuario, dicas, opcoes, sorteio):
		self.usuario = usuario
		self.dicas = dicas
		self.opcoes = opcoes
		self.sorteio = sorteio

		self.entrada_usuario()

	@property
	def get_usuario(self):
		return self.usuario

	def exibir_informacao(self):
		print(self.usuario)

	def entrada_usuario(self):
		aposta_usuario = str(input("Digite sua aposta: "))
		self.usuario
		print(self.exibir_informacao())
