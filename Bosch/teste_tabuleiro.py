	def verificar_tabuleiro(self):
		"""
        Verifica o tabuleiro para saber quem ganhou ou
        caso dê empate
        :param self:
        :return:
        """
		# Verificações das 3 verticais
		if self.tabuleiro['7'] == self.tabuleiro['4'] == self.tabuleiro['1'] != ' ':
			return self.tabuleiro['7']
		elif self.tabuleiro['8'] == self.tabuleiro['5'] == self.tabuleiro['2'] != ' ':
			return self.tabuleiro['8']
		elif self.tabuleiro['9'] == self.tabuleiro['6'] == self.tabuleiro['3'] != ' ':
			return self.tabuleiro['9']


		# Verificações das 3 horizontais
		elif self.tabuleiro['7'] == self.tabuleiro['8'] == self.tabuleiro['9'] != ' ':
			return self.tabuleiro['7']
		elif self.tabuleiro['4'] == self.tabuleiro['5'] == self.tabuleiro['6'] != ' ':
			return self.tabuleiro['8']
		elif self.tabuleiro['1'] == self.tabuleiro['2'] == self.tabuleiro['3'] != ' ':
			return self.tabuleiro['1']

		# Verificações das 2 diagonais
		elif self.tabuleiro['7'] == self.tabuleiro['5'] == self.tabuleiro['3'] != ' ':
			return self.tabuleiro['7']
		elif self.tabuleiro['1'] == self.tabuleiro['5'] == self.tabuleiro['9'] != ' ':
			return self.tabuleiro['1']

		# Verificando empate
		if [*self.tabuleiro.values()].count(' ') == 0:
			return "empate"
		else:
			return [*self.tabuleiro.values()].count(' ')
