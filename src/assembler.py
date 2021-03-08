import re
from bitarray import bitarray

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, registers, instructions):
        self.pc = 0
        self.labels = {}
        self.registers = registers
        self.instructions = instructions
        self.result = bitarray()

    def parse_label(self, tokens: list[str]) -> (str, list[str]):
        if not tokens:
            return (None, None)

        label, *tail = tokens

        if label[-1] == ':':
            return (label, tail)

        return (None, tokens)

    def parse_op(self, tokens: list[str]) -> (str, list[str]):
        if not tokens:
            return (None, None)

        op, *tail = tokens

        if op in self.instructions:
            return (op, tail)

        return (None, tokens)

    def tokenize(self, lines: list[str]) -> list[str]:
        result = []

        for line in lines:
            result.append([t for t in re.split(',| ', line) if t])

        return result

    def assemble(self, lines) -> bitarray:
        instructions = []
        tokens = self.tokenize(lines)

        # print(tokens)

        for line in tokens:
            label, instruction = self.parse_label(line)

            if tokens:
                self.pc += 1
                instructions.append(instruction)

            if label:
                self.labels[label] = self.pc

        for instruction in instructions:
            op, arguments = self.parse_op(instruction)

            if assembler := self.instructions.get(op):
                self.result.extend(assembler.assemble(arguments))

        print(self.result)
        return self.result
        


