library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package program is
    type program_t is array(0 to 1023) of unsigned(31 downto 0);

    constant program_c: program_t := (

        -- 0 [START]: movli REG_WITH_ONE, 1
        b"000101_00001_0000000000000001_00000",

        -- 1: str ZERO, REG_WITH_ONE, SPRITE_REGISTER_TICK_ADDRESS
        b"000010_00000_00000_00001_10000000101",

        -- 2: str ZERO, ZERO, SPRITE_REGISTER_TICK_ADDRESS
        b"000010_00000_00000_00000_10000000101",

        -- 3: addi r2, r2, 1
        b"001011_00010_00010_0000000000000001",

        -- 4: cmpi r2, 64
        b"100100_00000_00010_0000000001000000",

        -- 5: beq LOAD_SPRITE
        b"101000_00000000000000000000001000",

        -- 6: nop 
        b"000000_00000000000000000000000000",

        -- 7 [SLEEP]: movhi SLEEP_REG, SLEEP_DURATION
        b"000100_11110_1010101110010110_00000",

        -- 8: subi SLEEP_REG, SLEEP_REG, 1
        b"001101_11110_11110_0000000000000001",

        -- 9: cmpi SLEEP_REG, 0
        b"100100_00000_11110_0000000000000000",

        -- 10: bneq SLEEP
        b"101001_11111111111111111111111100",

        -- 11: nop 
        b"000000_00000000000000000000000000",

        -- 12: jmpi START, 0
        b"101111_11111111111111111111110011",

        -- 13: nop 
        b"000000_00000000000000000000000000",

        -- 14 [LOAD_SPRITE]: mov r2, ZERO
        b"000011_00010_00000_0000000000000000",

        -- 15: str ZERO, REG_WITH_ONE, SPRITE_REGISTER_DATA_ADDRESS
        b"000010_00000_00000_00001_10000000110",

        -- 16: str ZERO, ZERO, SPRITE_REGISTER_DATA_ADDRESS
        b"000010_00000_00000_00000_10000000110",

        -- 17: jmpi START, 0
        b"101111_11111111111111111111101110",

        -- 18: nop 
        b"000000_00000000000000000000000000",

        others => (others => '0')
    );
end program;
