from passes import remove_whitespace
from machine_code import MachineCodeBuilder

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.builder = MachineCodeBuilder()
        self.passes = [remove_whitespace]

    def assemble(self, lines):
        for _pass in self.passes:
            self.builder, lines = _pass(self.builder, lines)

        self.builder.insert_instruction(0xFFFFFFFF)
        return self.builder.get_machine_code()
