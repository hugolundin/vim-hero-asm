from bitarray import bitarray

INSTRUCTION_LEN = 32

class Instruction:
    def __init__(self, op, *builders):
        self.op = bitarray(op)
        self.builders = builders

    def assemble(self, mnemonic) -> bitarray:
        args = mnemonic.args
        result = self.op.copy()
        
        for index, builder in enumerate(self.builders):
            if not builder:
                continue

            builder(result, mnemonic, index)

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0'*padding)
        return result
