import logging
from machine_code import MachineCodeBuilder

def remove_whitespace(builder: MachineCodeBuilder, lines: list[str]) -> (MachineCodeBuilder, list[str]):
    logging.debug('Removing whitespace...')

    if not lines:
        return (builder, lines)

    return (builder, lines)
