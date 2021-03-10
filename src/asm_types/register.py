from bitarray import bitarray

class Register:
    def __init__(self, op):
        self.op = bitarray(op)

    def assemble(self) -> bitarray:
        return self.op
