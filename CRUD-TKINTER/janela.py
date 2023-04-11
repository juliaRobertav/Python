from tkinter import *
from tkinter import ttk
from create import  inserir_usuario

janela = Tk()


class Aplicacao():
    def __init__(self):
        self.janela = janela    #atributo do objeto
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()       #janela ficara na tela até fechar a tela

    def tela(self):
        self.janela.title('NETFLIX')
        self.janela.configure(background='#DACCE8')
        self.janela.geometry('700x500')
        self.janela.resizable(False, False)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame0 = Frame(self.janela, bg='#EFEBFE')
        self.frame0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)    #place=
        
        self.frame1 = Frame(self.janela, bg='#EFEBFE')
        self.frame1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.25)

        self.frame2 = Frame(self.janela, bg='#EFEBFE')
        self.frame2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)

    def botoes(self):
        self.btBuscar = Button(self.frame0, text='Buscar')
        self.btBuscar.place(relx=0.15, rely=0.40, relwidth=0.1, relheight=0.5)
    
        self.btLimpar = Button(self.frame0, text='Limpar')
        self.btLimpar.place(relx=0.27, rely=0.40, relwidth=0.1, relheight=0.5)

        self.btCreate = Button(self.frame0, text='Create', command=self.insert_user)
        self.btCreate.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.5)

        self.btRead = Button(self.frame0, text='Read')
        self.btRead.place(relx=0.57, rely=0.40, relwidth=0.1, relheight=0.5)

        self.btUpdate = Button(self.frame0, text='Update')
        self.btUpdate.place(relx=0.69, rely=0.40, relwidth=0.1, relheight=0.5)

        self.btDelete = Button(self.frame0, text='Delete')
        self.btDelete.place(relx=0.81, rely=0.40, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lbIDUsuario = Label(self.frame0, text='ID', bg='#EFEBFE' )
        self.lbIDUsuario.place(relx=0.05, rely=0.01, relwidth=0.1, relheight=0.30)

        self.lbNome = Label(self.frame1, text='Nome', bg='#EFEBFE' )
        self.lbNome.place(relx=0.005, rely=0.05, relwidth=0.1, relheight=0.30)

        self.lbEmail = Label(self.frame1, text='Email', bg='#EFEBFE' )
        self.lbEmail.place(relx=0.005, rely=0.35, relwidth=0.1, relheight=0.30)

        self.lbPlano = Label(self.frame1, text='Plano', bg='#EFEBFE' )
        self.lbPlano.place(relx=0.005, rely=0.65, relwidth=0.1, relheight=0.30)

        self.lbTipo = Label(self.frame1, text='Tipo', bg='#EFEBFE' )
        self.lbTipo.place(relx=0.305, rely=0.65, relwidth=0.1, relheight=0.30)

        self.lbIdade = Label(self.frame1, text='Idade', bg='#EFEBFE' )
        self.lbIdade.place(relx=0.605, rely=0.65, relwidth=0.1, relheight=0.30)

    def inputs(self):
        self.inpIDUsuario = Entry(self.frame0)      #Entry = input
        self.inpIDUsuario.place(relx=0.05, rely= 0.40, relwidth=0.10, relheight=0.50)

        self.inpNome = Entry(self.frame1)      
        self.inpNome.place(relx=0.10, rely= 0.125, relwidth=0.75, relheight=0.15)

        self.inpEmail = Entry(self.frame1)      
        self.inpEmail.place(relx=0.10, rely= 0.425, relwidth=0.75, relheight=0.15)

        self.inpPlano = Entry(self.frame1)      
        self.inpPlano.place(relx=0.10, rely= 0.725, relwidth=0.15, relheight=0.15)

        self.inpTipo = Entry(self.frame1)      
        self.inpTipo.place(relx=0.40, rely= 0.725, relwidth=0.15, relheight=0.15)

        self.inpIdade = Entry(self.frame1)      
        self.inpIdade.place(relx=0.70, rely= 0.725, relwidth=0.15, relheight=0.15)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))    #faixa dos labels
        self.listaCli.heading('#0', text='ID')     #cabeçalho
        self.listaCli.heading('#1', text='Nome')
        self.listaCli.heading('#2', text='Email')
        self.listaCli.heading('#3', text='Plano')
        self.listaCli.heading('#4', text='Tipo')
        self.listaCli.heading('#5', text='Idade')

        self.listaCli.column('#0', width=35)
        self.listaCli.column('#1', width=188)
        self.listaCli.column('#2', width=188)
        self.listaCli.column('#3', width=70)
        self.listaCli.column('#4', width=70)
        self.listaCli.column('#5', width=70)
     
        self.listaCli.place(relx=0.01, rely= 0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame2, orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely= 0.1, relwidth=0.04, relheight=0.85)

    def insert_user(self):
        inserir_usuario(self.inpNome.get(), self.inpEmail, self.inpPlano, self.inpTipo, self.inpIdade)
