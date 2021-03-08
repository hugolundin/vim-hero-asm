import re
from bitarray import bitarray

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, registers=[], instructions=[]):
        self.pc = 0
        self.labels = {}
        self.registers = registers
        self.instructions = instructions
        self.result = bitarray()

    def parse_label(self, tokens: list[str]) -> (str, list[str]):
        if not tokens:
            return (None, None)

        label, *tail = tokens

        print(label)

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

    def parse(self, line: str) -> (str, str, list[str]):
        s = line.strip()

        
        label, *tail = self.parse_label(s.split(' ', 1))

        print(tail)

        op, *arguments = self.parse_op(tail)

        return (label, op, arguments)

    def assemble(self, lines) -> bitarray:
        instructions = []

        for line in lines:
            label, op, *arguments = self.parse(line)

            if op:
                self.pc += 1
                instructions.append(instruction)

            if label:
                self.labels[label] = self.pc

        print(instructions)
        print(labels)

        for instruction in instructions:
            op, arguments = self.parse_op(instruction)

            if assembler := self.instructions.get(op):
                self.result.extend(assembler.assemble(arguments))

        print(self.result)
        return self.result
        


