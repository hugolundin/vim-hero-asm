from statement import Statement

class Parser:
    def __init__(self):
        pass

    def parse(self, line) -> Statement:
        s = Statement()

        tail = self.erase_comment(line)
        s.label, tail = self.parse_label(tail)
        s.op, tail = self.parse_op(tail)
        s.args = self.parse_args(tail)

        return s

    def erase_comment(self, line):
        if not line:
            return None

        s = line.split('#', 1)

        if len(s) > 1:
            return s[0]
        else:
            return line

    def parse_label(self, line):
        if not line:
            return (None, None)

        s = line.split(':', 1)

        if len(s) > 1:
            return (s[0].strip(), s[1].strip())
        else:
            return (None, line)

    def parse_op(self, line):
        if not line:
            return (None, None)

        s = line.split(' ', 1)

        if len(s) > 1:
            return (s[0].strip(), s[1].strip())
        else:
            return (s[0], None)

    def parse_args(self, line):
        if not line:
            return []

        return [arg.strip() for arg in line.split(',')]
