from architecture import REG, IMM11, IMM16, IMM26, PAD5, REGISTERS, get_instr_def
from simpleeval import simple_eval
from bitarray.util import int2ba
from instruction import Parser
from bitarray import bitarray
import os

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
            else:
                raise AssemblyException(
                    f'{self.path}:{instruction.line}: unknown op "{instruction.name}"')

        return self.result.tobytes()

    def instruction(self, instruction, definition):
        index = 0
        result = bitarray(definition['opcode'])
        
        for d in definition['format']:
            if d == REG:
                self.reg(instruction, index, result)
                index += 1
            elif d == IMM11:
                self.imm(instruction, 11, index, result)
                index += 1
            elif d == IMM16:
                self.imm(instruction, 16, index, result)
                index += 1
            elif d == IMM26:
                self.imm(instruction, 26, index, result)
                index += 1
            elif d == PAD5:
                result.extend('0' * 5)
            else:
                raise AssemblyException(
                    f'{self.path}:{instruction.line}: unknown instruction format directive: {d}')

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0' * padding) 
        self.result.extend(result)

    def reg(self, instruction, index, result):
        try:
            reg = instruction.args[index]
        except IndexError:
            raise AssemblyException(f'{self.path}:{instruction.line}: missing argument')

        # Resolve constants.
        if reg in self.parser.constants|self.parser.labels:
            reg = (self.parser.constants|self.parser.labels)[reg]

        if reg in REGISTERS:
            result.extend(REGISTERS[reg])
        else:
            raise AssemblyException(f'{self.path}:{instruction.line}: invalid register {reg}')

    def imm(self, instruction, size, index, result):
        try:
            imm = instruction.args[index]
        except IndexError:
            raise AssemblyException(f'{self.path}:{instruction.line}: missing argument')

        if imm in self.parser.constants:
            imm = self.parser.constants[imm]

        value = simple_eval(imm, names=self.parser.labels|self.parser.constants)
        binary = int2ba(value, length=size, endian='big')
        result.extend(binary)
