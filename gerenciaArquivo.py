#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

import validacaoTags as valida
import os

#Le um arquivo de tags, valida e carrega as validas na memoria
def importaArquivo(nomeArquivo, tags):
    try:
        with open(nomeArquivo) as arquivo:
            for linha in arquivo:
                if valida.verificaFormato(linha, tags):
                    if valida.validaTag(linha):
                        tags.append(linha)
        print ('[INFO] As definicoes de tags foram carregadas')
    except(IOError):
       print ("[WARN] Erro ao abrir o arquivo:", nomeArquivo)

#Salva em um arquivo todas as tags que foram validadas
def salvaArquivo (nomeArquivo, tags):
    if os.path.isfile(nomeArquivo):
        print('[WARN] O arquivo', nomeArquivo, 'ja existe e sera sobrescrito!')
    try:
        arquivo = open(nomeArquivo, "w") #w apaga e escreve por cima do arquivo caso ele ja exista
        for tag in tags:
            arquivo.write(tag)
        arquivo.close()
        print ('[INFO] As definicoes de tags foram salvas')
    except(IOError):
        print ("[WARN] Erro ao salvar o arquivo:", nomeArquivo)