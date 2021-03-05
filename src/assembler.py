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
        self.lines = [line.strip() for line in lines]

    def tokenize(self, line) -> (str, list[str]):
        tokens = line.split(' ')

        if tokens[0][-1] == ':':
            return (tokens[0], tokens[1:])

        return (None, tokens)

    def assemble(self) -> bytearray:
        for line in self.lines:
            label, instruction = self.tokenize(line)
            
            if instruction:
                self.pc += 1
                self.instructions.append(instruction)

            if label:
                self.labels[label] = self.pc

        print(self.labels)

        for instruction in self.instructions:
            print(instruction)
        
        return self.builder.get_machine_code()