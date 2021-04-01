from tokens import Statement, Directive

class Parser:
    def __init__(self):
        pass

    def parse(self, line) -> Statement:
        tail = self.erase_comment(line)

        if directive := self.parse_directive(tail):
            return directive

        s = Statement()
        s.label, tail = self.parse_label(tail)
        s.op, tail = self.parse_op(tail)
        s.args = self.parse_args(tail)
        return s

    def parse_directive(self, line):
        if not line:
            return None

        d = line.split(' ', 1)
        if len(d) <= 1:
            return None

        print(döhafgöhj)
        

        return line[0] == '.'

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
