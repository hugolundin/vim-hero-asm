from instruction import Instruction
from simpleeval import simple_eval
from bitarray.util import int2ba
from bitarray import bitarray

REGISTERS = {
    'r0'    : '00000',
    'r1'    : '00001',
    'r2'    : '00010',
    'r3'    : '00011',
    'r4'    : '00100',
    'r5'    : '00101',
    'r6'    : '00110',
    'r7'    : '00111',
    'r8'    : '01000',
    'r9'    : '01001',
    'r10'   : '01010',
    'r11'   : '01011',
    'r12'   : '01100',
    'r13'   : '01101',
    'r14'   : '01110',
    'r15'   : '01111',
    'r16'   : '10000',
    'r17'   : '10001',
    'r18'   : '10010',
    'r19'   : '10011',
    'r20'   : '10100',
    'r21'   : '10101',
    'r22'   : '10110',
    'r23'   : '10111',
    'r24'   : '11000',
    'r25'   : '11001',
    'r26'   : '11010',
    'pc'    : '11011',
    'sp'    : '11100',
    'flags' : '11101'
}

def reg(result, mnemonic, index):
    register = REGISTERS.get(mnemonic.args[index])

    if not register:
        raise ArchitectureException(f'Unknown register {mnemonic.args[index]}')

    result.extend(register)

def imm16(result, mnemonic, index):
    value = simple_eval(mnemonic.args[index])
    result.extend(int2ba(value, length=16))

def imm21(result, mnemonic, index):
    value = simple_eval(mnemonic.args[index])
    result.extend(int2ba(value, length=21))

INSTRUCTIONS = {

    # Load / Store
    'ld'    : Instruction('000001', reg, reg, imm16),
    'st'    : Instruction('000010', reg, reg, imm16),
    'mov'   : Instruction('000011', reg, reg),
    'movhi' : Instruction('000100', reg, imm16),
    'movli' : Instruction('000101', reg, imm16),
    'push'  : Instruction('000110'),
    'pop'   : Instruction('000111'),

    # Arithmetic
    'add'  : Instruction('001010'),
    'addi' : Instruction('001011'),
    'sub'  : Instruction('001100'),
    'subi' : Instruction('001101'),
    'mul'  : Instruction('001110'),
    'muli' : Instruction('001111'),
    'inc'  : Instruction('010000'),
    'dec'  : Instruction('010001'),

    # Shift
    'lsl' : Instruction('010100'),
    'asl' : Instruction('010101'),
    'lsr' : Instruction('010110'),
    'asr' : Instruction('010111'),

    # Logic
    'and'  : Instruction('011010'),
    'andi' : Instruction('011011'),
    'or'   : Instruction('011100'),
    'ori'  : Instruction('011101'),
    'not'  : Instruction('011110'),
    'xor'  : Instruction('011111'),

    # Compare
    'cmp'  : Instruction('100011'),
    'cmpi' : Instruction('100100'),

    # Branch
    'beq'   : Instruction('101000'),
    'bneq'  : Instruction('101001'),
    'blt'   : Instruction('101010'),
    'bgt'   : Instruction('101011'),
    'blteq' : Instruction('101100'),
    'bgteq' : Instruction('101101'),
    'jmp'   : Instruction('101110'),
    'jmpi'  : Instruction('101111'),

    # Subroutines
    'call' : Instruction('110001'),
    'ret'  : Instruction('110010'),

    # Other
    'nop'   : Instruction('000000'),
    'halt'  : Instruction('110110'),
    'henak' : Instruction('111111'),
}

# 000101 00000 0000000000110010 [00000]
#  op      D         50         padding
