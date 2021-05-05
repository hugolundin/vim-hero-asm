import logging

class InstructionException(Exception):
    pass

class ParseException(Exception):
    """Raised when an error occurs while tokenizing."""
    pass

class Instruction:
    def __init__(self, name, line, args=[]):
        self.name = name
        self.line = line
        self.args = args

    def __repr__(self):
        return str(self.__dict__)

class Parser:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.aliases = {'zero': 'r0'}
        self.constants = {'pi': '3', 'e': '3', 'g': '10', 'henak': '718'}
        self.instructions = []
        
    def __repr__(self):
        return str(self.__dict__)

    def parse(self, lines):
        self.pc = 0

        for index, line in enumerate(lines, start=1):
            
            # Start by discarding the comment. 
            line = self.erase_comment(line)

            # Fetch the label. 
            label, line = self.label(line)

            # If we have a label, add it to the list of labels
            # at the current program counter index.
            if label:
                self.labels[label.lower()] = self.pc

            # Then we look for an operand...
            op, line = self.op(line)

            if op:
                if self.directive(op, index, line):
                    continue

                instruction = self.instruction(op, index, line)

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

        # TODO: Raise exception.
        if not dot:
            return False

        # TODO: Raise exception.
        if not directive:
            return False

        if directive == 'constant':
            key, value = line.split(' ', 1)
            self.constants[key.lower().strip()] = value.strip()
            return True

        if directive == 'alias':
            key, value = line.split(' ', 1)
            self.aliases[key.lower().strip()] = value.strip()
            return True

        # TODO: Raise exception. 
        return False

    def instruction(self, op, index, line):
        if not op:
            return None

        if not line:
            return Instruction(op, index, [])
        
        return Instruction(op, index, [arg.strip() for arg in line.split(',')])

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


