from itertools import count
import os

'''
1 - Nome da pasta a ser criada
2 - Caminho onde a pasta vai ser criada
3 - Criação da pasta principal
4 - Criação das Subpastas
5 - Separação dos arquivos por tipo
6 - Criação de template de organização de pastas
7 - Edição do template'''

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
            txt = input(str('Nome da pasta: '))
        else:
            break
    return txt    

# Nome a ser designado para a nova pasta
while True:
    projeto = input(str('Nome do pasta: '))
    pasta = charcheck(projeto)
    confirma = input(str(f'Nome do projeto: {pasta}. Confirme [S/N] '))[0].upper()
    while True:
        if confirma not in 'SsNn':
            print('OPÇÃO INVÁLIDA! Tente novamente!')
            confirma = input(str(f'Nome do projeto: {pasta}. Confirme [S/N] '))[0].upper()
        elif confirma in 'SsNn':
            break
    if confirma in 'Ss':
        break


# Define o local onde a pasta será criada e valida se é um local válido

while True:
    caminho = input(str('Caminho do projeto: '))
    if os.path.isdir(caminho):
        print('Este caminho existe!')
        break
    else:
        print('Caminho inválido! Tente novamente.')
os.chdir(caminho)

# Criação das pastas e subpastas

try:
    os.mkdir(pasta)
except:
    print('ERRO!')
    