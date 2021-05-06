library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package program is
    type program_t is array(0 to 1023) of unsigned(31 downto 0);

    constant program_c: program_t := (

        -- 0: nop 
        b"000000_00000000000000000000000000",

        -- 1: nop 
        b"000000_00000000000000000000000000",

        -- 2: nop 
        b"000000_00000000000000000000000000",

        -- 3: addi r0, r0, YOLO
        b"001011_00000_00000_0000000000000110",

        -- 4: nop 
        b"000000_00000000000000000000000000",

        -- 5: nop 
        b"000000_00000000000000000000000000",

        -- 6 [YOLO]: nop 
        b"000000_00000000000000000000000000",

        others => (others => '0')
    );
end program;
