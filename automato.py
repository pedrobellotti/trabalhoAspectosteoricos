#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

from random import randint

class Automato:
    def __init__(self, tag):
        self.tag = tag #Tag definida para o automato
        self.estados = [] #Lista de estados
        self.eFinais = [] #Lista de estados finais
        self.eIniciais = [] #Lista de estados iniciais

    def processaChar (self, estado, char):
        transicoes = estado.getTransicoes(char)
        for t in transicoes:
            if (t.getSimbolo() == char):
                return t.getDestino()
        return 0

    def processaLambda(self, estado, char):
        #Verifica todas as transicoes lambda do estado e escolhe uma
        transicoes = estado.getTransicoes(char)
        opcoes = []
        if (len(transicoes) > 0):
            for t in transicoes:
                if (t.getSimbolo() == ''):
                    destino = t.getDestino()
                    #Olhando as transicoes do destino
                    if (self.processaChar(destino, char) != 0):
                        #opcoes.append(destino)
                        return destino
                    else:
                        #Processando as transicoes lambda do destino
                        t_dest = destino.getTransicoes(char)
                        for td in t_dest:
                            if (self.processaChar(destino, char) != 0 or td.getSimbolo() == ''):
                                #opcoes.append(destino)
                                return self.processaLambda(destino,char)
        #return opcoes

    #Tenta, a partir de um estado, chegar em um estado final usando apenas transicoes lambda
    def processaFinal (self, estado, lista_visitado):
        lista_visitado.append(estado)
        transicoes = estado.getTransicoes('+') #Trocar isso
        if (len(transicoes) > 0):
            for t in transicoes:
                if (t.getSimbolo() == ''):
                    destino = t.getDestino()
                    #Processando as transicoes lambda do destino
                    t_dest = destino.getTransicoes('+')
                    for td in t_dest:
                        if (td.getSimbolo() == ''):
                            return self.processaFinal(destino, lista_visitado)
                        else:
                            return None

    def aceita(self, palavra):
        estadoAtual = self.eIniciais[0]
        i = 0 #Posicao da palavra
        while True: #Processa a palavra ate chegar ao fim
            if i == len(palavra):
                break
            print ('Processando estado', estadoAtual.getId(), 'com a letra', palavra[i])
            #Ve se o estado tem uma transicao direta (usando a letra) para outro estado
            t = self.processaChar(estadoAtual, palavra[i])
            if (t != 0):
                i += 1
                estadoAtual = t
            else:
                #Se nao tem transicao direta, procura por transicoes lambda que tenham
                #como destino estados que tenham transicoes diretas usando a letra
                t = self.processaLambda(estadoAtual, palavra[i])
                if (t is not None):
                    estadoAtual = t
                #if (len(t) != 0):
                #    if(len(t) == 1):
                #        estadoAtual = t[0]
                #    else:
                #        estadoAtual = t[randint(1, len(t))]
                else:
                    break
        #Depois de todo o processamento, se parou em um estado final a palavra e aceita
        #Se parou em um estado que nao e final mas tem transicao lambda para um final, aceita tambem
        print ('Estado final:', estadoAtual.getId())
        if(estadoAtual.isFinal() and i == len(palavra)):
            return True
        else:
            visitado = []
            f = self.processaFinal(estadoAtual, visitado)
            for estado in visitado:
                if (estado.isFinal()):
                    print ('Chegou no final id', estado.getId())
                    return True
            #transicoes = estadoAtual.getTransicoes(palavra[0]) #Nao importa o indice
            #for t in transicoes:
                #if (t.getSimbolo() == '' and t.getDestino().isFinal()):
                    #return True
        return False

    #Retorna a tag (nome) do automato
    def getTag(self):
        return self.tag
    
    #Muda a tag (nome) do automato
    def setTag(self, t):
        self.tag = t
    
    #Retorna a lista de estados do automato
    def getEstados(self):
        return self.estados
    
    #Retorna a lista de estados iniciais do automato
    def getEstadosIniciais(self):
        return self.eIniciais
    
    #Retorna a lista de estados finais do automato
    def getEstadosFinais(self):
        return self.eFinais
    
    #Adiciona um estado na lista de estados
    def addEstado(self, e):
        self.estados.append(e)
    
    #Adiciona um estado na lista de estados iniciais
    def addEstadoInicial(self, e):
        self.eIniciais.append(e)
    
    #Adiciona um estado na lista de estados finais
    def addEstadoFinal(self, e):
        self.eFinais.append(e)
    
    #Atualiza a ID dos estados (apenas para conferir)
    def atualizaIds(self):
        id = 1
        for estado in self.estados:
            estado.setId(id)
            id += 1
   
    #Imprime automato (apenas para conferir)
    def imprimeAutomato(self):
        print('\n')
        print ('TAG:', self.tag)
        print ('Estados Iniciais:')
        for estado in self.eIniciais:
            print(estado.getId())
        print ('Estados Finais:')
        for estado in self.eFinais:
            print(estado.getId())
        print ('Todos os estados:')
        for estado in self.estados:
            estado.imprimeEstado()