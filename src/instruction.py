from bitarray import bitarray

INSTRUCTION_LEN = 32

class Instruction:
    def __init__(self, op, *builders):
        self.op = bitarray(op)
        self.builders = builders

    def assemble(self, arguments, labels, pc) -> bitarray:
        result = self.op.copy()

        for builder in self.builders:
            if builder := builder:
                argument, *arguments = arguments
                builder(result, argument, labels, pc)

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0'*padding)

        return result
