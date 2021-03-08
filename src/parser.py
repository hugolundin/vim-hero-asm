from lark import Lark
from lark import Transformer
from lark.exceptions import UnexpectedCharacters

class LineTransformer(Transformer):
    def assert_empty(self, var):
        if var:
            raise Exception('Invalid line parsed. ')
    
    def start(self, tokens):
        label = None
        op = None
        arguments = []
        comment = None

        for token in tokens:
            if token.type == 'ARGUMENT':
                arguments.append(token.value)
            elif token.type == 'COMMENT':
                self.assert_empty(comment)
                comment = token.value
            elif token.type == 'OP':
                self.assert_empty(op)
                op = token.value
            elif token.type == 'LABEL':
                self.assert_empty(label)
                label = token.value
            else:
                raise Exception('Unknown token')

        return (label, op, arguments, comment)

def parse(line):
    l = Lark("""
    start: [LABEL ":"]  OP [ARGUMENT ["," ARGUMENT]*] [COMMENT]

    LABEL: NAME
    OP.1: NAME
    ARGUMENT.2: VARIABLE
            | DECIMAL
            | HEXADECIMAL
            | BINARY

    VARIABLE : NAME
    DECIMAL.3 : DEC
    HEXADECIMAL.3 : HEX
    BINARY.3 : BIN
    
    %import common.CNAME -> NAME
    %import python.COMMENT -> COMMENT
    %import python.DEC_NUMBER -> DEC
    %import python.HEX_NUMBER -> HEX
    %import python.BIN_NUMBER -> BIN
    %import common.WS
    %ignore WS
    """, parser='lalr')

    try:
        tree = l.parse(line)
    except UnexpectedCharacters as e:
        print(e)
        exit(0)

    return LineTransformer().transform(tree)

if __name__ == '__main__':
    label, op, arguments, comment = parse('nop')

    print(label, op, arguments, comment)

# def parse(line):
#     l = Lark(r"""
#     line: [label] op [argument ("," argument)*] [comment]

#     label: STRING ":"
#     op: STRING
#     argument: STRING
#     comment: "#" STRING

#     %import common.ESCAPED_STRING -> STRING
#     %import common.WS
#     %ignore WS
#     """, start='line')
    
#     return l.parse(line)

# if __name__ == '__main__':
#     print(parse('nop:'))
#     # print(parse('bla: ldi r0, r1'))
