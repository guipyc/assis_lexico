import re

class Lexer(object):

    def __init__(self, codigo_fonte):
        self.codigo_fonte = codigo_fonte


    def tokenize(self):

        # guarda os tokens
        tokens = []
        flag = 1

        # Cria uma lista de palavras do código fonte
        codigo_fonte = self.codigo_fonte.split()

        # Mantém a contagem dos índices do código
        indice_codigo = 0

        # Looping de cada palavra do código
        while indice_codigo < len(codigo_fonte):

            palavra = codigo_fonte[indice_codigo]

            # VERIFICA OPERADORES

            if palavra == "++":
                tokens.append(['OPERADOR_INCREMENTO', '++'])

            elif palavra == "--":
                tokens.append(['OPERADOR_DECREMENTO', '--'])

            elif palavra == "+":
                tokens.append(['OPERADOR_ADICAO', '+'])

            elif palavra == "-":
                tokens.append(['OPERADOR_SUBTRACAO', '-'])

            elif palavra == "*":
                tokens.append(['OPERADOR_MULTIPLICACAO', '*'])

            elif palavra == "/":
                tokens.append(['OPERADOR_DIVISAO', '/'])

            elif palavra == "=":
                tokens.append(['OPERADOR_ATRIBUICAO', '='])

            elif palavra == "-":
                tokens.append(['OPERADOR_SUBTRACAO', '-'])

            elif palavra == ",":
                tokens.append(['OPERADOR_SEPARADOR', ','])

            # VERIFICA PALAVRAS-CHAVE

            if palavra.lower() == "for":
                tokens.append(['OPERADOR_LOOP', palavra])

            elif palavra.lower() == "while":
                tokens.append(['OPERADOR_LOOP', palavra])

            elif palavra.lower() == "if":
                tokens.append(['OPERADOR_CONDICIONAL', palavra])

            elif palavra.lower() == "elseif":
                tokens.append(['OPERADOR_CONDICIONAL', palavra])

            elif palavra.lower() == "else":
                tokens.append(['OPERADOR_CONDICIONAL', palavra])

            elif palavra.lower() == "break":
                tokens.append(['OPERADOR_BREAK', palavra])

            elif palavra.lower() == "enum":
                tokens.append(['OPERADOR_ENUM', palavra])

            elif palavra.lower() == "default":
                tokens.append(['OPERADOR_DEFAULT', palavra])

            elif palavra.lower() == "static":
                tokens.append(['OPERADOR_STATIC', palavra])

            # VERIFICA TIPOS DE DADOS

            if palavra.lower() == "int":
                tokens.append(['TIPO_DADO_INT', palavra])

            elif palavra.lower() == "double":
                tokens.append(['TIPO_DADO_DOUBLE', palavra])

            elif palavra.lower() == "bool":
                tokens.append(['TIPO_DADO_BOOL', palavra])

            elif palavra.lower() == "string":
                tokens.append(['TIPO_DADO_STRING', palavra])

            elif palavra.lower() == "char":
                tokens.append(['TIPO_DADO_CHAR', palavra])

            elif palavra.lower() == "float":
                tokens.append(['TIPO_DADO_FLOAT', palavra])

            elif palavra.lower() == "enum":
                tokens.append(['TIPO_DADO_ENUM', palavra])

            # OBTÉM O TIPO DE DADO DO VALOR

            if re.search(r'^\d*$', palavra):
                if palavra[len(palavra)-1] == ';':
                    tokens.append(['VALOR_INTEIRO', palavra[0:len(palavra)-1]])
                else:
                    tokens.append(['VALOR_INTEIRO', palavra])

            elif re.search(r'[0-9]', palavra) and re.search('.', palavra):
                if palavra[len(palavra)-1] == ";":
                    tokens.append(['VALOR_FLOAT', palavra[0:len(palavra)-1]])
                else:
                    tokens.append(['VALOR_FLOAT', palavra])

            elif re.search(r'\w|\d$', palavra) and palavra[0] == "'" and (palavra[len(palavra)-1] == "'" or palavra[len(palavra)-2 == "'"]):
                if palavra[len(palavra)-1] == ";":
                    tokens.append(['VALOR_CHAR', palavra[0:len(palavra)-1]])
                else:
                    tokens.append(['VALOR_CHAR', palavra])

            elif re.search('true', palavra.lower()) or re.search('false', palavra.lower()):
                if palavra[len(palavra)-1] == ";":
                    tokens.append(['VALOR_BOOLEANO', palavra[0:len(palavra)-1]])
                else:
                    tokens.append(['VALOR_BOOLEANO', palavra])

            if re.search(r'\w*|\w*[0-9]$', palavra) and re.search(r'^"', palavra) or re.search(r'$"',palavra):
                    if re.match(r'".*"', palavra):
                        tokens.append(['VALOR_STRING', palavra])

            # VERIFICA IDENTIFICADOR

            if re.search(r'^_\w*|^_A-Za-z|^A-Za-z[0-9]$', palavra):
                    tokens.append(['IDENTIFICADOR', palavra])

            # Se um STATEMENT_END (;) for encontrado no último caractere, cria um token OPERADOR para ele

            if palavra[len(palavra)-1] == ";":
                tokens.append(['FIM_DECLARACAO', ';'])

            # Incrementa o índice após cada verificação
            indice_codigo += 1

        print(tokens)

        # Retorna os tokens criados
        return tokens
