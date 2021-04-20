from isa import REGISTERS, INSTRUCTIONS
from bitarray import bitarray
from parser import Parser
import os

from line import Line
from exceptions.assembly import AssemblyException

INSTRUCTION_LEN = 32

class Assembler:
    def __init__(self):
        self.pc = 0
        self.parser = Parser()
        self.result = bitarray()

    def assemble(self, name) -> bytes:
        lines = self.process(self.load(name))
        self.parser.parse(lines)

        for instruction in self.parser.instructions:
            op_code = INSTRUCTIONS.get(instruction.op)

            if op_code:
                self.instruction(instruction, op_code)

            raise AssemblyException(
                f'{instruction.source.get_location()}: unknown op "{instruction.op}"')

        return self.result.tobytes()

    def load(self, name, paths=[]):
        instructions = []
        source_file = os.path.abspath(name)
        source_directory = os.path.dirname(source_file)

        if source_file in paths:
            return []
        else:
            paths.append(source_file)
        
        with open(source_file, 'r') as f:
            lines = [line.strip() for line in f.read().split('\n')]

            for index, line in enumerate(lines):
                if not line:
                    continue

                if line.startswith('.include'):
                    INCLUDE_START = '.include "' 
                    INCLUDE_END = '"'

                    child = line[line.find(INCLUDE_START) + len(INCLUDE_START):line.rfind(INCLUDE_END)]
                    instructions.extend(self.load(os.path.join(source_directory, child), paths))
                else:            
                    instructions.append(Line(line, source_file, index))

        return instructions

    def process(self, lines):
        process_parser = Parser()
        process_parser.parse(lines)

        for instruction in process_parser.instructions:
            op = instruction.op
            args = instruction.args

            # TODO: Why +1?
            if op == 'inc':
                lines[instruction.source.number + 1].content = f'addi {args[0]}, {args[0]}, 1'

            elif op == 'dec':                
                lines[instruction.source.number + 1].content = f'subi {args[0]}, {args[0]}, 1'

        return lines

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
        if len(instruction.args) 

    def instruction(self, instruction, op_code):
        result = bitarray(op_code)

        # opcode dispatch
        # ...
        # ...

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0' * padding) 
        self.result.extend(result)
