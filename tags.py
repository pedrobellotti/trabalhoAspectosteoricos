
print ('Trabalho de Aspectos Teoricos da Computacao')

#Le um arquivo de tags e carrega todas na memoria (nao faz a validacao)
def importaArquivo(nomeArquivo, tags):
    try:
        with open(nomeArquivo) as arquivo:
            for linha in arquivo:
                tags.append(linha)
        print ('[INFO] As definicoes de tags foram carregadas')
    except(IOError):
       print ("[ERROR] Erro ao abrir o arquivo:", nomeArquivo)
       quit()

#Salva em um arquivo todas as tags que foram validadas
def salvaArquivo (nomeArquivo, tags):
    arquivo = open(nomeArquivo, "w") #w apaga e escreve por cima do arquivo caso ele ja exista
    for tag in tags:
        arquivo.write(tag)
    arquivo.close()
    print ('[INFO] As definicoes de tags foram salvas')

#Faz a validacao de varias tags (para tags lidas do arquivo)
def validaTags (candidatas, reconhecidas):
    #Processa cada tag na lista de candidatas
    for tag in candidatas:
        validaTag (tag, reconhecidas)
    #Limpa a lista de tags candidatas, as tags que nao foram reconhecidas sao descartadas
    candidatas.clear()

#Faz a validacao de uma unica tag (para tags digitadas pelo usuario)
def validaTag (entrada, reconhecidas):
    pilha = []
    operadores = ['+', '.', '*']
    #Separa a tag em nome e a tag em si
    split = entrada.split(' ', 1) #Faz o split apenas ate o primeiro espaco (para reconhecer espaco)
    nomeTag = split[0]
    tag = split[1].rstrip() #rstrip remove o \n
    #Percorre toda a tag verificando cada caractere
    for char in tag:
        #Verifica se o caractere atual e um operador
        if char in operadores:
            #Operador unario, desempilha um elemento e adiciona o operador
            if char == '*':
                if len(pilha) < 1:
                    print ('[WARN] Tag',nomeTag,'nao reconhecida: operador unario precisa de um operando!')
                    return False
                else:
                    novaExpressao = pilha.pop() + char
                    pilha.append(novaExpressao)
            #Operador binario, desempilha dois elementos e adiciona o operador entre eles
            elif char == '+' or char == '.':
                if len(pilha) < 2:
                    print ('[WARN] Tag',nomeTag,'nao reconhecida: operador binario precisa de dois operandos!')
                    return False
                else:
                    novaExpressao = pilha.pop() + char + pilha.pop()
                    pilha.append(novaExpressao)
        #Caso o caractere nao seja um operador, ele e adicionado na pilha
        else:
            pilha.append(char)
    #Ao acabar de percorrer a tag, verifica se a pilha possui apenas um elemento, se sim a tag e valida
    if len(pilha) == 1:
        print ('[INFO] Tag',nomeTag,'reconhecida')
        reconhecidas.append(entrada)
        return True
    else:
        print ('[WARN] Tag',nomeTag,'nao reconhecida: expressao regular malformada!')
        return False

if __name__ == "__main__":
    tags_reconhecidas = [] #Tags que ja foram validadas
    tags_candidatas = [] #Tags ainda nao validadas (apenas lidas do arquivo)

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
                    salvaArquivo(comando[1], tags_reconhecidas)
            elif comando[0] == ':l':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de apenas um parametro!')
                else:
                    importaArquivo(comando[1], tags_candidatas)
                    validaTags(tags_candidatas, tags_reconhecidas)
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
            if len(entrada.split(' ', 1)) == 2:
                validaTag(entrada, tags_reconhecidas)
            else:
                print ('[ERROR] Formato de tag invalido! Exemplo de formato: "TAG: ab+c+x+"')