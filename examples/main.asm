
.constant END_VALUE 25

loop:
    subi r1, r0, 1
    cmpi r1, END_VALUE
    bneq loop
end:
    halt
