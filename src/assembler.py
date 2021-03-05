from passes import remove_whitespace

class Assembler:
    def __init__(self):
        self.result = []
        self.passes = [remove_whitespace]

    def assemble(self, lines):
        for _pass in self.passes:
            self.result = _pass(self.result)

        self.result.append(0xFFFFFFFF)
        self.result.append(0xABCDEFAB)

        return [b.to_bytes(4, 'little') for b in self.result]
