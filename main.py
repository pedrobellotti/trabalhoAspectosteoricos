#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Marcos Aquino                                         #
# Matheus Queiroz                                       #
# Pedro Bellotti                                        #
#########################################################

import validacaoTags as valida
import gerenciaArquivo as arquivo

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
                    arquivo.salvaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':l':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de apenas um parametro!')
                else:
                    arquivo.importaArquivo(comando[1], conjunto_tags)
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
            if valida.verificaFormato(entrada, conjunto_tags):
                if valida.validaTag(entrada):
                    conjunto_tags.append(entrada+'\n')
