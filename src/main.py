from pathlib import Path
import argparse
import logging
import sys

from assembler import Assembler, AssemblyError
from architecture import registers, instructions

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-v', '--verbose',
        help='Show verbose output',
        action='store_const', dest='level', const=logging.INFO)

    parser.add_argument(
        '-d', '--debug',
        help='Show debug output.',
        action='store_const', dest='level', const=logging.DEBUG)

    parser.add_argument(
        '-c', '--check',
        help='Assemble the project without writing the produced result to disk.',
        action='store_true')

    parser.add_argument(
        '-s', '--stdout',
        help='Assemble the file and print the result to stdout.',
        action='store_true')

    parser.add_argument(
        'file',
        help='File to assemble',
        type=argparse.FileType('r', encoding='UTF-8'))

    args = parser.parse_args()

    # If neither verbose mode or debug mode are used, the default
    # log level is `logging.WARNING`.  
    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=args.level)

    assembler = Assembler(registers, instructions)
    data = assembler.assemble(args.file.readlines())
    destination = f'{Path(args.file.name).stem}.dat'

    if not args.check:
        if args.stdout:
            sys.stdout.buffer.write(data)
        else:
            description = 'byte' if len(data) == 1 else 'bytes'
            logging.debug(f'Writing {len(data)} {description} to {destination}')

            with open(destination, 'wb') as output:
                output.write(data)

