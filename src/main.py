from pathlib import Path
import argparse
import logging
import sys

from utilities import describe_data, error, warning, info
from assembler import Assembler, AssemblyException

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
        '-a', '--assemble',
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

    assembler = Assembler()

    try:
        data = assembler.assemble(args.file.read().split('\n'))
    except Exception as e:
        error(str(e))

    destination = f'{Path(args.file.name).stem}.dat'

    if not args.assemble:        
        if args.stdout:
            sys.stdout.buffer.write(data)
        else:
            with open(destination, 'wb') as output:
                output.write(data)

            logging.debug(f'Wrote {describe_data(data)} to {destination}')
