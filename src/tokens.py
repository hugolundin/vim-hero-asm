
class Directive:
    def __init__(self, pc, op, args=[]):
        self.pc = pc
        self.op = op
        self.args = args

    def __repr__(self):
        return str(self.__dict__)

class Mnemonic:
    def __init__(self, pc, op, args=[]):
        self.pc = pc
        self.op = op
        self.args = args

    def __repr__(self):
        return str(self.__dict__)
