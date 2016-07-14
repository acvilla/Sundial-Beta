;-------------------------------------------------------------------------------
;                           Silicon Laboratories, Inc.
;                            http://www.silabs.com
;                                Copyright 2010
;-------------------------------------------------------------------------------
;
;     FILE:       si4010.inc
;     TARGET:     Si4010
;     TOOLCHAIN:  Keil, Raisonance
;     DATE:       May 05, 2010, Wednesday
;     RELEASE:    2.1 (MPech), ROM version 02.00
;
;---------------------------------------------------------------------------
;
;     DESCRIPTION:
;       Include file Keil and Raisonance assemblers as well as others,
;       ASM-51 compatible, assemblers. Use $INCLUDE directive:
;
;         $INCLUDE (si4010.inc)
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

; ---- Force no default defintions .. all is defined here

$NOMOD51

; >---- SFR byte registers -------------------------------------------------

P0              DATA  080H
SP              DATA  081H
DPL             DATA  082H
DPH             DATA  083H
GFM_DATA        DATA  084H
GFM_CONST       DATA  085H
SBOX_DATA       DATA  086H
PCON            DATA  087H
CLKOUT_SET      DATA  08FH
P1              DATA  090H
RBIT_DATA       DATA  099H
FC_CTRL         DATA  09BH
RTC_CTRL        DATA  09CH
FC_INTERVAL     DATA  09DH
P2              DATA  0A0H
P0CON           DATA  0A4H
P1CON           DATA  0A5H
IE              DATA  0A8H
ODS_CTRL        DATA  0A9H
ODS_TIMING      DATA  0AAH
ODS_DATA        DATA  0ABH
ODS_RATEL       DATA  0ACH
ODS_RATEH       DATA  0ADH
ODS_WARM1       DATA  0AEH
ODS_WARM2       DATA  0AFH
GPR_CTRL        DATA  0B1H
GPR_DATA        DATA  0B2H
PORT_CTRL       DATA  0B5H
PORT_SET        DATA  0B6H
PORT_INTCFG     DATA  0B7H
IP              DATA  0B8H
TMR3CTRL        DATA  0B9H
TMR3RL          DATA  0BAH
TMR3RH          DATA  0BBH
TMR3L           DATA  0BCH
TMR3H           DATA  0BDH
SYSGEN          DATA  0BEH
INT_FLAGS       DATA  0BFH
TMR2CTRL        DATA  0C8H
TMR_CLKSEL      DATA  0C9H
TMR2RL          DATA  0CAH
TMR2RH          DATA  0CBH
TMR2L           DATA  0CCH
TMR2H           DATA  0CDH
PA_LVL          DATA  0CEH
PSW             DATA  0D0H
PROT0_CTRL      DATA  0DAH
BOOT_FLAGS      DATA  0DDH
ACC             DATA  0E0H
LC_FSK          DATA  0E4H
EIE1            DATA  0E6H
SYS_SET         DATA  0EEH
B               DATA  0F0H
EIP1            DATA  0F6H

; >---- XREG (XDATA) registers ---------------------------------------------

bLPOSC_TRIM     XDATA  04002H
lFC_COUNT       XDATA  04008H
wPA_CAP         XDATA  0400CH
bPA_TRIM        XDATA  04012H
bXO_CTRL        XDATA  04016H
bPORT_TST       XDATA  04017H
abMTP_RDATA     XDATA  04040H


; >---- BOOT status variables ----------------------------------------------

wBoot_DpramTrimBeg  XDATA  011F3H
wBoot_NvmUserBeg    XDATA  011F5H
wBoot_NvmCopyAddr   XDATA  011FDH
bBoot_BootStat      XDATA  011FFH

;---------------------------------------------------------------------------
;
;     CONSTANTS:
;

; >---- SFR bit masks ------------------------------------------------------

; -- P0 .. 0x80
M_GPIO0               EQU  00000001B
M_GPIO1               EQU  00000010B
M_GPIO2               EQU  00000100B
M_GPIO3               EQU  00001000B
M_GPIO4               EQU  00010000B
M_GPIO5               EQU  00100000B
M_GPIO6               EQU  01000000B
M_GPIO7               EQU  10000000B

M_PORT_LED_ON         EQU  00100000B
M_GPIO_LED            EQU  00100000B

B_GPIO0               EQU  0
B_GPIO1               EQU  1
B_GPIO2               EQU  2
B_GPIO3               EQU  3
B_GPIO4               EQU  4
B_GPIO5               EQU  5
B_GPIO6               EQU  6
B_GPIO7               EQU  7

