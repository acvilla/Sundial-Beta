;-------------------------------------------------------------------------------
;                           Silicon Laboratories, Inc.
;                                Copyright 2010
;                          CONFIDENTIAL & PROPRIETARY
;-------------------------------------------------------------------------------
;
;     AUTHOR:   Martin Pechanec
;     DATE:     April 20, 2010, Tuesday
;     FILE:     si4010_diff.inc
;
;     File:     $URL: svn+ssh://svn.silabs.com/si6110/trunk/firmware/cust/si4010/common/diff/si4010_diff.inc $
;     Id:       $Id: si4010_diff.inc 4992 2010-06-18 19:07:10Z mapechan $
;     Author:   $Author: mapechan $
;     Version:  $Revision: 4992 $
;     Date:     $Date: 2010-06-18 12:07:10 -0700 (Fri, 18 Jun 2010) $
;
;---------------------------------------------------------------------------
;
;     DESCRIPTION:
;       This file is to be compiled and linked into builds which intend
;       to use ROM release 2.0 (revB).
;
;       Include file Keil and Raisonance assemblers as well as others,
;       ASM-51 compatible, assemblers.
;
;       This file is a difference file between the Si4010 user headers
;       and the development Si6110 full headers. Include this header
;       when using user application Si4010 headers to get the full
;       Si6110 development behavior.
;
;       Use $INCLUDE directives:
;
;         $INCLUDE (si4010.inc)
;         $INCLUDE (si4010_diff.inc)
;
;       Add this lines at the beginning of any of source files.
;
;       For each single bit field withing a register there is a mask
;       M_<field> and bit index defintion B_<field> defined.
;
;       For multiple bit fields there is only a mask defined.
;
;       If the register contains a single field occupying the
;       whole register width (8 bit field in 8 bit register),
;       the mask is not defined.
;
;---------------------------------------------------------------------------
;
;     DATA DECLARATIONS:
;

; >---- ROM and DPRAM beginnings and lengths -----------------------------

ROM_LEN         EQU     03000H
ROM_BEG         EQU     08000H
ROM_END         EQU     (ROM_BEG + ROM_LEN - 1)

; Alias to be compatible with RTL
PROM_LEN        EQU     ROM_LEN
PROM_BEG        EQU     ROM_BEG
PROM_END        EQU     ROM_END

DPRAM_LEN       EQU     01200H
DPRAM_BEG       EQU      0000H
DPRAM_END       EQU     (DPRAM_BEG + DPRAM_LEN - 1)

XREG_LEN        EQU      0100H
XREG_BEG        EQU     04000H
XREG_END        EQU     (XREG_BEG + XREG_LEN - 1)

MC_IRAM_LEN     EQU      0100H
MC_IRAM_BEG     EQU     07000H
MC_IRAM_END     EQU     (MC_IRAM_BEG + MC_IRAM_LEN - 1)

MC_NVM_LEN      EQU     02000H
MC_NVM_BEG      EQU     0e000H
MC_NVM_END      EQU     (MC_NVM_BEG + MC_NVM_LEN - 1)

; >-- MC commands
MC_CMD_IDLE        EQU  00000000B
MC_CMD_INC_ADDR    EQU  00000001B
MC_CMD_READ        EQU  00000010B
MC_CMD_NVM_ENA     EQU  00000110B
MC_CMD_NVM_ENA_RD  EQU  00000111B
MC_CMD_NVM_DIS     EQU  00000101B
MC_CMD_CLEAR       EQU  00000100B

; >-- BOOT_FLAGS and PROT3_CTRL boot loader software bits

; -- BOOT_FLAGS software bits
B_COPY_FLAG_POR EQU     7       ; revB

M_COPY_FLAG_POR EQU     01H SHL B_COPY_FLAG_POR    ; revB

; -- PROT3_CTRL software bits
B_TRIM_CALL_DIS EQU     0
B_USER_CONT     EQU     1       ; revB
B_BOOT_XO_ENA   EQU     4       ; revB
B_MEM_C2_PROT   EQU     5
B_MTP_C2_PROT   EQU     6
B_NVM_C2_PROT   EQU     7

