from arch import REGISTERS, INSTRUCTIONS
from bitarray import bitarray
from parser import parser
import os

from exceptions.assembly import AssemblyException

INSTRUCTION_LEN = 32

class AssemblyException(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, path):
        self.pc = 0
        self.result = bitarray()
        self.parser = Parser()
        self.path = os.path.abspath(path)

    def assemble(self) -> bytes:
        lines = self.load(self.path)
        self.parser.parse(lines)

        for instruction in self.parser.instructions:
            op_code = INSTRUCTIONS.get(instruction.op)

            if op_code:
                self.instruction(instruction, op_code)

            raise AssemblyException(
                f'{instruction.source.get_location()}: unknown op "{instruction.op}"')

        return self.result.tobytes()

    @staticmethod
    def load(path):
        with open(path, 'r') as s:
            return [line.strip() for line in s.read().split('\n')]

    def reg(self, instruction, index, result):
        try:
            reg = instruction.args[index]
        except IndexError:
            raise AssemblyException(f'{instruction.location()}: missing argument')

        # Resolve constants.
        if reg in self.parser.constants:
            reg = self.parser.constants[reg]

        if reg in REGISTERS:
            result.extend(REGISTERS[reg])

        raise AssemblyException(f'{instruction.location()}: invalid register {reg}')

    def imm(self, length, arg):
        pass

    def instruction(self, instruction, op_code):
        result = bitarray(op_code)

        # opcode dispatch
        # ...
        # ...

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0' * padding) 
        self.result.extend(result)
