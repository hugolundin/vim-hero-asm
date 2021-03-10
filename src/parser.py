class Line:
    def __init__(self):
        self.label = None
        self.op = None
        self.args = []

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
    
def parse(line):
    l = Line()

    tail = erase_comment(line)
    l.label, tail = parse_label(tail)
    l.op, tail = parse_op(tail)
    l.args = parse_args(tail)

    return l

if __name__ == '__main__':
    print(parse('nop'))
    print(parse('ldi r0, 2 + 2* 3'))
    print(parse('start: nop #blbablabla#hej'))
    
    
