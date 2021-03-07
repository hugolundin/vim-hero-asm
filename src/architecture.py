import csv
from bitarray import bitarray

INSTRUCTION_LEN = 32
ARGUMENT_REGISTER = 'reg'
ARGUMENT_IMMEDIATE = 'imm'

class Instruction:
    def __init__(self, op, builders):
        self.op = bitarray(op)
        self.builders = builders

    def assemble(self, arguments) -> bitarray:
        result = bitarray(self.op)

        for builder in self.builders:
            if builder := builder:
                argument, *arguments = arguments
                builder(argument, result)

        padding = INSTRUCTION_LEN - len(result)
        result.extend('0'*padding)

        return result

class Architecture:
    def __init__(self, instructions, registers):
        self.registers = self.read_registers(registers)
        self.instructions = self.read_instructions(instructions)

    @staticmethod
    def read_instructions(source):
        result = {}

        with open(source, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter='|')

            for instruction in reader:
                name = instruction[0].strip()
                op = instruction[1].strip()
                arguments = instruction[2].strip().split(',')
                builders = []

                for argument in arguments:
                    if argument is ARGUMENT_REGISTER:
                        builders.append(self.register)
                    elif argument is ARGUMENT_IMMEDIATE:
                        builders.append(self.argument)
                    else:
                        # TODO: Do something smart
                        continue

                result[name] = Instruction(op, builders)

        return result

    @staticmethod
    def read_registers(source):
        result = {}

        with open(source, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter='|')

            for instruction in reader:
                name = instruction[0]
                code = instructions[1]
                result[name] = bitarray(code)

        return result
                
    def valid_register(self, r: str) -> bool:
        return r in self.registers

    def register(self, argument, result):
        if coding := self.registers.get(argument):
            result.extend(coding)

    def immediate(self, argument, result):
        pass