M_TRIM_CALL_DIS EQU     01H SHL B_TRIM_CALL_DIS
M_USER_CONT     EQU     01H SHL B_USER_CONT        ; revB
M_BOOT_XO_ENA   EQU     01H SHL B_BOOT_XO_ENA      ; revB
M_MEM_C2_PROT   EQU     01H SHL B_MEM_C2_PROT
M_MTP_C2_PROT   EQU     01H SHL B_MTP_C2_PROT
M_NVM_C2_PROT   EQU     01H SHL B_NVM_C2_PROT


; >---- SFR byte registers -------------------------------------------------

BAND_CTRL       DATA  095H
CPNVM_CTRL      DATA  096H
TS_CTRL         DATA  097H
SPI_CTRL        DATA  098H
REG_CTRL        DATA  09AH
DAC_DATA        DATA  0A1H
DAC_CTRL        DATA  0A2H
TST_CTRL        DATA  0A3H
DSRH            DATA  0B4H
I2C_CTRL        DATA  0C0H
I2C_DATA        DATA  0C1H
LCM_DATAL       DATA  0C2H
LCM_DATAH       DATA  0C3H
HVRAM_CTRL      DATA  0C4H
HVRAM_DATA      DATA  0C5H
DMD_DATAL       DATA  0C6H
DMD_DATAH       DATA  0C7H
UCHTIM_CTRL     DATA  0CFH
MC_ADDRL        DATA  0D1H
MC_ADDRH        DATA  0D2H
MC_CMD          DATA  0D3H
MC_CTRL         DATA  0D4H
MC_WDATA        DATA  0D5H
MC_RDATA        DATA  0D6H
NVM_CTRL        DATA  0D8H
NVM_SET         DATA  0D9H
PROT1_CTRL      DATA  0DBH
PROT2_CTRL      DATA  0DCH
BOOT_CTRL       DATA  0DEH
NVM_LOCK        DATA  0DFH
SER_CFG         DATA  0E1H
SPI_DATA        DATA  0E2H
SPI_STAT        DATA  0E3H
DMD_CTRL        DATA  0E5H
EIE2            DATA  0E7H
MTP_CTRL        DATA  0E8H
MTP_SET         DATA  0E9H
ROM_CONST_PAGE  DATA  0EAH
ROM_BOOT_PAGE   DATA  0EBH
ROM_DSR_PAGE    DATA  0ECH
SYS_STAT        DATA  0EFH
BP_EN           DATA  0F1H
BP_PATCH        DATA  0F2H
BP_ADDR         DATA  0F3H
BPL             DATA  0F4H
BPH             DATA  0F5H
EIP2            DATA  0F7H
DSRFLG          DATA  0F8H
DSROP           DATA  0F9H
DSR_CTRL        DATA  0FFH


; >---- XREG (XDATA) registers ---------------------------------------------

bBAND_TRIM        XDATA  04000H
bCPNVM_CLIP       XDATA  04001H
bCHOSC_TRIM       XDATA  04002H
bCHOSC_TST        XDATA  04003H
bLDO_TRIM         XDATA  04004H
bLDO_REF_SEL      XDATA  04005H
bLDO_TST          XDATA  04006H
bPA_PD_OFFSET     XDATA  0400EH
bPA_PD_GEARSHIFT  XDATA  0400FH
bPA_TST           XDATA  04010H
bPA_COMP_SEL      XDATA  04011H
bMPLL_CONF        XDATA  04013H
bMPLL_TRIM        XDATA  04014H
bMPLL_TST         XDATA  04015H
bCPNVM_TST        XDATA  04018H
bTS_SET           XDATA  04019H
bTS_TST           XDATA  0401AH
wHEAT_POWER       XDATA  0401BH
bLC_DCT           XDATA  0401DH
bLC_COARSE        XDATA  0401EH
bLC_SET           XDATA  0401FH
bLC_DIVIDER       XDATA  04020H
bMTP_ATB          XDATA  04021H
bMTP_TMS          XDATA  04022H
bTEST_MUX         XDATA  04023H
bDEV_ID           XDATA  04024H
bREV_ID           XDATA  04025H
bDERIV_ID         XDATA  04026H
abXREG_NVM_PACK   XDATA  04080H

