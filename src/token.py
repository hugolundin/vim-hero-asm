TOKEN_LABEL = 0
TOKEN_MNEMONIC = 1
TOKEN_DIRECTIVE = 2
TOKEN_REGISTER = 3
TOKEN_EXPRESSION = 4

class Token:
    def __init__(self, kind, value, line):
        self.kind = kind
        self.value = value
        self.line = line
        self.args = []        

    def __repr__(self):
        def description(kind):
            if kind == TOKEN_LABEL:
                return 'Label'
            elif kind == TOKEN_MNEMONIC:
                return 'Mnemonic'
            elif kind == TOKEN_DIRECTIVE:
                return 'Directive'
            elif kind == TOKEN_REGISTER:
                return 'Register'
            elif kind == TOKEN_EXPRESSION:
                return 'Expression'
            else:
                return 'Unknown'

        if self.args:
            return f'{description(self.kind)}({self.value}, {self.args})'
        else:
            return f'{description(self.kind)}({self.value})'