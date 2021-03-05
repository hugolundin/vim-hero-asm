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
        '-c', '--check',
        help='Assemble the file without writing it to disk.',
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
        data = assembler.assemble(args.file.readlines())
        destination = f'{Path(args.file.name).stem}.dat'

        description = 'byte' if len(data) == 1 else 'bytes'
        logging.debug(f'Writing {len(data)*4} {description} to {destination}')

        if args.check:
            logging.debug(f'{data}')
        else:
            with open(destination, 'wb') as output:
                for byte in data:
                    output.write(byte)         

    except Exception as e:
        logging.error(e)
