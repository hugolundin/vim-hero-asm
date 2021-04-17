import logging

class ParseException(Exception):
    """Raised when an error occurs while parsing."""
    pass

class Directive:
    def __init__(self, location, pc, op, args=[]):
        self.location = location
        self.pc = pc
        self.op = op
        self.args = args

    def __repr__(self):
        return str(self.__dict__)

class Mnemonic:
    def __init__(self, line, op, args=[]):
        self.line = line
        self.op = op
        self.args = args

    def __repr__(self):
        return str(self.__dict__)

class Parser:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.mnemonics = []
        self.directives = []

    def __repr__(self):
        return str(self.__dict__)

    def parse(self, lines, offset=0):
        self.pc = 0

        for line_number, line in enumerate(lines, start=1):
        
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

                if directive := self.directive(op, line, line_number):
                    self.directives.append(directive)
                else:
                    if mnemonic := self.mnemonic(op, line, line_number):
                        self.mnemonics.append(mnemonic)
                        
                        # We only increase the program counter whenever
                        # an instruction is found. That way, labels followed
                        # by an empty row be attached to the next instruction.
                        self.pc += 1
                        
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

    def directive(self, op, line, line_number):
        if not op or op[0] != '.':
            # TODO: Raise exception.
            return None

        arg = ''
        args = []
        string = False
        
        for c in line:
            if c in ['"', "'"]:
                if string:
                    args.append(arg)
                    arg = ''
                else:
                    string = True

                continue
            
            if c.isspace():
                if string:
                    arg += c
                else:
                    args.append(arg)
                    arg = ''

            arg += c
                
        directive = Directive(line_number, self.pc, op[1:], args)
        return directive

    def mnemonic(self, op, line, line_number):
        arguments = [arg.strip() for arg in line.split(',')]
        mnemonic = Mnemonic(line_number, op, arguments)
        return mnemonic
