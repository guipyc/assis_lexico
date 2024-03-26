import re


class DataTypeValidation(object):

    def __init__(self, tokens):

        # guarda os tokens
        self.tokens = tokens
        # guarda o index do token
        self.token_index = 0
        self.line_number = 0

    def dt_validation(self):
        while self.token_index < len(self.tokens):

            # tipo de token IDENTIFIER
            token_type = self.tokens[self.token_index][0]

            # valor do token e.g var
            token_value = self.tokens[self.token_index][1]

            # quando a variavel declarada é achada
            if re.search(r'^DATATYPE_', token_type):
                self.line_number += 1

                self.check_data_type(self.tokens[self.token_index:len(self.tokens)])

            # looping pelo token
            self.token_index += 1

    def check_data_type(self, token_stream):

        tokens_checked = 0
        line_number = self.line_number

        for token_dt in range(0, len(token_stream)):

            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            if token_dt == 0 and token_type == 'DATATYPE_INT':
                tokens_checked += 3

                if token_stream[tokens_checked][0] == 'INTEGER_VALUE':
                    tokens_checked -= 3


                else:
                    print("Line Number:" + str(line_number))
                    print("Line No:" + str(line_number) + " ERROR: invalid data typeof assignment variable: '"
                          + token_stream[tokens_checked][1] + "' \n The value should be of int data type")
                    tokens_checked -= 3

                   # quit()

            elif token_dt == 0 and token_type == 'DATATYPE_CHAR':
                tokens_checked += 3

                if token_stream[tokens_checked][0] == 'CHAR_VALUE':
                    tokens_checked -= 3
                else:
                    print("Line Number:" + str(line_number))
                    print("Line No:" + str(line_number) + " ERROR: invalid data typeof assignment variable: '"
                          + token_stream[tokens_checked][1] + "' \n The value should be of char data type")
                    tokens_checked -= 3
                   # quit()

            tokens_checked += 1

        # incrementar o índice do token igual ao token verificado para que não o verifiquemos novamente

        self.token_index += tokens_checked
