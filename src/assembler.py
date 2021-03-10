import re
from line import parse
from bitarray import bitarray

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, registers=[], instructions=[]):
        self.pc = 0
        self.labels = {}
        self.tokens = []
        self.registers = registers
        self.instructions = instructions
        
        self.result = bitarray()

    def assemble(self, lines) -> bytes:
        instructions = []

        for line in lines:
            token = parse(line)

            if token.op:
                self.pc += 1
                self.tokens.append(token)

            if token.label:
                self.labels[label] = self.pc

        for token in self.tokens:
            if assembler := self.instructions.get(token.op):
                self.result.extend(assembler.assemble(token.args))

        return self.result.tobytes()
