
REG   = 0
IMM11 = 1
IMM16 = 2
IMM26 = 3
PAD5  = 4

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
    'r27'   : '11011',
    'r28'   : '11100',
    'r29'   : '11101',
    'r30'   : '11110',
    'r31'   : '11111'
}

LOAD_STORE_INSTRUCTIONS = [
    {'name': 'ld',    'opcode': '000001', 'format': [REG, REG, IMM16]},
    {'name': 'str',   'opcode': '000010', 'format': [PAD5, REG, REG, IMM11]},
    {'name': 'mov',   'opcode': '000011', 'format': [REG, REG]},
    {'name': 'movhi', 'opcode': '000100', 'format': [REG, IMM16]},
    {'name': 'movli', 'opcode': '000101', 'format': [REG, IMM16]},
    {'name': 'push',  'opcode': '000110', 'format': [PAD5, REG]},
    {'name': 'pop',   'opcode': '000111', 'format': [REG]}
]

ARITHMETIC_INSTRUCTIONS = [
    {'name': 'add',   'opcode': '001010', 'format': [REG, REG, REG]},
    {'name': 'addi',  'opcode': '001011', 'format': [REG, REG, IMM16]},
    {'name': 'sub',   'opcode': '001100', 'format': [REG, REG, REG]},
    {'name': 'subi',  'opcode': '001101', 'format': [REG, REG, IMM16]},
    {'name': 'mul',   'opcode': '001110', 'format': [REG, REG, REG]},
    {'name': 'muli',  'opcode': '001111', 'format': [REG, REG, IMM16]}
]

SHIFT_INSTRUCTIONS = [
    {'name': 'lsl',  'opcode': '010100', 'format': [REG, REG]},
    {'name': 'asl',  'opcode': '010101', 'format': [REG, REG]},
    {'name': 'lsr',  'opcode': '010110', 'format': [REG, REG]},
    {'name': 'asr',  'opcode': '010111', 'format': [REG, REG]}
]

LOGIC_INSTRUCTIONS = [
    {'name': 'and',  'opcode': '011010', 'format': [REG, REG, REG]},
    {'name': 'andi', 'opcode': '011011', 'format': [REG, REG, IMM16]},
    {'name': 'or',   'opcode': '011100', 'format': [REG, REG, REG]},
    {'name': 'ori',  'opcode': '011101', 'format': [REG, REG, IMM16]},
    {'name': 'not',  'opcode': '011110', 'format': [REG, REG]},
    {'name': 'xor',  'opcode': '011111', 'format': [REG, REG, REG]},
]

COMPARE_INSTRUCTIONS = [
    {'name': 'cmp',  'opcode': '100011', 'format': [PAD5, REG, REG]},
    {'name': 'cmpi', 'opcode': '100100', 'format': [PAD5, REG, IMM16]}
]

RELATIVE_BRANCH_INSTRUCTIONS = [
    {'name': 'beq',   'opcode': '101000', 'format': [IMM26]},
    {'name': 'bneq',  'opcode': '101001', 'format': [IMM26]},
    {'name': 'blt',   'opcode': '101010', 'format': [IMM26]},
    {'name': 'bgt',   'opcode': '101011', 'format': [IMM26]},
    {'name': 'blteq', 'opcode': '101100', 'format': [IMM26]},
    {'name': 'bgteq', 'opcode': '101101', 'format': [IMM26]},
    {'name': 'jmpi',  'opcode': '101111', 'format': [IMM26]}
]

DYNAMIC_BRANCH_INSTRUCTIONS = [
    {'name': 'jmp',   'opcode': '101110', 'format': [PAD5, REG, IMM16]},
]

BRANCH_INSTRUCTIONS = RELATIVE_BRANCH_INSTRUCTIONS + DYNAMIC_BRANCH_INSTRUCTIONS

SUBROUTINE_INSTRUCTIONS = [
    {'name': 'call', 'opcode': '110001', 'format': [REG, REG, REG]},
    {'name': 'ret',  'opcode': '110010', 'format': [REG, REG, REG]}
]

OTHER_INSTRUCTIONS = [
    {'name': 'nop',  'opcode': '000000', 'format': []},
    {'name': 'halt',  'opcode': '110110', 'format': []},
    {'name': 'henak',  'opcode': '111111', 'format': []}
]

INSTRUCTIONS = \
    LOAD_STORE_INSTRUCTIONS + \
    ARITHMETIC_INSTRUCTIONS + \
    SHIFT_INSTRUCTIONS      + \
    LOGIC_INSTRUCTIONS      + \
    COMPARE_INSTRUCTIONS    + \
    BRANCH_INSTRUCTIONS     + \
    SUBROUTINE_INSTRUCTIONS + \
    OTHER_INSTRUCTIONS

def get_instr_def(instructions, name):
    for instruction in instructions:
        if instruction['name'] == name:
            return instruction

    return None

ALIASES = {
    'zero': 'r0',
    'ret' : 'r31'
}

IO_BASE_ADDR = 1024

CONSTANTS = {
    'HENAK'        :  '718',
    'LEDS_ADDR'    : f'{IO_BASE_ADDR}',
    'KEYBOARD_ADDR': f'{IO_BASE_ADDR + 1}'
}
