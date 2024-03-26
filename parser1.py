import re
import dataTypeValidation


class Parser1(object):

    def __init__(self, tokens):

        # isso irá conter todos os tokens que foram criados pelo lexer
        self.tokens = tokens

        # isso irá conter o índice do token que estamos analisando
        self.token_index = 0

        self.numero_linha = 0

    def parse(self):
        while self.token_index < len(self.tokens):

            # guarda o tipo de token, por exemplo, IDENTIFICADOR
            tipo_token = self.tokens[self.token_index][0]

            # guarda o valor do token, por exemplo, var
            valor_token = self.tokens[self.token_index][1]

            # isso será acionado quando um token de declaração de variável for encontrado
            if re.search(r'^TIPO_DADO_', tipo_token):
                self.numero_linha += 1
                self.parse_declaracao_variavel(self.tokens[self.token_index:len(self.tokens)])

            # incrementa token_index em 1 para que possamos percorrer os tokens
            self.token_index += 1


    def parse_declaracao_variavel(self, token_stream):

        tokens_verificados = 0
        numero_linha = self.numero_linha
        print("Número da Linha:" + str(numero_linha))

        for token in range(0, len(token_stream)):

            tipo_token = token_stream[tokens_verificados][0]
            valor_token = token_stream[tokens_verificados][1]

            # isso irá obter o tipo de variável, por exemplo,
            if token == 0:
                print('Tipo de variável: ' + valor_token)

            if token == 4 and tipo_token == 'FIM_DECLARACAO':
                print('Fim_da_declaração: ' + valor_token)
                print()
                break

            elif token == 4 and tipo_token != 'FIM_DECLARACAO':
                print('Erro: Terminador de declaração ausente na linha número:' + str(numero_linha))
                quit()

            elif token == 1 and tipo_token == 'IDENTIFICADOR':
                print('Valor do Identificador: ' + valor_token)
            elif token == 1 and tipo_token != 'IDENTIFICADOR':
                print("ERRO: Nome de variável inválido '" + valor_token + "na linha número:" + str(numero_linha))
                quit()

            elif token == 2 and tipo_token == "OPERADOR_ATRIBUICAO":
                print('Operador de atribuição: ' + valor_token)
            elif token == 2 and tipo_token != "OPERADOR_ATRIBUICAO":
                print("ERRO: Valor de atribuição de variável ausente na linha número:" + str(numero_linha))
                quit()

            elif token == 3 and (tipo_token == 'IDENTIFICADOR' or re.search(r'_VALUE$', tipo_token)):
                print('Valor de atribuição:' + valor_token)
            elif token == 3 and (tipo_token != 'IDENTIFICADOR' or re.search(r'_VALUE$', tipo_token,flags=1)):
                print(
                    "ERRO: Valor de atribuição de variável inválido '" + valor_token + "' na linha número:" + str(numero_linha))
                quit()

            tokens_verificados += 1

        # incrementa o índice do token igual ao token verificado para que não o verifiquemos novamente
        self.token_index += tokens_verificados
