from bitarray import bitarray
from parser import Parser
from architecture import registers, instructions, pseudo_instructions

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self, parser=Parser()):
        self.pc = 0
        self.labels = {}
        self.parser = parser
        self.result = bitarray()
    
    def assemble(self, lines) -> bytes:
        statements = self.parse(lines)

        for statement in statements:

            # Assemble the current statement.
            result = instructions[statement.op].assemble(
                arguments=statement.args,
                labels=self.labels,
                pc=self.pc)

            self.result.extend(result)

        return self.result.tobytes()

    def parse(self, lines):
        statements = []

        for line in lines:
            statement = self.parser.parse(line)

            if statement.op:
                if statement.op in pseudo_instructions:
                    result = self.transform(statement)
                    
                    if isinstance(result, list):
                        statements.extend(result)
                    else:
                        statements.append(result)

                elif statement.op in instructions:
                    self.pc += 1
                    statements.append(statement)

                else:
                    raise AssemblyError(f'Invalid opcode: {statement.op}')

            if statement.label:
                self.labels[statement.label] = self.pc

        return statements
