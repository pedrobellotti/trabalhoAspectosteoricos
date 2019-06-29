#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

# Fabrica de automatos - Recebe uma expressao regular e cria um automato
#
# Comportamento da funcao de criacao de automato:
# 1) Se o caractere lido for uma letra (c), cria um automato simples (EI-----c------>EF) e coloca na pilha
#
# 2) Se o caractere lido for um '+', faz a uniao dos dois primeiros automatos na pilha da forma:
#  2.1) Desempilha os dois automatos
#  2.2) Cria um novo estado inicial, que aponta para os estados iniciais dos dois automatos retirados da pilha (usando transicao lambda)
#  2.3) Faz os estados iniciais dos automatos retirados da pilha virarem estados comuns
#  2.4) Cria um novo estado final, como destino dos estados finais dos dois automatos retirados da pilha (usando transicao lambda)
#  2.5) Faz os estados finais dos automatos retirados da pilha virarem estados comuns
#  2.6) Empilha o novo automato criado
#
# 3) Se o caractere lido for um '.', faz a uniao dos dois primeiros automatos na pilha da forma:
#  3.1) Desempilha os dois automatos
#  3.2) Faz o estado final do primeiro automato apontar para o estado inicial do segundo automato (usando transicao lambda)
#  3.3) Faz o estado final do primeiro automato virar um estado comum
#  3.4) Faz o estado inicial do segundo automato virar um estado comum
#  3.5) Empilha o novo automato criado
#
# 4) Se o caractere lido for um '*', faz a uniao do automato com ele mesmo da forma:
#  4.1) Faz o estado final do automato apontar para o estado inicial do mesmo (usando transicao lambda)
#
from estado import Estado
from transicao import Transicao
from automato import Automato

#Cria um automato simples (caso 1)
def automatoSimples (simbolo, tag):
    automato = Automato(tag) #Cria um novo automato
    eInicial = Estado(True, False) #Cria um estado inicial
    eFinal = Estado(False, True) #Cria um estado final
    #Adiciona os estados no automato
    automato.addEstado(eInicial)
    automato.addEstado(eFinal)
    automato.addEstadoInicial(eInicial)
    automato.addEstadoFinal(eFinal)
    transicao = Transicao(eInicial, eFinal, simbolo) #Cria uma transicao entre o estado final e inicial
    eInicial.addTransicao(transicao) #Adiciona a transicao na lista de transicoes do estado inicial
    automato.atualizaIds()
    return automato

#Faz a uniao descrita no caso 2 (+)
def uniaoOu(a1, a2, tag):
    novoAutomato = Automato(tag) #Cria um novo automato
    #Adicionando todos os estados dos automatos antigos no novo
    estados1 = a1.getEstados()
    estados2 = a2.getEstados()
    for estado in estados1:
        novoAutomato.addEstado(estado)
    for estado in estados2:
        novoAutomato.addEstado(estado)
    #Criando novos estados
    novoInicial = Estado(True, False)
    novoFinal = Estado(False, True)
    novoAutomato.addEstadoInicial(novoInicial)
    novoAutomato.addEstadoFinal(novoFinal)
    #Criando novas transicoes para os estados iniciais
    iniciais1 = a1.getEstadosIniciais()
    iniciais2 = a2.getEstadosIniciais()
    for estado in iniciais1:
        t = Transicao(novoInicial, estado, '')
        novoInicial.addTransicao(t)
        estado.setInicial(False)
    for estado in iniciais2:
        t = Transicao(novoInicial, estado, '')
        novoInicial.addTransicao(t)
        estado.setInicial(False)
    #Criando novas transicoes para os estados finais
    finais1 = a1.getEstadosFinais()
    finais2 = a2.getEstadosFinais()
    for estado in finais1:
        t = Transicao(estado, novoFinal, '')
        estado.addTransicao(t)
        estado.setFinal(False)
    for estado in finais2:
        t = Transicao(estado, novoFinal, '')
        estado.addTransicao(t)
        estado.setFinal(False)
    novoAutomato.atualizaIds()
    return novoAutomato

#Faz a uniao descrita no caso 3 (.)
def uniaoE(a1, a2, tag):
    novoAutomato = Automato(tag) #Cria um novo automato
    #Adicionando todos os estados dos automatos antigos no novo
    estados1 = a1.getEstados()
    estados2 = a2.getEstados()
    for estado in estados1:
        novoAutomato.addEstado(estado)
    for estado in estados2:
        novoAutomato.addEstado(estado)
    #Adicionando todos os estados iniciais de a1 como estados iniciais do novo automato
    for estado in a1.getEstadosIniciais():
        novoAutomato.addEstadoInicial(estado)
    #Fazendo todos os estados finais de a1 apontarem para os estados iniciais de a2
    for estadoFinal in a1.getEstadosFinais():
        estadoFinal.setFinal(False)
        for estadoInicial in a2.getEstadosIniciais():
            estadoInicial.setInicial(False)
            t = Transicao (estadoFinal, estadoInicial, '')
            estadoFinal.addTransicao(t)
    novoAutomato.atualizaIds()
    return novoAutomato

#Faz a uniao descrita no caso 4 (*)
def uniaoA(a1):
    eIniciais = a1.getEstadosIniciais()
    eFinais = a1.getEstadosFinais()
    for final in eFinais:
        for inicial in eIniciais:
            t = Transicao(final, inicial, '')
            final.addTransicao(t)
    a1.atualizaIds()
    return a1

def criaAutomato(expressao, pilha_automatos):
    #Separa a tag em nome e a tag em si
    split = expressao.split(' ', 1) #Faz o split apenas ate o primeiro espaco (para reconhecer espaco)
    nomeTag = split[0]
    tag = split[1].rstrip('\n') #rstrip remove o \n
    #Percorre toda a tag verificando cada caractere
    for char in tag:
        if(char == '.'):
            a2 = pilha_automatos.pop()
            a1 = pilha_automatos.pop()
            aux = uniaoE(a1, a2, nomeTag)
            pilha_automatos.append(aux)
        elif (char == '+'):
            a2 = pilha_automatos.pop()
            a1 = pilha_automatos.pop()
            aux = uniaoOu(a1, a2, nomeTag)
            pilha_automatos.append(aux)
        elif (char == '*'):
            aux = uniaoA(pilha_automatos.pop())
            pilha_automatos.append(aux)
        else:
            aux = automatoSimples(char, nomeTag)
            pilha_automatos.append(aux)