import sys
import colorama

def describe_data(data):
    length = len(data)

    if length == 1:
        return f'1 byte'

    return f'{length} bytes'

def message(title, msg, color):
    print(f'{color}{title}: {colorama.Style.RESET_ALL}{msg}')

def info(msg):
    message('Info', msg, colorama.Fore.GREEN)

def warning(msg):
    message('Warning', msg, colorama.Fore.YELLOW)

def error(msg):
    message('Error', msg, colorama.Fore.RED)
