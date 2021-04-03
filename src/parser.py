from tokens import Directive, Mnemonic

class ParseException(Exception):
    """Raised when an error occurs while parsing."""
    pass

class Parser:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.mnemonics = []
        self.directives = []

    def __repr__(self):
        return str(self.__dict__)

    def parse(self, lines):
        self.pc = 0

        for line in lines:
        
            # Start by discarding the comment. 
            line = self.erase_comment(line)

            # Fetch the label. 
            label, line = self.label(line)

            # If we have a label, add it to the list of labels
            # at the current program counter index.
            if label:
                self.labels[label] = self.pc

            # Then we look for an operand...
            op, line = self.op(line)

            if op:

                # We only increase the program counter whenever
                # an instruction is found. That way, labels followed
                # by an empty row be attached to the next instruction.
                self.pc += 1

                if directive := self.directive(op, line):
                    self.directives.append(directive)
                else:
                    if mnemonic := self.mnemonic(op, line):
                        self.mnemonics.append(mnemonic)
                    else:
                        raise ParseException('Unexpected operand.')
                    

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

    def directive(self, op, line):
        if not op or op[0] != '.':
            return None

        arguments = [arg.strip() for arg in line.split(' ')]
        directive = Directive(self.pc, op[1:], arguments)
        return directive

    def mnemonic(self, op, line):
        arguments = [arg.strip() for arg in line.split(',')]
        mnemonic = Mnemonic(self.pc, op, arguments)
        return mnemonic
