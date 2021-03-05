
class MachineCodeBuilder:
    def __init__(self):
        self.data = bytearray()

    def insert_instruction(self, instruction):
        self.data.extend(instruction.to_bytes(4, 'little'))

    def insert_byte(self, byte):
        self.data.extend(byte)

    def insert_bytes(self, bytes):
        for byte in bytes:
            self.insert_byte(byte)

    def get_machine_code(self) -> bytearray:
        return self.data
