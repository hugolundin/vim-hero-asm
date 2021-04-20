from bitarray import bitarray

INSTRUCTION_LEN = 32

class InstructionException(Exception):
    pass

class Instruction:
    def __init__(self, op, *builders):
        self.op = bitarray(op)
        self.builders = builders

    def assemble(self, mnemonic, labels, constants) -> bitarray:
        args = mnemonic.args
        result = self.op.copy()

        if len(args) != len(self.builders):
            raise InstructionException(
                f'Unexpected number of arguments for {mnemonic.op} on line {mnemonic.pc}.')
        
        for index, builder in enumerate(self.builders):
            if not builder:
                continue

            builder(result, mnemonic, labels, constants, index)

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0'*padding)
        return result
