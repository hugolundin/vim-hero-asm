import sys
import colorama

def describe_data(data):
    length = len(data)

    if length == 1:
        return f'1 byte'

    return f'{length} bytes'

def error(title, message):
    print(f'{colorama.Fore.RED}{title}: {colorama.Style.RESET_ALL} {message}')
    exit(1)
