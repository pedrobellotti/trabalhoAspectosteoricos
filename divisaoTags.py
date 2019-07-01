#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

import gerenciaArquivo as arquivo

#Processa todas as palavras em todos os automatos e salva quais aceitaram (comando :p)
def divideTag (lista_palavra, lista_automatos, nomeArquivo):
    aceito = []
    quantidade_aceito = 0
    sobreposicao = []
    #Percorre todas as palavras da lista
    for palavra in lista_palavra:
        for automato in lista_automatos:
            if (automato.aceita(palavra)):
                quantidade_aceito += 1
                aceito.append(automato.getTag()[:-1])
                sobreposicao.append(automato.getTag()[:-1])
        if (quantidade_aceito > 1):
            #Se tiver mais de um aceito, guarda apenas o primeiro
            print ('[WARN] Sobreposicao na definicao das tags', *sobreposicao)
            pri = aceito.pop(0)
            aceito = []
            aceito.append(pri)
        quantidade_aceito = 0
        sobreposicao = []
    if (len(aceito) > 0):
        if(nomeArquivo == ''):
            print (*aceito)
        else:
            arquivo.salvaArquivoDivisao(nomeArquivo,aceito)
    
#Processa todas as palavras em todos os automatos e salva quais aceitaram (comando :f)
def divideTagTexto (lista_palavra, lista_automatos, nomeArquivo):
    aceito = []
    quantidade_aceito = 0
    sobreposicao = []
    #Percorre todas as palavras da lista
    for palavra in lista_palavra:
        palavra = palavra.rstrip('\n') #rstrip remove o \n
        palavra = palavra.split(' ')
        for char in palavra:
            for automato in lista_automatos:
                if (automato.aceita(char)):
                    quantidade_aceito += 1
                    aceito.append(automato.getTag()[:-1])
                    sobreposicao.append(automato.getTag()[:-1])
            if (quantidade_aceito > 1):
                print ('[WARN] Sobreposicao na definicao das tags', *sobreposicao)
            quantidade_aceito = 0
            sobreposicao = []
        if (len(aceito) > 0):
            if(nomeArquivo == ''):
                print (*aceito)
            else:
                arquivo.salvaArquivoDivisao(nomeArquivo,aceito)
        aceito = []
    