;---------------------------------------------------------------------------
;
;     CONSTANTS:
;

; >---- SFR bit masks ------------------------------------------------------

; -- BAND_CTRL .. 0x95
M_BAND_EN_VPHREF      EQU  00000001B
M_BAND_FRCI           EQU  00000010B
M_BAND_SNSV           EQU  00000100B
M_BAND_ENA            EQU  10000000B

B_BAND_EN_VPHREF      EQU  0
B_BAND_FRCI           EQU  1
B_BAND_SNSV           EQU  2
B_BAND_ENA            EQU  7

; -- CPNVM_CTRL .. 0x96
M_CPNVM_MODE          EQU  00000011B
M_CPNVM_EN_VPP_MAIN   EQU  00000100B

B_CPNVM_MODE          EQU  0
B_CPNVM_EN_VPP_MAIN   EQU  2

; -- TS_CTRL .. 0x97
M_TS_RANGE            EQU  00000011B
M_TS_POL_ATB          EQU  00000100B
M_TS_NOCHOP           EQU  00001000B
M_DMD_TEMP_POL        EQU  00010000B
M_DMD_HOLD            EQU  00100000B
M_DMD_CLK_SYS         EQU  01000000B

B_TS_RANGE            EQU  0
B_TS_POL_ATB          EQU  2
B_TS_NOCHOP           EQU  3
B_DMD_TEMP_POL        EQU  4
B_DMD_HOLD            EQU  5
B_DMD_CLK_SYS         EQU  6

; -- SPI_CTRL .. 0x98
M_SPICLR              EQU  00000001B
M_RXOVRN              EQU  00000010B
M_WCOL                EQU  00000100B
M_SPIF                EQU  00001000B
M_TXBMT               EQU  00010000B
M_RXBMT               EQU  00100000B
M_SRMT                EQU  01000000B
M_SPIBSY              EQU  10000000B

B_SPICLR              EQU  0
B_RXOVRN              EQU  1
B_WCOL                EQU  2
B_SPIF                EQU  3
B_TXBMT               EQU  4
B_RXBMT               EQU  5
B_SRMT                EQU  6
B_SPIBSY              EQU  7

; -- RBIT_DATA .. 0x99
M_PA_COMPOUT          EQU  00000001B
M_TRNG_OUT            EQU  00000010B

B_PA_COMPOUT          EQU  0
B_TRNG_OUT            EQU  1

; -- REG_CTRL .. 0x9a
M_REG_SFR_CLEAR       EQU  00000001B
M_REG_TEST_CLEAR      EQU  00000010B
M_REG_NVM_CLEAR       EQU  00000100B
M_XREG_LOAD_MASK      EQU  00010000B

B_REG_SFR_CLEAR       EQU  0
B_REG_TEST_CLEAR      EQU  1
B_REG_NVM_CLEAR       EQU  2
B_XREG_LOAD_MASK      EQU  4

; -- DAC_CTRL .. 0xa2
M_DAC_FEN             EQU  00000001B
M_DAC_SEN             EQU  00000010B
M_DAC_SENDIFF         EQU  00000100B
M_DAC_HIZ             EQU  00001000B
M_SH_DRV              EQU  00010000B
M_SH_TRACK            EQU  00100000B

B_DAC_FEN             EQU  0
B_DAC_SEN             EQU  1
B_DAC_SENDIFF         EQU  2
B_DAC_HIZ             EQU  3
B_SH_DRV              EQU  4
B_SH_TRACK            EQU  5

