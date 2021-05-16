from architecture import get_instr_def, REG, IMM11, IMM16, IMM26, PAD5, INSTRUCTIONS
import inspect

def format_args(args):
    result = ''
    separator = ''

    for arg in args:
        result += f'{separator}{arg}'
        separator = ', '

    return result

def get_line_name(parser, index):
    for label, line in parser.labels.items():
        if line == index:
            return f'{index} [{label.upper()}]'

    return f'{index}'

def generate_program(parser, data):
    result = inspect.cleandoc("""
    library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;

    package program is
    """)

    result += "\n    type program_t is array(0 to 1023) of unsigned(31 downto 0);\n\n"
    result += '    constant program_c: program_t := (\n\n'

    for index, instruction in enumerate(parser.instructions):
        offset = index * 32
        result += f'        -- {get_line_name(parser, index)}: {instruction.name} {format_args(instruction.args)}\n        b"'

        result += f'{data[offset:offset+6].to01()}'
        offset += 6

        for d in get_instr_def(INSTRUCTIONS, instruction.name)['format']:
            if d == REG:
                result += f'_{data[offset:offset+5].to01()}'
                offset += 5
            elif d == IMM11:
                result += f'_{data[offset:offset+11].to01()}'
                offset += 11
            elif d == IMM16:
                result += f'_{data[offset:offset+16].to01()}'
                offset += 16
            elif d == IMM26:
                result += f'_{data[offset:offset+26].to01()}'
                offset += 26
            elif d == PAD5:
                result += f'_{data[offset:offset+5].to01()}'
                offset += 5

        padding = ((index + 1) * 32) - offset
        if padding > 0:
            result += f'_{data[offset:offset+padding].to01()}'

        result += f'",\n\n'

    result += "        others => (others => '0')\n    );\nend program;\n"
    return result

def get_index_name(parser, index):
    for label, line in parser.data_labels.items():
        if line == index:
            return f'{index} [{label.upper()}]'

    return f'{index}'


def generate_data(parser, data):
    result = inspect.cleandoc("""
    library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;

    package data is
    """)

    result += "\n    type data_memory_t is array(0 to DATA_MEMORY_SIZE-1) of unsigned (31 downto 0);\n\n"
    result += '    constant data_memory_c: data_memory_t := (\n\n'

    for i in range(len(parser.data)):
        result += f'        -- {get_index_name(parser, i)}: {parser.data[i]}\n'

        # TODO: Fix...
        result += f'        b"{data[i * 31: i * 31 + 7].to01()}'
        result += f'_{data[(i * 32) + 9: (i * 32) + 17].to01()}'
        result += f'_{data[(i * 32) + 18: (i *32) + 26].to01()}'
        result += f'_{data[(i * 32) + 23: (i * 32) + 31].to01()}'
        result += '",\n\n'

        print(result)

    result += "        others => (others => '0')\n    );\nend data;\n"
    return result
