
class Directive:
    def __init__(self, line, pc, op, args=[]):
        self.line = line
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
