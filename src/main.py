from pathlib import Path
import argparse
import logging
import sys
import os

from utilities import describe_data, error, warning, info
from assembler import Assembler, AssemblyException

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a', '--assemble',
        help='Assemble the project without writing the produced result to disk.',
        action='store_true')

    parser.add_argument(
        '-s', '--stdout',
        help='Assemble the file and print the result to stdout.',
        action='store_true')

    parser.add_argument(
        'file',
        help='File to assemble')

    args = parser.parse_args()
    assembler = Assembler()
    data = assembler.assemble(args.file)
    destination = f'{Path(args.file).stem}.dat'

    if not args.assemble:        
        if args.stdout:
            sys.stdout.buffer.write(data)
        else:
            with open(destination, 'wb') as output:
                output.write(data)

            logging.debug(f'Wrote {describe_data(data)} to {destination}')
