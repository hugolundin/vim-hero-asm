library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package program is
    type program_t is array(0 to 1023) of unsigned(31 downto 0);

    constant program_c: program_t := (

        others => (others => '0')
    );
end program;
