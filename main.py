#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz - 201776030                           #
# Pedro Bellotti - 201676043                            #
#########################################################

import validacaoTags as valida
import gerenciaArquivo as arquivo
import fabricaAutomato as fabrica
import divisaoTags as divide

if __name__ == "__main__":
    conjunto_tags = [] #Conjunto de tags validas (tags invalidas nao sao armazenadas)
    conjunto_automatos = [] #Conjunto de automatos criados a partir das tags
    texto_divisao = [] #Conjunto de linhas lida do arquivo para ser dividida usando as tags

    #Le entradas do usuario ate que o comando :q seja digitado
    while True:
        entrada = input()
        while not entrada: #Evita erro de linha em branco
            entrada = input()
        #Reconhece os comandos iniciados com ':'
        if entrada[0] == ':':
            comando = entrada.split()
            if comando[0] == ':q':
                print ('[INFO] Encerrando programa.')
                quit()
            elif comando[0] == ':s':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de 1 parametro!')
                else:
                    arquivo.salvaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':l':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de 1 parametro!')
                else:
                    importa = arquivo.importaArquivo(comando[1], conjunto_tags)
                    #Criando automatos para todas as tags lidas
                    if (importa):
                        for tag in conjunto_tags:
                            auto = fabrica.criaAutomato(tag)
                            if (auto != 0):
                                conjunto_automatos.append(auto)
            elif comando[0] == ':f':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de 1 parametro!')
                else:
                    if (arquivo.importaDivisao(comando[1], texto_divisao)):
                        #Faz a divisao em tags de todos as linhas do texto
                        #for linha in texto_divisao:
                        divide.divideTagTexto(texto_divisao, conjunto_automatos)
            elif comando[0] == ':o':
                print ('[INFO] Comando para especificar o caminho do arquivo de saida ainda nao implementado!')
            elif comando[0] == ':p':
                if len(comando) < 2:
                    print ('[WARN] Este comando precisa de pelo menos 1 parametro!')
                else:
                    divide.divideTag(comando[1:], conjunto_automatos)
            ### Comando para imprimir todos os automatos da lista (apenas para testes, remover na versao final) ###
            elif comando[0] == ':i':
                for automato in conjunto_automatos:
                    automato.imprimeAutomato()
                    print ('-------------------')
            else:
                print ('[ERROR] Comando invalido!')
        #Usuario digitou uma tag (do tipo VAR: ab+c+x+) diretamente e ela precisa ser validada
        else:
            if valida.verificaFormato(entrada, conjunto_tags):
                if valida.validaTag(entrada):
                    conjunto_tags.append(entrada+'\n') #Salva a tag lida
                    auto = fabrica.criaAutomato(entrada) #Cria um automato com a tag
                    if (auto != 0): #Salva o automato na lista caso ele tenha sido criado corretamente
                        conjunto_automatos.append(auto)