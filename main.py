import lexer


def main():

    # ler o código fonte atual do fluxo em test.lang e armazená-lo em uma variável

    conteudo = "int main()"
    with open('test.lang', 'r') as arquivo:
        conteudo = arquivo.read()


    # Lexer


    # chamar o lexer
    lex = lexer.Lexer(conteudo)
    #  tokenizar
    tokens = lex.tokenize()


    # Parser

    import parser1

    tokens_para_analise = tokens
    analise = parser1.Parser1(tokens_para_analise)
    obj = analise.parse()


    # Verificação de Tipo de Dados


    import dataTypeValidation
    tokens_para_validacao_dt = tokens
    validacao_dt = dataTypeValidation.DataTypeValidation(tokens_para_validacao_dt)
    obj_dt = validacao_dt.dt_validation()


main()
