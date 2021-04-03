from architecture import REGISTERS, INSTRUCTIONS
from bitarray import bitarray
from parser import Parser
import logging

class AssemblyException(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.pc = 0
        self.parser = Parser()
        self.result = bitarray()
    
    def assemble(self, lines) -> bytes:
        self.parser.parse(lines)

        for mnemonic in self.parser.mnemonics:
            # Assemble the current mnemonic.
            instruction = INSTRUCTIONS.get(mnemonic.op)

            if not instruction:
                raise AssemblyException(
                    f'Unknown instruction on line {mnemonic.pc}: {mnemonic.op}')

            result = instruction.assemble(mnemonic)
            self.result.extend(result)

        return self.result.tobytes()      
