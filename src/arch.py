from instructions import Instruction

class Architecture:
    def __init__(self):
        self.registers = {
            'r0' : '11111',
            'r1' : '11111'
        }

        self.instructions = {
            'nop'  : Instruction('000000', None),
            'ld'   : Instruction('000001', self.register, self.register),
            'ldi'  : Instruction('000010', self.register, self.immediate),
            'cmp'  : Instruction('000011', self.register, self.register),
            'cmpi' : Instruction('000100', self.register, self.immediate),
            'inc'  : Instruction('000101', self.register),
            'dec'  : Instruction('000110', self.register),
            'breq' : Instruction('000111', self.register, self.register)
        }

    def valid_register(self, r: str) -> bool:
        return r in self.registers

    def register(self, argument, result):
        if coding := self.registers.get(argument):
            result.extend(coding)

    def immediate(self, argument, result):
        pass
