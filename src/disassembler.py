from bitarray import bitarray
from pathlib import Path
import argparse
import logging
import sys

from architecture import instructions

def get_op(op_code):
    for key, value in instructions.items():
        if value.op == op_code:
            return key
        
    return 'unknown'

def disassemble(instruction):
    b = bitarray()
    b.frombytes(instruction)

    print(get_op(b[:6]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file',
        help='File to assemble',
        type=argparse.FileType('rb'))

    args = parser.parse_args()

    while instruction := args.file.read(4):
        disassemble(instruction)

