from instructions import Instruction
from arguments import register

REGISTERS = {
    'r0' : '11111',
    'r1' : '11111'
}

INSTRUCTIONS = {
    'nop'  : Instruction('000000', None),
    'ld'   : Instruction('000001', register, register),
    'ldi'  : Instruction('000010', None),
    'cmp'  : Instruction('000011', None),
    'cmpi' : Instruction('000100', None),
    'inc'  : Instruction('000101', None),
    'dec'  : Instruction('000110', None),
    'breq' : Instruction('000111', None)
}

