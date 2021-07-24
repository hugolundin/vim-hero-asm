# vim-hero-asm

*vim-hero-asm is an assembler targeting the custom computer architecture that me and my team constructed in [TSEA83](https://www.isy.liu.se/edu/kurs/TSEA83/) at Linköping University.*

## Features

- Machine code generator (of course 😅). 
- VHDL generator
    - Will automatically create VHDL packages for the program and data memory that can be imported in VHDL code. 
    - The generated VHDL is annotated with original instruction, labels and line number.
    - The generated binary code is formatted according to the current instruction format. For example, if an instruction takes two registers with 5 bit addresses, they will be separated for readability: `..._10010_10010`.
- Constants
    - Supports binary, hexadecimal and decimal constants. 
    - Dependency resolution at compile-time, allowing constants to be aliases for other constants (basically infinite nesting supported).  
    - Example: `.constant NAME0 0x100`
    - There are pre-defined constants for all I/O-addresses. 
- Register aliases
    - Example: `.alias ZERO r0`
- Pointers to data placed in the data memory
    - By using `.data <name> <value>`, the value will be placed in the data memory and the name will be a constant containing the address in the data memory. 
    - Reading from a file: `.data PTR0 "memory.hex"`.
    - Reading a value: `.data PTR1 5`
- Expression evaluation
    - Mathematical expressions are evaluated everywhere they can be used. For example when defining constants or when an instruction takes an immediate.
- Automatic calculation of relative jumps
    - If the user writes `jmpi <label>` it will be converted to `line(current) - line(label)`. Negative jumps are automatically converted to two's complement.

## Usage

For flags, see the argument parser in `src/main.py`. 

```bash
$ python3 main.py ../examples/main.asm
```

## Credits

I would like to thank Henrik Åkesson, Adam Sundberg and Ilja Müller Rasmussen for being awesome (and for writing `docs/instructions.pdf` so that I didn't have to ❤️). 