from src.assembler import Assembler

def test_tokenizer():
    assembler = Assembler()

    lines = ['ldi r0, 5 + 5']
    tokens = assembler.tokenize(lines)
    assert(tokens == ['ldi', 'r0', '5 + 5'])
    
    lines = ['ldi r0, 5+5']
    tokens = assembler.tokenize(lines)
    assert(tokens == ['ldi', 'r0', '5+5'])

    lines = ['ldi r0, r1']
    tokens = assembler.tokenize(lines)
    assert(tokens == ['ld', 'r0', 'r1'])
