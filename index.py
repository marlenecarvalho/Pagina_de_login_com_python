#importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database

# criando janela
jan = Tk()
jan.title('MC Systems - Acess Painel')
jan.geometry('600x300') #tamanho da janela
jan.configure(background='white') #cor da janela
jan.resizable(width=False, height=False) #para não poder alterar o tamanho da TELA
jan.attributes('-alpha', 0.9) #transparencia
jan.iconbitmap(default='favicon.ico') #Inserindo o ícone da logo 

# Carregando imagens
logo = PhotoImage(file='logo.png')

# Ajustes de cor da janela
LeftFrame = Frame(jan, width=200, height=300, bg='purple', relief='raise')
LeftFrame.pack (side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg='purple', relief='raise')
RightFrame.pack (side=RIGHT)

# Inserindo a logo na janela
LogoLabel = Label(LeftFrame, image=logo, bg='purple')
LogoLabel.place(x=2, y=2)

# Criando campo de usuario e senha
UserLabel = Label(RightFrame, text='Usuário:', font=('arial', 20), bg='purple', fg='white')
UserLabel.place(x=5, y=110)
UserEntry= ttk.Entry(RightFrame, width= 30)
UserEntry.place(x=150, y=110)

SenhaLabel= Label(RightFrame, text='Senha:', font=('arial', 20), bg='purple', fg='white')
SenhaLabel.place(x=5, y=150)
SenhaEntry= ttk.Entry(RightFrame, width= 30, show='*')
SenhaEntry.place(x=150, y=160)

# Botões
LoginButton= ttk.Button(RightFrame, text='Login', width=30)
LoginButton.place(x=100, y=223) #Place = posição
#Removendo os botões
def Cadastrar():
  LoginButton.place(x=5000)
  CadastroButton.place(x=5000)
  #Pedindo as informações para cadastro
  NomeLabel= Label(RightFrame, text='Nome:', font= ('Ariel', 20), bg='purple', fg='white')
  NomeLabel.place(x=5, y=20)
  NomeEntry= ttk.Entry(RightFrame, width= 40)
  NomeEntry.place(x=95, y=30)

  EmailLabel= Label(RightFrame, text='E-mail:', font=('Ariel', 20), bg='purple', fg='white')
  EmailLabel.place(x=5, y=62)
  EmailEntry= ttk.Entry(RightFrame, width=40)
  EmailEntry.place(x=95, y=72)

  #Definindo os comando para o cadastro ao banco
  def Cadastrarbancodedados():
    Nome = NomeEntry.get()
    Email = EmailEntry.get()
    Usuario = UserEntry.get()
    Senha = SenhaEntry.get()
    database.cursor.execute("""
    INSERT INTO Usuario (Nome, Email, Usuario, Senha) VALUES(?, ?, ?, ?)
    """, (Nome, Email, Usuario, Senha))
    database.conn.commit()
    messagebox.showinfo(title="Informação de cadastro" , Message="Conta criada com sucesso!")

  #Colocando os botões de volta
  CadastrarButton = ttk.Button(RightFrame, text='Cadastro', width=30, command=Cadastrarbancodedados)
  CadastrarButton.place(x=100, y=225)
  def Voltar():
    NomeLabel.place(x=5000)
    EmailLabel.place(x=5000)
    NomeEntry.place(x=5000)
    EmailEntry.place(x=5000)

    #Trocando os botões novamente
    CadastrarButton.place(x=5000)
    VoltarButton.place(x=5000)
    LoginButton.place(x=100)
    CadastroButton.place(x=125)

  VoltarButton = ttk.Button(RightFrame, text='Voltar', width=20, command=Voltar)
  VoltarButton.place(x=130, y=260)

CadastroButton = ttk.Button(RightFrame, text='Cadastrar', width=20, command=Cadastrar)
CadastroButton.place(x=125, y=260)

# Sempre botar para final de janela
jan.mainloop()

