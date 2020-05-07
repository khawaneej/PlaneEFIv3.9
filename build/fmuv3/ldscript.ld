/* generated ldscript.ld */
MEMORY
{
    flash : org = 0x08004000, len = 2032K
    ram0  : org = 0x20000000, len = 192k
}

INCLUDE common.ld
