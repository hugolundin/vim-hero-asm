from bitarray import bitarray

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, registers, instructions):
        self.pc = 0
        self.labels = {}
        self.registers = registers
        self.instructions = instructions
        self.result = bitarray()

    def parse_label(self, tokens: list[str]) -> (str, list[str]):
        if not tokens:
            return (None, None)

        label, *tail = tokens

        if label[-1] == ':':
            return (label, tail)

        return (None, tokens)

    def parse_op(self, tokens: list[str]) -> (str, list[str]):
        if not tokens:
            return (None, None)

        op, *tail = tokens

        if op in self.instructions:
            return (op, tail)

        return (None, tokens)

    def tokenize(self, lines: list[str]) -> list[str]:
        clean_lines = [line for line in [line.strip() for line in lines] if line]
        tokenized = [line.replace(' ', ',').split(',') for line in clean_lines]
        return tokenized

    def assemble(self, lines) -> bytes:
        instructions = []
        tokens = self.tokenize(lines)

        for line in tokens:
            label, instruction = self.parse_label(line)

            if tokens:
                self.pc += 1
                instructions.append(instruction)

            if label:
                self.labels[label] = self.pc

        for instruction in instructions:
            op, arguments = self.parse_op(instruction)

            if assembler := self.instructions.get(op):
                self.result.extend(assembler.assemble(arguments))

        return self.result.tobytes()
        


