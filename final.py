import re

def lexico(code):
    tokens = []
    symbols = set()

    expressoes_tokens = [
        ('STRING', r'\".*?\"'),
        ('NUMERO', r'\d+(\.\d+)?'),
        ('NOVA_LINHA', r'\n'),
        ('INDENTACAO', r'\s{4}'),
        ('DEDENTACAO', r'\n(?=\S)'),
        ('SIMBOLO', r'[\(\)\{\}\[\]\.\,\:\;\=\+\-\*\/\<\>\!\&\|\%\@\#]'),
        ('NOME', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ]

    expressoes_combinadas = '|'.join('(?P<%s>%s)' % par for par in expressoes_tokens)
    padrao = re.compile(expressoes_combinadas)

    for correspondencia in padrao.finditer(code):
        tipo_token = correspondencia.lastgroup
        valor_token = correspondencia.group()

        if tipo_token == 'NOVA_LINHA' or tipo_token == 'INDENTACAO':
            continue

        tokens.append((tipo_token, valor_token))

        if tipo_token == 'SIMBOLO':
            symbols.add(valor_token)

    return tokens, list(symbols)

def salvar_tokens(tokens, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for token in tokens:
            arquivo.write(f"{token}\n")

codigo = '''
def FalaAssis(nome):
    return "Olá, " + nome + "!"

print(FalaAssis("Mundo"))
'''

tokens, simbolos = lexico(codigo)
print("Tokens salvos em 'tokens.txt'.")
salvar_tokens(tokens, 'tokens.txt')