B_PORT_LED_ON         EQU  5
B_GPIO_LED            EQU  5

; -- P1 .. 0x90
M_GPIO8               EQU  00000001B
M_GPIO9               EQU  00000010B

B_GPIO8               EQU  0
B_GPIO9               EQU  1

; -- PCON .. 0x87
M_IDLE                EQU  00000001B
M_STOP                EQU  00000010B
M_GF5_0               EQU  11111100B

B_IDLE                EQU  0
B_STOP                EQU  1
B_GF5_0               EQU  2

; -- CLKOUT_SET .. 0x8f
M_CLKOUT_DIV          EQU  00011111B
M_CLKOUT_SYM          EQU  00100000B
M_CLKOUT_INV          EQU  01000000B
M_CLKOUT_CLR          EQU  10000000B

B_CLKOUT_DIV          EQU  0
B_CLKOUT_SYM          EQU  5
B_CLKOUT_INV          EQU  6
B_CLKOUT_CLR          EQU  7

; -- RBIT_DATA .. 0x99
M_ODS_NODATA          EQU  00000100B
M_ODS_EMPTY           EQU  00001000B
M_XO_CKGOOD           EQU  00010000B
M_GPIO_LED_DRIVE      EQU  00100000B

B_ODS_NODATA          EQU  2
B_ODS_EMPTY           EQU  3
B_XO_CKGOOD           EQU  4
B_GPIO_LED_DRIVE      EQU  5

; -- FC_CTRL .. 0x9b
M_FC_MODE             EQU  00000111B
M_FC_DIV_SEL          EQU  00100000B
M_FC_BUSY             EQU  01000000B
M_FC_DONE             EQU  10000000B

B_FC_MODE             EQU  0
B_FC_DIV_SEL          EQU  5
B_FC_BUSY             EQU  6
B_FC_DONE             EQU  7

; -- RTC_CTRL .. 0x9c
M_RTC_DIV             EQU  00000111B
M_RTC_CLR             EQU  00100000B
M_RTC_ENA             EQU  01000000B
M_RTC_INT             EQU  10000000B

B_RTC_DIV             EQU  0
B_RTC_CLR             EQU  5
B_RTC_ENA             EQU  6
B_RTC_INT             EQU  7

; -- IE .. 0xa8
M_EINT0               EQU  00000001B
M_ETMR2               EQU  00000010B
M_EDMD                EQU  00000100B
M_ERTC                EQU  00001000B
M_EODS                EQU  00010000B
M_ETMR3               EQU  00100000B
M_EINT1               EQU  01000000B
M_EA                  EQU  10000000B

B_EINT0               EQU  0
B_ETMR2               EQU  1
B_EDMD                EQU  2
B_ERTC                EQU  3
B_EODS                EQU  4
B_ETMR3               EQU  5
B_EINT1               EQU  6
B_EA                  EQU  7

; -- ODS_CTRL .. 0xa9
M_ODS_EN              EQU  00000001B
M_FORCE_PA            EQU  00000010B
M_FORCE_DIV           EQU  00000100B
M_FORCE_LC            EQU  00001000B
M_FSK_MODE            EQU  00010000B
M_FSK_FORCE_DEV       EQU  00100000B
M_ODS_SHIFT_CTRL      EQU  11000000B

B_ODS_EN              EQU  0
B_FORCE_PA            EQU  1
B_FORCE_DIV           EQU  2
B_FORCE_LC            EQU  3
B_FSK_MODE            EQU  4
B_FSK_FORCE_DEV       EQU  5
B_ODS_SHIFT_CTRL      EQU  6

; -- ODS_TIMING .. 0xaa
M_ODS_CK_DIV          EQU  00000111B
M_ODS_EDGE_TIME       EQU  00011000B
M_ODS_GROUP_WIDTH     EQU  11100000B

B_ODS_CK_DIV          EQU  0
B_ODS_EDGE_TIME       EQU  3
B_ODS_GROUP_WIDTH     EQU  5

; -- ODS_WARM1 .. 0xae
M_ODS_WARM_PA         EQU  00001111B
M_ODS_WARM_DIV        EQU  11110000B

B_ODS_WARM_PA         EQU  0
B_ODS_WARM_DIV        EQU  4

; -- ODS_WARM2 .. 0xaf
M_ODS_WARM_LC         EQU  00001111B

B_ODS_WARM_LC         EQU  0

