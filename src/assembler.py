from arch import REGISTERS, INSTRUCTIONS, PSEUDO_INSTRUCTIONS, get_instr_def
from arch import REG, IMM11, IMM16, IMM26, PAD5
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
        self.parser = Parser()
        self.result = bitarray()
        self.path = os.path.abspath(path)

    @staticmethod
    def load(path):
        with open(path, 'r') as s:
            return [line.strip() for line in s.read().split('\n')]

    def assemble(self) -> bytes:
        lines = self.load(self.path)
        self.parser.parse(lines)
        
        # First pass. Resolve pseudo instructions.
        for instruction in self.parser.instructions:
            pass

        # Second pass. Assemble instructions.
        for instruction in self.parser.instructions:
            definition = get_instr_def(instruction.name)

            if definition:
                self.instruction(instruction, definition)

            raise AssemblyException(
                f'{instruction.source.get_location()}: unknown op "{instruction.op}"')

        return self.result.tobytes()

    def instruction(self, instruction, definition):
        result = bitarray(definition.opcode)

        for fd in definition.format:
            if fd == REG:

            elif fd == IMM11:
                
            elif fd == IMM16:

            elif fd == IMM26:

            elif fd == PAD5
                result.extend('0' * 5)
            else:
                raise AssemblyException(
                    f'unknown instruction format directive: {d}')

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0' * padding) 
        self.result.extend(result)

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
