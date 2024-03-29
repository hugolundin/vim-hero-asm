.alias REG_WITH_ONE r1
.alias RETURN r29
.alias SLEEP_REG r30

.constant SLEEP_DURATION -0b101010001_10_1010

START:
    movli REG_WITH_ONE, 1

    str ZERO, REG_WITH_ONE, SPRITE_REGISTER_TICK_ADDRESS
    str ZERO, ZERO, SPRITE_REGISTER_TICK_ADDRESS

    addi r2, r2, 1
    cmpi r2, 64
    beq LOAD_SPRITE
    nop

SLEEP:
    movhi SLEEP_REG, SLEEP_DURATION ; this is a comment
    subi SLEEP_REG, SLEEP_REG, 1
    cmpi SLEEP_REG, 0
    bneq SLEEP
    nop
    jmpi START, 0
    nop

LOAD_SPRITE:
    mov r2, ZERO
    str ZERO, REG_WITH_ONE, SPRITE_REGISTER_DATA_ADDRESS
    str ZERO, ZERO, SPRITE_REGISTER_DATA_ADDRESS
    jmpi START, 0
    nop
