import re
from line import parse_line
from bitarray import bitarray
from architecture import registers, instructions, transformers

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.pc = 0
        self.labels = {}
        self.instructions = []
        self.result = bitarray()

    def instruction(self, line):
        return line.op

    def label(self, line):
        return line.label

    def transformer(self, line):
        return transformers.get(line.op)

    def transform(self, line):
        return transformers[parsed_line.op](parsed_line.args)

    def parse_instructions(self, lines):        
        for line in lines:
            parsed_line = parse_line(line)

            if self.instruction(parsed_line):
                if transformer := self.transformer(parsed_line):
                    result = transformer(parsed_line.args)

                    if isinstance(result, list):
                        self.instructions.extend(result)
                    else:
                        self.instructions.append(result)
                else:
                    self.pc += 1
                    self.instructions.append(parsed_line)

            if label := self.label(parsed_line):
                self.labels[label] = self.pc

    def assemble(self, lines) -> bytes:
        self.parse_instructions(lines)

        for line in self.instructions:
            if instruction := instructions.get(line.op):
                self.result.extend(instruction.assemble(line.args, self.labels, self.pc))

        return self.result.tobytes()