; -- PORT_CTRL .. 0xb5
M_PORT_LED            EQU  00000011B
M_PORT_MIDRANGE       EQU  00000100B
M_PORT_5_MIDRANGE     EQU  00001000B
M_PORT_DRV2X          EQU  00010000B
M_PORT_MATRIX         EQU  00100000B
M_PORT_ROFF           EQU  01000000B
M_PORT_STROBE         EQU  10000000B

B_PORT_LED            EQU  0
B_PORT_MIDRANGE       EQU  2
B_PORT_5_MIDRANGE     EQU  3
B_PORT_DRV2X          EQU  4
B_PORT_MATRIX         EQU  5
B_PORT_ROFF           EQU  6
B_PORT_STROBE         EQU  7

; -- PORT_SET .. 0xb6
M_PORT_SEREN          EQU  00000001B
M_PORT_SERMODE        EQU  00000010B
M_PORT_REFEN          EQU  00000100B
M_PORT_CLKEN          EQU  00001000B
M_PORT_CLKOUT         EQU  00110000B
M_EDGE_INT0           EQU  01000000B
M_EDGE_INT1           EQU  10000000B

B_PORT_SEREN          EQU  0
B_PORT_SERMODE        EQU  1
B_PORT_REFEN          EQU  2
B_PORT_CLKEN          EQU  3
B_PORT_CLKOUT         EQU  4
B_EDGE_INT0           EQU  6
B_EDGE_INT1           EQU  7

; -- PORT_INTCFG .. 0xb7
M_SEL_INT0            EQU  00000111B
M_NEG_INT0            EQU  00001000B
M_SEL_INT1            EQU  01110000B
M_NEG_INT1            EQU  10000000B

B_SEL_INT0            EQU  0
B_NEG_INT0            EQU  3
B_SEL_INT1            EQU  4
B_NEG_INT1            EQU  7

; -- IP .. 0xb8
M_PINT0               EQU  00000001B
M_PTMR2               EQU  00000010B
M_PDMD                EQU  00000100B
M_PRTC                EQU  00001000B
M_PODS                EQU  00010000B
M_PTMR3               EQU  00100000B
M_PINT1               EQU  01000000B

B_PINT0               EQU  0
B_PTMR2               EQU  1
B_PDMD                EQU  2
B_PRTC                EQU  3
B_PODS                EQU  4
B_PTMR3               EQU  5
B_PINT1               EQU  6

; -- TMR3CTRL .. 0xb9
M_TMR3L_RUN           EQU  00000001B
M_TMR3H_RUN           EQU  00000010B
M_TMR3L_CAP           EQU  00000100B
M_TMR3H_CAP           EQU  00001000B
M_TMR3SPLIT           EQU  00010000B
M_TMR3INTL_EN         EQU  00100000B
M_TMR3INTL            EQU  01000000B
M_TMR3INTH            EQU  10000000B

B_TMR3L_RUN           EQU  0
B_TMR3H_RUN           EQU  1
B_TMR3L_CAP           EQU  2
B_TMR3H_CAP           EQU  3
B_TMR3SPLIT           EQU  4
B_TMR3INTL_EN         EQU  5
B_TMR3INTL            EQU  6
B_TMR3INTH            EQU  7

; -- SYSGEN .. 0xbe
M_SYSGEN_DIV          EQU  00000111B
M_PORT_HOLD           EQU  00001000B
M_RTC_TICKCLR         EQU  00010000B
M_POWER_1ST_TIME      EQU  00100000B
M_SYSGEN_SHUTDOWN     EQU  10000000B

B_SYSGEN_DIV          EQU  0
B_PORT_HOLD           EQU  3
B_RTC_TICKCLR         EQU  4
B_POWER_1ST_TIME      EQU  5
B_SYSGEN_SHUTDOWN     EQU  7

; -- INT_FLAGS .. 0xbf
M_INT0_FLAG           EQU  00000001B
M_INT1_FLAG           EQU  00000010B
M_ODS_FLAG            EQU  00000100B
M_VOID0_FLAG          EQU  00001000B
M_VOID1_FLAG          EQU  00010000B

B_INT0_FLAG           EQU  0
B_INT1_FLAG           EQU  1
B_ODS_FLAG            EQU  2
B_VOID0_FLAG          EQU  3
B_VOID1_FLAG          EQU  4

