import re

def lex(code):
    # Lista de tokens e símbolos
    tokens = []
    symbols = set()
    
    # Expressões regulares para os diferentes tipos de tokens
    token_expressions = [
        ('COMMENT', r'#[^\n]*'),        # Comentários
        ('STRING', r'\".*?\"'),         # Strings
        ('NUMBER', r'\d+(\.\d+)?'),     # Números
        ('NEWLINE', r'\n'),             # Nova linha
        ('INDENT', r'\s{4}'),           # Indentação (4 espaços)
        ('DEDENT', r'\n(?=\S)'),        # Dedentação
        ('SYMBOL', r'[\(\)\{\}\[\]\.\,\:\;\=\+\-\*\/\<\>\!\&\|\%\@\#]'),  # Símbolos
        ('NAME', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores
    ]
    
    # Combinando todas as expressões regulares
    combined_expressions = '|'.join('(?P<%s>%s)' % pair for pair in token_expressions)
    pattern = re.compile(combined_expressions)
    
    # Encontrando os tokens na entrada
    for match in pattern.finditer(code):
        token_type = match.lastgroup
        token_value = match.group()
        
        # Ignorar nova linha e indentação
        if token_type == 'NEWLINE' or token_type == 'INDENT':
            continue
        
        # Adicionar token à lista de tokens
        tokens.append((token_type, token_value))
        
        # Adicionar símbolo à lista de símbolos, se for um
        if token_type == 'SYMBOL':
            symbols.add(token_value)
    
    return tokens, list(symbols)

# Teste
code = '''
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    return a

print(fibonacci(10))
'''

tokens, symbols = lex(code)
print("Tokens:")
for token in tokens:
    print(token)
print("\nSímbolos:")
print(symbols)
