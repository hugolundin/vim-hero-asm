from bitarray import bitarray

INSTRUCTION_LEN = 32

class Instruction:
    def __init__(self, op, *builders):
        self.op = bitarray(op)
        self.builders = builders

    def assemble(self, arguments) -> bitarray:
        result = bitarray(self.op)

        for builder in self.builders:
            if builder := builder:
                argument, *arguments = arguments
                builder(argument, result)

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0'*padding)

        return result