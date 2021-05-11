library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package program is
    type program_t is array(0 to 1023) of unsigned(31 downto 0);

    constant program_c: program_t := (

        -- 0: addi r1, r2, 5
        b"001011_00001_00010_0000000000000101",

        others => (others => '0')
    );
end program;
