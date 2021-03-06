from bidict import bidict
from bitarray import bitarray

INSTRUCTIONS = {
    'nop'  : bitarray('000000'),
    'ld'   : bitarray('000001'),
    'ldi'  : bitarray('000010'),
    'cmp'  : bitarray('000011'),
    'cmpi' : bitarray('000100'),
    'inc'  : bitarray('000101'),
    'dec'  : bitarray('000110'),
    'breq' : bitarray('000111')
}

class InstructionError(Exception):
    """Raised when an error occurs while parsing an instruction."""
    pass

class Instruction:
    def __init__(self, tokens, line_number):
        self.instruction, self.arguments = self.parse(tokens)
        self.line_number = line_number

    @staticmethod
    def parse(tokens) -> (str, list[str]):
        if not tokens:
            raise InstructionError('Invalid tokens.')

        instruction, *arguments = tokens

        if instruction not in INSTRUCTIONS:
            raise InstructionError('Invalid instruction.')

        return instruction, arguments

    def assemble(self) -> bitarray:
        result = bitarray()
        result.extend(INSTRUCTIONS[self.instruction])
        result.extend(bitarray('00000000000000000000000000'))
        return result

    def __repr__(self):
        return f'<{self.instruction} {self.arguments}>'
