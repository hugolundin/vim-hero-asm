from simpleeval import simple_eval
from bitarray.util import int2ba

from instruction import Instruction
from register import Register

registers = {
    'r0'    : '11111',
    'r1'    : '00010',
    'r2'    : '00011',
    'r3'    : '00100',
    'r4'    : '00101',
    'r5'    : '00000',
    'r6'    : '00000',
    'r7'    : '00000',
    'r8'    : '00000',
    'r9'    : '00000',
    'r10'   : '00000',
    'r11'   : '00000',
    'r12'   : '00000',
    'r13'   : '00000',
    'r14'   : '00000',
    'r15'   : '00000',
    'r16'   : '00000',
    'r17'   : '00000',
    'r18'   : '00000',
    'r19'   : '00000',
    'r20'   : '00000',
    'r21'   : '00000',
    'r22'   : '00000',
    'r23'   : '00000',
    'r24'   : '00000',
    'r25'   : '00000',
    'r26'   : '00000',
    'pc'    : '00000',
    'sp'    : '00000',
    'flags' : '00000'
}

def reg(result, argument):
    if register := registers.get(argument):
        result.extend(register)

def imm21(result, argument):
    value = simple_eval(argument)
    result.extend(int2ba(value, length=21))

def imm16(result, argument):
    value = simple_eval(argument)
    result.extend(int2ba(value, length=16))

instructions = {
    'nop'  : Instruction('000000'),
    'ld'   : Instruction('000001', reg, reg),
    'ldi'  : Instruction('111111', reg, imm21),
    'cmp'  : Instruction('000011', reg, reg),
    'cmpi' : Instruction('000011', reg, imm16)
}
