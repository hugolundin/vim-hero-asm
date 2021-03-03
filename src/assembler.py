from passes import remove_whitespace

class Assembler:
    def __init__(self):
        self.result = []
        self.transformations = [
            remove_whitespace
        ]

    def assemble(self, lines):
        for transformation in self.transformations:
            self.result = transformation(self.result)

        self.result.append(0xFFFFFFFF)
        self.result.append(0xABCDEFAB)

        return [b.to_bytes(4, 'little') for b in self.result]
