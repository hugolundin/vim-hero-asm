
class MachineCode:
    def __init__(self):
        self.data = bytearray()

    def add_instruction(self, bytes):
        self.data.extend(bytes.to_bytes(4, 'little'))

    def get_machine_code(self):
        return self.data