from pathlib import Path
import argparse
import logging
import sys
import os

from bitarray import bitarray
from architecture import INSTRUCTIONS, REGISTERS

class Disassembler:
    def __init__(self):
        self.result = ''

    def disassemble(self, name) -> str:
        data = self.load(name)

        print(data)

        return self.result

    def load(self, name):
        with open(name, 'rb') as f:
            b = bitarray()
            return b.fromfile(f).to01()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a', '--disassemble',
        help='Assemble the project without writing the produced result to disk.',
        action='store_true')

    parser.add_argument(
        '-s', '--stdout',
        help='Disassemble the file and print the result to stdout.',
        action='store_true')

    parser.add_argument(
        'file',
        help='File to disassemble')

    args = parser.parse_args()
    disassembler = Disassembler()
    result = disassembler.disassemble(args.file)
    destination = f'{Path(args.file).stem}.txt'

    if not args.disassemble:
        if args.stdout:
            print(result)
        else:
            with open(destination, 'w') as output:
                output.write(result)
