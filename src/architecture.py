from bitarray.util import int2ba

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
TONE_LENGTH=8
TONE_ENDIAN='big'

CONSTANTS = {
    'henak'                             :  '718',
    'leds_address'                      : f'{IO_BASE_ADDR}',
    'keyboard_address'                  : f'{IO_BASE_ADDR + 1}',
    'sound_address'                     : f'{IO_BASE_ADDR + 2}',
    'buttons_pressed_address'           : f'{IO_BASE_ADDR + 3}',
    'score_add_address'                 : f'{IO_BASE_ADDR + 4}',
    'sprite_register_tick_address'      : f'{IO_BASE_ADDR + 5}',
    'sprite_register_data_address'      : f'{IO_BASE_ADDR + 6}',
    'sprite_register_notes_hit_address' : f'{IO_BASE_ADDR + 7}',
    'tick_address'                      : f'{IO_BASE_ADDR + 8}',
    'silencio': f'0b{int2ba(0, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c1': f'0b{int2ba(1, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#1': f'0b{int2ba(2, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd1': f'0b{int2ba(3, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#1': f'0b{int2ba(4, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e1': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f1': f'0b{int2ba(6, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#1': f'0b{int2ba(7, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g1': f'0b{int2ba(8, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#1': f'0b{int2ba(9, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a1': f'0b{int2ba(10, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#1': f'0b{int2ba(1, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b1': f'0b{int2ba(12, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',

    'c2': f'0b{int2ba(13, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#2': f'0b{int2ba(1, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd2': f'0b{int2ba(15, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#2': f'0b{int2ba(1, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e2': f'0b{int2ba(17, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f2': f'0b{int2ba(18, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#2': f'0b{int2ba(1, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g2': f'0b{int2ba(20, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#2': f'0b{int2ba(2, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a2': f'0b{int2ba(22, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#2': f'0b{int2ba(2, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b2': f'0b{int2ba(24, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',

    'c3': f'0b{int2ba(25, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#3': f'0b{int2ba(2, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd3': f'0b{int2ba(27, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#3': f'0b{int2ba(2, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e3': f'0b{int2ba(29, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f3': f'0b{int2ba(30, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#3': f'0b{int2ba(3, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g3': f'0b{int2ba(32, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#3': f'0b{int2ba(3, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a3': f'0b{int2ba(34, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#3': f'0b{int2ba(3, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b3': f'0b{int2ba(36, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    ''
    'c4': f'0b{int2ba(37, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#4': f'0b{int2ba(3, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd4': f'0b{int2ba(39, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#4': f'0b{int2ba(4, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e4': f'0b{int2ba(41, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f4': f'0b{int2ba(42, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#4': f'0b{int2ba(4, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g4': f'0b{int2ba(44, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#4': f'0b{int2ba(4, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a4': f'0b{int2ba(46, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#4': f'0b{int2ba(4, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b4': f'0b{int2ba(48, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',

    'c5': f'0b{int2ba(49, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#5': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd5': f'0b{int2ba(51, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#5': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e5': f'0b{int2ba(53, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f5': f'0b{int2ba(54, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#5': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g5': f'0b{int2ba(56, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#5': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a5': f'0b{int2ba(58, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#5': f'0b{int2ba(5, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b5': f'0b{int2ba(60, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',

    'c6': f'0b{int2ba(61, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#6': f'0b{int2ba(6, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd6': f'0b{int2ba(63, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#6': f'0b{int2ba(6, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e6': f'0b{int2ba(65, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f6': f'0b{int2ba(66, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#6': f'0b{int2ba(6, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g6': f'0b{int2ba(68, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#6': f'0b{int2ba(6, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a6': f'0b{int2ba(70, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#6': f'0b{int2ba(7, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b6': f'0b{int2ba(72, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',

    'c7': f'0b{int2ba(73, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'c#7': f'0b{int2ba(7, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd7': f'0b{int2ba(75, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'd#7': f'0b{int2ba(7, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'e7': f'0b{int2ba(77, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f7': f'0b{int2ba(78, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'f#7': f'0b{int2ba(7, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g7': f'0b{int2ba(80, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'g#7': f'0b{int2ba(8, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a7': f'0b{int2ba(82, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'a#7': f'0b{int2ba(8, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
    'b7': f'0b{int2ba(84, length=TONE_LENGTH, endian=TONE_ENDIAN).to01()}',
}
