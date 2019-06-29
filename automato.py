#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

class Automato:
    def __init__(self, tag):
        self.tag = tag #Tag definida para o automato
        self.estados = [] #Lista de estados
        self.eFinais = [] #Lista de estados finais
        self.eIniciais = [] #Lista de estados iniciais

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