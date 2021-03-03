from pathlib import Path
import argparse
import logging
import sys

from assembler import Assembler

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
        data = assembler.assemble(args.file.readlines())
        destination = f'{Path(args.file.name).stem}.dat'

        with open(destination, 'wb') as output:
            for byte in data:
                output.write(byte)
            
            description = 'byte' if len(data) == 0 else 'bytes'
            logging.debug(f'Writing {len(data)*4} {description} to {destination}')

    except Exception as e:
        logging.error(e)
    