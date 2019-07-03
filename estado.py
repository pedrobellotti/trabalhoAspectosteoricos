#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino - 201276024                             #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

class Estado:
    def __init__(self, inicial, final):
        self.id = 0 #ID do estado
        self.final = final #True se o estado e final, False se nao
        self.inicial = inicial #True se o estado e inicial, False se nao
        self.transicoes = [] #Lista de transicoes deste estado

    #Retorna se o estado e final ou nao
    def isFinal(self):
        return self.final
    
    #Retorna se o estado e inicial ou nao
    def isInicial(self):
        return self.inicial
    
    #Muda o valor da variavel de estado inicial
    def setInicial(self, ini):
        self.inicial = ini
    
    #Muda o valor da variavel de estado final
    def setFinal(self, fim):
        self.final = fim
    
    #Adiciona uma transicao na lista de transicoes do estado
    def addTransicao(self, t):
        self.transicoes.append(t)
    
    #Retorna a ID do estado
    def getId(self):
        return self.id
    
    #Muda a ID do estado
    def setId(self, i):
        self.id = i
    
    #Retorna as transicoes do estado que aceitam um caractere (ou lambda)
    def getTransicoes(self, char):
        lista = []
        for t in self.transicoes:
            if(t.getSimbolo() == char or t.getSimbolo() == ''):
                lista.append(t)
        return lista