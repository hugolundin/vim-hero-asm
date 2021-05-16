from architecture import REG, IMM11, IMM16, IMM26, PAD5, REGISTERS, INSTRUCTIONS, BRANCH_INSTRUCTIONS, RELATIVE_BRANCH_INSTRUCTIONS, get_instr_def
from utilities import info, warning, error
from simpleeval import simple_eval
from bitarray.util import int2ba
from instruction import Instruction, InstructionParser
from bitarray import bitarray
from bitstring import Bits
import os

INSTRUCTION_LEN = 32

class AssemblyException(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, path):
        self.pc = 0
        self.parser = InstructionParser()
        self.data = bitarray()
        self.program = bitarray()
        self.path = os.path.abspath(path)

    @staticmethod
    def load(path):
        with open(path, 'r') as s:
            return [line.strip() for line in s.read().split('\n')]

    def assemble(self):
        lines = self.load(self.path)
        self.parser.parse(lines)

        # First pass. Build resulting data file. 
        if len(self.parser.data) > 0:
            for data in self.parser.data:
                value = simple_eval(data)
                binary = int2ba(value, length=32, endian='big', signed=True if value < 0 else False)
                self.data.extend(binary)
        
        # Second pass. Resolve pseudo instructions.
        # To limit the scope of this project, only
        # instructions of equal length can be pseudoed. 
        for index, instruction in enumerate(self.parser.instructions):
            if instruction.name == 'inc':
                self.parser.instructions[index] = Instruction(
                    'addi', instruction.line, [instruction.args[0], instruction.args[0], '1'])

            elif instruction.name == 'dec':
                self.parser.instructions[index] = Instruction(
                    'addi', instruction.line, [instruction.args[0], instruction.args[0], '-1'])

            elif instruction.name == 'henak718':
                self.parser.instructions[index] = Instruction(
                    'jmpi', instruction.line, ['718'])

        # Third pass. Assemble instructions.
        for index, instruction in enumerate(self.parser.instructions):
            definition = get_instr_def(INSTRUCTIONS, instruction.name)

            if definition:
                self.instruction(instruction, definition)

                # If the current instruction is a branch instruction, 
                # we want to check that it is not placed in the delay
                # slot of a previous branch instruction. 
                if get_instr_def(BRANCH_INSTRUCTIONS, instruction.name):

                    # The first instruction does not have a previous one. 
                    if index > 0:
                        previous = self.parser.instructions[index-1]

                        if get_instr_def(BRANCH_INSTRUCTIONS, previous.name):
                            message = f'{previous.source_line} (line {previous.line}) has a branch instruction ({instruction.source_line}) in its delay slot.'
                            warning(message)
            else:
                raise AssemblyException(
                    f'{self.path}:{instruction.line}: unknown op "{instruction.name}"')

            self.pc += 1

        return self.program, self.data

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
        self.program.extend(result)

    def reg(self, instruction, index, result):
        try:
            reg = instruction.args[index]
        except IndexError:
            raise AssemblyException(f'{self.path}:{instruction.line}: missing argument')

        # Resolve aliases.
        if reg.lower() in self.parser.aliases:
            reg = self.parser.aliases[reg.lower()]

        if reg in REGISTERS:
            result.extend(REGISTERS[reg])
        else:
            raise AssemblyException(f'{self.path}:{instruction.line}: invalid register {reg}')

    def imm(self, instruction, size, index, result):
        try:
            imm = instruction.args[index]
        except IndexError:
            raise AssemblyException(f'{self.path}:{instruction.line}: missing argument')

        if imm.lower() in self.parser.constants:
            imm = f'{self.parser.constants[imm.lower()]}'

        elif imm.lower() in self.parser.labels:
           
            if get_instr_def(RELATIVE_BRANCH_INSTRUCTIONS, instruction.name):
                imm = f'{self.parser.labels[imm.lower()] - self.pc - 1}'
            else:
                imm = f'{self.parser.labels[imm.lower()]}'

        value = simple_eval(imm)
        binary = int2ba(value, length=size, endian='big', signed=True if value < 0 else False)
        result.extend(binary)
