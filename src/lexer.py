from token import Token, TOKEN_LABEL, TOKEN_MNEMONIC, TOKEN_DIRECTIVE, TOKEN_REGISTER, TOKEN_EXPRESSION
from architecture import registers  

class Lexer:
    def __init__(self):
        self.tokens = []

    def lex(self, lines):
        for index, line in enumerate(lines):
        
            # Start by removing the optional comment. 
            line = self.erase_comment(line)

            # Then we parse and obtain the label, 
            label, line = self.label(line)

            if label:
                self.tokens.append(Token(TOKEN_LABEL, label, index))

            # Parse the line operand. 
            op, line = self.op(line)

            if op:
                if op[0] == '.':
                    token = Token(TOKEN_DIRECTIVE, op[1:], index)
                else:
                    token = Token(TOKEN_MNEMONIC, op, index)
                            
                for arg in self.args(line):
                    if arg in registers:
                        token.args.append(Token(TOKEN_REGISTER, arg, index))
                    else:
                        token.args.append(Token(TOKEN_EXPRESSION, arg, index))

                self.tokens.append(token)

        return self.tokens

    def erase_comment(self, line):
        if not line:
            return None

        s = line.split('#', 1)

        if len(s) > 1:
            return s[0]
        else:
            return line

    def label(self, line):
        if not line:
            return (None, None)

        s = line.split(':', 1)

        if len(s) > 1:
            return (s[0].strip(), s[1].strip())
        else:
            return (None, line)

    def op(self, line):
        if not line:
            return (None, None)

        s = line.split(' ', 1)

        if len(s) > 1:
            return (s[0].strip(), s[1].strip())
        else:
            return (s[0], None)

    def args(self, line):
        if not line:
            return []

        return [arg.strip() for arg in line.split(',')]

if __name__ == '__main__':
    lexer = Lexer()
    result = lexer.lex(['ADD r0, r1, r2', 'yolo: .REMOVE r0, r1, r2, r3'])
    print(result)
