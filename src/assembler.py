import re
from asm_types.line import parse
from bitarray import bitarray

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, registers=[], instructions=[]):
        self.pc = 0
        self.labels = {}
        self.program = []
        self.registers = registers
        self.instructions = instructions
        
        self.result = bitarray()

    def assemble(self, lines) -> bytes:
        instructions = []

        for line in lines:
            parsed_line = parse(line)

            if parsed_line.op:
                self.pc += 1
                self.program.append(parsed_line)

            if parsed_line.label:
                self.labels[label] = self.pc

        for line in self.program:
            if assembler := self.instructions.get(line.op):
                self.result.extend(assembler.assemble(line.args))            

        return self.result.tobytes()
