from ctypes import alignment
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import font


'''
1 - Nome da pasta a ser criada
2 - Caminho onde a pasta vai ser criada
3 - Criação da pasta principal
4 - Criação das Subpastas
5 - Separação dos arquivos por tipo
6 - Criação de template de organização de pastas
7 - Edição do template
'''

def confirma():
    global telaConfirma
    global pasta
    telaConfirma = Toplevel()
    telaConfirma.title('DirOrgan')
    telaConfirma.config(background='#212121')
    ttk.Label(telaConfirma, text=f'Confirme o nome da pasta: {pasta}', style='Dark.TLabel').pack()
    painel2 = Frame(telaConfirma, background='#212121')
    painel2.pack(padx=15, pady=10)
    Button(painel2, text='Sim', command=cria_pasta).pack(side=LEFT, padx=10)
    Button(painel2, text='Não', command=telaConfirma.destroy).pack(side=LEFT, padx=10)

def caminho_pasta():
    global pasta
    caminho = filedialog.askdirectory()
    os.chdir(caminho)
    pasta = entrada.get()
    confirma()
    
def cria_pasta():
    global telaConfirma
    telaConfirma.destroy()
    try: 
        os.mkdir(pasta)
        flag = 0
        janela_subpastas()
    except:
        flag = 1
    if flag == 1:
        if pasta == '':
            msgErro = ttk.Label(janelaInicial, text='Digite o nome da pasta', style='ERROR.TLabel')
            msgErro.pack()
        else:
            msgErro = ttk.Label(janelaInicial, text='Os nomes de arquivo não podem conter nenhum dos seguintes caracteres:\n /\?:*<>|', style='ERROR.TLabel')
            msgErro.pack(padx=5, pady=5)


def janela_subpastas():
    janelaSubpastas = Tk()
    janelaSubpastas.title('DirOrgan') #Define o nome da janela
    janelaSubpastas.config(background='#212121') #Define cor de fundo
    janelaInicial.destroy()

janelaInicial = Tk()
janelaInicial.config(background='#212121') #Define cor de fundo
janelaInicial.title('DirOrgan') #Define o nome da janela
style = ttk.Style()
style.configure('Dark.TLabel', font=('Lucida Console', 11), background='#212121', foreground='#00ff1e')
style.configure('ERROR.TLabel', font=('Lucida Console', 11), background='#212121', foreground='red', justify=CENTER)

ttk.Label(janelaInicial, text='Bem vindo ao DirOrgan', style="Dark.TLabel").pack(pady=15) #Msg de boas vindas
ttk.Label(janelaInicial, text='Selecione o local de criação da nova pasta', style="Dark.TLabel").pack(pady=6) #Msg Instruções
painel = Frame(janelaInicial, bg='#212121') 
painel.pack(padx=10, pady=10)
ttk.Label(painel, text='Nome da pasta:', style='Dark.TLabel').pack(side=LEFT)
entrada = Entry(painel, width=30, borderwidth=1, relief=SUNKEN)
entrada.pack(side=LEFT, pady=5)
Button(painel, text='Procurar', command=caminho_pasta).pack(side=LEFT, padx=10)


janelaInicial.mainloop()