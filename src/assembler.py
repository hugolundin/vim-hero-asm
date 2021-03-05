from passes import remove_whitespace
from machine_code import MachineCode

class AssemblyError(Exception):
    """Raised when an error occurs during assembly."""
    pass

class Assembler:
    def __init__(self):
        self.result = MachineCode()
        self.passes = [remove_whitespace]

    def assemble(self, lines):
        for _pass in self.passes:
            self.result = _pass(self.result)

        self.result.add_instruction(0xFFFFFFFF)
        self.result.add_instruction(0x00000000)
        self.result.add_instruction(0xFF000000)
        self.result.add_instruction(0xFF000000)
        self.result.add_instruction(0xFF000000)
        self.result.add_instruction(0xFF000000)
        self.result.add_instruction(0xFF000000)
        

        return self.result.get_machine_code()
        #return [b.to_bytes(4, 'little') for b in self.result]
