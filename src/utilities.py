import sys

def description(data):
    length = len(data.tobytes())

    if length == 1:
        return f'1 byte'

    return f'{length} bytes'