; -- TMR2CTRL .. 0xc8
M_TMR2L_RUN           EQU  00000001B
M_TMR2H_RUN           EQU  00000010B
M_TMR2L_CAP           EQU  00000100B
M_TMR2H_CAP           EQU  00001000B
M_TMR2SPLIT           EQU  00010000B
M_TMR2INTL_EN         EQU  00100000B
M_TMR2INTL            EQU  01000000B
M_TMR2INTH            EQU  10000000B

B_TMR2L_RUN           EQU  0
B_TMR2H_RUN           EQU  1
B_TMR2L_CAP           EQU  2
B_TMR2H_CAP           EQU  3
B_TMR2SPLIT           EQU  4
B_TMR2INTL_EN         EQU  5
B_TMR2INTL            EQU  6
B_TMR2INTH            EQU  7

; -- TMR_CLKSEL .. 0xc9
M_TMR2L_MODE          EQU  00000011B
M_TMR2H_MODE          EQU  00001100B
M_TMR3L_MODE          EQU  00110000B
M_TMR3H_MODE          EQU  11000000B

B_TMR2L_MODE          EQU  0
B_TMR2H_MODE          EQU  2
B_TMR3L_MODE          EQU  4
B_TMR3H_MODE          EQU  6

; -- PA_LVL .. 0xce
M_PA_LVL_BIAS         EQU  00000111B
M_PA_LVL_NSLICE       EQU  11111000B

B_PA_LVL_BIAS         EQU  0
B_PA_LVL_NSLICE       EQU  3

; -- PSW .. 0xd0
M_P                   EQU  00000001B
M_F1                  EQU  00000010B
M_OV                  EQU  00000100B
M_RS0                 EQU  00001000B
M_RS1                 EQU  00010000B
M_F0                  EQU  00100000B
M_AC                  EQU  01000000B
M_CY                  EQU  10000000B

B_P                   EQU  0
B_F1                  EQU  1
B_OV                  EQU  2
B_RS0                 EQU  3
B_RS1                 EQU  4
B_F0                  EQU  5
B_AC                  EQU  6
B_CY                  EQU  7

; -- PROT0_CTRL .. 0xda
M_NVM_BLOWN           EQU  00000111B
M_NVM_WR_PROT         EQU  00001000B
M_MTP_PROT            EQU  00010000B
M_CLOCK_PROT          EQU  00100000B
M_C2_OFF              EQU  01000000B
M_NVM_PROT            EQU  10000000B

B_NVM_BLOWN           EQU  0
B_NVM_WR_PROT         EQU  3
B_MTP_PROT            EQU  4
B_CLOCK_PROT          EQU  5
B_C2_OFF              EQU  6
B_NVM_PROT            EQU  7

; -- BOOT_FLAGS .. 0xdd
M_BFLAG_SYS           EQU  00001111B
M_BFLAG_POR           EQU  11110000B

B_BFLAG_SYS           EQU  0
B_BFLAG_POR           EQU  4

M_BOOT_CONT_SYS       EQU  00000001B
M_BOOT_DONE_SYS       EQU  00000010B
M_BOOT_FAIL_SYS       EQU  00000100B
M_BOOT_CONT_POR       EQU  00010000B
M_BOOT_TRIM_POR       EQU  00100000B

B_BOOT_CONT_SYS       EQU  0
B_BOOT_DONE_SYS       EQU  1
B_BOOT_FAIL_SYS       EQU  2
B_BOOT_CONT_POR       EQU  4
B_BOOT_TRIM_POR       EQU  5

; -- LC_FSK .. 0xe4
M_FSK_DEVIATION       EQU  01111111B
M_LC_DIVM             EQU  10000000B

B_FSK_DEVIATION       EQU  0
B_LC_DIVM             EQU  7

; -- EIE1 .. 0xe6
M_ESPI                EQU  00000001B
M_EI2C                EQU  00000010B
M_EFC                 EQU  00000100B
M_EVOID0              EQU  00001000B
M_EVOID1              EQU  00010000B

B_ESPI                EQU  0
B_EI2C                EQU  1
B_EFC                 EQU  2
B_EVOID0              EQU  3
B_EVOID1              EQU  4

; -- SYS_SET .. 0xee
M_AES_DECRYPT         EQU  00001000B

B_AES_DECRYPT         EQU  3

; -- EIP1 .. 0xf6
M_PSPI                EQU  00000001B
M_PI2C                EQU  00000010B
M_PFC                 EQU  00000100B
M_PVOID0              EQU  00001000B
M_PVOID1              EQU  00010000B

