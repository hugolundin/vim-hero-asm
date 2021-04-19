.include "constants.asm"
.include "init.asm"

loop:
    subi r1, r1, SUB_VALUE
    cmpi r1, END_VALUE
    bneq loop
end:
    halt