; -- TST_CTRL .. 0xa3
M_TST_SEL             EQU  00001111B
M_TST_SENSEON         EQU  00100000B
M_TST_F2LOCAL         EQU  01000000B
M_TST_F2S             EQU  10000000B

B_TST_SEL             EQU  0
B_TST_SENSEON         EQU  5
B_TST_F2LOCAL         EQU  6
B_TST_F2S             EQU  7

; -- ODS_CTRL .. 0xa9
M_FORCE_MPLL          EQU  00000100B

B_FORCE_MPLL          EQU  2

; -- ODS_WARM1 .. 0xae
M_ODS_WARM_MPLL       EQU  11110000B

B_ODS_WARM_MPLL       EQU  4

; -- I2C_CTRL .. 0xc0
M_SI                  EQU  00000001B
M_ACK                 EQU  00000010B
M_ARBLOST             EQU  00000100B
M_ACKRQ               EQU  00001000B
M_STO                 EQU  00010000B
M_STA                 EQU  00100000B
M_TXMODE              EQU  01000000B
M_BUSY                EQU  10000000B

B_SI                  EQU  0
B_ACK                 EQU  1
B_ARBLOST             EQU  2
B_ACKRQ               EQU  3
B_STO                 EQU  4
B_STA                 EQU  5
B_TXMODE              EQU  6
B_BUSY                EQU  7

; -- HVRAM_CTRL .. 0xc4
M_HVRAM_ADDR          EQU  00000111B
M_HVRAM_WR            EQU  00100000B
M_HVRAM_RD            EQU  01000000B
M_HVRAM_ENA           EQU  10000000B

B_HVRAM_ADDR          EQU  0
B_HVRAM_WR            EQU  5
B_HVRAM_RD            EQU  6
B_HVRAM_ENA           EQU  7

; -- UCHTIM_CTRL .. 0xcf
M_UCHTIM_DIN          EQU  00000001B
M_UCHTIM_SHIFT        EQU  00000010B
M_UCHTIM_TALK         EQU  00000100B
M_UCHTIM_DOUT         EQU  00001000B

B_UCHTIM_DIN          EQU  0
B_UCHTIM_SHIFT        EQU  1
B_UCHTIM_TALK         EQU  2
B_UCHTIM_DOUT         EQU  3

; -- MC_CMD .. 0xd3
M_MC_CMD_TYPE         EQU  00000111B
M_MC_CPU_IDLE         EQU  00010000B
M_MC_CPU_STOP         EQU  00100000B
M_MC_CPU_DIS_USER     EQU  01000000B
M_MC_BUSY             EQU  10000000B

B_MC_CMD_TYPE         EQU  0
B_MC_CPU_IDLE         EQU  4
B_MC_CPU_STOP         EQU  5
B_MC_CPU_DIS_USER     EQU  6
B_MC_BUSY             EQU  7

; -- MC_CTRL .. 0xd4
M_MC_NOAUTOINC        EQU  00000001B
M_MC_RDBURST          EQU  00000010B
M_NVM_BITACC          EQU  00000100B
M_NVM_SHORT           EQU  00001000B
M_IRAM_FORCE          EQU  00010000B

B_MC_NOAUTOINC        EQU  0
B_MC_RDBURST          EQU  1
B_NVM_BITACC          EQU  2
B_NVM_SHORT           EQU  3
B_IRAM_FORCE          EQU  4

; -- NVM_CTRL .. 0xd8
M_NVM_CHIPEN          EQU  00000001B
M_NVM_RST             EQU  00000010B
M_NVM_READ            EQU  00000100B
M_NVM_CLE             EQU  00001000B
M_NVM_DLE             EQU  00010000B
M_NVM_PROG            EQU  00100000B
M_NVM_WRITE           EQU  01000000B
M_NVM_VPPSEL          EQU  10000000B

B_NVM_CHIPEN          EQU  0
B_NVM_RST             EQU  1
B_NVM_READ            EQU  2
B_NVM_CLE             EQU  3
B_NVM_DLE             EQU  4
B_NVM_PROG            EQU  5
B_NVM_WRITE           EQU  6
B_NVM_VPPSEL          EQU  7

