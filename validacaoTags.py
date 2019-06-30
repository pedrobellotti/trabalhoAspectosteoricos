#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

#Faz a validacao de uma tag
def validaTag (entrada):
    pilha = []
    operadores = ['+', '.', '*']
    escape = ['n','\\','*','.','+','l']
    charanterior = ''
    #Separa a tag em nome e a tag em si
    split = entrada.split(' ', 1) #Faz o split apenas ate o primeiro espaco (para reconhecer espaco)
    nomeTag = split[0]
    tag = split[1].rstrip('\n') #rstrip remove o \n
    #Percorre toda a tag verificando cada caractere
    for char in tag:
        #Verifica se o caractere atual foi precedido por '\' e é um caractere de escape
        if charanterior == '\\':
            #Se ele for de escape, adiciona na pilha e passa para a proxima iteracao, se nao, exibe erro
            if char in escape:
                pilha.append(char)
                break
            else:
                print ('[ERROR] Tag',nomeTag,'nao reconhecida: caractere',char,'não é um caractere de escape!')
                return False
        #Verifica se o caractere atual e um operador
        if char in operadores:
            #Operador unario, desempilha um elemento e adiciona o operador
            if char == '*':
                if len(pilha) < 1:
                    print ('[ERROR] Tag',nomeTag,'nao reconhecida: operador unario precisa de um operando!')
                    return False
                else:
                    novaExpressao = pilha.pop() + char
                    pilha.append(novaExpressao)
            #Operador binario, desempilha dois elementos e adiciona o operador entre eles
            elif char == '+' or char == '.':
                if len(pilha) < 2:
                    print ('[ERROR] Tag',nomeTag,'nao reconhecida: operador binario precisa de dois operandos!')
                    return False
                else:
                    novaExpressao = pilha.pop() + char + pilha.pop()
                    pilha.append(novaExpressao)
        #Caso o caractere nao seja um operador, ele e adicionado na pilha
        else:
            if char != '\\': #Nao adiciona \ na pilha para nao gerar problemas no reconhecimento
                pilha.append(char)
        charanterior = char
    #Ao acabar de percorrer a tag, verifica se a pilha possui apenas um elemento, se sim a tag e valida
    if len(pilha) == 1:
        print ('[INFO] Tag',nomeTag,'reconhecida')
        #print (pilha.pop())
        return True
    else:
        print ('[ERROR] Tag',nomeTag,'nao reconhecida: expressao regular malformada!')
        return False

def verificaFormato (entrada, tags):
    try:
        nomeEntrada = entrada.split()[0]
        expressaoEntrada = entrada.split()[1]
    except:
        print ('[ERROR] Tag',nomeEntrada,'nao reconhecida: expressao regular vazia!')
        return False
    if len(entrada.split(' ', 1)) == 2:
        for tag in tags:
            nomeTag = tag.split()[0]
            expressaoTag = tag.split()[1]
            if nomeEntrada == nomeTag:
                print ('[ERROR] Tag',nomeEntrada,'nao reconhecida: ja existe uma tag com esse nome!')
                return False
    else:
        print ('[ERROR] Tag',nomeEntrada,'formato invalido! Exemplo de formato: "TAG: ab+c+x+"')
        return False
    return True