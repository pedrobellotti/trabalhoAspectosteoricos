#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

class Estado:
    def __init__(self, id, final, inicial):
        self.id = id
        self.final = final
        self.inicial = inicial
    def isFinal(self):
        return self.final
    def isInicial(self):
        return self.inicial
    def setInicial(self, ini):
        self.inicial = ini
    def setFinal(self, fim):
        self.final = fim