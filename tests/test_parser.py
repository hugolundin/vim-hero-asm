from src.parser import Parser

parser = Parser()

def test_simple():
    line = 'ldi r0, 5 + 5'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ldi')
    assert(parsed_line.label == None)
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == '5 + 5')
    
    line = 'ldi r0, 5+5'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ldi')
    assert(parsed_line.label == None)
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == '5+5')

    line = 'ld r0, r1'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ld')
    assert(parsed_line.label == None)
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == 'r1')

def test_with_comment():
    line = 'nop # hello world'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'nop')
    assert(parsed_line.label == None)
    assert(len(parsed_line.args) == 0)

def test_with_label():
    line = 'start: nop'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'nop')
    assert(len(parsed_line.args) == 0)
    assert(parsed_line.label == 'start')

def test_with_comment_and_label():
    line = 'start: nop # hello world'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'nop')
    assert(len(parsed_line.args) == 0)
    assert(parsed_line.label == 'start')

def test_with_comment_and_args():
    line = 'ldi r0, 0x5 # hello world'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ldi')
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == '0x5')
    
def test_with_label_and_args():
    line = 'start: ldi r0, 0x5'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ldi')
    assert(parsed_line.label == 'start')
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == '0x5')

def test_with_comment_label_and_args():
    line = 'start: ldi r0, 0x5 # hello world'
    parsed_line = parser.parse(line)
    assert(parsed_line.op == 'ldi')
    assert(parsed_line.label == 'start')
    assert(len(parsed_line.args) == 2)
    assert(parsed_line.args[0] == 'r0')
    assert(parsed_line.args[1] == '0x5')
