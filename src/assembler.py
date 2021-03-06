from passes import remove_whitespace
from machine_code import MachineCodeBuilder

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass


class Assembler:
    def __init__(self, lines):
        self.pc = 0
        self.labels = {}
        self.instructions = []
        self.passes = [remove_whitespace]
        self.builder = MachineCodeBuilder()
        self.lines = [line for line in [line.strip() for line in lines] if line]

    def label(self, token) -> str:
        return token if token[-1] == ':' else None

    def tokenize(self, line, lc) -> (str, list[str]):
        tokens = line.split(' ')

        if not tokens:
            return (None, None)

        if label := self.label(tokens[0]):
            return (label, tokens[1:])

        return (None, tokens)

    def assemble(self) -> bytearray:
        for line, line in enumerate(self.lines):
            label, instruction = self.tokenize(line, index)
            
            if instruction:
                self.pc += 1
                self.instructions.append((index, instruction))

            if label:
                self.labels[label] = self.pc

        print(self.labels)

        for instruction in self.instructions:
            print(instruction)
        
        return self.builder.get_machine_code()