#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################
class Transicao:
    def __init__(self, origem, destino, simbolo):
        self.origem = origem
        self.destino = destino
        self.simbolo = simbolo
    def getOrigem(self):
        return self.origem
    def setOrigem(self, o):
        self.origem = o
    def getDestino(self):
        return self.destino
    def setOrigem(self, d):
        self.destino = d
    def getSimbolo (self):
        return self.simbolo
    def setSimbolo (self, s):
        self.simbolo = s
