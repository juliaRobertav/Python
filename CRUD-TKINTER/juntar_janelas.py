import tkinter as tk


def abrir_janela():
	janela2 = tk.Toplevel()  # Ccomando que permite criar outra janela acima da primeira
	janela2.title('janela nova')
	label_nome = tk.Label(janela2, text= 'Nome')     # qual janela o label está
	label_nome.grid(row1=0, column1=0)
	botao_voltar = tk.Button(janela2, text='Fechar janela 2',command=janela2.destroy)  #comando p/ destruir janela 2
	botao_voltar.grid(row2=0, column2=0)

	janela = tk.Tk()

	botao = tk.Button(janela, text='Ir para nova janela',command=abrir_janela)
	# abrir_janela:função para executar no botão

	botao.grid(row3=0, column3=0)  # colocar botao dentro da janela

	janela.mainloop()
