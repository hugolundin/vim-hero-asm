start:
    ldi r0, 5
loop:
    dec r0
    cmpi r0, 0
    breq loop
end:
    ldi r1, 1
