#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino - 201276024                             #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

class Transicao:
    def __init__(self, origem, destino, simbolo):
        self.origem = origem #Estado de origem
        self.destino = destino #Estado de destino
        self.simbolo = simbolo #Simbolo consumido pela transicao

    #Retorna o estado de origem da transicao
    def getOrigem(self):
        return self.origem
    #Muda o estado de origem da transicao
    def setOrigem(self, o):
        self.origem = o
    #Retorna o estado de destino da transicao
    def getDestino(self):
        return self.destino
    #Muda o estado de destino da transicao
    def setDestino(self, d):
        self.destino = d
    #Retorna o simbolo consumido pela transicao
    def getSimbolo (self):
        return self.simbolo
    #Muda o simbolo consumido pela transicao
    def setSimbolo (self, s):
        self.simbolo = s
