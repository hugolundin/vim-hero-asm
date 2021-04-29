import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../src"))

from bitarray import bitarray
from assembler import Assembler

def test_program1():
    assembler = Assembler('tests/program1.asm')
    data = bitarray()
    data.frombytes(assembler.assemble())
    
    assert data[0:31].to01() == '00101100001000000000000000000001'
    