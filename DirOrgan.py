import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk



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
    try: 
        os.mkdir(pasta)
        os.chdir(pasta)
        flag = 0
        janela_subpastas()
    except:
        flag = 1
    if flag == 1:
        if pasta == '':
            telaConfirma.destroy()
            erro01 = Toplevel()
            erro01.title('DirOrgan')
            erro01.config(background='#212121')
            msgErro = ttk.Label(erro01, text='Digite o nome da pasta', style='ERROR.TLabel')
            msgErro.pack(padx=5, pady=10)
            Button(erro01, text='OK', command=erro01.destroy).pack(pady=10)
        else:
            telaConfirma.destroy()
            erro02 = Toplevel()
            erro02.title('DirOrgan')
            erro02.config(background='#212121')
            msgErro = ttk.Label(erro02, text='Os nomes de arquivo não podem conter nenhum dos seguintes caracteres:\n /\?:*<>|', style='ERROR.TLabel')
            Button(erro02, text='OK', command=erro02.destroy).pack(pady=10, side=BOTTOM)
            msgErro.pack(padx=5, pady=5)

def cria_subpasta():
    subpasta = entrada2.get()
    try:
        os.mkdir(subpasta)
    except:
        if subpasta == '':
            erro01 = Toplevel()
            erro01.title('DirOrgan')
            erro01.config(background='#212121')
            msgErro = ttk.Label(erro01, text='Digite o nome da pasta', style='ERROR.TLabel')
            msgErro.pack(padx=5, pady=10)
            Button(erro01, text='OK', command=erro01.destroy).pack(pady=10)
        else:
            erro02 = Toplevel()
            erro02.title('DirOrgan')
            erro02.config(background='#212121')
            msgErro = ttk.Label(erro02, text='Os nomes de arquivo não podem conter nenhum dos seguintes caracteres:\n /\?:*<>|', style='ERROR.TLabel')
            Button(erro02, text='OK', command=erro02.destroy).pack(pady=10, side=BOTTOM)
            msgErro.pack(padx=5, pady=5)

def janela_subpastas():
    global entrada2
    janelaInicial.destroy()
    janelaSubpastas = Tk()
    janelaSubpastas.title('DirOrgan') #Define o nome da janela
    janelaSubpastas.config(background='#212121') #Define cor de fundo
    
    #Estilo das Labels
    style = ttk.Style()
    style.configure('Dark.TLabel', font=('Lucida Console', 11), background='#212121', foreground='#00ff1e')
    style.configure('ERROR.TLabel', font=('Lucida Console', 11), background='#212121', foreground='red', justify=CENTER)    
    
    ttk.Label(janelaSubpastas, text='Crie suas subpastas:', style='Dark.TLabel').pack()
    painel2 = Frame(janelaSubpastas, bg='#212121')
    painel2.pack(padx=10, pady=10)
    ttk.Label(painel2, text='Nome da subpasta:', style='Dark.TLabel').pack(side=LEFT)
    entrada2 = Entry(painel2, width=30, relief=SUNKEN)
    entrada2.pack(side=LEFT, pady=5)
    Button(painel2, text='Nova pasta', command=cria_subpasta).pack(side=LEFT, padx=10)

# Janela inicial principal do programa
janelaInicial = Tk()
janelaInicial.config(background='#212121') #Define cor de fundo
janelaInicial.title('DirOrgan') #Define o nome da janela

#Estilo das Labels
style = ttk.Style()
style.configure('Dark.TLabel', font=('Lucida Console', 11), background='#212121', foreground='#00ff1e')
style.configure('ERROR.TLabel', font=('Lucida Console', 11), background='#212121', foreground='red', justify=CENTER)

ttk.Label(janelaInicial, text='Bem vindo ao DirOrgan', style="Dark.TLabel").pack(pady=15) #Msg de boas vindas
ttk.Label(janelaInicial, text='Selecione o local de criação da nova pasta', style="Dark.TLabel").pack(pady=6) #Msg Instruções
painel = Frame(janelaInicial, bg='#212121') 
painel.pack(padx=10, pady=10)
ttk.Label(painel, text='Nome da pasta:', style='Dark.TLabel').pack(side=LEFT)
entrada = Entry(painel, width=30, borderwidth=1, relief=SUNKEN) #Espaço para usuário inserir o nome da pasta do seu projeto
entrada.pack(side=LEFT, pady=5)
Button(painel, text='Procurar', command=caminho_pasta).pack(side=LEFT, padx=10)

janelaInicial.mainloop()