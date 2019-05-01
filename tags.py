
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
        print (tag)

#Faz a validacao de uma unica tag (para tags digitadas pelo usuario)
def validaTag (entrada, reconhecidas):
    print ('validar')

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
                print ('[WARN] Comando invalido!')
        #Usuario digitou uma tag (do tipo VAR: ab+x) diretamente e ela precisa ser validada
        else:
            print (entrada)
            validaTag(entrada, tags_reconhecidas)