B_PSPI                EQU  0
B_PI2C                EQU  1
B_PFC                 EQU  2
B_PVOID0              EQU  3
B_PVOID1              EQU  4

; >---- XREG bit masks -----------------------------------------------------

; -- bPA_TRIM .. 0x4012
M_PA_BIAS_TRIM      EQU  00001111B
M_PA_MAX_DRV        EQU  00010000B

B_PA_BIAS_TRIM      EQU  0
B_PA_MAX_DRV        EQU  4

; -- bXO_CTRL .. 0x4016
M_XO_ENA            EQU  00000001B
M_XO_LOWCAP         EQU  00000010B
M_XO_TST            EQU  00001100B

B_XO_ENA            EQU  0
B_XO_LOWCAP         EQU  1
B_XO_TST            EQU  2

; -- bPORT_TST .. 0x4017
M_PORT_TST_IND      EQU  00001111B
M_PORT_TST_FS       EQU  01110000B

B_PORT_TST_IND      EQU  0
B_PORT_TST_FS       EQU  4

;---------------------------------------------------------------------------
;
;     BIT VARIABLES:
;

; >---- SFR bit fields -----------------------------------------------------

; -- P0 .. 0x80
GPIO0           BIT  P0.0                   ; 0x80 .. 0
GPIO1           BIT  P0.1                   ; 0x81
GPIO2           BIT  P0.2                   ; 0x82
GPIO3           BIT  P0.3                   ; 0x83
GPIO4           BIT  P0.4                   ; 0x84
GPIO5           BIT  P0.5                   ; 0x85
GPIO6           BIT  P0.6                   ; 0x86
GPIO7           BIT  P0.7                   ; 0x87 .. 7

PORT_LED_ON     BIT  P0.5                   ; 0x85 .. 5
GPIO_LED        BIT  P0.5                   ; 0x85 .. 5

; -- P1 .. 0x90
GPIO8           BIT  P1.0                   ; 0x90 .. 0
GPIO9           BIT  P1.1                   ; 0x91 .. 1

; -- IE .. 0xa8
EINT0           BIT  IE.B_EINT0             ; 0xa8
ETMR2           BIT  IE.B_ETMR2             ; 0xa9
EDMD            BIT  IE.B_EDMD              ; 0xaa
ERTC            BIT  IE.B_ERTC              ; 0xab
EODS            BIT  IE.B_EODS              ; 0xac
ETMR3           BIT  IE.B_ETMR3             ; 0xad
EINT1           BIT  IE.B_EINT1             ; 0xae
EA              BIT  IE.B_EA                ; 0xaf

; -- IP .. 0xb8
PINT0           BIT  IP.B_PINT0             ; 0xb8 .. 0
PTMR2           BIT  IP.B_PTMR2             ; 0xb9
PDMD            BIT  IP.B_PDMD              ; 0xba
PRTC            BIT  IP.B_PRTC              ; 0xbb
PODS            BIT  IP.B_PODS              ; 0xbc
PTMR3           BIT  IP.B_PTMR3             ; 0xbd
PINT1           BIT  IP.B_PINT1             ; 0xbe .. 6

; -- TMR2CTRL .. 0xc8
TMR2L_RUN       BIT  TMR2CTRL.B_TMR2L_RUN   ; 0xc8
TMR2H_RUN       BIT  TMR2CTRL.B_TMR2H_RUN   ; 0xc9
TMR2L_CAP       BIT  TMR2CTRL.B_TMR2L_CAP   ; 0xca
TMR2H_CAP       BIT  TMR2CTRL.B_TMR2H_CAP   ; 0xcb
TMR2SPLIT       BIT  TMR2CTRL.B_TMR2SPLIT   ; 0xcc
TMR2INTL_EN     BIT  TMR2CTRL.B_TMR2INTL_EN ; 0xcd
TMR2INTL        BIT  TMR2CTRL.B_TMR2INTL    ; 0xce
TMR2INTH        BIT  TMR2CTRL.B_TMR2INTH    ; 0xcf

; -- PSW 0xd0
P               BIT  PSW.0                  ; 0xd0
F1              BIT  PSW.1                  ; 0xd1
OV              BIT  PSW.2                  ; 0xd2
RS0             BIT  PSW.3                  ; 0xd3
RS1             BIT  PSW.4                  ; 0xd4
F0              BIT  PSW.5                  ; 0xd5
AC              BIT  PSW.6                  ; 0xd6
CY              BIT  PSW.7                  ; 0xd7

;
;------------------------------------------------------------------------------
;

