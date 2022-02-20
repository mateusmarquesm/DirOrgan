from cgitb import text
import os
from sqlite3 import Row
from tkinter import *
from tkinter import filedialog


'''
1 - Nome da pasta a ser criada
2 - Caminho onde a pasta vai ser criada
3 - Criação da pasta principal
4 - Criação das Subpastas
5 - Separação dos arquivos por tipo
6 - Criação de template de organização de pastas
7 - Edição do template
'''

def criar_pasta():
    caminho = filedialog.askdirectory()
    os.chdir(caminho)
    pasta = entrada.get()
    try: 
        os.mkdir(pasta)
        flag = 0
        subpastas()
    except:
        flag = 1
    if flag == 1:
        if pasta == '':
            msgErro = Label(janelaInicial, text='Digite o nome da pasta', font=('Lucida Console',11), bg='#212121', fg='red', padx=5, pady=5)
            msgErro.pack()
        else:
            msgErro = Label(janelaInicial, text='Os nomes de arquivo não podem conter nenhum dos seguintes caracteres:\n /\?:*<>|', font=('Lucida Console',11), bg='#212121', fg='red', padx=5, pady=5)
            msgErro.pack()

def subpastas():
    janelaSubpastas = Tk()
    janelaSubpastas.title('DirOrgan') #Define o nome da janela
    janelaSubpastas.config(background='#212121') #Define cor de fundo

    janelaInicial.destroy()

janelaInicial = Tk()
janelaInicial.config(background='#212121') #Define cor de fundo
janelaInicial.title('DirOrgan') #Define o nome da janela

Label(janelaInicial, text='Bem vindo ao DirOrgan', font=('Lucida Console',13), bg='#212121', fg='#00ff1e', padx=20, pady=20).pack() #Msg de boas vindas
Label(janelaInicial, text='Selecione o local de criação da nova pasta', font=('Lucida Console',11), bg='#212121', fg='#00ff1e', padx=5, pady=5).pack() #Msg Instruções
painel = Frame(janelaInicial, bg='#212121') 
painel.pack(padx=15, pady=10)
Label(painel, text='Nome da pasta: ', font=('Lucida Console',11), bg='#212121', fg='#00ff1e', padx=5, pady=5).pack(side=LEFT)
entrada = Entry(painel, width=30, borderwidth=1, relief=SUNKEN)
entrada.pack(side=LEFT, pady=5)
Button(painel, text='Procurar', command=criar_pasta).pack(side=LEFT, padx=10)


janelaInicial.mainloop()