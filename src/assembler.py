from bitarray import bitarray
from arch import INSTRUCTIONS, REGISTERS

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.instructions = []
        self.result = bitarray()

    @staticmethod
    def remove_whitespace(lines):
        return [line for line in [line.strip() for line in lines] if line]

    @staticmethod
    def label(token) -> str:
        return token if token[-1] == ':' else None

    def parse_label(self, line) -> (str, list[str]):
        tokens = line.replace(' ', ',').split(',')

        if not tokens:
            return (None, None)

        if label := self.label(tokens[0]):
            return (label, tokens[1:])

        return (None, tokens)

    def parse_instruction(self, tokens):
        if not tokens:
            raise Exception('Invalid tokens.')

        instruction, *arguments = tokens

        return instruction, arguments

    def assemble(self, lines) -> bytes:
        lines = self.remove_whitespace(lines)

        for line in lines:
            label, tokens = self.parse_label(line)

            if tokens:
                self.pc += 1
                self.instructions.append(tokens)

            if label:
                self.labels[label] = self.pc

        for tokens in self.instructions:
            op, arguments = self.parse_instruction(tokens)

            if instruction := INSTRUCTIONS.get(op):
                self.result.extend(instruction.assemble(arguments))

        return self.result.tobytes()
        


