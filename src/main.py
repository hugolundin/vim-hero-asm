from pathlib import Path
import argparse
import logging
import sys
import os

from utilities import describe_data, error, warning, info
from assembler import Assembler, AssemblyException
import vhdl

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
        '--vhdl',
        help='Assemble the file and write the result as a vhdl array.',
        action='store_true')

    parser.add_argument(
        'file',
        help='File to assemble')

    args = parser.parse_args()
    assembler = Assembler(args.file)
    program, data = assembler.assemble()
    
    program_destination = f'{Path(args.file).stem}.program'
    data_destination = f'{Path(args.file).stem}.data'

    if not args.assemble:
        if args.stdout:
            sys.stdout.buffer.write(program)

            if len(data) > 0:
                sys.stdout.buffer.write(data)
        else:
            if args.vhdl:
                with open('program.vhd', 'w') as output:
                    output.write(vhdl.generate_program(assembler.parser, program))

                if len(data) > 0:
                    with open('data.vhd', 'w') as output:
                        output.write(vhdl.generate_data(data))
            else:
                with open(program_destination, 'wb') as output:
                    output.write(program.tobytes())
                    logging.debug(f'Wrote {describe_data(program)} to {program_destination}')

                if len(data) > 0:
                    with open(data_destination, 'wb') as output:
                        output.write(data.tobytes())
                        logging.debug(f'Wrote {describe_data(data)} to {data_destination}')
