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

def reg(result, mnemonic, labels, constants, index):
    register = REGISTERS.get(mnemonic.args[index])

    if not register:
        raise ArchitectureException(f'Unknown register {mnemonic.args[index]}')

    result.extend(register)

def imm(length):
    def f(result, mnemonic, labels, constants, index):
        value = int(simple_eval(mnemonic.args[index], names=labels|constants))
        result.extend(int2ba(value, length=length))

    return f

imm16 = imm(16)
imm21 = imm(21)
imm26 = imm(26)

INSTRUCTIONS = {

    # Load / Store
    'ld'    : Instruction('000001', reg, reg, imm16),
    'str'    : Instruction('000010', reg, reg, imm16),
    'mov'   : Instruction('000011', reg, reg),
    'movhi' : Instruction('000100', reg, imm16),
    'movli' : Instruction('000101', reg, imm16),
    'push'  : Instruction('000110', reg),
    'pop'   : Instruction('000111', reg),

    # Arithmetic
    'add'  : Instruction('001010', reg, reg, reg),
    'addi' : Instruction('001011', reg, reg, imm16),
    'sub'  : Instruction('001100', reg, reg, reg),
    'subi' : Instruction('001101', reg, reg, imm16),
    'mul'  : Instruction('001110', reg, reg, reg),
    'muli' : Instruction('001111', reg, reg, imm16),
    'inc'  : Instruction('010000', reg),
    'dec'  : Instruction('010001', reg),

    # Shift
    'lsl' : Instruction('010100', reg, reg),
    'asl' : Instruction('010101', reg, reg),
    'lsr' : Instruction('010110', reg, reg),
    'asr' : Instruction('010111', reg, reg),

    # Logic
    'and'  : Instruction('011010', reg, reg, reg),
    'andi' : Instruction('011011', reg, reg, imm16),
    'or'   : Instruction('011100', reg, reg, reg),
    'ori'  : Instruction('011101', reg, reg, imm16),
    'not'  : Instruction('011110', reg, reg),
    'xor'  : Instruction('011111', reg, reg, reg),

    # Compare
    'cmp'  : Instruction('100011', reg, reg),
    'cmpi' : Instruction('100100', reg, imm21),

    # Branch
    'beq'   : Instruction('101000', imm26),
    'bneq'  : Instruction('101001', imm26),
    'blt'   : Instruction('101010', imm26),
    'bgt'   : Instruction('101011', imm26),
    'blteq' : Instruction('101100', imm26),
    'bgteq' : Instruction('101101', imm26),
    'jmp'   : Instruction('101110', reg, imm21),
    'jmpi'  : Instruction('101111', imm26),

    # Subroutines
    # TODO: How should they be set? Weird in the datasheet at the moment. 
    'call' : Instruction('110001'),
    'ret'  : Instruction('110010'),

    # Other
    'nop'   : Instruction('000000'),
    'halt'  : Instruction('110110'),
    'henak' : Instruction('111111'),
}
