from itertools import count
import os
from threading import local

'''
1 - Nome da pasta a ser criada
2 - Caminho onde a pasta vai ser criada
3 - Criação da pasta principal
4 - Criação das Subpastas
5 - Separação dos arquivos por tipo
6 - Criação de template de organização de pastas
7 - Edição do template'''

# Analisa se existe caracteres especiais que não podem ser utilizados em nomes de pastas.
def charcheck(txt):
    """
    Analisa se existe caracteres especiais que não podem ser utilizados em nomes de pastas.
    
    """
    while True:
        cont = 0
        for c in range(0, len(txt)):
            if txt[c] in '?/\:<>*|':
                cont += 1
        if cont >= 1:
            print('Os nomes de arquivo não podem conter nenhum dos seguintes caracteres:\n /\?:*<>|')
            txt = str(input('Nome da pasta: '))
        else:
            break
    return txt    


# Requisita o local onde será criada a pasta e analisa se é um local válido.
def caminho():
    """
    Requisita o local onde será criada a pasta e analisa se é um local válido.
    
    """
    while True:
        local = str(input('Local de criação da pasta: '))
        if os.path.isdir(local):
            break
        else:
            print('Caminho inválido! Tente novamente.')
    os.chdir(local)


# Nome a ser designado para a nova pasta
while True:
    projeto = str(input('Nome do pasta: '))
    pasta = charcheck(projeto)
    confirma = str(input(f'Nome do projeto: {pasta}. Confirme [S/N] '))[0].upper()
    while True:
        if confirma not in 'SsNn':
            print('OPÇÃO INVÁLIDA! Tente novamente!')
            confirma = str(input(f'Nome do projeto: {pasta}. Confirme [S/N] '))[0].upper()
        elif confirma in 'SsNn':
            break
    if confirma in 'Ss':
        break

caminho()

# Criação das pastas e subpastas
try:
    os.mkdir(pasta)
    erros = 0
except:
    errocnt = 1
    print('ERRO!')
if erros == 0:
    os.chdir(pasta)
    qntsub = int(input('Quantas subastas deseja criar? '))
    for c in range(1, qntsub + 1):
        try:
            os.mkdir(pasta + ' ' + str(c))
        except:
            print('ERRO!')
