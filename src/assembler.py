from bitarray import bitarray
from instructions import Instruction

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

    def tokenize(self, line, line_number) -> (str, list[str]):
        tokens = line.split(' ')

        if not tokens:
            return (None, None)

        if label := self.label(tokens[0]):
            return (label, tokens[1:])

        return (None, tokens)

    def assemble(self, lines) -> bytes:
        lines = self.remove_whitespace(lines)

        for line_number, line in enumerate(lines):
            label, tokens = self.tokenize(line, line_number)
            
            if tokens:
                self.pc += 1
                self.instructions.append(Instruction(tokens, line_number))

            if label:
                self.labels[label] = self.pc

        for instruction in self.instructions:
            self.result.extend(instruction.assemble())

        return self.result.tobytes()
        


