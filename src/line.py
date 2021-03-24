class Line:
    def __init__(self, label=None, op=None, args=[]):
        self.label = label
        self.op = op
        self.args = args

    def __repr__(self):
        return f'label={self.label}, op={self.op}, args={self.args}'

def erase_comment(line):
    if not line:
        return None

    s = line.split('#', 1)

    if len(s) > 1:
        return s[0]
    else:
        return line

def parse_label(line):
    if not line:
        return (None, None)

    s = line.split(':', 1)

    if len(s) > 1:
        return (s[0].strip(), s[1].strip())
    else:
        return (None, line)

def parse_op(line):
    if not line:
        return (None, None)

    s = line.split(' ', 1)

    if len(s) > 1:
        return (s[0].strip(), s[1].strip())
    else:
        return (s[0], None)

def parse_args(line):
    if not line:
        return []

    return [arg.strip() for arg in line.split(',')]
    
def parse_line(line):
    l = Line()

    tail = erase_comment(line)
    l.label, tail = parse_label(tail)
    l.op, tail = parse_op(tail)
    l.args = parse_args(tail)

    return l
