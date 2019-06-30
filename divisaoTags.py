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
    #Percorre todas as palavras da lista
    for palavra in lista_palavra:
        for automato in lista_automatos:
            if (automato.aceita(palavra)):
                aceito.append(automato.getTag()[:-1])
    print (aceito)
    