; -- NVM_SET .. 0xd9
M_NVM_RTIME           EQU  00001111B
M_NVM_NOVDDLO         EQU  00100000B
M_NVM_NOGRAY          EQU  01000000B
M_NVM_VDDIO_LO        EQU  10000000B

B_NVM_RTIME           EQU  0
B_NVM_NOVDDLO         EQU  5
B_NVM_NOGRAY          EQU  6
B_NVM_VDDIO_LO        EQU  7

; -- PROT1_CTRL .. 0xdb
M_ROM_PROT            EQU  00000111B
M_ROM_BOOT_PROT       EQU  00001000B
M_ROM_PROT_IMMED      EQU  00010000B

B_ROM_PROT            EQU  0
B_ROM_BOOT_PROT       EQU  3
B_ROM_PROT_IMMED      EQU  4

; -- PROT2_CTRL .. 0xdc
M_NVM_TRIM_PROT       EQU  01111111B
M_NVM_TRIM_RD_PROT    EQU  10000000B

B_NVM_TRIM_PROT       EQU  0
B_NVM_TRIM_RD_PROT    EQU  7

; -- BOOT_CTRL .. 0xde
M_C2_ENA              EQU  00000001B
M_C2_ENA_POR          EQU  00000010B
M_PB_ENA              EQU  00000100B
M_PB_LOCK             EQU  00001000B
M_ROM_BOOT_OFF        EQU  00010000B
M_BOOT_DONE           EQU  00100000B
M_C2CLK_VAL           EQU  01000000B

B_C2_ENA              EQU  0
B_C2_ENA_POR          EQU  1
B_PB_ENA              EQU  2
B_PB_LOCK             EQU  3
B_ROM_BOOT_OFF        EQU  4
B_BOOT_DONE           EQU  5
B_C2CLK_VAL           EQU  6

; -- SER_CFG .. 0xe1
M_SEREN               EQU  00000001B
M_SERMODE             EQU  00000010B
M_SERSTATE            EQU  00111100B
M_EXTHOLD             EQU  01000000B

B_SEREN               EQU  0
B_SERMODE             EQU  1
B_SERSTATE            EQU  2
B_EXTHOLD             EQU  6

; -- SPI_STAT .. 0xe3
M_BITCNT              EQU  00000111B
M_SPINSS              EQU  00001000B
M_NSSMD               EQU  00010000B
M_CKPOL               EQU  00100000B
M_CKPHA               EQU  01000000B

B_BITCNT              EQU  0
B_SPINSS              EQU  3
B_NSSMD               EQU  4
B_CKPOL               EQU  5
B_CKPHA               EQU  6

; -- DMD_CTRL .. 0xe5
M_DMD_SPEED           EQU  00000011B
M_DMD_CLEAR           EQU  00000100B
M_DMD_NEW             EQU  00001000B
M_DMD_TCLK_ENA        EQU  00110000B
M_DMD_ENA             EQU  01000000B
M_TS_ENA              EQU  10000000B

B_DMD_SPEED           EQU  0
B_DMD_CLEAR           EQU  2
B_DMD_NEW             EQU  3
B_DMD_TCLK_ENA        EQU  4
B_DMD_ENA             EQU  6
B_TS_ENA              EQU  7

; -- MTP_CTRL .. 0xe8
M_MTP_DIN             EQU  00000001B
M_MTP_DCLK            EQU  00000010B
M_MTP_PROG            EQU  00000100B
M_MTP_STROBE          EQU  00001000B
M_MTP_HV_EN           EQU  00010000B
M_MTP_PRESET_HV       EQU  00100000B
M_MTP_RESET_OUT       EQU  01000000B
M_MTP_DATA_MATCH      EQU  10000000B

