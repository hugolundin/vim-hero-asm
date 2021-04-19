from architecture import REGISTERS, INSTRUCTIONS
from bitarray import bitarray
from parser import Parser
import os

class Line:
    def __init__(self, content, name, number):
        self.content = content
        self.name = name
        self.number = number

    def description(self) -> str:
        return f'{self.name}, line {self.number + 1}'

    def __repr__(self):
        #return f'"{self.content}"'
        return str(self.__dict__)

class AssemblyException(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.pc = 0
        self.parser = Parser()
        self.result = bitarray()
    
    def assemble(self, name) -> bytes:
        lines = self.load(name)
        self.parser.parse(lines)

        for directive in self.parser.directives:
            print(directive)
            pass

        for mnemonic in self.parser.mnemonics:
            print(mnemonic)

            # Assemble the current mnemonic.
            instruction = INSTRUCTIONS.get(mnemonic.op)

            if not instruction:
                raise AssemblyException(
                    f'{mnemonic.source.description()}: unknown op "{mnemonic.op}"')

            result = instruction.assemble(mnemonic)
            self.result.extend(result)

        return self.result.tobytes()

    def load(self, name, paths=[]):
        instructions = []

        paths.append(name)
        
        with open(name, 'r') as f:
            current = os.path.abspath(name)
            lines = [line.strip() for line in f.read().split('\n')]

            for index, line in enumerate(lines):
                if not line:
                    continue

                if line.startswith('.include'):
                    INCLUDE_START = '.include("' 
                    INCLUDE_END = '")'

                    child = line[line.find(INCLUDE_START) + len(INCLUDE_START):line.rfind(INCLUDE_END)]

                    if child not in paths:
                        instructions.extend(self.load(child, paths))
                else:            
                    instructions.append(Line(line, current, index))

        return instructions
