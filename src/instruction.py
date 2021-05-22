from bitarray import bitarray

from architecture import ALIASES, CONSTANTS

class InstructionException(Exception):
    pass

class ParseException(Exception):
    """Raised when an error occurs while tokenizing."""
    pass

TOKEN_COMMENT = ';'
DIRECTIVE_DATA = 'data'
DIRECTIVE_ALIAS = 'alias'
DIRECTIVE_CONSTANT = 'constant'

class Instruction:
    def __init__(self, name, line, args, source_line):
        self.name = name
        self.line = line
        self.args = args
        self.source_line = source_line

    def __repr__(self):
        return str(self.__dict__)

class InstructionParser:
    def __init__(self):
        self.pc = 0
        self.data = []
        self.labels = {}
        self.data_labels = {}
        self.aliases = dict(ALIASES)
        self.constants = dict(CONSTANTS)
        self.instructions = []
        
    def __repr__(self):
        return str(self.__dict__)

    def parse(self, lines):
        self.pc = 0

        for index, source_line in enumerate(lines, start=1):
            
            # Start by discarding the comment. 
            source_line = self.erase_comment(source_line)

            # Fetch the label. 
            label, line = self.label(source_line)

            # If we have a label, add it to the list of labels
            # at the current program counter index.
            if label:
                self.labels[label.lower()] = self.pc

            # Then we look for an operand...
            op, line = self.op(line)

            if op:
                if self.directive(op, index, line):
                    continue

                instruction = self.instruction(op, index, line, source_line)

                if instruction:
                    self.instructions.append(instruction)

                    # We only increase the program counter whenever
                    # an instruction is found. That way, labels followed
                    # by an empty row be attached to the next instruction.
                    self.pc += 1
                else:
                    raise ParseException(
                        f'line {index}: invalid instruction: "{line}"')   

    def directive(self, op, index, line):
        if not op:
            raise ParseException('Invalid state, op should always exist here.')

        dot, directive = op[0] == '.', op[1:]

        if not dot:
            return False

        if not directive:
            raise ParseException(f'Expected directive after ".": {line}')

        key, value = line.split(' ', 1)

        if directive == DIRECTIVE_CONSTANT:
            self.constants[key.lower().strip()] = value.strip()
        elif directive == DIRECTIVE_ALIAS:
            self.aliases[key.lower().strip()] = value.strip()
        elif directive == DIRECTIVE_DATA:

            if value.startswith('"'):
                with open(value[1:-1], 'rb') as ext:
                    self.data_labels[key.lower()] = len(self.data)

                    b = bitarray()
                    b.frombytes(ext.read())

                    if len(b) % 32 != 0:
                        b.extend([False]*(32 - (len(b) % 32)))
                    
                    for i in range(len(b) // 32):
                        self.data.append(f'0b{b[i * 32:(i + 1) * 32].to01()}')        
            else:
                self.data.append(value)
                self.data_labels[key.lower()] = len(self.data) - 1
        else:
            raise ParseException(f'Unknown directive: {directive}')

        return True

    def instruction(self, op, index, line, source_line):
        if not op:
            return None

        if not line:
            return Instruction(op, index, [], source_line)
        
        return Instruction(op, index, [arg.strip() for arg in line.split(',')], source_line)

    def erase_comment(self, line):
        if not line:
            return None

        s = line.split(TOKEN_COMMENT, 1)

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


