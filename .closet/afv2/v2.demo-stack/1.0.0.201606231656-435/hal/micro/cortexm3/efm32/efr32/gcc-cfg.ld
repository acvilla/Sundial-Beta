/* GCC linker configuration file.                                             */
/*                                                                            */
/* THIS IS A GENERATED FILE.  DO NOT EDIT.                                    */
/*                                                                            */
/* Copyright 2015 Silicon Laboratories, Inc.                               *80*/
/*----------------------------------------------------------------------------*/

/* Memory map for the EFR32 */
MEMORY {
  flash (rx) : ORIGIN = 0x00000000, LENGTH = 0x00040000
  ram  (rwx) : ORIGIN = 0x20000000, LENGTH = 0x00008000
}

/* Default to 256k Flash and 32K Ram */
FLASH_SIZE = DEFINED(FLASH_SIZE) ? FLASH_SIZE : 256K;
RAM_SIZE = DEFINED(RAM_SIZE) ? RAM_SIZE : 32K;

/* Create useful defines for the gcc.ld file to use */
RAM_BOTTOM          = 0x20000000;
RAM_TOP             = RAM_BOTTOM + RAM_SIZE - 1;

MFB_BOTTOM          = 0x00000000;
MFB_TOP             = MFB_BOTTOM + FLASH_SIZE - 1;

/* The FIB does not exist on the EFM32 */
FIB_BOTTOM          = 0xFFFFFFFF;
FIB_TOP             = 0xFFFFFFFF;

FLASH_PAGE_SIZE     = 0x00000800;
WRITE_PROTECT_SIZE  = 4;
DEFAULT_BTL_SIZE    = FLASH_PAGE_SIZE * WRITE_PROTECT_SIZE;

/* If we were given a RAM_RETAIN_SIZE then make sure that we don't use */
/* any RAM outside of that range by setting it to be in the unused region. */
UNUSED_RAM_SIZE = DEFINED(RAM_RETAIN_SIZE) ? (RAM_TOP - RAM_BOTTOM + 1 - RAM_RETAIN_SIZE): 0;

/* Include the common gcc.ld linker script */
INCLUDE "gcc.ld"