B_MTP_DIN             EQU  0
B_MTP_DCLK            EQU  1
B_MTP_PROG            EQU  2
B_MTP_STROBE          EQU  3
B_MTP_HV_EN           EQU  4
B_MTP_PRESET_HV       EQU  5
B_MTP_RESET_OUT       EQU  6
B_MTP_DATA_MATCH      EQU  7

; -- MTP_SET .. 0xe9
M_MTP_DOUT_SEL        EQU  00000001B
M_MTP_POR_DIS         EQU  00000010B
M_MC_MTP_PROT         EQU  00000100B

B_MTP_DOUT_SEL        EQU  0
B_MTP_POR_DIS         EQU  1
B_MC_MTP_PROT         EQU  2

; -- SYS_SET .. 0xee
M_HEAT_ENA            EQU  00000001B
M_HEAT_HIPOW          EQU  00000010B
M_LCM_DIS             EQU  00000100B
M_MCU_AN              EQU  00010000B

B_HEAT_ENA            EQU  0
B_HEAT_HIPOW          EQU  1
B_LCM_DIS             EQU  2
B_MCU_AN              EQU  4

; -- SYS_STAT .. 0xef
M_DBI_ACTIVE          EQU  00000001B
M_ISR_ACTIVE          EQU  00000010B
M_CPU_IDLE            EQU  00010000B
M_CPU_STOP            EQU  00100000B
M_CPU_DIS_USER        EQU  01000000B
M_SYS_BOOT_DONE       EQU  10000000B

B_DBI_ACTIVE          EQU  0
B_ISR_ACTIVE          EQU  1
B_CPU_IDLE            EQU  4
B_CPU_STOP            EQU  5
B_CPU_DIS_USER        EQU  6
B_SYS_BOOT_DONE       EQU  7

; -- DSRFLG .. 0xf8
M_DSR_OUT_RDY         EQU  00000001B
M_DSR_IN_RDY          EQU  00000010B
M_DSR_BP_DBI          EQU  00000100B
M_DSR_FLAG            EQU  00001000B
M_DSR_RMW_FLAG        EQU  00010000B
M_DSR_STROBE_REQ      EQU  00100000B
M_DSR_STROBE_ACK      EQU  01000000B
M_C2_DBI_HALTED       EQU  10000000B

B_DSR_OUT_RDY         EQU  0
B_DSR_IN_RDY          EQU  1
B_DSR_BP_DBI          EQU  2
B_DSR_FLAG            EQU  3
B_DSR_RMW_FLAG        EQU  4
B_DSR_STROBE_REQ      EQU  5
B_DSR_STROBE_ACK      EQU  6
B_C2_DBI_HALTED       EQU  7

; -- DSR_CTRL .. 0xff
M_C2CLK_LO            EQU  00000001B
M_C2CLK_HI            EQU  00000010B
M_PATCH_DBI           EQU  00000100B
M_BREAK_DBI           EQU  00001000B
M_DSR_RAM             EQU  00010000B
M_LED_OFF             EQU  00100000B
M_ROM_DSR             EQU  01000000B
M_NVM_DSR             EQU  10000000B

B_C2CLK_LO            EQU  0
B_C2CLK_HI            EQU  1
B_PATCH_DBI           EQU  2
B_BREAK_DBI           EQU  3
B_DSR_RAM             EQU  4
B_LED_OFF             EQU  5
B_ROM_DSR             EQU  6
B_NVM_DSR             EQU  7


; >---- XREG bit masks -----------------------------------------------------

; -- BAND_TRIM .. 0x4000
M_BAND_VTRIM        EQU  00001111B
M_BAND_ITRIM        EQU  00110000B

B_BAND_VTRIM        EQU  0
B_BAND_ITRIM        EQU  4

; -- LDO_TRIM .. 0x4004
M_LDO_PWR           EQU  00000011B
M_LDO_ITRIM         EQU  00001100B

B_LDO_PWR           EQU  0
B_LDO_ITRIM         EQU  2

