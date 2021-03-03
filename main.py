from assembler import Assembler2
import argparse
import logging
import sys

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

    args = parser.parse_args()
    
    # If neither verbose mode or debug mode are used, the default
    # log level is `logging.WARNING`.  
    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=args.level)

    asm = assembler.Assembler()
    asm.assemble('hello')
    
    # TODO: Take another argument, the assembly file
    # to generate machine code for.

    # TODO: Read the contents of the file and pass it to
    # some function in the `assembly` module. 
