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

    #Verifica se o estado pode alcancar diretamente outros utilizando o char
    def processaChar (self, estado, char):
        transicoes = estado.getTransicoes(char)
        for t in transicoes:
            if (t.getSimbolo() == char):
                return t.getDestino()
        return 0

    #Verifica todos os possiveis estados que podem ser alcancados usando transicoes lambda
    def processaLambda (self, estado, opcoes):
        transicoes = estado.getTransicoes('+') #Trocar isso
        opcoes.append(estado)
        if (len(transicoes) > 0):
            for t in transicoes:
                if (t.getSimbolo() == ''):
                    self.processaLambda(t.getDestino(), opcoes)

    #Tenta, a partir de um estado, chegar em um estado final usando apenas transicoes lambda
    def processaFinal (self, estado, lista_visitado):
        transicoes = estado.getTransicoes('+') #Trocar isso
        if (len(transicoes) > 0):
            for t in transicoes:
                if (t.getSimbolo() == ''):
                    destino = t.getDestino()
                    lista_visitado.append(destino)
                    #Processando as transicoes lambda do destino
                    t_dest = destino.getTransicoes('+')
                    for td in t_dest:
                        if (td.getSimbolo() == ''):
                            return self.processaFinal(destino, lista_visitado)

    #Determina se o automato aceita ou nao uma palavra
    def aceita(self, palavra):
        estadoAtual = self.eIniciais[0]
        i = 0 #Posicao da palavra
        while True: #Processa a palavra ate chegar ao fim
            if i == len(palavra):
                break
            #Ve se o estado tem uma transicao direta (usando o char) para outro estado
            t = self.processaChar(estadoAtual, palavra[i])
            if (t != 0):
                i += 1
                estadoAtual = t
            else:
                #Se nao tem transicao direta, procura por transicoes lambda que tenham
                #como destino estados que tenham transicoes diretas usando o char
                opcoes_estado = []
                self.processaLambda(estadoAtual, opcoes_estado)
                achou_estado = False
                #Apos verificar todos os estados que podem ser atingidos usando transicoes lambda
                #procura por qual deles aceita o caractere atual
                for estado in opcoes_estado:
                    transicoes = estado.getTransicoes(palavra[i])
                    for t in transicoes:
                        if (t.getSimbolo() == palavra[i]):
                            achou_estado = True
                            estadoAtual = t.getDestino()
                #Se achou algum estado compativel, passa para a proxima letra e continua a iteracao
                if (achou_estado):
                    i += 1
                else: #Se nao achou, significa que nao existe nenhuma transicao compativel com o char atual
                    break #Sai do while para evitar loop infinito
        #Depois de todo o processamento, se parou em um estado final a palavra e aceita
        #Se parou em um estado que nao e final mas tem transicao lambda para um final, aceita tambem
        #Se nao processou a palavra toda, nao aceita
        if (i < len(palavra)):
            return False
        if(estadoAtual.isFinal()):
            return True
        else:
            visitado = []
            self.processaFinal(estadoAtual, visitado)
            for estado in visitado:
                if (estado.isFinal()):
                    return True
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