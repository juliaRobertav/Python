import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class Janela(QMainWindow):  # Herança
	def __init__(self):
		super().__init__()  # Chamando o construtor da classe mãe(QMainWindow)
		self.topo = 100
		self.esquerda = 100
		self.largura = 800
		self.altura = 600
		self.titulo = " Primeira Jnaela"
		self.carregar_janela()

	def carregar_janela(self):
		self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
		self.setWindowTitle(self.titulo)
		self.show()


if __name__ == "__main__":
	aplicacao = QApplication(sys.argv)
	j = Janela()
	sys.exit(aplicacao.exec())
