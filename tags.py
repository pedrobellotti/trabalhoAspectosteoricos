
print ('Trabalho de Aspectos Teoricos da Computacao')

#Le um arquivo de tags, valida e carrega as validas na memoria
def importaArquivo(nomeArquivo, tags):
    try:
        with open(nomeArquivo) as arquivo:
            for linha in arquivo:
                if verificaFormato(linha, tags):
                    if validaTag(linha):
                        tags.append(linha)
        print ('[INFO] As definicoes de tags foram carregadas')
    except(IOError):
       print ("[WARN] Erro ao abrir o arquivo:", nomeArquivo)

#Salva em um arquivo todas as tags que foram validadas
def salvaArquivo (nomeArquivo, tags):
    try:
        arquivo = open(nomeArquivo, "w") #w apaga e escreve por cima do arquivo caso ele ja exista
        for tag in tags:
            arquivo.write(tag)
        arquivo.close()
    except(IOError):
        print ("[WARN] Erro ao salvar o arquivo:", nomeArquivo)
    print ('[INFO] As definicoes de tags foram salvas')

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
        return True
    else:
        print ('[ERROR] Tag',nomeTag,'nao reconhecida: expressao regular malformada!')
        return False

def verificaFormato (entrada, tags):
    nomeTag = entrada.split()[0]
    expressaoTag = entrada.split()[1]
    if len(entrada.split(' ', 1)) == 2:
        for tag in tags:
            if nomeTag in tag:
                print ('[ERROR] Tag',nomeTag,'nao reconhecida: ja existe uma tag com esse nome!')
                return False
            if expressaoTag in tag:
                print ('[ERROR] Tag',nomeTag,'nao reconhecida: ja existe uma tag com essa expressao!')
                return False
    else:
        print ('[ERROR] Tag',nomeTag,'formato invalido! Exemplo de formato: "TAG: ab+c+x+"')
        return False
    return True

if __name__ == "__main__":
    conjunto_tags = [] #Conjunto de tags validas (tags invalidas nao sao armazenadas)

    #Le entradas do usuario ate que o comando :q seja digitado
    while True:
        entrada = input('Digite um comando ou tag: ')
        #Reconhece os comandos iniciados com ':'
        if entrada[0] == ':':
            comando = entrada.split()
            if comando[0] == ':q':
                print ('[INFO] Encerrando programa.')
                quit()
            elif comando[0] == ':s':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de apenas um parametro!')
                else:
                    salvaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':l':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de apenas um parametro!')
                else:
                    importaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':f':
                print ('[INFO] Comando para realizar a divisao de tags do arquivo ainda nao implementado!')
            elif comando[0] == ':o':
                print ('[INFO] Comando para especificar o caminho do arquivo de saida ainda nao implementado!')
            elif comando[0] == ':p':
                print ('[INFO] Comando para realizar a divisao de tags da entrada ainda nao implementado!')
            else:
                print ('[ERROR] Comando invalido!')
        #Usuario digitou uma tag (do tipo VAR: ab+c+x+) diretamente e ela precisa ser validada
        else:
            if verificaFormato(entrada, conjunto_tags):
                if validaTag(entrada):
                    conjunto_tags.append(entrada+'\n')
