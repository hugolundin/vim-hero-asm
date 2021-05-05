movhi r1, b"0000000000010000"
subi r1, r1, 1
cmpi r1, 0
bneq -3
addi r2, r0, b"0000000011111111"
str r0, r2, 1024
movhi r1, b"0000000000010000"
subi r1, r1, 1
cmpi r1, 0
bneq -3
add r2, r0, r0
str r0, r2, 1024
jmp r0, 0
