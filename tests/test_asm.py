import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))

import inspect
import tempfile
from bitarray import bitarray
from assembler import Assembler

def verify(program, machine_code, debug=False):
    """Verify that the given program assembles to the given machine code."""

    # Because the assembler expects a file path, we create a temporary file
    # and write the program to it.
    fd, path = tempfile.mkstemp()

    with os.fdopen(fd, 'w') as f:
        f.write(program)

    assembler = Assembler(path)
    data = bitarray()
    data.frombytes(assembler.assemble())

    if debug:
        print(f'Instructions: {assembler.parser.instructions}')
        print(f'Constants: {assembler.parser.constants}')
        print(f'Aliases: {assembler.parser.aliases}')

    # Go through and check that every 32 bits corresponds to the
    # given machine code. 

    for index, binary in enumerate(machine_code):
        lower = index * 32
        upper = (index + 1) * 32
        assert data[lower:upper].to01() == binary.replace('_', '')

    # The temporary file that we created is not removed automatically. 
    # We need to unlink it on our own.
    os.unlink(path)

def test_simple():
    program = inspect.cleandoc("""
    addi r1, r0, 1
    nop
    movli r1, 1
    movli r2, 2
    movli r3, 3
    str r0, r1, 1
    str r0, r2, 2
    str r0, r3, 3
    ld r1, r2, 0
    addi r3, r1, 0
    cmpi r10, 5
    beq 5
    jmp r0, 9
    """)

    machine_code = [
        '001011_00001_00000_0000000000000001',
        '00000000000000000000000000000000',
        '000101_00001_0000000000000001_00000',
        '000101_00010_0000000000000010_00000',
        '000101_00011_0000000000000011_00000',
        '000010_00000_00000_00001_00000000001',
        '000010_00000_00000_00010_00000000010',
        '000010_00000_00000_00011_00000000011',
        '000001_00001_00010_0000000000000000',
        '001011_00011_00001_0000000000000000',
        '100100_00000_01010_0000000000000101',
        '101000_00000000000000000000000101',
        '101110_00000_00000_0000000000001001'
    ]

    verify(program, machine_code)

def test_label():
    program = inspect.cleandoc("""
        nop
        nop
    MAIN:
        addi r1, r0, 1
        jmpi MAIN
    """)

    machine_code = [
        '00000000000000000000000000000000',
        '00000000000000000000000000000000',
        '001011_00001_00000_0000000000000001',
        '101111_11111111111111111111111110'
    ]

    verify(program, machine_code, debug=True)

def test_constant_expression():
    program = inspect.cleandoc("""
    
    addi r0, r1, 0
    """)

    machine_code = []

    verify(program, machine_code)