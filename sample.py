import lexer
import re

def main():
    with open('test.lang', 'r') as arquivo:
        conteudo = arquivo.read()

    lex = lexer.Lexer(conteudo)
    # # Agora chamamos o método tokenize
    token = lex.tokenize()


main()