; -- MPLL_CONF .. 0x4013
M_MPLL_BYPASS       EQU  00000001B
M_MPLL_SEL_DIV2     EQU  00000010B

B_MPLL_BYPASS       EQU  0
B_MPLL_SEL_DIV2     EQU  1

; -- MPLL_TRIM .. 0x4014
M_MPLL_RES_TRIM     EQU  00001111B
M_MPLL_SPEED        EQU  01110000B

B_MPLL_RES_TRIM     EQU  0
B_MPLL_SPEED        EQU  4

; -- MPLL_TST .. 0x4015
M_MPLL_RST_OVR      EQU  00100000B

B_MPLL_RST_OVR      EQU  5

; -- TS_SET .. 0x4019
M_TS_TRIM           EQU  00000111B
M_TS_VERT           EQU  00001000B

B_TS_TRIM           EQU  0
B_TS_VERT           EQU  3

; -- TS_TST .. 0x401a
M_TS_SNS_VPD        EQU  00000001B
M_TS_SNS_VPA        EQU  00000010B
M_TS_S_BRIDGE       EQU  00000100B
M_TS_S_1P2          EQU  00001000B
M_TS_EN_ATB         EQU  00010000B
M_TS_SNSDIO         EQU  00100000B
M_TS_FRCDIO         EQU  01000000B
M_TS_EN_DIO         EQU  10000000B

B_TS_SNS_VPD        EQU  0
B_TS_SNS_VPA        EQU  1
B_TS_S_BRIDGE       EQU  2
B_TS_S_1P2          EQU  3
B_TS_EN_ATB         EQU  4
B_TS_SNSDIO         EQU  5
B_TS_FRCDIO         EQU  6
B_TS_EN_DIO         EQU  7

; -- LC_SET .. 0x401f
M_LC_VARSIZE        EQU  00000011B
M_LC_REF            EQU  01111100B

B_LC_VARSIZE        EQU  0
B_LC_REF            EQU  2

; -- LC_DIVIDER .. 0x4020
M_LC_DIVN           EQU  00111111B
M_LC_DIV_HS         EQU  01000000B

B_LC_DIVN           EQU  0
B_LC_DIV_HS         EQU  6

; -- MTP_ATB .. 0x4021
M_MTP_SEL3          EQU  00000001B
M_MTP_SENSE23       EQU  00000010B
M_MTP_FORCE23       EQU  00000100B
M_MTP_SENSE1        EQU  00001000B

B_MTP_SEL3          EQU  0
B_MTP_SENSE23       EQU  1
B_MTP_FORCE23       EQU  2
B_MTP_SENSE1        EQU  3

; -- TEST_MUX .. 0x4023
M_TEST_SEL          EQU  00011111B

B_TEST_SEL          EQU  0

; -- DERIV_ID .. 0x4026
M_DERIV_ID_VAR      EQU  00111111B
M_DERIV_ID_FIX      EQU  11000000B

B_DERIV_ID_VAR      EQU  0
B_DERIV_ID_FIX      EQU  6


;---------------------------------------------------------------------------
;
;     BIT VARIABLES:
;

; >---- SFR bit fields -----------------------------------------------------

; -- SPI_CTRL .. 0x98
SPICLR          BIT  SPI_CTRL.B_SPICLR      ; 0x98 .. 0
RXOVRN          BIT  SPI_CTRL.B_RXOVRN      ; 0x99
WCOL            BIT  SPI_CTRL.B_WCOL        ; 0x9a
SPIF            BIT  SPI_CTRL.B_SPIF        ; 0x9b
TXBMT           BIT  SPI_CTRL.B_TXBMT       ; 0x9c
RXBMT           BIT  SPI_CTRL.B_RXBMT       ; 0x9d
SRMT            BIT  SPI_CTRL.B_SRMT        ; 0x9e
SPIBSY          BIT  SPI_CTRL.B_SPIBSY      ; 0x9f .. 7

