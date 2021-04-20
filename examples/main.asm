.include "constants.asm"
.include "init.asm"

loop:
    dec r1
    cmpi r1, END_VALUE
    bneq loop
end:
    halt
