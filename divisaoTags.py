#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

#Processa todas as palavras em todos os automatos e salva quais aceitaram
def divideTag (lista_palavra, lista_automatos):
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
            print ('[WARN] Sobreposicao na definicao das tags', *sobreposicao)
        quantidade_aceito = 0
        sobreposicao = []
    print (*aceito)
    