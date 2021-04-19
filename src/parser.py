import logging

class ParseException(Exception):
    """Raised when an error occurs while parsing."""
    pass

class Mnemonic:
    def __init__(self, source, op, args=[]):
        self.source = source
        self.op = op
        self.args = args

    def __repr__(self):
        return str(self.__dict__)

class Parser:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.constants = {}
        self.mnemonics = []
        self.directives = []

    def __repr__(self):
        return str(self.__dict__)

    def parse(self, lines, offset=0):
        self.pc = 0

        for source in lines:
            
            # Start by discarding the comment. 
            line = self.erase_comment(source.content)

            # Fetch the label. 
            label, line = self.label(line)

            # If we have a label, add it to the list of labels
            # at the current program counter index.
            if label:
                self.labels[label] = self.pc

            # Then we look for an operand...
            op, line = self.op(line)

            if op:
                if self.directive(op, line, source):
                    continue
                else:
                    if mnemonic := self.mnemonic(op, line, source):
                        self.mnemonics.append(mnemonic)
                        
                        # We only increase the program counter whenever
                        # an instruction is found. That way, labels followed
                        # by an empty row be attached to the next instruction.
                        self.pc += 1
                        
                    else:
                        raise ParseException(f'{source.name}:{source.number}: invalid instruction: "{source.content}"')   

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

    def directive(self, op, line, source):
        if not op:
            # TODO: Raise exception.
            return False

        if op[0] != '.':
            return False

        # TODO: Improve constant handling.
        if op == '.constant':
            key, value = line.split(' ', 1)
            self.constants[key] = value
            return True

        # TODO: Raise exception. 
        return False
                
    def mnemonic(self, op, line, source):
        if not op:
            return None

        if not line:
            return Mnemonic(source, op, [])
        
        args = [arg.strip() for arg in line.split(',')]
        return Mnemonic(source, op, args)