; -- I2C_CTRL .. 0xc0
SI              BIT  I2C_CTRL.B_SI          ; 0xc0
ACK             BIT  I2C_CTRL.B_ACK         ; 0xc1
ARBLOST         BIT  I2C_CTRL.B_ARBLOST     ; 0xc2
ACKRQ           BIT  I2C_CTRL.B_ACKRQ       ; 0xc3
STO             BIT  I2C_CTRL.B_STO         ; 0xc4
STA             BIT  I2C_CTRL.B_STA         ; 0xc5
TXMODE          BIT  I2C_CTRL.B_TXMODE      ; 0xc6
BUSY            BIT  I2C_CTRL.B_BUSY        ; 0xc7

; -- NVM_CTRL 0xd8
NVM_CHIPEN      BIT  NVM_CTRL.B_NVM_CHIPEN  ; 0xd8
NVM_RST         BIT  NVM_CTRL.B_NVM_RST     ; 0xd9
NVM_READ        BIT  NVM_CTRL.B_NVM_READ    ; 0xda
NVM_CLE         BIT  NVM_CTRL.B_NVM_CLE     ; 0xdb
NVM_DLE         BIT  NVM_CTRL.B_NVM_DLE     ; 0xdc
NVM_PROG        BIT  NVM_CTRL.B_NVM_PROG    ; 0xdd
NVM_WRITE       BIT  NVM_CTRL.B_NVM_WRITE   ; 0xde
NVM_VPPSEL      BIT  NVM_CTRL.B_NVM_VPPSEL  ; 0xdf

; -- MTP_CTRL 0xe8
MTP_DIN         BIT  MTP_CTRL.B_MTP_DIN         ; 0xe8
MTP_DCLK        BIT  MTP_CTRL.B_MTP_DCLK        ; 0xe9
MTP_PROG        BIT  MTP_CTRL.B_MTP_PROG        ; 0xea
MTP_STROBE      BIT  MTP_CTRL.B_MTP_STROBE      ; 0xeb
MTP_HV_EN       BIT  MTP_CTRL.B_MTP_HV_EN       ; 0xec
MTP_PRESET_HV   BIT  MTP_CTRL.B_MTP_PRESET_HV   ; 0xed
MTP_RESET_OUT   BIT  MTP_CTRL.B_MTP_RESET_OUT   ; 0xee
MTP_DATA_MATCH  BIT  MTP_CTRL.B_MTP_DATA_MATCH  ; 0xef

; -- DSRFLG 0xf8
DSR_OUT_RDY     BIT  DSRFLG.B_DSR_OUT_RDY       ; 0xf8
DSR_IN_RDY      BIT  DSRFLG.B_DSR_IN_RDY        ; 0xf9
DSR_BP_DBI      BIT  DSRFLG.B_DSR_BP_DBI        ; 0xfa
DSR_FLAG        BIT  DSRFLG.B_DSR_FLAG          ; 0xfb
DSR_RMW_FLAG    BIT  DSRFLG.B_DSR_RMW_FLAG      ; 0xfc
DSR_STROBE_REQ  BIT  DSRFLG.B_DSR_STROBE_REQ    ; 0xfd
DSR_STROBE_ACK  BIT  DSRFLG.B_DSR_STROBE_ACK    ; 0xfe
C2_DBI_HALTED   BIT  DSRFLG.B_C2_DBI_HALTED     ; 0xff

;---------------------------------------------------------------------------
;
;     INTERRUPTS:
;

; -- Interrupt priorities
INTERRUPT_SPI   EQU     7   ; SPI
INTERRUPT_I2C   EQU     8   ; I2C/SMB
INTERRUPT_SMB   EQU     8   ; I2C/SMB

; -- Interrupt entry points in CODE
ISRENTRY_SPI    CODE    (03H + 8 * INTERRUPT_SPI)
ISRENTRY_I2C    CODE    (03H + 8 * INTERRUPT_I2C)
ISRENTRY_SMB    CODE    (03H + 8 * INTERRUPT_SMB)

;
;------------------------------------------------------------------------------
;

