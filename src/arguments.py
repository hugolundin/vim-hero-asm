from arch import REGISTERS

def register(argument, result):
    if coding := REGISTERS.get(argument):
        result.extend(coding)