
class Statement:
    def __init__(self, label=None, op=None, args=[]):
        self.label = label
        self.op = op
        self.args = args

    def __repr__(self):
        return f'label={self.label}, op={self.op}, args={self.args}'

class Directive:
    def __init__(self, directive, args=[]):
        self.directive = directive
        self.args = args

class Alias(Directive):
    pass

class Const(Directive):
    pass

class Byte(Directive):
    pass