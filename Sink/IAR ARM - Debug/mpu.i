//=============================================================================
// FILE
//   mpu.c - Functions to setup and control the EM3588's MPU
//
// DESCRIPTION
//   This file contains the definitions, data table and software used to
//   setup the MPU.
//
//   Author:
//   Copyright 2008-2011 by Ember Corporation. All rights reserved.         *80*
//=============================================================================

/** @file hal/micro/cortexm3/compiler/iar.h
 * See @ref iar for detailed documentation.
 *
 * <!-- Copyright 2008-2011 by Ember Corporation. All rights reserved.   *80*-->
 */

/** @addtogroup iar
 * @brief Compiler and Platform specific definitions and typedefs for the
 *  IAR ARM C compiler.
 *
 * @note iar.h should be included first in all source files by setting the
 *  preprocessor macro PLATFORM_HEADER to point to it.  iar.h automatically
 *  includes platform-common.h.
 *
 *  See iar.h and platform-common.h for source code.
 *@{
 */





/**************************************************
 *
 * This file declares the ARM intrinsic inline functions.
 *
 * Copyright 1999-2006 IAR Systems. All rights reserved.
 *
 * $Revision: 99951 $
 *
 **************************************************/


/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */





/* A definiton for a function of what effects it has.
   NS  = no_state, errno, i.e. it uses no internal or external state. It may
         write to errno though
   NE  = no_state, i.e. it uses no internal or external state, not even
         writing to errno. 
   NRx = no_read(x), i.e. it doesn't read through pointer parameter x.
   NWx = no_write(x), i.e. it doesn't write through pointer parameter x.
   Rx  = returns x, i.e. the function will return parameter x.
   
   All the functions with effects also has "always_returns", 
   i.e. the function will always return.
*/







  #pragma system_include

/*
 * Check that the correct C compiler is used.
 */


/* Define function effects for intrinsics */


#pragma language=save
#pragma language=extended

__intrinsic __nounwind void    __no_operation(void);

__intrinsic __nounwind void    __disable_interrupt(void);
__intrinsic __nounwind void    __enable_interrupt(void);

typedef unsigned long __istate_t;

__intrinsic __nounwind __istate_t __get_interrupt_state(void);
__intrinsic __nounwind void __set_interrupt_state(__istate_t);


/* System control access for Cortex-M cores */
__intrinsic __nounwind unsigned long __get_PSR( void );
__intrinsic __nounwind unsigned long __get_IPSR( void );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_MSP( void );
__intrinsic __nounwind void          __set_MSP( unsigned long );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_PSP( void );
__intrinsic __nounwind void          __set_PSP( unsigned long );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_PRIMASK( void );
__intrinsic __nounwind void          __set_PRIMASK( unsigned long );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_CONTROL( void );
__intrinsic __nounwind void          __set_CONTROL( unsigned long );


/* These are only available for v7M */
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_FAULTMASK( void );
__intrinsic __nounwind void          __set_FAULTMASK(unsigned long);
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __get_BASEPRI( void );
__intrinsic __nounwind void          __set_BASEPRI( unsigned long );


__intrinsic __nounwind void __disable_fiq(void);
__intrinsic __nounwind void __enable_fiq(void);


/* ARM-mode intrinsics */

_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned long __SWP( unsigned long, volatile unsigned long * );
_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned char __SWPB( unsigned char, volatile unsigned char * );

typedef unsigned long __ul;


/*  Co-processor access */
__intrinsic __nounwind void          __MCR( unsigned __constrange(0,15) coproc, unsigned __constrange(0,8) opcode_1, __ul src,
                                 unsigned __constrange(0,15) CRn, unsigned __constrange(0,15) CRm, unsigned __constrange(0,8) opcode_2 );
__intrinsic __nounwind unsigned long __MRC( unsigned __constrange(0,15) coproc, unsigned __constrange(0,8) opcode_1,
                                 unsigned __constrange(0,15) CRn, unsigned __constrange(0,15) CRm, unsigned __constrange(0,8) opcode_2 );
__intrinsic __nounwind void          __MCR2( unsigned __constrange(0,15) coproc, unsigned __constrange(0,8) opcode_1, __ul src,
                                  unsigned __constrange(0,15) CRn, unsigned __constrange(0,15) CRm, unsigned __constrange(0,8) opcode_2 );
__intrinsic __nounwind unsigned long __MRC2( unsigned __constrange(0,15) coproc, unsigned __constrange(0,8) opcode_1,
                                  unsigned __constrange(0,15) CRn, unsigned __constrange(0,15) CRm, unsigned __constrange(0,8) opcode_2 );

/* Load coprocessor register. */
__intrinsic __nounwind void __LDC( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src);
__intrinsic __nounwind void __LDCL( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src);
__intrinsic __nounwind void __LDC2( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src);
__intrinsic __nounwind void __LDC2L( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src);

/* Store coprocessor register. */
__intrinsic __nounwind void __STC( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst);
__intrinsic __nounwind void __STCL( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst);
__intrinsic __nounwind void __STC2( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst);
__intrinsic __nounwind void __STC2L( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst);

/* Load coprocessor register (noindexed version with coprocessor option). */
__intrinsic __nounwind void __LDC_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src,
                              unsigned __constrange(0,255) option);

__intrinsic __nounwind void __LDCL_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src,
                               unsigned __constrange(0,255) option);

__intrinsic __nounwind void __LDC2_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src,
                               unsigned __constrange(0,255) option);

__intrinsic __nounwind void __LDC2L_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul const *src,
                                unsigned __constrange(0,255) option);

/* Store coprocessor register (version with coprocessor option). */
__intrinsic __nounwind void __STC_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst,
                              unsigned __constrange(0,255) option);

__intrinsic __nounwind void __STCL_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst,
                               unsigned __constrange(0,255) option);

__intrinsic __nounwind void __STC2_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst,
                               unsigned __constrange(0,255) option);

__intrinsic __nounwind void __STC2L_noidx( unsigned __constrange(0,15) coproc, unsigned __constrange(0,15) CRn, volatile __ul *dst,
                                unsigned __constrange(0,255) option);

/* Status register access, v7M: */
__intrinsic __nounwind unsigned long __get_APSR( void );
__intrinsic __nounwind void          __set_APSR( unsigned long );

/* Floating-point status and control register access */
__intrinsic __nounwind unsigned long __get_FPSCR( void );
__intrinsic __nounwind void __set_FPSCR( unsigned long );

/* Architecture v5T, CLZ is also available in Thumb mode for Thumb2 cores */
_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned char __CLZ( unsigned long );

/* Architecture v5TE */

_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind int         __QCFlag( void );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind void __reset_QC_flag( void );

_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind signed long __SMUL( signed short, signed short );

/* Architecture v6, REV and REVSH are also available in thumb mode */
_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned long __REV( unsigned long );
_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind signed long __REVSH( short );

_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned long __REV16( unsigned long );
_Pragma("function_effects = no_state, always_returns") __intrinsic __nounwind unsigned long __RBIT( unsigned long );

_Pragma("function_effects = no_state, no_write(1), always_returns") __intrinsic __nounwind unsigned char  __LDREXB( volatile unsigned char const * );
_Pragma("function_effects = no_state, no_write(1), always_returns") __intrinsic __nounwind unsigned short __LDREXH( volatile unsigned short const * );
_Pragma("function_effects = no_state, no_write(1), always_returns") __intrinsic __nounwind unsigned long  __LDREX ( volatile unsigned long const * );
_Pragma("function_effects = no_state, no_write(1), always_returns") __intrinsic __nounwind unsigned long long __LDREXD( volatile unsigned long long const * );

_Pragma("function_effects = no_state, no_read(2), always_returns") __intrinsic __nounwind unsigned long  __STREXB( unsigned char, volatile unsigned char * );
_Pragma("function_effects = no_state, no_read(2), always_returns") __intrinsic __nounwind unsigned long  __STREXH( unsigned short, volatile unsigned short * );
_Pragma("function_effects = no_state, no_read(2), always_returns") __intrinsic __nounwind unsigned long  __STREX ( unsigned long, volatile unsigned long * );
_Pragma("function_effects = no_state, no_read(2), always_returns") __intrinsic __nounwind unsigned long  __STREXD( unsigned long long, volatile unsigned long long * );

__intrinsic __nounwind void __CLREX( void );

__intrinsic __nounwind void __SEV( void );
__intrinsic __nounwind void __WFE( void );
__intrinsic __nounwind void __WFI( void );
__intrinsic __nounwind void __YIELD( void );

__intrinsic __nounwind void __PLI( volatile void const * );
__intrinsic __nounwind void __PLD( volatile void const * );
__intrinsic __nounwind void __PLDW( volatile void const * );

_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind   signed long __SSAT     (unsigned long val,
                                      unsigned int __constrange( 1, 32 ) sat );
_Pragma("function_effects = hidden_state, always_returns") __intrinsic __nounwind unsigned long __USAT     (unsigned long val,
                                      unsigned int __constrange( 0, 31 ) sat );



/* Architecture v7 instructions */
__intrinsic __nounwind void __DMB(void);
__intrinsic __nounwind void __DSB(void);
__intrinsic __nounwind void __ISB(void);

/* Architecture v8-M instructions */
__intrinsic __nounwind unsigned long __TT(unsigned long);
__intrinsic __nounwind unsigned long __TTT(unsigned long);
__intrinsic __nounwind unsigned long __TTA(unsigned long);
__intrinsic __nounwind unsigned long __TTAT(unsigned long);


__intrinsic __nounwind unsigned long __get_LR(void);
__intrinsic __nounwind void __set_LR(unsigned long);

__intrinsic __nounwind unsigned long __get_SP(void);
__intrinsic __nounwind void __set_SP(unsigned long);

#pragma language=restore



  #include <stdarg.h>
/* stdint.h standard header */
/* Copyright 2003-2010 IAR Systems AB.  */

  #pragma system_include

/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */




/* yvals.h internal configuration header file. */
/* Copyright 2001-2010 IAR Systems AB. */


  #pragma system_include

/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */





                /* Convenience macros */



/* Used to refer to '__aeabi' symbols in the library. */ 

                /* Versions */



/*
 * Support for some C99 or other symbols
 *
 * This setting makes available some macros, functions, etc that are
 * beneficial.
 *
 * Default is to include them.
 *
 * Disabling this in C++ mode will not compile (some C++ functions uses C99
 * functionality).
 */

  /* Default turned on when compiling C++, EC++, or C99. */



                /* Configuration */
/***************************************************
 *
 * DLib_Defaults.h is the library configuration manager.
 *
 * Copyright 2003-2010 IAR Systems AB.  
 *
 * This configuration header file performs the following tasks:
 *
 * 1. Includes the configuration header file, defined by _DLIB_CONFIG_FILE,
 *    that sets up a particular runtime environment.
 *
 * 2. Includes the product configuration header file, DLib_Product.h, that
 *    specifies default values for the product and makes sure that the
 *    configuration is valid.
 *
 * 3. Sets up default values for all remaining configuration symbols.
 *
 * This configuration header file, the one defined by _DLIB_CONFIG_FILE, and
 * DLib_Product.h configures how the runtime environment should behave. This
 * includes all system headers and the library itself, i.e. all system headers
 * includes this configuration header file, and the library has been built
 * using this configuration header file.
 *
 ***************************************************
 *
 * DO NOT MODIFY THIS FILE!
 *
 ***************************************************/


  #pragma system_include

/* Include the main configuration header file. */
/* Customer-specific DLib configuration. */
/* Copyright (C) 2003 IAR Systems.  All rights reserved. */


  #pragma system_include

/* No changes to the defaults. */

  /* _DLIB_CONFIG_FILE_STRING is the quoted variant of above */

/* Include the product specific header file. */

   #pragma system_include


/*********************************************************************
*
*       Configuration
*
*********************************************************************/

/* Wide character and multi byte character support in library.
 * This is not allowed to vary over configurations, since math-library
 * is built with wide character support.
 */

/* ARM uses the large implementation of DLib */

/* This ensures that the standard header file "string.h" includes
 * the Arm-specific file "DLib_Product_string.h". */

/* This ensures that the standard header file "fenv.h" includes
 * the Arm-specific file "DLib_Product_fenv.h". */

/* Max buffer used for swap in qsort */

/* Enable system locking  */

/* Enable AEABI support */

/* Enable rtmodel for setjump buffer size */

/* Enable parsing of hex floats */

/* Special placement for locale structures when building ropi libraries */

/* CPP-library uses software floatingpoint interface */

/* Use speedy implementation of floats (simple quad). */

/* Configure generic ELF init routines. */






/*
 * The remainder of the file sets up defaults for a number of
 * configuration symbols, each corresponds to a feature in the
 * libary.
 *
 * The value of the symbols should either be 1, if the feature should
 * be supported, or 0 if it shouldn't. (Except where otherwise
 * noted.)
 */


/*
 * Small or Large target
 *
 * This define determines whether the target is large or small. It must be 
 * setup in the DLib_Product header or in the compiler itself.
 *
 * For a small target some functionality in the library will not deliver 
 * the best available results. For instance the _accurate variants will not use
 * the extra precision packet for large arguments.
 * 
 */



/*
 * File handling
 *
 * Determines whether FILE descriptors and related functions exists or not.
 * When this feature is selected, i.e. set to 1, then FILE descriptors and
 * related functions (e.g. fprintf, fopen) exist. All files, even stdin,
 * stdout, and stderr will then be handled with a file system mechanism that
 * buffers files before accessing the lowlevel I/O interface (__open, __read,
 * __write, etc).
 *
 * If not selected, i.e. set to 0, then FILE descriptors and related functions
 * (e.g. fprintf, fopen) does not exist. All functions that normally uses
 * stderr will use stdout instead. Functions that uses stdout and stdin (like
 * printf and scanf) will access the lowlevel I/O interface directly (__open,
 * __read, __write, etc), i.e. there will not be any buffering.
 *
 * The default is not to have support for FILE descriptors.
 */


/*
 * Use static buffers for stdout
 *
 * This setting controls whether the stream stdout uses a static 80 bytes
 * buffer or uses a one byte buffer allocated in the file descriptor. This
 * setting is only applicable if the FILE descriptors are enabled above.
 *
 * Default is to use a static 80 byte buffer.
 */


/*
 * Support of locale interface
 *
 * "Locale" is the system in C that support language- and
 * contry-specific settings for a number of areas, including currency
 * symbols, date and time, and multibyte encodings.
 *
 * This setting determines whether the locale interface exist or not.
 * When this feature is selected, i.e. set to 1, the locale interface exist
 * (setlocale, etc). A number of preselected locales can be activated during
 * runtime. The preselected locales and encodings is choosen by defining any
 * number of _LOCALE_USE_xxx and _ENCODING_USE_xxx symbols. The application
 * will start with the "C" locale choosen. (Single byte encoding is always
 * supported in this mode.)
 *
 *
 * If not selected, i.e. set to 0, the locale interface (setlocale, etc) does
 * not exist. One preselected locale and one preselected encoding is then used
 * directly. That locale can not be changed during runtime. The preselected
 * locale and encoding is choosen by defining at most one of _LOCALE_USE_xxx
 * and at most one of _ENCODING_USE_xxx. The default is to use the "C" locale
 * and the single byte encoding, respectively.
 *
 * The default is not to have support for the locale interface with the "C"
 * locale and the single byte encoding.
 *
 * Supported locales
 * -----------------
 * _LOCALE_USE_C                  C standard locale (the default)
 * _LOCALE_USE_POSIX ISO-8859-1   Posix locale
 * _LOCALE_USE_CS_CZ ISO-8859-2   Czech language locale for Czech Republic
 * _LOCALE_USE_DA_DK ISO-8859-1   Danish language locale for Denmark
 * _LOCALE_USE_DA_EU ISO-8859-15  Danish language locale for Europe
 * _LOCALE_USE_DE_AT ISO-8859-1   German language locale for Austria
 * _LOCALE_USE_DE_BE ISO-8859-1   German language locale for Belgium
 * _LOCALE_USE_DE_CH ISO-8859-1   German language locale for Switzerland
 * _LOCALE_USE_DE_DE ISO-8859-1   German language locale for Germany
 * _LOCALE_USE_DE_EU ISO-8859-15  German language locale for Europe
 * _LOCALE_USE_DE_LU ISO-8859-1   German language locale for Luxemburg
 * _LOCALE_USE_EL_EU ISO-8859-7x  Greek language locale for Europe
 *                                (Euro symbol added)
 * _LOCALE_USE_EL_GR ISO-8859-7   Greek language locale for Greece
 * _LOCALE_USE_EN_AU ISO-8859-1   English language locale for Australia
 * _LOCALE_USE_EN_CA ISO-8859-1   English language locale for Canada
 * _LOCALE_USE_EN_DK ISO_8859-1   English language locale for Denmark
 * _LOCALE_USE_EN_EU ISO-8859-15  English language locale for Europe
 * _LOCALE_USE_EN_GB ISO-8859-1   English language locale for United Kingdom
 * _LOCALE_USE_EN_IE ISO-8859-1   English language locale for Ireland
 * _LOCALE_USE_EN_NZ ISO-8859-1   English language locale for New Zealand
 * _LOCALE_USE_EN_US ISO-8859-1   English language locale for USA
 * _LOCALE_USE_ES_AR ISO-8859-1   Spanish language locale for Argentina
 * _LOCALE_USE_ES_BO ISO-8859-1   Spanish language locale for Bolivia
 * _LOCALE_USE_ES_CL ISO-8859-1   Spanish language locale for Chile
 * _LOCALE_USE_ES_CO ISO-8859-1   Spanish language locale for Colombia
 * _LOCALE_USE_ES_DO ISO-8859-1   Spanish language locale for Dominican Republic
 * _LOCALE_USE_ES_EC ISO-8859-1   Spanish language locale for Equador
 * _LOCALE_USE_ES_ES ISO-8859-1   Spanish language locale for Spain
 * _LOCALE_USE_ES_EU ISO-8859-15  Spanish language locale for Europe
 * _LOCALE_USE_ES_GT ISO-8859-1   Spanish language locale for Guatemala
 * _LOCALE_USE_ES_HN ISO-8859-1   Spanish language locale for Honduras
 * _LOCALE_USE_ES_MX ISO-8859-1   Spanish language locale for Mexico
 * _LOCALE_USE_ES_PA ISO-8859-1   Spanish language locale for Panama
 * _LOCALE_USE_ES_PE ISO-8859-1   Spanish language locale for Peru
 * _LOCALE_USE_ES_PY ISO-8859-1   Spanish language locale for Paraguay
 * _LOCALE_USE_ES_SV ISO-8859-1   Spanish language locale for Salvador
 * _LOCALE_USE_ES_US ISO-8859-1   Spanish language locale for USA
 * _LOCALE_USE_ES_UY ISO-8859-1   Spanish language locale for Uruguay
 * _LOCALE_USE_ES_VE ISO-8859-1   Spanish language locale for Venezuela
 * _LOCALE_USE_ET_EE ISO-8859-1   Estonian language for Estonia
 * _LOCALE_USE_EU_ES ISO-8859-1   Basque language locale for Spain
 * _LOCALE_USE_FI_EU ISO-8859-15  Finnish language locale for Europe
 * _LOCALE_USE_FI_FI ISO-8859-1   Finnish language locale for Finland
 * _LOCALE_USE_FO_FO ISO-8859-1   Faroese language locale for Faroe Islands
 * _LOCALE_USE_FR_BE ISO-8859-1   French language locale for Belgium
 * _LOCALE_USE_FR_CA ISO-8859-1   French language locale for Canada
 * _LOCALE_USE_FR_CH ISO-8859-1   French language locale for Switzerland
 * _LOCALE_USE_FR_EU ISO-8859-15  French language locale for Europe
 * _LOCALE_USE_FR_FR ISO-8859-1   French language locale for France
 * _LOCALE_USE_FR_LU ISO-8859-1   French language locale for Luxemburg
 * _LOCALE_USE_GA_EU ISO-8859-15  Irish language locale for Europe
 * _LOCALE_USE_GA_IE ISO-8859-1   Irish language locale for Ireland
 * _LOCALE_USE_GL_ES ISO-8859-1   Galician language locale for Spain
 * _LOCALE_USE_HR_HR ISO-8859-2   Croatian language locale for Croatia
 * _LOCALE_USE_HU_HU ISO-8859-2   Hungarian language locale for Hungary
 * _LOCALE_USE_ID_ID ISO-8859-1   Indonesian language locale for Indonesia
 * _LOCALE_USE_IS_EU ISO-8859-15  Icelandic language locale for Europe
 * _LOCALE_USE_IS_IS ISO-8859-1   Icelandic language locale for Iceland
 * _LOCALE_USE_IT_EU ISO-8859-15  Italian language locale for Europe
 * _LOCALE_USE_IT_IT ISO-8859-1   Italian language locale for Italy
 * _LOCALE_USE_IW_IL ISO-8859-8   Hebrew language locale for Israel
 * _LOCALE_USE_KL_GL ISO-8859-1   Greenlandic language locale for Greenland
 * _LOCALE_USE_LT_LT   BALTIC     Lithuanian languagelocale for Lithuania
 * _LOCALE_USE_LV_LV   BALTIC     Latvian languagelocale for Latvia
 * _LOCALE_USE_NL_BE ISO-8859-1   Dutch language locale for Belgium
 * _LOCALE_USE_NL_EU ISO-8859-15  Dutch language locale for Europe
 * _LOCALE_USE_NL_NL ISO-8859-9   Dutch language locale for Netherlands
 * _LOCALE_USE_NO_EU ISO-8859-15  Norwegian language locale for Europe
 * _LOCALE_USE_NO_NO ISO-8859-1   Norwegian language locale for Norway
 * _LOCALE_USE_PL_PL ISO-8859-2   Polish language locale for Poland
 * _LOCALE_USE_PT_BR ISO-8859-1   Portugese language locale for Brazil
 * _LOCALE_USE_PT_EU ISO-8859-15  Portugese language locale for Europe
 * _LOCALE_USE_PT_PT ISO-8859-1   Portugese language locale for Portugal
 * _LOCALE_USE_RO_RO ISO-8859-2   Romanian language locale for Romania
 * _LOCALE_USE_RU_RU ISO-8859-5   Russian language locale for Russia
 * _LOCALE_USE_SL_SI ISO-8859-2   Slovenian language locale for Slovenia
 * _LOCALE_USE_SV_EU ISO-8859-15  Swedish language locale for Europe
 * _LOCALE_USE_SV_FI ISO-8859-1   Swedish language locale for Finland
 * _LOCALE_USE_SV_SE ISO-8859-1   Swedish language locale for Sweden
 * _LOCALE_USE_TR_TR ISO-8859-9   Turkish language locale for Turkey
 *
 *  Supported encodings
 *  -------------------
 * n/a                            Single byte (used if no other is defined).
 * _ENCODING_USE_UTF8             UTF8 encoding.
 */


/* We need to have the "C" locale if we have full locale support. */


/*
 * Support of multibytes in printf- and scanf-like functions
 *
 * This is the default value for _DLIB_PRINTF_MULTIBYTE and
 * _DLIB_SCANF_MULTIBYTE. See them for a description.
 *
 * Default is to not have support for multibytes in printf- and scanf-like
 * functions.
 */



/*
 * Throw handling in the EC++ library
 *
 * This setting determines what happens when the EC++ part of the library
 * fails (where a normal C++ library 'throws').
 *
 * The following alternatives exists (setting of the symbol):
 * 0                - The application does nothing, i.e. continues with the
 *                    next statement.
 * 1                - The application terminates by calling the 'abort'
 *                    function directly.
 * <anything else>  - An object of class "exception" is created.  This
 *                    object contains a string describing the problem.
 *                    This string is later emitted on "stderr" before
 *                    the application terminates by calling the 'abort'
 *                    function directly.
 *
 * Default is to do nothing.
 */



/*
 * Hexadecimal floating-point numbers in strtod
 *
 * If selected, i.e. set to 1, strtod supports C99 hexadecimal floating-point
 * numbers. This also enables hexadecimal floating-points in internal functions
 * used for converting strings and wide strings to float, double, and long
 * double.
 *
 * If not selected, i.e. set to 0, C99 hexadecimal floating-point numbers
 * aren't supported.
 *
 * Default is not to support hexadecimal floating-point numbers.
 */



/*
 * Printf configuration symbols.
 *
 * All the configuration symbols described further on controls the behaviour
 * of printf, sprintf, and the other printf variants.
 *
 * The library proves four formatters for printf: 'tiny', 'small',
 * 'large', and 'default'.  The setup in this file controls all except
 * 'tiny'.  Note that both small' and 'large' explicitly removes
 * some features.
 */

/*
 * Handle multibytes in printf
 *
 * This setting controls whether multibytes and wchar_ts are supported in
 * printf. Set to 1 to support them, otherwise set to 0.
 *
 * See _DLIB_FORMATTED_MULTIBYTE for the default setting.
 */


/*
 * Long long formatting in printf
 *
 * This setting controls long long support (%lld) in printf. Set to 1 to
 * support it, otherwise set to 0.

 * Note, if long long should not be supported and 'intmax_t' is larger than
 * an ordinary 'long', then %jd and %jn will not be supported.
 *
 * Default is to support long long formatting.
 */




/*
 * Floating-point formatting in printf
 *
 * This setting controls whether printf supports floating-point formatting.
 * Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support floating-point formatting.
 */


/*
 * Hexadecimal floating-point formatting in printf
 *
 * This setting controls whether the %a format, i.e. the output of
 * floating-point numbers in the C99 hexadecimal format. Set to 1 to support
 * it, otherwise set to 0.
 *
 * Default is to support %a in printf.
 */


/*
 * Output count formatting in printf
 *
 * This setting controls whether the output count specifier (%n) is supported
 * or not in printf. Set to 1 to support it, otherwise set to 0.
 *
 * Default is to support %n in printf.
 */


/*
 * Support of qualifiers in printf
 *
 * This setting controls whether qualifiers that enlarges the input value
 * [hlLjtz] is supported in printf or not. Set to 1 to support them, otherwise
 * set to 0. See also _DLIB_PRINTF_INT_TYPE_IS_INT and
 * _DLIB_PRINTF_INT_TYPE_IS_LONG.
 *
 * Default is to support [hlLjtz] qualifiers in printf.
 */


/*
 * Support of flags in printf
 *
 * This setting controls whether flags (-+ #0) is supported in printf or not.
 * Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support flags in printf.
 */


/*
 * Support widths and precisions in printf
 *
 * This setting controls whether widths and precisions are supported in printf.
 * Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support widths and precisions in printf.
 */


/*
 * Support of unsigned integer formatting in printf
 *
 * This setting controls whether unsigned integer formatting is supported in
 * printf. Set to 1 to support it, otherwise set to 0.
 *
 * Default is to support unsigned integer formatting in printf.
 */


/*
 * Support of signed integer formatting in printf
 *
 * This setting controls whether signed integer formatting is supported in
 * printf. Set to 1 to support it, otherwise set to 0.
 *
 * Default is to support signed integer formatting in printf.
 */


/*
 * Support of formatting anything larger than int in printf
 *
 * This setting controls if 'int' should be used internally in printf, rather
 * than the largest existing integer type. If 'int' is used, any integer or
 * pointer type formatting use 'int' as internal type even though the
 * formatted type is larger. Set to 1 to use 'int' as internal type, otherwise
 * set to 0.
 *
 * See also next configuration.
 *
 * Default is to internally use largest existing internally type.
 */


/*
 * Support of formatting anything larger than long in printf
 *
 * This setting controls if 'long' should be used internally in printf, rather
 * than the largest existing integer type. If 'long' is used, any integer or
 * pointer type formatting use 'long' as internal type even though the
 * formatted type is larger. Set to 1 to use 'long' as internal type,
 * otherwise set to 0.
 *
 * See also previous configuration.
 *
 * Default is to internally use largest existing internally type.
 */



/*
 * Emit a char a time in printf
 *
 * This setting controls internal output handling. If selected, i.e. set to 1,
 * then printf emits one character at a time, which requires less code but
 * can be slightly slower for some types of output.
 *
 * If not selected, i.e. set to 0, then printf buffers some outputs.
 *
 * Note that it is recommended to either use full file support (see
 * _DLIB_FILE_DESCRIPTOR) or -- for debug output -- use the linker
 * option "-e__write_buffered=__write" to enable buffered I/O rather
 * than deselecting this feature.
 */



/*
 * Scanf configuration symbols.
 *
 * All the configuration symbols described here controls the
 * behaviour of scanf, sscanf, and the other scanf variants.
 *
 * The library proves three formatters for scanf: 'small', 'large',
 * and 'default'.  The setup in this file controls all, however both
 * 'small' and 'large' explicitly removes some features.
 */

/*
 * Handle multibytes in scanf
 *
 * This setting controls whether multibytes and wchar_t:s are supported in
 * scanf. Set to 1 to support them, otherwise set to 0.
 *
 * See _DLIB_FORMATTED_MULTIBYTE for the default.
 */


/*
 * Long long formatting in scanf
 *
 * This setting controls whether scanf supports long long support (%lld). It
 * also controls, if 'intmax_t' is larger than an ordinary 'long', i.e. how
 * the %jd and %jn specifiers behaves. Set to 1 to support them, otherwise set
 * to 0.
 *
 * Default is to support long long formatting in scanf.
 */



/*
 * Support widths in scanf
 *
 * This controls whether scanf supports widths. Set to 1 to support them,
 * otherwise set to 0.
 *
 * Default is to support widths in scanf.
 */


/*
 * Support qualifiers [hjltzL] in scanf
 *
 * This setting controls whether scanf supports qualifiers [hjltzL] or not. Set
 * to 1 to support them, otherwise set to 0.
 *
 * Default is to support qualifiers in scanf.
 */


/*
 * Support floating-point formatting in scanf
 *
 * This setting controls whether scanf supports floating-point formatting. Set
 * to 1 to support them, otherwise set to 0.
 *
 * Default is to support floating-point formatting in scanf.
 */


/*
 * Support output count formatting (%n)
 *
 * This setting controls whether scanf supports output count formatting (%n).
 * Set to 1 to support it, otherwise set to 0.
 *
 * Default is to support output count formatting in scanf.
 */


/*
 * Support scansets ([]) in scanf
 *
 * This setting controls whether scanf supports scansets ([]) or not. Set to 1
 * to support them, otherwise set to 0.
 *
 * Default is to support scansets in scanf.
 */


/*
 * Support signed integer formatting in scanf
 *
 * This setting controls whether scanf supports signed integer formatting or
 * not. Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support signed integer formatting in scanf.
 */


/*
 * Support unsigned integer formatting in scanf
 *
 * This setting controls whether scanf supports unsigned integer formatting or
 * not. Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support unsigned integer formatting in scanf.
 */


/*
 * Support assignment suppressing [*] in scanf
 *
 * This setting controls whether scanf supports assignment suppressing [*] or
 * not. Set to 1 to support them, otherwise set to 0.
 *
 * Default is to support assignment suppressing in scanf.
 */


/*
 * Handle multibytes in asctime and strftime.
 *
 * This setting controls whether multibytes and wchar_ts are
 * supported.Set to 1 to support them, otherwise set to 0.
 *
 * See _DLIB_FORMATTED_MULTIBYTE for the default setting.
 */


/*
 * True if "qsort" should be implemented using bubble sort.
 *
 * Bubble sort is less efficient than quick sort but requires less RAM
 * and ROM resources.
 */


/*
 * Set Buffert size used in qsort
 */


/*
 * The default "rand" function uses an array of 32 long:s of memory to
 * store the current state.
 *
 * The simple "rand" function uses only a single long. However, the
 * quality of the generated psuedo-random numbers are not as good as
 * the default implementation.
 */


/*
 * Wide character and multi byte character support in library.
 */


/*
 * Set attributes on the function used by the C-SPY debug interface to set a
 * breakpoint in.
 */


/*
 * Support threading in the library
 *
 * 0    No thread support
 * 1    Thread support with a, b, and d.
 * 2    Thread support with a, b, and e.
 * 3    Thread support with all thread-local storage in a dynamically allocated
 *        memory area and a, and b.
 *      a. Lock on heap accesses
 *      b. Optional lock on file accesses (see _DLIB_FILE_OP_LOCKS below)
 *      d. Use an external thread-local storage interface for all the
 *         libraries static and global variables.
 *      e. Static and global variables aren't safe for access from several
 *         threads.
 *
 * Note that if locks are used the following symbols must be defined:
 *
 *   _DLIB_THREAD_LOCK_ONCE_TYPE
 *   _DLIB_THREAD_LOCK_ONCE_MACRO(control_variable, init_function)
 *   _DLIB_THREAD_LOCK_ONCE_TYPE_INIT
 *
 * They will be used to initialize the needed locks only once. TYPE is the
 * type for the static control variable, MACRO is the expression that will be
 * evaluated at each usage of a lock, and INIT is the initializer for the
 * control variable.
 *
 * Note that if thread model 3 is used the symbol _DLIB_TLS_POINTER must be
 * defined. It is a thread local pointer to a dynamic memory area that
 * contains all used TLS variables for the library. Optionally the following
 * symbols can be defined as well (default is to use the default const data
 * and data memories):
 *
 *   _DLIB_TLS_INITIALIZER_MEMORY The memory to place the initializers for the
 *                                TLS memory area
 *   _DLIB_TLS_MEMORY             The memory to use for the TLS memory area. A
 *                                pointer to this memory must be castable to a
 *                                default pointer and back.
 *   _DLIB_TLS_REQUIRE_INIT       Set to 1 to require __cstart_init_tls
 *                                when needed to initialize the TLS data
 *                                segment for the main thread.
 *   _DLIB_TLS_SEGMENT_DATA       The name of the TLS RAM data segment
 *   _DLIB_TLS_SEGMENT_INIT       The name of the used to initialize the
 *                                TLS data segment.
 *
 * See DLib_Threads.h for a description of what interfaces needs to be
 * defined for thread support.
 */


/*
 * Used by products where one runtime library can be used by applications
 * with different data models, in order to reduce the total number of
 * libraries required. Typically, this is used when the pointer types does
 * not change over the data models used, but the placement of data variables
 * or/and constant variables do.
 *
 * If defined, this symbol is typically defined to the memory attribute that
 * is used by the runtime library. The actual define must use a
 * _Pragma("type_attribute = xxx") construct. In the header files, it is used
 * on all statically linked data objects seen by the application.
 */



/*
 * Turn on support for the Target-specific ABI. The ABI is based on the
 * ARM AEABI. A target, except ARM, may deviate from it.
 */


  /* Possible AEABI deviations */

  /*
   * The "difunc" table contains information about C++ objects that
   * should be dynamically initialized, where each entry in the table
   * represents an initialization function that should be called. When
   * the symbol _DLIB_AEABI_DIFUNC_CONTAINS_OFFSETS is true, each
   * entry in the table is encoded as an offset from the entry
   * location. When false, the entries contain the actual addresses to
   * call.
   */


/*
 * Turn on usage of a pragma to tell the linker the number of elements used
 * in a setjmp jmp_buf.
 */


/*
 * If true, the product supplies a "DLib_Product_string.h" file that
 * is included from "string.h".
 */


/*
 * Determine whether the math fma routines are fast or not.
 */

/*
 * Rtti support.
 */


/*
 * Use the "pointers to short" or "pointers to long" implementation of 
 * the basic floating point routines (like Dnorm, Dtest, Dscale, and Dunscale).
 */

/*
 * Use 64-bit long long as intermediary type in Dtest, and fabs.
 * Default is to do this if long long is 64-bits.
 */

/*
 * Favor speed versus some size enlargements in floating point functions.
 */

/*
 * Include dlmalloc as an alternative heap manager in product.
 *
 * Typically, an application will use a "malloc" heap manager that is
 * relatively small but not that efficient. An application can
 * optionally use the "dlmalloc" package, which provides a more
 * effective "malloc" heap manager, if it is included in the product
 * and supported by the settings.
 *
 * See the product documentation on how to use it, and whether or not
 * it is included in the product.
 */
  /* size_t/ptrdiff_t must be a 4 bytes unsigned integer. */


/*
 * Allow the 64-bit time_t interface?
 *
 * Default is yes if long long is 64 bits.
 */
  #pragma language = save 
  #pragma language = extended
  #pragma language = restore


/*
 * Is time_t 64 or 32 bits?
 *
 * Default is 32 bits.
 */

/*
 * Do we include math functions that demands lots of constant bytes?
 * (like erf, erfc, expm1, fma, lgamma, tgamma, and *_accurate)
 *
 */

/*
 * Set this to __weak, if supported.
 *
 */


/*
 * Deleted options
 *
 */








                /* Floating-point */

/*
 * Whenever a floating-point type is equal to another, we try to fold those
 * two types into one. This means that if float == double then we fold float to
 * use double internally. Example sinf(float) will use _Sin(double, uint).
 *
 * _X_FNAME is a redirector for internal support routines. The X can be
 *          D (double), F (float), or L (long double). It redirects by using
 *          another prefix. Example calls to Dtest will be __iar_Dtest,
 *          __iar_FDtest, or __iarLDtest.
 * _X_FUN   is a redirector for functions visible to the customer. As above, the
 *          X can be D, F, or L. It redirects by using another suffix. Example
 *          calls to sin will be sin, sinf, or sinl.
 * _X_TYPE  The type that one type is folded to.
 * _X_PTRCAST is a redirector for a cast operation involving a pointer.
 * _X_CAST  is a redirector for a cast involving the float type.
 *
 * _FLOAT_IS_DOUBLE signals that all internal float routines aren't needed.
 * _LONG_DOUBLE_IS_DOUBLE signals that all internal long double routines
 *                        aren't needed.
 */


                /* NAMING PROPERTIES */

/* Has support for fixed point types */

/* Has support for secure functions (printf_s, scanf_s, etc) */
/* Will not compile if enabled */

/* Has support for complex C types */

/* If is Embedded C++ language */

/* If is true C++ language */

/* True C++ language setup */



                /* NAMESPACE CONTROL */






/* xencoding_limits.h internal header file */
/* Copyright 2003-2010 IAR Systems AB.  */


  #pragma system_include

/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */




/* yvals.h internal configuration header file. */
/* Copyright 2001-2010 IAR Systems AB. */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */

                                /* Multibyte encoding length. */





                                /* Utility macro */








                /* FLOATING-POINT PROPERTIES */

                /* float properties */

                /* double properties */

                /* long double properties */
                /* (must be same as double) */



                /* INTEGER PROPERTIES */
                                /* MB_LEN_MAX */


  #pragma language=save
  #pragma language=extended
  typedef long long _Longlong;
  typedef unsigned long long _ULonglong;
  #pragma language=restore

  typedef unsigned short int _Wchart;
  typedef unsigned short int _Wintt;



                /* POINTER PROPERTIES */

typedef signed int  _Ptrdifft;
typedef unsigned int     _Sizet;

/* IAR doesn't support restrict  */

                /* stdarg PROPERTIES */
  typedef struct __va_list __Va_list;


__intrinsic __nounwind void __iar_Atexit(void (*)(void));


  typedef struct
  {       /* state of a multibyte translation */
    unsigned int _Wchar;
    unsigned int _State;
  } _Mbstatet;





typedef struct
{       /* file position */
  _Longlong _Off;    /* can be system dependent */
  _Mbstatet _Wstate;
} _Fpost;




                /* THREAD AND LOCALE CONTROL */

/***************************************************
 *
 * DLib_Threads.h is the library threads manager.
 *
 * Copyright 2004-2010 IAR Systems AB.  
 *
 * This configuration header file sets up how the thread support in the library
 * should work.
 *
 ***************************************************
 *
 * DO NOT MODIFY THIS FILE!
 *
 ***************************************************/


  #pragma system_include

/*
 * DLib can support a multithreaded environment. The preprocessor symbol 
 * _DLIB_THREAD_SUPPORT governs the support. It can be 0 (no support), 
 * 1 (currently not supported), 2 (locks only), and 3 (simulated TLS and locks).
 */

/*
 * This header sets the following symbols that governs the rest of the
 * library:
 * ------------------------------------------
 * _DLIB_MULTI_THREAD     0 No thread support
 *                        1 Multithread support
 * _DLIB_GLOBAL_VARIABLES 0 Use external TLS interface for the libraries global
 *                          and static variables
 *                        1 Use a lock for accesses to the locale and no 
 *                          security for accesses to other global and static
 *                          variables in the library
 * _DLIB_FILE_OP_LOCKS    0 No file-atomic locks
 *                        1 File-atomic locks

 * _DLIB_COMPILER_TLS     0 No Thread-Local-Storage support in the compiler
 *                        1 Thread-Local-Storage support in the compiler
 * _DLIB_TLS_QUAL         The TLS qualifier, define only if _COMPILER_TLS == 1
 *
 * _DLIB_THREAD_MACRO_SETUP_DONE Whether to use the standard definitions of
 *                               TLS macros defined in xtls.h or the definitions
 *                               are provided here.
 *                        0 Use default macros
 *                        1 Macros defined for xtls.h
 *
 * _DLIB_THREAD_LOCK_ONCE_TYPE
 *                        type for control variable in once-initialization of 
 *                        locks
 * _DLIB_THREAD_LOCK_ONCE_MACRO(control_variable, init_function)
 *                        expression that will be evaluated at each lock access
 *                        to determine if an initialization must be done
 * _DLIB_THREAD_LOCK_ONCE_TYPE_INIT
 *                        initial value for the control variable
 *
 ****************************************************************************
 * Description
 * -----------
 *
 * If locks are to be used (_DLIB_MULTI_THREAD != 0), the following options
 * has to be used in ilink: 
 *   --redirect __iar_Locksyslock=__iar_Locksyslock_mtx
 *   --redirect __iar_Unlocksyslock=__iar_Unlocksyslock_mtx
 *   --redirect __iar_Lockfilelock=__iar_Lockfilelock_mtx
 *   --redirect __iar_Unlockfilelock=__iar_Unlockfilelock_mtx
 *   --keep     __iar_Locksyslock_mtx
 * and, if C++ is used, also:
 *   --redirect __iar_Initdynamicfilelock=__iar_Initdynamicfilelock_mtx
 *   --redirect __iar_Dstdynamicfilelock=__iar_Dstdynamicfilelock_mtx
 *   --redirect __iar_Lockdynamicfilelock=__iar_Lockdynamicfilelock_mtx
 *   --redirect __iar_Unlockdynamicfilelock=__iar_Unlockdynamicfilelock_mtx
 * Xlink uses similar options (-e and -g). The following lock interface must
 * also be implemented: 
 *   typedef void *__iar_Rmtx;                   // Lock info object
 *
 *   void __iar_system_Mtxinit(__iar_Rmtx *);    // Initialize a system lock
 *   void __iar_system_Mtxdst(__iar_Rmtx *);     // Destroy a system lock
 *   void __iar_system_Mtxlock(__iar_Rmtx *);    // Lock a system lock
 *   void __iar_system_Mtxunlock(__iar_Rmtx *);  // Unlock a system lock
 * The interface handles locks for the heap, the locale, the file system
 * structure, the initialization of statics in functions, etc. 
 *
 * The following lock interface is optional to be implemented:
 *   void __iar_file_Mtxinit(__iar_Rmtx *);    // Initialize a file lock
 *   void __iar_file_Mtxdst(__iar_Rmtx *);     // Destroy a file lock
 *   void __iar_file_Mtxlock(__iar_Rmtx *);    // Lock a file lock
 *   void __iar_file_Mtxunlock(__iar_Rmtx *);  // Unlock a file lock
 * The interface handles locks for each file stream.
 * 
 * These three once-initialization symbols must also be defined, if the 
 * default initialization later on in this file doesn't work (done in 
 * DLib_product.h):
 *
 *   _DLIB_THREAD_LOCK_ONCE_TYPE
 *   _DLIB_THREAD_LOCK_ONCE_MACRO(control_variable, init_function)
 *   _DLIB_THREAD_LOCK_ONCE_TYPE_INIT
 *
 * If an external TLS interface is used, the following must
 * be defined:
 *   typedef int __iar_Tlskey_t;
 *   typedef void (*__iar_Tlsdtor_t)(void *);
 *   int __iar_Tlsalloc(__iar_Tlskey_t *, __iar_Tlsdtor_t); 
 *                                                    // Allocate a TLS element
 *   int __iar_Tlsfree(__iar_Tlskey_t);               // Free a TLS element
 *   int __iar_Tlsset(__iar_Tlskey_t, void *);        // Set a TLS element
 *   void *__iar_Tlsget(__iar_Tlskey_t);              // Get a TLS element
 *
 */

/* We don't have a compiler that supports tls declarations */


  /* Thread support, library supports threaded variables in a user specified
     memory area, locks on heap and on FILE */

  /* See Documentation/ThreadsInternal.html for a description. */


  





  #pragma language=save 
  #pragma language=extended
  __intrinsic __nounwind void __iar_dlib_perthread_initialize(void  *);
  __intrinsic __nounwind void  *__iar_dlib_perthread_allocate(void);
  __intrinsic __nounwind void __iar_dlib_perthread_destroy(void);
  __intrinsic __nounwind void __iar_dlib_perthread_deallocate(void  *);



  #pragma segment = "__DLIB_PERTHREAD" 
  #pragma segment = "__DLIB_PERTHREAD_init" 









  /* The thread-local variable access function */
  void  *__iar_dlib_perthread_access(void  *);
  #pragma language=restore








    /* Make sure that each destructor is inserted into _Deallocate_TLS */
  



  /* Internal function declarations. */

  


  
  typedef void *__iar_Rmtx;
  
  
  __intrinsic __nounwind void __iar_system_Mtxinit(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_system_Mtxdst(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_system_Mtxlock(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_system_Mtxunlock(__iar_Rmtx *m);

  __intrinsic __nounwind void __iar_file_Mtxinit(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_file_Mtxdst(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_file_Mtxlock(__iar_Rmtx *m);
  __intrinsic __nounwind void __iar_file_Mtxunlock(__iar_Rmtx *m);

  /* Function to destroy the locks. Should be called after atexit and 
     _Close_all. */
  __intrinsic __nounwind void __iar_clearlocks(void);



  



  


  typedef unsigned _Once_t;

  








                /* THREAD-LOCAL STORAGE */


                /* MULTITHREAD PROPERTIES */
  
  
  /* The lock interface for DLib to use. */ 
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock_Locale(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock_Malloc(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock_Stream(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock_Debug(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock_StaticGuard(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Locksyslock(unsigned int);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock_Locale(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock_Malloc(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock_Stream(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock_Debug(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock_StaticGuard(void);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlocksyslock(unsigned int);

  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Initdynamicfilelock(__iar_Rmtx *);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Dstdynamicfilelock(__iar_Rmtx *);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Lockdynamicfilelock(__iar_Rmtx *);
  _Pragma("object_attribute = __weak") __intrinsic __nounwind void __iar_Unlockdynamicfilelock(__iar_Rmtx *);
  
  

                /* LOCK MACROS */


                /* MISCELLANEOUS MACROS AND FUNCTIONS*/




/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */


/* Fixed size types. These are all optional. */
  typedef signed char   int8_t;
  typedef unsigned char uint8_t;

  typedef signed short int   int16_t;
  typedef unsigned short int uint16_t;

  typedef signed int   int32_t;
  typedef unsigned int uint32_t;

  #pragma language=save
  #pragma language=extended
  typedef signed long long int   int64_t;
  typedef unsigned long long int uint64_t;
  #pragma language=restore

/* Types capable of holding at least a certain number of bits.
   These are not optional for the sizes 8, 16, 32, 64. */
typedef signed char   int_least8_t;
typedef unsigned char uint_least8_t;

typedef signed short int   int_least16_t;
typedef unsigned short int uint_least16_t;

typedef signed int   int_least32_t;
typedef unsigned int uint_least32_t;

/* This isn't really optional, but make it so for now. */
  #pragma language=save
  #pragma language=extended
  typedef signed long long int int_least64_t;
  #pragma language=restore
  #pragma language=save
  #pragma language=extended
  typedef unsigned long long int uint_least64_t;
  #pragma language=restore

/* The fastest type holding at least a certain number of bits.
   These are not optional for the size 8, 16, 32, 64.
   For now, the 64 bit size is optional in IAR compilers. */
typedef signed int   int_fast8_t;
typedef unsigned int uint_fast8_t;

typedef signed int   int_fast16_t;
typedef unsigned int uint_fast16_t;

typedef signed int   int_fast32_t;
typedef unsigned int uint_fast32_t;

  #pragma language=save
  #pragma language=extended
  typedef signed long long int int_fast64_t;
  #pragma language=restore
  #pragma language=save
  #pragma language=extended
  typedef unsigned long long int uint_fast64_t;
  #pragma language=restore

/* The integer type capable of holding the largest number of bits. */
#pragma language=save
#pragma language=extended
typedef signed long long int   intmax_t;
typedef unsigned long long int uintmax_t;
#pragma language=restore

/* An integer type large enough to be able to hold a pointer.
   This is optional, but always supported in IAR compilers. */
typedef signed long int   intptr_t;
typedef unsigned long int uintptr_t;

/* An integer capable of holding a pointer to a specific memory type. */
typedef int __data_intptr_t; typedef unsigned int __data_uintptr_t;

/* Minimum and maximum limits. */

























/* Macros expanding to integer constants. */











/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
/* stdbool.h header */
/* Copyright 2003-2010 IAR Systems AB.  */

/* NOTE: IAR Extensions must be enabled in order to use the bool type! */


  #pragma system_include







/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
/* string.h standard header */
/* Copyright 2009-2010 IAR Systems AB. */

  #pragma system_include

/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */




/* ysizet.h internal header file. */
/* Copyright 2003-2010 IAR Systems AB.  */


  #pragma system_include

/* ycheck.h internal checking header file. */
/* Copyright 2005-2010 IAR Systems AB. */

/* Note that there is no include guard for this header. This is intentional. */

  #pragma system_include

/* __INTRINSIC
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that intrinsic support could be turned off
 * individually for each file.
 */


/* __AEABI_PORTABILITY_INTERNAL_LEVEL
 *
 * Note: Redefined each time ycheck.h is included, i.e. for each
 * system header, to ensure that ABI support could be turned off/on
 * individually for each file.
 *
 * Possible values for this preprocessor symbol:
 *
 * 0 - ABI portability mode is disabled.
 *
 * 1 - ABI portability mode (version 1) is enabled.
 *
 * All other values are reserved for future use.
 */






                /* type definitions */
typedef _Sizet size_t;

typedef unsigned int __data_size_t;





/**************************************************
 *
 * ARM-specific configuration for string.h in DLib.
 *
 * Copyright 2006 IAR Systems. All rights reserved.
 *
 * $Id: DLib_Product_string.h 78576 2014-05-05 13:37:27Z mats $
 *
 **************************************************/


  #pragma system_include


  
  

  /*
   * The following is pre-declared by the compiler.
   *
   * __INTRINSIC void __aeabi_memset (void *, size_t, int);
   * __INTRINSIC void __aeabi_memcpy (void *, const void *, size_t);
   * __INTRINSIC void __aeabi_memmove(void *, const void *, size_t);
   */


  /*
   * Inhibit inline definitions for routines with an effective
   * ARM-specific implementation.
   *
   * Not in Cortex-M1 and Cortex-MS1
   */




  /*
   * Redirect calls to standard functions to the corresponding
   * __aeabi_X function.
   */

  #pragma inline=forced_no_body
  __intrinsic __nounwind void * memcpy(void * _D, const void * _S, size_t _N)
  {
    __aeabi_memcpy(_D, _S, _N);
    return _D;
  }

  #pragma inline=forced_no_body
  __intrinsic __nounwind void * memmove(void * _D, const void * _S, size_t _N)
  {
    __aeabi_memmove(_D, _S, _N);
    return _D;
  }

  #pragma inline=forced_no_body
  __intrinsic __nounwind void * memset(void * _D, int _C, size_t _N)
  {
    __aeabi_memset(_D, _N, _C);
    return _D;
  }

  
  




                /* macros */

                /* declarations */

_Pragma("function_effects = no_state, no_write(1,2), always_returns")   __intrinsic __nounwind int        memcmp(const void *, const void *,
                                                size_t);
_Pragma("function_effects = no_state, no_read(1), no_write(2), returns 1, always_returns") __intrinsic __nounwind void *     memcpy(void *, 
                                                const void *, size_t);
_Pragma("function_effects = no_state, no_read(1), no_write(2), returns 1, always_returns") __intrinsic __nounwind void *     memmove(void *, const void *, size_t);
_Pragma("function_effects = no_state, no_read(1), returns 1, always_returns")    __intrinsic __nounwind void *     memset(void *, int, size_t);
_Pragma("function_effects = no_state, no_write(2), returns 1, always_returns")    __intrinsic __nounwind char *     strcat(char *, 
                                                const char *);
_Pragma("function_effects = no_state, no_write(1,2), always_returns")   __intrinsic __nounwind int        strcmp(const char *, const char *);
_Pragma("function_effects = no_write(1,2), always_returns")     __intrinsic __nounwind int        strcoll(const char *, const char *);
_Pragma("function_effects = no_state, no_read(1), no_write(2), returns 1, always_returns") __intrinsic __nounwind char *     strcpy(char *, 
                                                const char *);
_Pragma("function_effects = no_state, no_write(1,2), always_returns")   __intrinsic __nounwind size_t     strcspn(const char *, const char *);
                 __intrinsic __nounwind char *     strerror(int);
_Pragma("function_effects = no_state, no_write(1), always_returns")      __intrinsic __nounwind size_t     strlen(const char *);
_Pragma("function_effects = no_state, no_write(2), returns 1, always_returns")    __intrinsic __nounwind char *     strncat(char *, 
                                                 const char *, size_t);
_Pragma("function_effects = no_state, no_write(1,2), always_returns")   __intrinsic __nounwind int        strncmp(const char *, const char *, 
                                                 size_t);
_Pragma("function_effects = no_state, no_read(1), no_write(2), returns 1, always_returns") __intrinsic __nounwind char *     strncpy(char *, 
                                                 const char *, size_t);
_Pragma("function_effects = no_state, no_write(1,2), always_returns")   __intrinsic __nounwind size_t     strspn(const char *, const char *);
_Pragma("function_effects = no_write(2), always_returns")        __intrinsic __nounwind char *     strtok(char *, 
                                                const char *);
_Pragma("function_effects = no_write(2), always_returns")        __intrinsic __nounwind size_t     strxfrm(char *, 
                                                 const char *, size_t);

  _Pragma("function_effects = no_write(1), always_returns")      __intrinsic __nounwind char *   strdup(const char *);
  _Pragma("function_effects = no_write(1,2), always_returns")   __intrinsic __nounwind int      strcasecmp(const char *, const char *);
  _Pragma("function_effects = no_write(1,2), always_returns")   __intrinsic __nounwind int      strncasecmp(const char *, const char *, 
                                                   size_t);
  _Pragma("function_effects = no_state, no_write(2), always_returns")    __intrinsic __nounwind char *   strtok_r(char *, const char *, char **);
  _Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind size_t   strnlen(char const *, size_t);



  _Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind void *memchr(const void *_S, int _C, size_t _N);
  _Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind char *strchr(const char *_S, int _C);
  _Pragma("function_effects = no_state, no_write(1,2), always_returns") __intrinsic __nounwind char *strpbrk(const char *_S, const char *_P);
  _Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind char *strrchr(const char *_S, int _C);
  _Pragma("function_effects = no_state, no_write(1,2), always_returns") __intrinsic __nounwind char *strstr(const char *_S, const char *_P);


                /* Inline definitions. */

                /* The implementations. */

_Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind void *__iar_Memchr(const void *, int, size_t);
_Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind char *__iar_Strchr(const char *, int);
               __intrinsic __nounwind char *__iar_Strerror(int, char *);
_Pragma("function_effects = no_state, no_write(1,2), always_returns") __intrinsic __nounwind char *__iar_Strpbrk(const char *, const char *);
_Pragma("function_effects = no_state, no_write(1), always_returns")    __intrinsic __nounwind char *__iar_Strrchr(const char *, int);
_Pragma("function_effects = no_state, no_write(1,2), always_returns") __intrinsic __nounwind char *__iar_Strstr(const char *, const char *);


                /* inlines and overloads, for C and C++ */
                /* Then the overloads for C. */
    #pragma inline
    void *memchr(const void *_S, int _C, size_t _N)
    {
      return (__iar_Memchr(_S, _C, _N));
    }

    #pragma inline
    char *strchr(const char *_S, int _C)
    {
      return (__iar_Strchr(_S, _C));
    }

    #pragma inline
    char *strpbrk(const char *_S, const char *_P)
    {
      return (__iar_Strpbrk(_S, _P));
    }

    #pragma inline
    char *strrchr(const char *_S, int _C)
    {
      return (__iar_Strrchr(_S, _C));
    }

    #pragma inline
    char *strstr(const char *_S, const char *_P)
    {
      return (__iar_Strstr(_S, _P));
    }

  #pragma inline
  char *strerror(int _Err)
  {
    return (__iar_Strerror(_Err, 0));
  }






/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
    // EFR32, EZR32
      //EZR32WG
/**************************************************************************//**
 * @file em_device.h
 * @brief CMSIS Cortex-M Peripheral Access Layer for Silicon Laboratories
 *        microcontroller devices
 *
 * This is a convenience header file for defining the part number on the
 * build command line, instead of specifying the part specific header file.
 *
 * @verbatim
 * Example: Add "-DEFM32G890F128" to your build options, to define part
 *          Add "#include "em_device.h" to your source files
 *
 *
 * @endverbatim
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/


/**************************************************************************//**
 * @file ezr32wg330f256r60.h
 * @brief CMSIS Cortex-M Peripheral Access Layer Header File
 *        for EZR32WG330F256R60
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/



/**************************************************************************//**
 * @addtogroup Parts
 * @{
 *****************************************************************************/

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60 EZR32WG330F256R60
 * @{
 *****************************************************************************/

/** Interrupt Number Definition */
typedef enum IRQn
{
/******  Cortex-M4 Processor Exceptions Numbers *******************************************/
  NonMaskableInt_IRQn   = -14,              /*!< 2 Cortex-M4 Non Maskable Interrupt       */
  HardFault_IRQn        = -13,              /*!< 3 Cortex-M4 Hard Fault Interrupt         */
  MemoryManagement_IRQn = -12,              /*!< 4 Cortex-M4 Memory Management Interrupt  */
  BusFault_IRQn         = -11,              /*!< 5 Cortex-M4 Bus Fault Interrupt          */
  UsageFault_IRQn       = -10,              /*!< 6 Cortex-M4 Usage Fault Interrupt        */
  SVCall_IRQn           = -5,               /*!< 11 Cortex-M4 SV Call Interrupt           */
  DebugMonitor_IRQn     = -4,               /*!< 12 Cortex-M4 Debug Monitor Interrupt     */
  PendSV_IRQn           = -2,               /*!< 14 Cortex-M4 Pend SV Interrupt           */
  SysTick_IRQn          = -1,               /*!< 15 Cortex-M4 System Tick Interrupt       */

/******  EZR32WG Peripheral Interrupt Numbers *********************************************/
  DMA_IRQn              = 0,  /*!< 16+0 EZR32 DMA Interrupt */
  GPIO_EVEN_IRQn        = 1,  /*!< 16+1 EZR32 GPIO_EVEN Interrupt */
  TIMER0_IRQn           = 2,  /*!< 16+2 EZR32 TIMER0 Interrupt */
  USARTRF0_RX_IRQn      = 3,  /*!< 16+3 EZR32 USARTRF0_RX Interrupt */
  USARTRF0_TX_IRQn      = 4,  /*!< 16+4 EZR32 USARTRF0_TX Interrupt */
  USB_IRQn              = 5,  /*!< 16+5 EZR32 USB Interrupt */
  ACMP0_IRQn            = 6,  /*!< 16+6 EZR32 ACMP0 Interrupt */
  ADC0_IRQn             = 7,  /*!< 16+7 EZR32 ADC0 Interrupt */
  DAC0_IRQn             = 8,  /*!< 16+8 EZR32 DAC0 Interrupt */
  I2C0_IRQn             = 9,  /*!< 16+9 EZR32 I2C0 Interrupt */
  I2C1_IRQn             = 10, /*!< 16+10 EZR32 I2C1 Interrupt */
  GPIO_ODD_IRQn         = 11, /*!< 16+11 EZR32 GPIO_ODD Interrupt */
  TIMER1_IRQn           = 12, /*!< 16+12 EZR32 TIMER1 Interrupt */
  TIMER2_IRQn           = 13, /*!< 16+13 EZR32 TIMER2 Interrupt */
  TIMER3_IRQn           = 14, /*!< 16+14 EZR32 TIMER3 Interrupt */
  USART1_RX_IRQn        = 15, /*!< 16+15 EZR32 USART1_RX Interrupt */
  USART1_TX_IRQn        = 16, /*!< 16+16 EZR32 USART1_TX Interrupt */
  LESENSE_IRQn          = 17, /*!< 16+17 EZR32 LESENSE Interrupt */
  USART2_RX_IRQn        = 18, /*!< 16+18 EZR32 USART2_RX Interrupt */
  USART2_TX_IRQn        = 19, /*!< 16+19 EZR32 USART2_TX Interrupt */
  UART0_RX_IRQn         = 20, /*!< 16+20 EZR32 UART0_RX Interrupt */
  UART0_TX_IRQn         = 21, /*!< 16+21 EZR32 UART0_TX Interrupt */
  UART1_RX_IRQn         = 22, /*!< 16+22 EZR32 UART1_RX Interrupt */
  UART1_TX_IRQn         = 23, /*!< 16+23 EZR32 UART1_TX Interrupt */
  LEUART0_IRQn          = 24, /*!< 16+24 EZR32 LEUART0 Interrupt */
  LEUART1_IRQn          = 25, /*!< 16+25 EZR32 LEUART1 Interrupt */
  LETIMER0_IRQn         = 26, /*!< 16+26 EZR32 LETIMER0 Interrupt */
  PCNT0_IRQn            = 27, /*!< 16+27 EZR32 PCNT0 Interrupt */
  PCNT1_IRQn            = 28, /*!< 16+28 EZR32 PCNT1 Interrupt */
  PCNT2_IRQn            = 29, /*!< 16+29 EZR32 PCNT2 Interrupt */
  RTC_IRQn              = 30, /*!< 16+30 EZR32 RTC Interrupt */
  BURTC_IRQn            = 31, /*!< 16+31 EZR32 BURTC Interrupt */
  CMU_IRQn              = 32, /*!< 16+32 EZR32 CMU Interrupt */
  VCMP_IRQn             = 33, /*!< 16+33 EZR32 VCMP Interrupt */
  MSC_IRQn              = 35, /*!< 16+35 EZR32 MSC Interrupt */
  AES_IRQn              = 36, /*!< 16+36 EZR32 AES Interrupt */
  EMU_IRQn              = 38, /*!< 16+38 EZR32 EMU Interrupt */
  FPUEH_IRQn            = 39, /*!< 16+39 EZR32 FPUEH Interrupt */
} IRQn_Type;

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_Core EZR32WG330F256R60 Core
 * @{
 * @brief Processor and Core Peripheral Section
 *****************************************************************************/

/** @} End of group EZR32WG330F256R60_Core */

/**************************************************************************//**
* @defgroup EZR32WG330F256R60_Part EZR32WG330F256R60 Part
* @{
******************************************************************************/

/** Part family */

/* If part number is not defined as compiler option, define it */

/** Configure part number */

/** Memory Base addresses and limits */

/** Bit banding area */

/** Flash and SRAM limits for EZR32WG330F256R60 */

/** AF channels connect the different on-chip peripherals with the af-mux */
/** Analog AF channels */

/* Part number capabilities */


/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_RF_Interface EZR32WG330F256R60 RF_Interface
 * @brief MCU port/pins used for RF interface.
 * @{
 *****************************************************************************/

/** @} End of group EZR32WG330F256R60_RF_Interface */

/**************************************************************************//**
 * @file     core_cm4.h
 * @brief    CMSIS Cortex-M4 Core Peripheral Access Layer Header File
 * @version  V4.00
 * @date     22. August 2014
 *
 * @note
 *
 ******************************************************************************/
/* Copyright (c) 2009 - 2014 ARM LIMITED

   All rights reserved.
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
   - Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   - Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
   - Neither the name of ARM nor the names of its contributors may be used
     to endorse or promote products derived from this software without
     specific prior written permission.
   *
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
   ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDERS AND CONTRIBUTORS BE
   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
   POSSIBILITY OF SUCH DAMAGE.
   ---------------------------------------------------------------------------*/


 #pragma system_include  /* treat file as system include file for MISRA check */



/** \page CMSIS_MISRA_Exceptions  MISRA-C:2004 Compliance Exceptions
  CMSIS violates the following MISRA-C:2004 rules:

   \li Required Rule 8.5, object/function definition in header file.<br>
     Function definitions in header files are used to allow 'inlining'.

   \li Required Rule 18.4, declaration of union type or object of union type: '{...}'.<br>
     Unions are used for effective representation of core registers.

   \li Advisory Rule 19.7, Function-like macro defined.<br>
     Function-like macros are used to allow more efficient code.
 */


/*******************************************************************************
 *                 CMSIS definitions
 ******************************************************************************/
/** \ingroup Cortex_M4
  @{
 */

/*  CMSIS CM4 definitions */





/** __FPU_USED indicates whether an FPU is used or not.
    For this, __FPU_PRESENT has to be checked prior to making use of FPU specific registers and functions.
*/


/* stdint.h standard header */
/* Copyright 2003-2010 IAR Systems AB.  */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
/**************************************************************************//**
 * @file     core_cmInstr.h
 * @brief    CMSIS Cortex-M Core Instruction Access Header File
 * @version  V4.00
 * @date     28. August 2014
 *
 * @note
 *
 ******************************************************************************/
/* Copyright (c) 2009 - 2014 ARM LIMITED

   All rights reserved.
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
   - Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   - Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
   - Neither the name of ARM nor the names of its contributors may be used
     to endorse or promote products derived from this software without
     specific prior written permission.
   *
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
   ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDERS AND CONTRIBUTORS BE
   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
   POSSIBILITY OF SUCH DAMAGE.
   ---------------------------------------------------------------------------*/




/* ##########################  Core Instruction Access  ######################### */
/** \defgroup CMSIS_Core_InstructionInterface CMSIS Core Instruction Interface
  Access to dedicated instructions
  @{
*/

/* IAR iccarm specific functions */
/**************************************************
 *
 * This file shall be included in appropriate CMSIS header
 * files, to provide required functions and intrinsics when
 * building with the IAR C/C++ Compiler for ARM (iccarm).
 *
 * Copyright 2011 IAR Systems. All rights reserved.
 *
 * $Revision: 78346 $
 *
 **************************************************/



#pragma system_include



#pragma diag_suppress=Pe940
#pragma diag_suppress=Pe177






static uint32_t __get_xPSR(void)
{
  return __get_PSR();   /* __get_PSR() intrinsic introduced in iccarm 6.20 */
}












static inline uint32_t __RRX(uint32_t value)
{
  uint32_t result;
  __asm("RRX %0, %1" : "=r"(result) : "r" (value) );
  return(result);
}

static inline uint8_t __LDRBT(volatile uint8_t *addr)
{
  uint32_t result;
  __asm("LDRBT %0, [%1]" : "=r" (result) : "r" (addr) : "memory" );
  return ((uint8_t) result);
}

static inline uint16_t __LDRHT(volatile uint16_t *addr)
{
  uint32_t result;
  __asm("LDRHT %0, [%1]" : "=r" (result) : "r" (addr) : "memory" );
  return ((uint16_t) result);
}

static inline uint32_t __LDRT(volatile uint32_t *addr)
{
  uint32_t result;
  __asm("LDRT %0, [%1]" : "=r" (result) : "r" (addr) : "memory" );
  return(result);
}

static inline void __STRBT(uint8_t value, volatile uint8_t *addr)
{
  __asm("STRBT %1, [%0]" : : "r" (addr), "r" ((uint32_t)value) : "memory" );
}

static inline void __STRHT(uint16_t value, volatile uint16_t *addr)
{
  __asm("STRHT %1, [%0]" : : "r" (addr), "r" ((uint32_t)value) : "memory" );
}

static inline void __STRT(uint32_t value, volatile uint32_t *addr)
{
  __asm("STRT %1, [%0]" : : "r" (addr), "r" (value) : "memory" );
}



static inline uint32_t __ROR(uint32_t op1, uint32_t op2)
{
  return (op1 >> op2) | (op1 << ((sizeof(op1)*8)-op2));
}

#pragma diag_default=Pe940
#pragma diag_default=Pe177




/*@}*/ /* end of group CMSIS_Core_InstructionInterface */

/**************************************************************************//**
 * @file     core_cmFunc.h
 * @brief    CMSIS Cortex-M Core Function Access Header File
 * @version  V4.00
 * @date     28. August 2014
 *
 * @note
 *
 ******************************************************************************/
/* Copyright (c) 2009 - 2014 ARM LIMITED

   All rights reserved.
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
   - Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   - Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
   - Neither the name of ARM nor the names of its contributors may be used
     to endorse or promote products derived from this software without
     specific prior written permission.
   *
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
   ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDERS AND CONTRIBUTORS BE
   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
   POSSIBILITY OF SUCH DAMAGE.
   ---------------------------------------------------------------------------*/




/* ###########################  Core Function Access  ########################### */
/** \ingroup  CMSIS_Core_FunctionInterface
    \defgroup CMSIS_Core_RegAccFunctions CMSIS Core Register Access Functions
  @{
 */

/* IAR iccarm specific functions */



/*@} end of CMSIS_Core_RegAccFunctions */

/**************************************************************************//**
 * @file     core_cmSimd.h
 * @brief    CMSIS Cortex-M SIMD Header File
 * @version  V4.00
 * @date     22. August 2014
 *
 * @note
 *
 ******************************************************************************/
/* Copyright (c) 2009 - 2014 ARM LIMITED

   All rights reserved.
   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are met:
   - Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.
   - Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.
   - Neither the name of ARM nor the names of its contributors may be used
     to endorse or promote products derived from this software without
     specific prior written permission.
   *
   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
   ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDERS AND CONTRIBUTORS BE
   LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
   SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
   INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
   CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
   ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
   POSSIBILITY OF SUCH DAMAGE.
   ---------------------------------------------------------------------------*/


 #pragma system_include  /* treat file as system include file for MISRA check */




/*******************************************************************************
 *                Hardware Abstraction Layer
 ******************************************************************************/


/* ###################  Compiler specific Intrinsics  ########################### */
/** \defgroup CMSIS_SIMD_intrinsics CMSIS SIMD Intrinsics
  Access to dedicated SIMD instructions
  @{
*/

/* IAR iccarm specific functions */



/*@} end of group CMSIS_SIMD_intrinsics */









/* check device defines and use defaults */

/* IO definitions (access restrictions to peripheral registers) */
/**
    \defgroup CMSIS_glob_defs CMSIS Global Defines

    <strong>IO Type Qualifiers</strong> are used
    \li to specify the access to peripheral variables.
    \li for automatic generation of peripheral register debug information.
*/

/*@} end of group Cortex_M4 */



/*******************************************************************************
 *                 Register Abstraction
  Core Register contain:
  - Core Register
  - Core NVIC Register
  - Core SCB Register
  - Core SysTick Register
  - Core Debug Register
  - Core MPU Register
  - Core FPU Register
 ******************************************************************************/
/** \defgroup CMSIS_core_register Defines and Type Definitions
    \brief Type definitions and defines for Cortex-M processor based devices.
*/

/** \ingroup    CMSIS_core_register
    \defgroup   CMSIS_CORE  Status and Control Registers
    \brief  Core Register type definitions.
  @{
 */

/** \brief  Union type to access the Application Program Status Register (APSR).
 */
typedef union
{
  struct
  {
    uint32_t _reserved0:16;              /*!< bit:  0..15  Reserved                           */
    uint32_t GE:4;                       /*!< bit: 16..19  Greater than or Equal flags        */
    uint32_t _reserved1:7;               /*!< bit: 20..26  Reserved                           */
    uint32_t Q:1;                        /*!< bit:     27  Saturation condition flag          */
    uint32_t V:1;                        /*!< bit:     28  Overflow condition code flag       */
    uint32_t C:1;                        /*!< bit:     29  Carry condition code flag          */
    uint32_t Z:1;                        /*!< bit:     30  Zero condition code flag           */
    uint32_t N:1;                        /*!< bit:     31  Negative condition code flag       */
  } b;                                   /*!< Structure used for bit  access                  */
  uint32_t w;                            /*!< Type      used for word access                  */
} APSR_Type;


/** \brief  Union type to access the Interrupt Program Status Register (IPSR).
 */
typedef union
{
  struct
  {
    uint32_t ISR:9;                      /*!< bit:  0.. 8  Exception number                   */
    uint32_t _reserved0:23;              /*!< bit:  9..31  Reserved                           */
  } b;                                   /*!< Structure used for bit  access                  */
  uint32_t w;                            /*!< Type      used for word access                  */
} IPSR_Type;


/** \brief  Union type to access the Special-Purpose Program Status Registers (xPSR).
 */
typedef union
{
  struct
  {
    uint32_t ISR:9;                      /*!< bit:  0.. 8  Exception number                   */
    uint32_t _reserved0:7;               /*!< bit:  9..15  Reserved                           */
    uint32_t GE:4;                       /*!< bit: 16..19  Greater than or Equal flags        */
    uint32_t _reserved1:4;               /*!< bit: 20..23  Reserved                           */
    uint32_t T:1;                        /*!< bit:     24  Thumb bit        (read 0)          */
    uint32_t IT:2;                       /*!< bit: 25..26  saved IT state   (read 0)          */
    uint32_t Q:1;                        /*!< bit:     27  Saturation condition flag          */
    uint32_t V:1;                        /*!< bit:     28  Overflow condition code flag       */
    uint32_t C:1;                        /*!< bit:     29  Carry condition code flag          */
    uint32_t Z:1;                        /*!< bit:     30  Zero condition code flag           */
    uint32_t N:1;                        /*!< bit:     31  Negative condition code flag       */
  } b;                                   /*!< Structure used for bit  access                  */
  uint32_t w;                            /*!< Type      used for word access                  */
} xPSR_Type;


/** \brief  Union type to access the Control Registers (CONTROL).
 */
typedef union
{
  struct
  {
    uint32_t nPRIV:1;                    /*!< bit:      0  Execution privilege in Thread mode */
    uint32_t SPSEL:1;                    /*!< bit:      1  Stack to be used                   */
    uint32_t FPCA:1;                     /*!< bit:      2  FP extension active flag           */
    uint32_t _reserved0:29;              /*!< bit:  3..31  Reserved                           */
  } b;                                   /*!< Structure used for bit  access                  */
  uint32_t w;                            /*!< Type      used for word access                  */
} CONTROL_Type;

/*@} end of group CMSIS_CORE */


/** \ingroup    CMSIS_core_register
    \defgroup   CMSIS_NVIC  Nested Vectored Interrupt Controller (NVIC)
    \brief      Type definitions for the NVIC Registers
  @{
 */

/** \brief  Structure type to access the Nested Vectored Interrupt Controller (NVIC).
 */
typedef struct
{
  volatile uint32_t ISER[8];                 /*!< Offset: 0x000 (R/W)  Interrupt Set Enable Register           */
       uint32_t RESERVED0[24];
  volatile uint32_t ICER[8];                 /*!< Offset: 0x080 (R/W)  Interrupt Clear Enable Register         */
       uint32_t RSERVED1[24];
  volatile uint32_t ISPR[8];                 /*!< Offset: 0x100 (R/W)  Interrupt Set Pending Register          */
       uint32_t RESERVED2[24];
  volatile uint32_t ICPR[8];                 /*!< Offset: 0x180 (R/W)  Interrupt Clear Pending Register        */
       uint32_t RESERVED3[24];
  volatile uint32_t IABR[8];                 /*!< Offset: 0x200 (R/W)  Interrupt Active bit Register           */
       uint32_t RESERVED4[56];
  volatile uint8_t  IP[240];                 /*!< Offset: 0x300 (R/W)  Interrupt Priority Register (8Bit wide) */
       uint32_t RESERVED5[644];
  volatile  uint32_t STIR;                    /*!< Offset: 0xE00 ( /W)  Software Trigger Interrupt Register     */
}  NVIC_Type;

/* Software Triggered Interrupt Register Definitions */

/*@} end of group CMSIS_NVIC */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_SCB     System Control Block (SCB)
    \brief      Type definitions for the System Control Block Registers
  @{
 */

/** \brief  Structure type to access the System Control Block (SCB).
 */
typedef struct
{
  volatile const  uint32_t CPUID;                   /*!< Offset: 0x000 (R/ )  CPUID Base Register                                   */
  volatile uint32_t ICSR;                    /*!< Offset: 0x004 (R/W)  Interrupt Control and State Register                  */
  volatile uint32_t VTOR;                    /*!< Offset: 0x008 (R/W)  Vector Table Offset Register                          */
  volatile uint32_t AIRCR;                   /*!< Offset: 0x00C (R/W)  Application Interrupt and Reset Control Register      */
  volatile uint32_t SCR;                     /*!< Offset: 0x010 (R/W)  System Control Register                               */
  volatile uint32_t CCR;                     /*!< Offset: 0x014 (R/W)  Configuration Control Register                        */
  volatile uint8_t  SHP[12];                 /*!< Offset: 0x018 (R/W)  System Handlers Priority Registers (4-7, 8-11, 12-15) */
  volatile uint32_t SHCSR;                   /*!< Offset: 0x024 (R/W)  System Handler Control and State Register             */
  volatile uint32_t CFSR;                    /*!< Offset: 0x028 (R/W)  Configurable Fault Status Register                    */
  volatile uint32_t HFSR;                    /*!< Offset: 0x02C (R/W)  HardFault Status Register                             */
  volatile uint32_t DFSR;                    /*!< Offset: 0x030 (R/W)  Debug Fault Status Register                           */
  volatile uint32_t MMFAR;                   /*!< Offset: 0x034 (R/W)  MemManage Fault Address Register                      */
  volatile uint32_t BFAR;                    /*!< Offset: 0x038 (R/W)  BusFault Address Register                             */
  volatile uint32_t AFSR;                    /*!< Offset: 0x03C (R/W)  Auxiliary Fault Status Register                       */
  volatile const  uint32_t PFR[2];                  /*!< Offset: 0x040 (R/ )  Processor Feature Register                            */
  volatile const  uint32_t DFR;                     /*!< Offset: 0x048 (R/ )  Debug Feature Register                                */
  volatile const  uint32_t ADR;                     /*!< Offset: 0x04C (R/ )  Auxiliary Feature Register                            */
  volatile const  uint32_t MMFR[4];                 /*!< Offset: 0x050 (R/ )  Memory Model Feature Register                         */
  volatile const  uint32_t ISAR[5];                 /*!< Offset: 0x060 (R/ )  Instruction Set Attributes Register                   */
       uint32_t RESERVED0[5];
  volatile uint32_t CPACR;                   /*!< Offset: 0x088 (R/W)  Coprocessor Access Control Register                   */
} SCB_Type;

/* SCB CPUID Register Definitions */





/* SCB Interrupt Control State Register Definitions */










/* SCB Vector Table Offset Register Definitions */

/* SCB Application Interrupt and Reset Control Register Definitions */







/* SCB System Control Register Definitions */



/* SCB Configuration Control Register Definitions */






/* SCB System Handler Control and State Register Definitions */














/* SCB Configurable Fault Status Registers Definitions */



/* SCB Hard Fault Status Registers Definitions */



/* SCB Debug Fault Status Register Definitions */





/*@} end of group CMSIS_SCB */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_SCnSCB System Controls not in SCB (SCnSCB)
    \brief      Type definitions for the System Control and ID Register not in the SCB
  @{
 */

/** \brief  Structure type to access the System Control and ID Register not in the SCB.
 */
typedef struct
{
       uint32_t RESERVED0[1];
  volatile const  uint32_t ICTR;                    /*!< Offset: 0x004 (R/ )  Interrupt Controller Type Register      */
  volatile uint32_t ACTLR;                   /*!< Offset: 0x008 (R/W)  Auxiliary Control Register              */
} SCnSCB_Type;

/* Interrupt Controller Type Register Definitions */

/* Auxiliary Control Register Definitions */





/*@} end of group CMSIS_SCnotSCB */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_SysTick     System Tick Timer (SysTick)
    \brief      Type definitions for the System Timer Registers.
  @{
 */

/** \brief  Structure type to access the System Timer (SysTick).
 */
typedef struct
{
  volatile uint32_t CTRL;                    /*!< Offset: 0x000 (R/W)  SysTick Control and Status Register */
  volatile uint32_t LOAD;                    /*!< Offset: 0x004 (R/W)  SysTick Reload Value Register       */
  volatile uint32_t VAL;                     /*!< Offset: 0x008 (R/W)  SysTick Current Value Register      */
  volatile const  uint32_t CALIB;                   /*!< Offset: 0x00C (R/ )  SysTick Calibration Register        */
} SysTick_Type;

/* SysTick Control / Status Register Definitions */




/* SysTick Reload Register Definitions */

/* SysTick Current Register Definitions */

/* SysTick Calibration Register Definitions */



/*@} end of group CMSIS_SysTick */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_ITM     Instrumentation Trace Macrocell (ITM)
    \brief      Type definitions for the Instrumentation Trace Macrocell (ITM)
  @{
 */

/** \brief  Structure type to access the Instrumentation Trace Macrocell Register (ITM).
 */
typedef struct
{
  volatile  union
  {
    volatile  uint8_t    u8;                  /*!< Offset: 0x000 ( /W)  ITM Stimulus Port 8-bit                   */
    volatile  uint16_t   u16;                 /*!< Offset: 0x000 ( /W)  ITM Stimulus Port 16-bit                  */
    volatile  uint32_t   u32;                 /*!< Offset: 0x000 ( /W)  ITM Stimulus Port 32-bit                  */
  }  PORT [32];                          /*!< Offset: 0x000 ( /W)  ITM Stimulus Port Registers               */
       uint32_t RESERVED0[864];
  volatile uint32_t TER;                     /*!< Offset: 0xE00 (R/W)  ITM Trace Enable Register                 */
       uint32_t RESERVED1[15];
  volatile uint32_t TPR;                     /*!< Offset: 0xE40 (R/W)  ITM Trace Privilege Register              */
       uint32_t RESERVED2[15];
  volatile uint32_t TCR;                     /*!< Offset: 0xE80 (R/W)  ITM Trace Control Register                */
       uint32_t RESERVED3[29];
  volatile  uint32_t IWR;                     /*!< Offset: 0xEF8 ( /W)  ITM Integration Write Register            */
  volatile const  uint32_t IRR;                     /*!< Offset: 0xEFC (R/ )  ITM Integration Read Register             */
  volatile uint32_t IMCR;                    /*!< Offset: 0xF00 (R/W)  ITM Integration Mode Control Register     */
       uint32_t RESERVED4[43];
  volatile  uint32_t LAR;                     /*!< Offset: 0xFB0 ( /W)  ITM Lock Access Register                  */
  volatile const  uint32_t LSR;                     /*!< Offset: 0xFB4 (R/ )  ITM Lock Status Register                  */
       uint32_t RESERVED5[6];
  volatile const  uint32_t PID4;                    /*!< Offset: 0xFD0 (R/ )  ITM Peripheral Identification Register #4 */
  volatile const  uint32_t PID5;                    /*!< Offset: 0xFD4 (R/ )  ITM Peripheral Identification Register #5 */
  volatile const  uint32_t PID6;                    /*!< Offset: 0xFD8 (R/ )  ITM Peripheral Identification Register #6 */
  volatile const  uint32_t PID7;                    /*!< Offset: 0xFDC (R/ )  ITM Peripheral Identification Register #7 */
  volatile const  uint32_t PID0;                    /*!< Offset: 0xFE0 (R/ )  ITM Peripheral Identification Register #0 */
  volatile const  uint32_t PID1;                    /*!< Offset: 0xFE4 (R/ )  ITM Peripheral Identification Register #1 */
  volatile const  uint32_t PID2;                    /*!< Offset: 0xFE8 (R/ )  ITM Peripheral Identification Register #2 */
  volatile const  uint32_t PID3;                    /*!< Offset: 0xFEC (R/ )  ITM Peripheral Identification Register #3 */
  volatile const  uint32_t CID0;                    /*!< Offset: 0xFF0 (R/ )  ITM Component  Identification Register #0 */
  volatile const  uint32_t CID1;                    /*!< Offset: 0xFF4 (R/ )  ITM Component  Identification Register #1 */
  volatile const  uint32_t CID2;                    /*!< Offset: 0xFF8 (R/ )  ITM Component  Identification Register #2 */
  volatile const  uint32_t CID3;                    /*!< Offset: 0xFFC (R/ )  ITM Component  Identification Register #3 */
} ITM_Type;

/* ITM Trace Privilege Register Definitions */

/* ITM Trace Control Register Definitions */









/* ITM Integration Write Register Definitions */

/* ITM Integration Read Register Definitions */

/* ITM Integration Mode Control Register Definitions */

/* ITM Lock Status Register Definitions */



/*@}*/ /* end of group CMSIS_ITM */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_DWT     Data Watchpoint and Trace (DWT)
    \brief      Type definitions for the Data Watchpoint and Trace (DWT)
  @{
 */

/** \brief  Structure type to access the Data Watchpoint and Trace Register (DWT).
 */
typedef struct
{
  volatile uint32_t CTRL;                    /*!< Offset: 0x000 (R/W)  Control Register                          */
  volatile uint32_t CYCCNT;                  /*!< Offset: 0x004 (R/W)  Cycle Count Register                      */
  volatile uint32_t CPICNT;                  /*!< Offset: 0x008 (R/W)  CPI Count Register                        */
  volatile uint32_t EXCCNT;                  /*!< Offset: 0x00C (R/W)  Exception Overhead Count Register         */
  volatile uint32_t SLEEPCNT;                /*!< Offset: 0x010 (R/W)  Sleep Count Register                      */
  volatile uint32_t LSUCNT;                  /*!< Offset: 0x014 (R/W)  LSU Count Register                        */
  volatile uint32_t FOLDCNT;                 /*!< Offset: 0x018 (R/W)  Folded-instruction Count Register         */
  volatile const  uint32_t PCSR;                    /*!< Offset: 0x01C (R/ )  Program Counter Sample Register           */
  volatile uint32_t COMP0;                   /*!< Offset: 0x020 (R/W)  Comparator Register 0                     */
  volatile uint32_t MASK0;                   /*!< Offset: 0x024 (R/W)  Mask Register 0                           */
  volatile uint32_t FUNCTION0;               /*!< Offset: 0x028 (R/W)  Function Register 0                       */
       uint32_t RESERVED0[1];
  volatile uint32_t COMP1;                   /*!< Offset: 0x030 (R/W)  Comparator Register 1                     */
  volatile uint32_t MASK1;                   /*!< Offset: 0x034 (R/W)  Mask Register 1                           */
  volatile uint32_t FUNCTION1;               /*!< Offset: 0x038 (R/W)  Function Register 1                       */
       uint32_t RESERVED1[1];
  volatile uint32_t COMP2;                   /*!< Offset: 0x040 (R/W)  Comparator Register 2                     */
  volatile uint32_t MASK2;                   /*!< Offset: 0x044 (R/W)  Mask Register 2                           */
  volatile uint32_t FUNCTION2;               /*!< Offset: 0x048 (R/W)  Function Register 2                       */
       uint32_t RESERVED2[1];
  volatile uint32_t COMP3;                   /*!< Offset: 0x050 (R/W)  Comparator Register 3                     */
  volatile uint32_t MASK3;                   /*!< Offset: 0x054 (R/W)  Mask Register 3                           */
  volatile uint32_t FUNCTION3;               /*!< Offset: 0x058 (R/W)  Function Register 3                       */
} DWT_Type;

/* DWT Control Register Definitions */


















/* DWT CPI Count Register Definitions */

/* DWT Exception Overhead Count Register Definitions */

/* DWT Sleep Count Register Definitions */

/* DWT LSU Count Register Definitions */

/* DWT Folded-instruction Count Register Definitions */

/* DWT Comparator Mask Register Definitions */

/* DWT Comparator Function Register Definitions */









/*@}*/ /* end of group CMSIS_DWT */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_TPI     Trace Port Interface (TPI)
    \brief      Type definitions for the Trace Port Interface (TPI)
  @{
 */

/** \brief  Structure type to access the Trace Port Interface Register (TPI).
 */
typedef struct
{
  volatile uint32_t SSPSR;                   /*!< Offset: 0x000 (R/ )  Supported Parallel Port Size Register     */
  volatile uint32_t CSPSR;                   /*!< Offset: 0x004 (R/W)  Current Parallel Port Size Register */
       uint32_t RESERVED0[2];
  volatile uint32_t ACPR;                    /*!< Offset: 0x010 (R/W)  Asynchronous Clock Prescaler Register */
       uint32_t RESERVED1[55];
  volatile uint32_t SPPR;                    /*!< Offset: 0x0F0 (R/W)  Selected Pin Protocol Register */
       uint32_t RESERVED2[131];
  volatile const  uint32_t FFSR;                    /*!< Offset: 0x300 (R/ )  Formatter and Flush Status Register */
  volatile uint32_t FFCR;                    /*!< Offset: 0x304 (R/W)  Formatter and Flush Control Register */
  volatile const  uint32_t FSCR;                    /*!< Offset: 0x308 (R/ )  Formatter Synchronization Counter Register */
       uint32_t RESERVED3[759];
  volatile const  uint32_t TRIGGER;                 /*!< Offset: 0xEE8 (R/ )  TRIGGER */
  volatile const  uint32_t FIFO0;                   /*!< Offset: 0xEEC (R/ )  Integration ETM Data */
  volatile const  uint32_t ITATBCTR2;               /*!< Offset: 0xEF0 (R/ )  ITATBCTR2 */
       uint32_t RESERVED4[1];
  volatile const  uint32_t ITATBCTR0;               /*!< Offset: 0xEF8 (R/ )  ITATBCTR0 */
  volatile const  uint32_t FIFO1;                   /*!< Offset: 0xEFC (R/ )  Integration ITM Data */
  volatile uint32_t ITCTRL;                  /*!< Offset: 0xF00 (R/W)  Integration Mode Control */
       uint32_t RESERVED5[39];
  volatile uint32_t CLAIMSET;                /*!< Offset: 0xFA0 (R/W)  Claim tag set */
  volatile uint32_t CLAIMCLR;                /*!< Offset: 0xFA4 (R/W)  Claim tag clear */
       uint32_t RESERVED7[8];
  volatile const  uint32_t DEVID;                   /*!< Offset: 0xFC8 (R/ )  TPIU_DEVID */
  volatile const  uint32_t DEVTYPE;                 /*!< Offset: 0xFCC (R/ )  TPIU_DEVTYPE */
} TPI_Type;

/* TPI Asynchronous Clock Prescaler Register Definitions */

/* TPI Selected Pin Protocol Register Definitions */

/* TPI Formatter and Flush Status Register Definitions */




/* TPI Formatter and Flush Control Register Definitions */


/* TPI TRIGGER Register Definitions */

/* TPI Integration ETM Data Register Definitions (FIFO0) */







/* TPI ITATBCTR2 Register Definitions */

/* TPI Integration ITM Data Register Definitions (FIFO1) */







/* TPI ITATBCTR0 Register Definitions */

/* TPI Integration Mode Control Register Definitions */

/* TPI DEVID Register Definitions */






/* TPI DEVTYPE Register Definitions */


/*@}*/ /* end of group CMSIS_TPI */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_MPU     Memory Protection Unit (MPU)
    \brief      Type definitions for the Memory Protection Unit (MPU)
  @{
 */

/** \brief  Structure type to access the Memory Protection Unit (MPU).
 */
typedef struct
{
  volatile const  uint32_t TYPE;                    /*!< Offset: 0x000 (R/ )  MPU Type Register                              */
  volatile uint32_t CTRL;                    /*!< Offset: 0x004 (R/W)  MPU Control Register                           */
  volatile uint32_t RNR;                     /*!< Offset: 0x008 (R/W)  MPU Region RNRber Register                     */
  volatile uint32_t RBAR;                    /*!< Offset: 0x00C (R/W)  MPU Region Base Address Register               */
  volatile uint32_t RASR;                    /*!< Offset: 0x010 (R/W)  MPU Region Attribute and Size Register         */
  volatile uint32_t RBAR_A1;                 /*!< Offset: 0x014 (R/W)  MPU Alias 1 Region Base Address Register       */
  volatile uint32_t RASR_A1;                 /*!< Offset: 0x018 (R/W)  MPU Alias 1 Region Attribute and Size Register */
  volatile uint32_t RBAR_A2;                 /*!< Offset: 0x01C (R/W)  MPU Alias 2 Region Base Address Register       */
  volatile uint32_t RASR_A2;                 /*!< Offset: 0x020 (R/W)  MPU Alias 2 Region Attribute and Size Register */
  volatile uint32_t RBAR_A3;                 /*!< Offset: 0x024 (R/W)  MPU Alias 3 Region Base Address Register       */
  volatile uint32_t RASR_A3;                 /*!< Offset: 0x028 (R/W)  MPU Alias 3 Region Attribute and Size Register */
} MPU_Type;

/* MPU Type Register */



/* MPU Control Register */



/* MPU Region Number Register */

/* MPU Region Base Address Register */



/* MPU Region Attribute and Size Register */










/*@} end of group CMSIS_MPU */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_FPU     Floating Point Unit (FPU)
    \brief      Type definitions for the Floating Point Unit (FPU)
  @{
 */

/** \brief  Structure type to access the Floating Point Unit (FPU).
 */
typedef struct
{
       uint32_t RESERVED0[1];
  volatile uint32_t FPCCR;                   /*!< Offset: 0x004 (R/W)  Floating-Point Context Control Register               */
  volatile uint32_t FPCAR;                   /*!< Offset: 0x008 (R/W)  Floating-Point Context Address Register               */
  volatile uint32_t FPDSCR;                  /*!< Offset: 0x00C (R/W)  Floating-Point Default Status Control Register        */
  volatile const  uint32_t MVFR0;                   /*!< Offset: 0x010 (R/ )  Media and FP Feature Register 0                       */
  volatile const  uint32_t MVFR1;                   /*!< Offset: 0x014 (R/ )  Media and FP Feature Register 1                       */
} FPU_Type;

/* Floating-Point Context Control Register */









/* Floating-Point Context Address Register */

/* Floating-Point Default Status Control Register */




/* Media and FP Feature Register 0 */








/* Media and FP Feature Register 1 */




/*@} end of group CMSIS_FPU */


/** \ingroup  CMSIS_core_register
    \defgroup CMSIS_CoreDebug       Core Debug Registers (CoreDebug)
    \brief      Type definitions for the Core Debug Registers
  @{
 */

/** \brief  Structure type to access the Core Debug Register (CoreDebug).
 */
typedef struct
{
  volatile uint32_t DHCSR;                   /*!< Offset: 0x000 (R/W)  Debug Halting Control and Status Register    */
  volatile  uint32_t DCRSR;                   /*!< Offset: 0x004 ( /W)  Debug Core Register Selector Register        */
  volatile uint32_t DCRDR;                   /*!< Offset: 0x008 (R/W)  Debug Core Register Data Register            */
  volatile uint32_t DEMCR;                   /*!< Offset: 0x00C (R/W)  Debug Exception and Monitor Control Register */
} CoreDebug_Type;

/* Debug Halting Control and Status Register */












/* Debug Core Register Selector Register */


/* Debug Exception and Monitor Control Register */













/*@} end of group CMSIS_CoreDebug */


/** \ingroup    CMSIS_core_register
    \defgroup   CMSIS_core_base     Core Definitions
    \brief      Definitions for base addresses, unions, and structures.
  @{
 */

/* Memory mapping of Cortex-M4 Hardware */




/*@} */



/*******************************************************************************
 *                Hardware Abstraction Layer
  Core Function Interface contains:
  - Core NVIC Functions
  - Core SysTick Functions
  - Core Debug Functions
  - Core Register Access Functions
 ******************************************************************************/
/** \defgroup CMSIS_Core_FunctionInterface Functions and Instructions Reference
*/



/* ##########################   NVIC functions  #################################### */
/** \ingroup  CMSIS_Core_FunctionInterface
    \defgroup CMSIS_Core_NVICFunctions NVIC Functions
    \brief      Functions that manage interrupts and exceptions via the NVIC.
    @{
 */

/** \brief  Set Priority Grouping

  The function sets the priority grouping field using the required unlock sequence.
  The parameter PriorityGroup is assigned to the field SCB->AIRCR [10:8] PRIGROUP field.
  Only values from 0..7 are used.
  In case of a conflict between priority grouping and available
  priority bits (__NVIC_PRIO_BITS), the smallest possible priority group is set.

    \param [in]      PriorityGroup  Priority grouping field.
 */
static inline void NVIC_SetPriorityGrouping(uint32_t PriorityGroup)
{
  uint32_t reg_value;
  uint32_t PriorityGroupTmp = (PriorityGroup & (uint32_t)0x07);               /* only values 0..7 are used          */

  reg_value  =  ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->AIRCR;                                                   /* read old register configuration    */
  reg_value &= ~((0xFFFFUL << 16) | (7UL << 8));             /* clear bits to change               */
  reg_value  =  (reg_value                                 |
                ((uint32_t)0x5FA << 16) |
                (PriorityGroupTmp << 8));                                     /* Insert write key and priorty group */
  ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->AIRCR =  reg_value;
}


/** \brief  Get Priority Grouping

  The function reads the priority grouping field from the NVIC Interrupt Controller.

    \return                Priority grouping field (SCB->AIRCR [10:8] PRIGROUP field).
 */
static inline uint32_t NVIC_GetPriorityGrouping(void)
{
  return ((((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->AIRCR & (7UL << 8)) >> 8);   /* read priority grouping field */
}


/** \brief  Enable External Interrupt

    The function enables a device-specific interrupt in the NVIC interrupt controller.

    \param [in]      IRQn  External interrupt number. Value cannot be negative.
 */
static inline void NVIC_EnableIRQ(IRQn_Type IRQn)
{
/*  NVIC->ISER[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F));  enable interrupt */
  ((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->ISER[(uint32_t)((int32_t)IRQn) >> 5] = (uint32_t)(1 << ((uint32_t)((int32_t)IRQn) & (uint32_t)0x1F)); /* enable interrupt */
}


/** \brief  Disable External Interrupt

    The function disables a device-specific interrupt in the NVIC interrupt controller.

    \param [in]      IRQn  External interrupt number. Value cannot be negative.
 */
static inline void NVIC_DisableIRQ(IRQn_Type IRQn)
{
  ((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->ICER[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F)); /* disable interrupt */
}


/** \brief  Get Pending Interrupt

    The function reads the pending register in the NVIC and returns the pending bit
    for the specified interrupt.

    \param [in]      IRQn  Interrupt number.

    \return             0  Interrupt status is not pending.
    \return             1  Interrupt status is pending.
 */
static inline uint32_t NVIC_GetPendingIRQ(IRQn_Type IRQn)
{
  return((uint32_t) ((((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->ISPR[(uint32_t)(IRQn) >> 5] & (1 << ((uint32_t)(IRQn) & 0x1F)))?1:0)); /* Return 1 if pending else 0 */
}


/** \brief  Set Pending Interrupt

    The function sets the pending bit of an external interrupt.

    \param [in]      IRQn  Interrupt number. Value cannot be negative.
 */
static inline void NVIC_SetPendingIRQ(IRQn_Type IRQn)
{
  ((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->ISPR[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F)); /* set interrupt pending */
}


/** \brief  Clear Pending Interrupt

    The function clears the pending bit of an external interrupt.

    \param [in]      IRQn  External interrupt number. Value cannot be negative.
 */
static inline void NVIC_ClearPendingIRQ(IRQn_Type IRQn)
{
  ((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->ICPR[((uint32_t)(IRQn) >> 5)] = (1 << ((uint32_t)(IRQn) & 0x1F)); /* Clear pending interrupt */
}


/** \brief  Get Active Interrupt

    The function reads the active register in NVIC and returns the active bit.

    \param [in]      IRQn  Interrupt number.

    \return             0  Interrupt status is not active.
    \return             1  Interrupt status is active.
 */
static inline uint32_t NVIC_GetActive(IRQn_Type IRQn)
{
  return((uint32_t)((((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->IABR[(uint32_t)(IRQn) >> 5] & (1 << ((uint32_t)(IRQn) & 0x1F)))?1:0)); /* Return 1 if active else 0 */
}


/** \brief  Set Interrupt Priority

    The function sets the priority of an interrupt.

    \note The priority cannot be set for every core interrupt.

    \param [in]      IRQn  Interrupt number.
    \param [in]  priority  Priority to set.
 */
static inline void NVIC_SetPriority(IRQn_Type IRQn, uint32_t priority)
{
  if(IRQn < 0) {
    ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->SHP[((uint32_t)(IRQn) & 0xF)-4] = ((priority << (8 - 3)) & 0xff); } /* set Priority for Cortex-M  System Interrupts */
  else {
    ((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->IP[(uint32_t)(IRQn)] = ((priority << (8 - 3)) & 0xff);    }        /* set Priority for device specific Interrupts  */
}


/** \brief  Get Interrupt Priority

    The function reads the priority of an interrupt. The interrupt
    number can be positive to specify an external (device specific)
    interrupt, or negative to specify an internal (core) interrupt.


    \param [in]   IRQn  Interrupt number.
    \return             Interrupt Priority. Value is aligned automatically to the implemented
                        priority bits of the microcontroller.
 */
static inline uint32_t NVIC_GetPriority(IRQn_Type IRQn)
{

  if(IRQn < 0) {
    return((uint32_t)(((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->SHP[((uint32_t)(IRQn) & 0xF)-4] >> (8 - 3)));  } /* get priority for Cortex-M  system interrupts */
  else {
    return((uint32_t)(((NVIC_Type *) ((0xE000E000UL) + 0x0100UL) )->IP[(uint32_t)(IRQn)]           >> (8 - 3)));  } /* get priority for device specific interrupts  */
}


/** \brief  Encode Priority

    The function encodes the priority for an interrupt with the given priority group,
    preemptive priority value, and subpriority value.
    In case of a conflict between priority grouping and available
    priority bits (__NVIC_PRIO_BITS), the smallest possible priority group is set.

    \param [in]     PriorityGroup  Used priority group.
    \param [in]   PreemptPriority  Preemptive priority value (starting from 0).
    \param [in]       SubPriority  Subpriority value (starting from 0).
    \return                        Encoded priority. Value can be used in the function \ref NVIC_SetPriority().
 */
static inline uint32_t NVIC_EncodePriority (uint32_t PriorityGroup, uint32_t PreemptPriority, uint32_t SubPriority)
{
  uint32_t PriorityGroupTmp = (PriorityGroup & 0x07);          /* only values 0..7 are used          */
  uint32_t PreemptPriorityBits;
  uint32_t SubPriorityBits;

  PreemptPriorityBits = ((7 - PriorityGroupTmp) > 3) ? 3 : 7 - PriorityGroupTmp;
  SubPriorityBits     = ((PriorityGroupTmp + 3) < 7) ? 0 : PriorityGroupTmp - 7 + 3;

  return (
           ((PreemptPriority & ((1 << (PreemptPriorityBits)) - 1)) << SubPriorityBits) |
           ((SubPriority     & ((1 << (SubPriorityBits    )) - 1)))
         );
}


/** \brief  Decode Priority

    The function decodes an interrupt priority value with a given priority group to
    preemptive priority value and subpriority value.
    In case of a conflict between priority grouping and available
    priority bits (__NVIC_PRIO_BITS) the smallest possible priority group is set.

    \param [in]         Priority   Priority value, which can be retrieved with the function \ref NVIC_GetPriority().
    \param [in]     PriorityGroup  Used priority group.
    \param [out] pPreemptPriority  Preemptive priority value (starting from 0).
    \param [out]     pSubPriority  Subpriority value (starting from 0).
 */
static inline void NVIC_DecodePriority (uint32_t Priority, uint32_t PriorityGroup, uint32_t* pPreemptPriority, uint32_t* pSubPriority)
{
  uint32_t PriorityGroupTmp = (PriorityGroup & 0x07);          /* only values 0..7 are used          */
  uint32_t PreemptPriorityBits;
  uint32_t SubPriorityBits;

  PreemptPriorityBits = ((7 - PriorityGroupTmp) > 3) ? 3 : 7 - PriorityGroupTmp;
  SubPriorityBits     = ((PriorityGroupTmp + 3) < 7) ? 0 : PriorityGroupTmp - 7 + 3;

  *pPreemptPriority = (Priority >> SubPriorityBits) & ((1 << (PreemptPriorityBits)) - 1);
  *pSubPriority     = (Priority                   ) & ((1 << (SubPriorityBits    )) - 1);
}


/** \brief  System Reset

    The function initiates a system reset request to reset the MCU.
 */
static inline void NVIC_SystemReset(void)
{
  __DSB();                                                     /* Ensure all outstanding memory accesses included
                                                                  buffered write are completed before reset */
  ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->AIRCR  = ((0x5FA << 16)      |
                 (((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->AIRCR & (7UL << 8)) |
                 (1UL << 2));                   /* Keep priority group unchanged */
  __DSB();                                                     /* Ensure completion of memory access */
  while(1);                                                    /* wait until reset */
}

/*@} end of CMSIS_Core_NVICFunctions */



/* ##################################    SysTick function  ############################################ */
/** \ingroup  CMSIS_Core_FunctionInterface
    \defgroup CMSIS_Core_SysTickFunctions SysTick Functions
    \brief      Functions that configure the System.
  @{
 */


/** \brief  System Tick Configuration

    The function initializes the System Timer and its interrupt, and starts the System Tick Timer.
    Counter is in free running mode to generate periodic interrupts.

    \param [in]  ticks  Number of ticks between two interrupts.

    \return          0  Function succeeded.
    \return          1  Function failed.

    \note     When the variable <b>__Vendor_SysTickConfig</b> is set to 1, then the
    function <b>SysTick_Config</b> is not included. In this case, the file <b><i>device</i>.h</b>
    must contain a vendor-specific implementation of this function.

 */
static inline uint32_t SysTick_Config(uint32_t ticks)
{
  if ((ticks - 1) > (0xFFFFFFUL << 0))  return (1);      /* Reload value impossible */

  ((SysTick_Type *) ((0xE000E000UL) + 0x0010UL) )->LOAD  = ticks - 1;                                  /* set reload register */
  NVIC_SetPriority (SysTick_IRQn, (1<<3) - 1);  /* set Priority for Systick Interrupt */
  ((SysTick_Type *) ((0xE000E000UL) + 0x0010UL) )->VAL   = 0;                                          /* Load the SysTick Counter Value */
  ((SysTick_Type *) ((0xE000E000UL) + 0x0010UL) )->CTRL  = (1UL << 2) |
                   (1UL << 1)   |
                   (1UL << 0);                    /* Enable SysTick IRQ and SysTick Timer */
  return (0);                                                  /* Function successful */
}


/*@} end of CMSIS_Core_SysTickFunctions */



/* ##################################### Debug In/Output function ########################################### */
/** \ingroup  CMSIS_Core_FunctionInterface
    \defgroup CMSIS_core_DebugFunctions ITM Functions
    \brief   Functions that access the ITM debug interface.
  @{
 */

extern volatile int32_t ITM_RxBuffer;                    /*!< External variable to receive characters.                         */


/** \brief  ITM Send Character

    The function transmits a character via the ITM channel 0, and
    \li Just returns when no debugger is connected that has booked the output.
    \li Is blocking when a debugger is connected, but the previous character sent has not been transmitted.

    \param [in]     ch  Character to transmit.

    \returns            Character to transmit.
 */
static inline uint32_t ITM_SendChar (uint32_t ch)
{
  if ((((ITM_Type *) (0xE0000000UL) )->TCR & (1UL << 0))                  &&      /* ITM enabled */
      (((ITM_Type *) (0xE0000000UL) )->TER & (1UL << 0)        )                    )     /* ITM Port #0 enabled */
  {
    while (((ITM_Type *) (0xE0000000UL) )->PORT[0].u32 == 0);
    ((ITM_Type *) (0xE0000000UL) )->PORT[0].u8 = (uint8_t) ch;
  }
  return (ch);
}


/** \brief  ITM Receive Character

    The function inputs a character via the external variable \ref ITM_RxBuffer.

    \return             Received character.
    \return         -1  No character pending.
 */
static inline int32_t ITM_ReceiveChar (void) {
  int32_t ch = -1;                           /* no character available */

  if (ITM_RxBuffer != 0x5AA55AA5) {
    ch = ITM_RxBuffer;
    ITM_RxBuffer = 0x5AA55AA5;       /* ready for next character */
  }

  return (ch);
}


/** \brief  ITM Check Character

    The function checks whether a character is pending for reading in the variable \ref ITM_RxBuffer.

    \return          0  No character available.
    \return          1  Character available.
 */
static inline int32_t ITM_CheckChar (void) {

  if (ITM_RxBuffer == 0x5AA55AA5) {
    return (0);                                 /* no character available */
  } else {
    return (1);                                 /*    character available */
  }
}

/*@} end of CMSIS_core_DebugFunctions */






/***************************************************************************//**
 * @file system_ezr32wg.h
 * @brief CMSIS Cortex-M4 System Layer for EZR32WG devices.
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/



/* stdint.h standard header */
/* Copyright 2003-2010 IAR Systems AB.  */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */

/*******************************************************************************
 **************************   GLOBAL VARIABLES   *******************************
 ******************************************************************************/

extern uint32_t SystemCoreClock;    /**< System Clock Frequency (Core Clock) */

/*******************************************************************************
 *****************************   PROTOTYPES   **********************************
 ******************************************************************************/

/* Interrupt routines - prototypes */
void Reset_Handler(void);
void NMI_Handler(void);
void HardFault_Handler(void);
void MemManage_Handler(void);
void BusFault_Handler(void);
void UsageFault_Handler(void);
void SVC_Handler(void);
void DebugMon_Handler(void);
void PendSV_Handler(void);
void SysTick_Handler(void);
void DMA_IRQHandler(void);
void GPIO_EVEN_IRQHandler(void);
void TIMER0_IRQHandler(void);
void USARTRF_RX_IRQHandler(void);
void USARTRF_TX_IRQHandler(void);
void USB_IRQHandler(void);
void ACMP0_IRQHandler(void);
void ADC0_IRQHandler(void);
void DAC0_IRQHandler(void);
void I2C0_IRQHandler(void);
void I2C1_IRQHandler(void);
void GPIO_ODD_IRQHandler(void);
void TIMER1_IRQHandler(void);
void TIMER2_IRQHandler(void);
void TIMER3_IRQHandler(void);
void USART1_RX_IRQHandler(void);
void USART1_TX_IRQHandler(void);
void LESENSE_IRQHandler(void);
void USART2_RX_IRQHandler(void);
void USART2_TX_IRQHandler(void);
void UART0_RX_IRQHandler(void);
void UART0_TX_IRQHandler(void);
void UART1_RX_IRQHandler(void);
void UART1_TX_IRQHandler(void);
void LEUART0_IRQHandler(void);
void LEUART1_IRQHandler(void);
void LETIMER0_IRQHandler(void);
void PCNT0_IRQHandler(void);
void PCNT1_IRQHandler(void);
void PCNT2_IRQHandler(void);
void RTC_IRQHandler(void);
void BURTC_IRQHandler(void);
void CMU_IRQHandler(void);
void VCMP_IRQHandler(void);
void LCD_IRQHandler(void);
void MSC_IRQHandler(void);
void AES_IRQHandler(void);
void EMU_IRQHandler(void);
void FPUEH_IRQHandler(void);

uint32_t SystemCoreClockGet(void);
uint32_t SystemMaxCoreClockGet(void);

/**************************************************************************//**
 * @brief
 *   Update CMSIS SystemCoreClock variable.
 *
 * @details
 *   CMSIS defines a global variable SystemCoreClock that shall hold the
 *   core frequency in Hz. If the core frequency is dynamically changed, the
 *   variable must be kept updated in order to be CMSIS compliant.
 *
 *   Notice that if only changing core clock frequency through the emlib CMU
 *   API, this variable will be kept updated. This function is only provided
 *   for CMSIS compliance and if a user modifies the the core clock outside
 *   the CMU API.
 *****************************************************************************/
static inline void SystemCoreClockUpdate(void)
{
  SystemCoreClockGet();
}

void SystemInit(void);
uint32_t SystemHFClockGet(void);
uint32_t SystemHFXOClockGet(void);
void SystemHFXOClockSet(uint32_t freq);
uint32_t SystemLFRCOClockGet(void);
uint32_t SystemULFRCOClockGet(void);
uint32_t SystemLFXOClockGet(void);
void SystemLFXOClockSet(uint32_t freq);


/** @} End of group EZR32WG330F256R60_Part */

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_Peripheral_TypeDefs EZR32WG330F256R60 Peripheral TypeDefs
 * @{
 * @brief Device Specific Peripheral Register Structures
 *****************************************************************************/

/**************************************************************************//**
 * @file ezr32wg_dma_ch.h
 * @brief EZR32WG_DMA_CH register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief DMA_CH EZR32WG DMA CH
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL; /**< Channel Control Register  */
} DMA_CH_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_dma.h
 * @brief EZR32WG_DMA register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_DMA
 * @{
 * @brief EZR32WG_DMA Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile const uint32_t   STATUS;         /**< DMA Status Registers  */
  volatile uint32_t   CONFIG;         /**< DMA Configuration Register  */
  volatile uint32_t  CTRLBASE;       /**< Channel Control Data Base Pointer Register  */
  volatile const uint32_t   ALTCTRLBASE;    /**< Channel Alternate Control Data Base Pointer Register  */
  volatile const uint32_t   CHWAITSTATUS;   /**< Channel Wait on Request Status Register  */
  volatile uint32_t   CHSWREQ;        /**< Channel Software Request Register  */
  volatile uint32_t  CHUSEBURSTS;    /**< Channel Useburst Set Register  */
  volatile uint32_t   CHUSEBURSTC;    /**< Channel Useburst Clear Register  */
  volatile uint32_t  CHREQMASKS;     /**< Channel Request Mask Set Register  */
  volatile uint32_t   CHREQMASKC;     /**< Channel Request Mask Clear Register  */
  volatile uint32_t  CHENS;          /**< Channel Enable Set Register  */
  volatile uint32_t   CHENC;          /**< Channel Enable Clear Register  */
  volatile uint32_t  CHALTS;         /**< Channel Alternate Set Register  */
  volatile uint32_t   CHALTC;         /**< Channel Alternate Clear Register  */
  volatile uint32_t  CHPRIS;         /**< Channel Priority Set Register  */
  volatile uint32_t   CHPRIC;         /**< Channel Priority Clear Register  */
  uint32_t       RESERVED0[3];   /**< Reserved for future use **/
  volatile uint32_t  ERRORC;         /**< Bus Error Clear Register  */

  uint32_t       RESERVED1[880]; /**< Reserved for future use **/
  volatile const uint32_t   CHREQSTATUS;    /**< Channel Request Status  */
  uint32_t       RESERVED2[1];   /**< Reserved for future use **/
  volatile const uint32_t   CHSREQSTATUS;   /**< Channel Single Request Status  */

  uint32_t       RESERVED3[121]; /**< Reserved for future use **/
  volatile const uint32_t   IF;             /**< Interrupt Flag Register  */
  volatile uint32_t  IFS;            /**< Interrupt Flag Set Register  */
  volatile uint32_t  IFC;            /**< Interrupt Flag Clear Register  */
  volatile uint32_t  IEN;            /**< Interrupt Enable register  */
  volatile uint32_t  CTRL;           /**< DMA Control Register  */
  volatile uint32_t  RDS;            /**< DMA Retain Descriptor State  */

  uint32_t       RESERVED4[2];   /**< Reserved for future use **/
  volatile uint32_t  LOOP0;          /**< Channel 0 Loop Register  */
  volatile uint32_t  LOOP1;          /**< Channel 1 Loop Register  */
  uint32_t       RESERVED5[14];  /**< Reserved for future use **/
  volatile uint32_t  RECT0;          /**< Channel 0 Rectangle Register  */

  uint32_t       RESERVED6[39];  /**< Reserved registers */
  DMA_CH_TypeDef CH[12];         /**< Channel registers */
} DMA_TypeDef;                   /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_DMA_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for DMA STATUS */

/* Bit fields for DMA CONFIG */

/* Bit fields for DMA CTRLBASE */

/* Bit fields for DMA ALTCTRLBASE */

/* Bit fields for DMA CHWAITSTATUS */

/* Bit fields for DMA CHSWREQ */

/* Bit fields for DMA CHUSEBURSTS */

/* Bit fields for DMA CHUSEBURSTC */

/* Bit fields for DMA CHREQMASKS */

/* Bit fields for DMA CHREQMASKC */

/* Bit fields for DMA CHENS */

/* Bit fields for DMA CHENC */

/* Bit fields for DMA CHALTS */

/* Bit fields for DMA CHALTC */

/* Bit fields for DMA CHPRIS */

/* Bit fields for DMA CHPRIC */

/* Bit fields for DMA ERRORC */

/* Bit fields for DMA CHREQSTATUS */

/* Bit fields for DMA CHSREQSTATUS */

/* Bit fields for DMA IF */

/* Bit fields for DMA IFS */

/* Bit fields for DMA IFC */

/* Bit fields for DMA IEN */

/* Bit fields for DMA CTRL */

/* Bit fields for DMA RDS */

/* Bit fields for DMA LOOP0 */

/* Bit fields for DMA LOOP1 */

/* Bit fields for DMA RECT0 */

/* Bit fields for DMA CH_CTRL */

/** @} End of group EZR32WG_DMA */


/**************************************************************************//**
 * @file ezr32wg_aes.h
 * @brief EZR32WG_AES register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_AES
 * @{
 * @brief EZR32WG_AES Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Control Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t DATA;         /**< DATA Register  */
  volatile uint32_t XORDATA;      /**< XORDATA Register  */
  uint32_t      RESERVED0[3]; /**< Reserved for future use **/
  volatile uint32_t KEYLA;        /**< KEY Low Register  */
  volatile uint32_t KEYLB;        /**< KEY Low Register  */
  volatile uint32_t KEYLC;        /**< KEY Low Register  */
  volatile uint32_t KEYLD;        /**< KEY Low Register  */
  volatile uint32_t KEYHA;        /**< KEY High Register  */
  volatile uint32_t KEYHB;        /**< KEY High Register  */
  volatile uint32_t KEYHC;        /**< KEY High Register  */
  volatile uint32_t KEYHD;        /**< KEY High Register  */
} AES_TypeDef;                /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_AES_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for AES CTRL */

/* Bit fields for AES CMD */

/* Bit fields for AES STATUS */

/* Bit fields for AES IEN */

/* Bit fields for AES IF */

/* Bit fields for AES IFS */

/* Bit fields for AES IFC */

/* Bit fields for AES DATA */

/* Bit fields for AES XORDATA */

/* Bit fields for AES KEYLA */

/* Bit fields for AES KEYLB */

/* Bit fields for AES KEYLC */

/* Bit fields for AES KEYLD */

/* Bit fields for AES KEYHA */

/* Bit fields for AES KEYHB */

/* Bit fields for AES KEYHC */

/* Bit fields for AES KEYHD */

/** @} End of group EZR32WG_AES */


/**************************************************************************//**
 * @file ezr32wg_usb_hc.h
 * @brief EZR32WG_USB_HC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief USB_HC EZR32WG USB HC
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CHAR;         /**< Host Channel x Characteristics Register  */
  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t INT;          /**< Host Channel x Interrupt Register  */
  volatile uint32_t INTMSK;       /**< Host Channel x Interrupt Mask Register  */
  volatile uint32_t TSIZ;         /**< Host Channel x Transfer Size Register  */
  volatile uint32_t DMAADDR;      /**< Host Channel x DMA Address Register  */
  uint32_t      RESERVED1[2]; /**< Reserved future */
} USB_HC_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_usb_diep.h
 * @brief EZR32WG_USB_DIEP register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief USB_DIEP EZR32WG USB DIEP
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTL;          /**< Device IN Endpoint x+1 Control Register  */
  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t INT;          /**< Device IN Endpoint x+1 Interrupt Register  */
  uint32_t      RESERVED1[1]; /**< Reserved for future use **/
  volatile uint32_t TSIZ;         /**< Device IN Endpoint x+1 Transfer Size Register  */
  volatile uint32_t DMAADDR;      /**< Device IN Endpoint x+1 DMA Address Register  */
  volatile const uint32_t  TXFSTS;       /**< Device IN Endpoint x+1 Transmit FIFO Status Register  */
  uint32_t      RESERVED2[1]; /**< Reserved future */
} USB_DIEP_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_usb_doep.h
 * @brief EZR32WG_USB_DOEP register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief USB_DOEP EZR32WG USB DOEP
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTL;          /**< Device OUT Endpoint x+1 Control Register  */
  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t INT;          /**< Device OUT Endpoint x+1 Interrupt Register  */
  uint32_t      RESERVED1[1]; /**< Reserved for future use **/
  volatile uint32_t TSIZ;         /**< Device OUT Endpoint x+1 Transfer Size Register  */
  volatile uint32_t DMAADDR;      /**< Device OUT Endpoint x+1 DMA Address Register  */
  uint32_t      RESERVED2[2]; /**< Reserved future */
} USB_DOEP_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_usb.h
 * @brief EZR32WG_USB register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_USB
 * @{
 * @brief EZR32WG_USB Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t    CTRL;              /**< System Control Register  */
  volatile const uint32_t     STATUS;            /**< System Status Register  */
  volatile const uint32_t     IF;                /**< Interrupt Flag Register  */
  volatile uint32_t    IFS;               /**< Interrupt Flag Set Register  */
  volatile uint32_t    IFC;               /**< Interrupt Flag Clear Register  */
  volatile uint32_t    IEN;               /**< Interrupt Enable Register  */
  volatile uint32_t    ROUTE;             /**< I/O Routing Register  */

  uint32_t         RESERVED0[61433];  /**< Reserved for future use **/
  volatile uint32_t    GOTGCTL;           /**< OTG Control and Status Register  */
  volatile uint32_t    GOTGINT;           /**< OTG Interrupt Register  */
  volatile uint32_t    GAHBCFG;           /**< AHB Configuration Register  */
  volatile uint32_t    GUSBCFG;           /**< USB Configuration Register  */
  volatile uint32_t    GRSTCTL;           /**< Reset Register  */
  volatile uint32_t    GINTSTS;           /**< Interrupt Register  */
  volatile uint32_t    GINTMSK;           /**< Interrupt Mask Register  */
  volatile const uint32_t     GRXSTSR;           /**< Receive Status Debug Read Register  */
  volatile const uint32_t     GRXSTSP;           /**< Receive Status Read and Pop Register  */
  volatile uint32_t    GRXFSIZ;           /**< Receive FIFO Size Register  */
  volatile uint32_t    GNPTXFSIZ;         /**< Non-periodic Transmit FIFO Size Register  */
  volatile const uint32_t     GNPTXSTS;          /**< Non-periodic Transmit FIFO/Queue Status Register  */
  uint32_t         RESERVED1[11];     /**< Reserved for future use **/
  volatile uint32_t    GDFIFOCFG;         /**< Global DFIFO Configuration Register  */

  uint32_t         RESERVED2[40];     /**< Reserved for future use **/
  volatile uint32_t    HPTXFSIZ;          /**< Host Periodic Transmit FIFO Size Register  */
  volatile uint32_t    DIEPTXF1;          /**< Device IN Endpoint Transmit FIFO 1 Size Register  */
  volatile uint32_t    DIEPTXF2;          /**< Device IN Endpoint Transmit FIFO 2 Size Register  */
  volatile uint32_t    DIEPTXF3;          /**< Device IN Endpoint Transmit FIFO 3 Size Register  */
  volatile uint32_t    DIEPTXF4;          /**< Device IN Endpoint Transmit FIFO 4 Size Register  */
  volatile uint32_t    DIEPTXF5;          /**< Device IN Endpoint Transmit FIFO 5 Size Register  */
  volatile uint32_t    DIEPTXF6;          /**< Device IN Endpoint Transmit FIFO 6 Size Register  */

  uint32_t         RESERVED3[185];    /**< Reserved for future use **/
  volatile uint32_t    HCFG;              /**< Host Configuration Register  */
  volatile uint32_t    HFIR;              /**< Host Frame Interval Register  */
  volatile const uint32_t     HFNUM;             /**< Host Frame Number/Frame Time Remaining Register  */
  uint32_t         RESERVED4[1];      /**< Reserved for future use **/
  volatile const uint32_t     HPTXSTS;           /**< Host Periodic Transmit FIFO/Queue Status Register  */
  volatile const uint32_t     HAINT;             /**< Host All Channels Interrupt Register  */
  volatile uint32_t    HAINTMSK;          /**< Host All Channels Interrupt Mask Register  */
  uint32_t         RESERVED5[9];      /**< Reserved for future use **/
  volatile uint32_t    HPRT;              /**< Host Port Control and Status Register  */

  uint32_t         RESERVED6[47];     /**< Reserved registers */
  USB_HC_TypeDef   HC[14];            /**< Host Channel Registers */

  uint32_t         RESERVED7[80];     /**< Reserved for future use **/
  volatile uint32_t    DCFG;              /**< Device Configuration Register  */
  volatile uint32_t    DCTL;              /**< Device Control Register  */
  volatile const uint32_t     DSTS;              /**< Device Status Register  */
  uint32_t         RESERVED8[1];      /**< Reserved for future use **/
  volatile uint32_t    DIEPMSK;           /**< Device IN Endpoint Common Interrupt Mask Register  */
  volatile uint32_t    DOEPMSK;           /**< Device OUT Endpoint Common Interrupt Mask Register  */
  volatile const uint32_t     DAINT;             /**< Device All Endpoints Interrupt Register  */
  volatile uint32_t    DAINTMSK;          /**< Device All Endpoints Interrupt Mask Register  */
  uint32_t         RESERVED9[2];      /**< Reserved for future use **/
  volatile uint32_t    DVBUSDIS;          /**< Device VBUS Discharge Time Register  */
  volatile uint32_t    DVBUSPULSE;        /**< Device VBUS Pulsing Time Register  */

  uint32_t         RESERVED10[1];     /**< Reserved for future use **/
  volatile uint32_t    DIEPEMPMSK;        /**< Device IN Endpoint FIFO Empty Interrupt Mask Register  */

  uint32_t         RESERVED11[50];    /**< Reserved for future use **/
  volatile uint32_t    DIEP0CTL;          /**< Device IN Endpoint 0 Control Register  */
  uint32_t         RESERVED12[1];     /**< Reserved for future use **/
  volatile uint32_t    DIEP0INT;          /**< Device IN Endpoint 0 Interrupt Register  */
  uint32_t         RESERVED13[1];     /**< Reserved for future use **/
  volatile uint32_t    DIEP0TSIZ;         /**< Device IN Endpoint 0 Transfer Size Register  */
  volatile uint32_t    DIEP0DMAADDR;      /**< Device IN Endpoint 0 DMA Address Register  */
  volatile const uint32_t     DIEP0TXFSTS;       /**< Device IN Endpoint 0 Transmit FIFO Status Register  */

  uint32_t         RESERVED14[1];     /**< Reserved registers */
  USB_DIEP_TypeDef DIEP[6];           /**< Device IN Endpoint x+1 Registers */

  uint32_t         RESERVED15[72];    /**< Reserved for future use **/
  volatile uint32_t    DOEP0CTL;          /**< Device OUT Endpoint 0 Control Register  */
  uint32_t         RESERVED16[1];     /**< Reserved for future use **/
  volatile uint32_t    DOEP0INT;          /**< Device OUT Endpoint 0 Interrupt Register  */
  uint32_t         RESERVED17[1];     /**< Reserved for future use **/
  volatile uint32_t    DOEP0TSIZ;         /**< Device OUT Endpoint 0 Transfer Size Register  */
  volatile uint32_t    DOEP0DMAADDR;      /**< Device OUT Endpoint 0 DMA Address Register  */

  uint32_t         RESERVED18[2];     /**< Reserved registers */
  USB_DOEP_TypeDef DOEP[6];           /**< Device OUT Endpoint x+1 Registers */

  uint32_t         RESERVED19[136];   /**< Reserved for future use **/
  volatile uint32_t    PCGCCTL;           /**< Power and Clock Gating Control Register  */

  uint32_t         RESERVED20[127];   /**< Reserved registers */
  volatile uint32_t    FIFO0D[512];       /**< Device EP 0/Host Channel 0 FIFO  */

  uint32_t         RESERVED21[512];   /**< Reserved registers */
  volatile uint32_t    FIFO1D[512];       /**< Device EP 1/Host Channel 1 FIFO  */

  uint32_t         RESERVED22[512];   /**< Reserved registers */
  volatile uint32_t    FIFO2D[512];       /**< Device EP 2/Host Channel 2 FIFO  */

  uint32_t         RESERVED23[512];   /**< Reserved registers */
  volatile uint32_t    FIFO3D[512];       /**< Device EP 3/Host Channel 3 FIFO  */

  uint32_t         RESERVED24[512];   /**< Reserved registers */
  volatile uint32_t    FIFO4D[512];       /**< Device EP 4/Host Channel 4 FIFO  */

  uint32_t         RESERVED25[512];   /**< Reserved registers */
  volatile uint32_t    FIFO5D[512];       /**< Device EP 5/Host Channel 5 FIFO  */

  uint32_t         RESERVED26[512];   /**< Reserved registers */
  volatile uint32_t    FIFO6D[512];       /**< Device EP 6/Host Channel 6 FIFO  */

  uint32_t         RESERVED27[512];   /**< Reserved registers */
  volatile uint32_t    FIFO7D[512];       /**< Host Channel 7 FIFO  */

  uint32_t         RESERVED28[512];   /**< Reserved registers */
  volatile uint32_t    FIFO8D[512];       /**< Host Channel 8 FIFO  */

  uint32_t         RESERVED29[512];   /**< Reserved registers */
  volatile uint32_t    FIFO9D[512];       /**< Host Channel 9 FIFO  */

  uint32_t         RESERVED30[512];   /**< Reserved registers */
  volatile uint32_t    FIFO10D[512];      /**< Host Channel 10 FIFO  */

  uint32_t         RESERVED31[512];   /**< Reserved registers */
  volatile uint32_t    FIFO11D[512];      /**< Host Channel 11 FIFO  */

  uint32_t         RESERVED32[512];   /**< Reserved registers */
  volatile uint32_t    FIFO12D[512];      /**< Host Channel 12 FIFO  */

  uint32_t         RESERVED33[512];   /**< Reserved registers */
  volatile uint32_t    FIFO13D[512];      /**< Host Channel 13 FIFO  */

  uint32_t         RESERVED34[17920]; /**< Reserved registers */
  volatile uint32_t    FIFORAM[512];      /**< Direct Access to Data FIFO RAM for Debugging (2 KB)  */
} USB_TypeDef;                        /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_USB_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for USB CTRL */

/* Bit fields for USB STATUS */

/* Bit fields for USB IF */

/* Bit fields for USB IFS */

/* Bit fields for USB IFC */

/* Bit fields for USB IEN */

/* Bit fields for USB ROUTE */

/* Bit fields for USB GOTGCTL */

/* Bit fields for USB GOTGINT */

/* Bit fields for USB GAHBCFG */

/* Bit fields for USB GUSBCFG */

/* Bit fields for USB GRSTCTL */

/* Bit fields for USB GINTSTS */

/* Bit fields for USB GINTMSK */

/* Bit fields for USB GRXSTSR */

/* Bit fields for USB GRXSTSP */

/* Bit fields for USB GRXFSIZ */

/* Bit fields for USB GNPTXFSIZ */

/* Bit fields for USB GNPTXSTS */

/* Bit fields for USB GDFIFOCFG */

/* Bit fields for USB HPTXFSIZ */

/* Bit fields for USB DIEPTXF1 */

/* Bit fields for USB DIEPTXF2 */

/* Bit fields for USB DIEPTXF3 */

/* Bit fields for USB DIEPTXF4 */

/* Bit fields for USB DIEPTXF5 */

/* Bit fields for USB DIEPTXF6 */

/* Bit fields for USB HCFG */

/* Bit fields for USB HFIR */

/* Bit fields for USB HFNUM */

/* Bit fields for USB HPTXSTS */

/* Bit fields for USB HAINT */

/* Bit fields for USB HAINTMSK */

/* Bit fields for USB HPRT */

/* Bit fields for USB HC_CHAR */

/* Bit fields for USB HC_INT */

/* Bit fields for USB HC_INTMSK */

/* Bit fields for USB HC_TSIZ */

/* Bit fields for USB HC_DMAADDR */

/* Bit fields for USB DCFG */

/* Bit fields for USB DCTL */

/* Bit fields for USB DSTS */

/* Bit fields for USB DIEPMSK */

/* Bit fields for USB DOEPMSK */

/* Bit fields for USB DAINT */

/* Bit fields for USB DAINTMSK */

/* Bit fields for USB DVBUSDIS */

/* Bit fields for USB DVBUSPULSE */

/* Bit fields for USB DIEPEMPMSK */

/* Bit fields for USB DIEP0CTL */

/* Bit fields for USB DIEP0INT */

/* Bit fields for USB DIEP0TSIZ */

/* Bit fields for USB DIEP0DMAADDR */

/* Bit fields for USB DIEP0TXFSTS */

/* Bit fields for USB DIEP_CTL */

/* Bit fields for USB DIEP_INT */

/* Bit fields for USB DIEP_TSIZ */

/* Bit fields for USB DIEP_DMAADDR */

/* Bit fields for USB DIEP_TXFSTS */

/* Bit fields for USB DOEP0CTL */

/* Bit fields for USB DOEP0INT */

/* Bit fields for USB DOEP0TSIZ */

/* Bit fields for USB DOEP0DMAADDR */

/* Bit fields for USB DOEP_CTL */

/* Bit fields for USB DOEP_INT */

/* Bit fields for USB DOEP_TSIZ */

/* Bit fields for USB DOEP_DMAADDR */

/* Bit fields for USB PCGCCTL */

/* Bit fields for USB FIFO0D */

/* Bit fields for USB FIFO1D */

/* Bit fields for USB FIFO2D */

/* Bit fields for USB FIFO3D */

/* Bit fields for USB FIFO4D */

/* Bit fields for USB FIFO5D */

/* Bit fields for USB FIFO6D */

/* Bit fields for USB FIFO7D */

/* Bit fields for USB FIFO8D */

/* Bit fields for USB FIFO9D */

/* Bit fields for USB FIFO10D */

/* Bit fields for USB FIFO11D */

/* Bit fields for USB FIFO12D */

/* Bit fields for USB FIFO13D */

/* Bit fields for USB FIFORAM */

/** @} End of group EZR32WG_USB */


/**************************************************************************//**
 * @file ezr32wg_msc.h
 * @brief EZR32WG_MSC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_MSC
 * @{
 * @brief EZR32WG_MSC Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Memory System Control Register  */
  volatile uint32_t READCTRL;     /**< Read Control Register  */
  volatile uint32_t WRITECTRL;    /**< Write Control Register  */
  volatile uint32_t WRITECMD;     /**< Write Command Register  */
  volatile uint32_t ADDRB;        /**< Page Erase/Write Address Buffer  */

  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t WDATA;        /**< Write Data Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */

  uint32_t      RESERVED1[3]; /**< Reserved for future use **/
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile uint32_t LOCK;         /**< Configuration Lock Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile const uint32_t  CACHEHITS;    /**< Cache Hits Performance Counter  */
  volatile const uint32_t  CACHEMISSES;  /**< Cache Misses Performance Counter  */
  uint32_t      RESERVED2[1]; /**< Reserved for future use **/
  volatile uint32_t TIMEBASE;     /**< Flash Write and Erase Timebase  */
  volatile uint32_t MASSLOCK;     /**< Mass Erase Lock Register  */
} MSC_TypeDef;                /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_MSC_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for MSC CTRL */

/* Bit fields for MSC READCTRL */

/* Bit fields for MSC WRITECTRL */

/* Bit fields for MSC WRITECMD */

/* Bit fields for MSC ADDRB */

/* Bit fields for MSC WDATA */

/* Bit fields for MSC STATUS */

/* Bit fields for MSC IF */

/* Bit fields for MSC IFS */

/* Bit fields for MSC IFC */

/* Bit fields for MSC IEN */

/* Bit fields for MSC LOCK */

/* Bit fields for MSC CMD */

/* Bit fields for MSC CACHEHITS */

/* Bit fields for MSC CACHEMISSES */

/* Bit fields for MSC TIMEBASE */

/* Bit fields for MSC MASSLOCK */

/** @} End of group EZR32WG_MSC */


/**************************************************************************//**
 * @file ezr32wg_emu.h
 * @brief EZR32WG_EMU register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_EMU
 * @{
 * @brief EZR32WG_EMU Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;          /**< Control Register  */

  uint32_t      RESERVED0[1];  /**< Reserved for future use **/
  volatile uint32_t LOCK;          /**< Configuration Lock Register  */

  uint32_t      RESERVED1[6];  /**< Reserved for future use **/
  volatile uint32_t AUXCTRL;       /**< Auxiliary Control Register  */

  uint32_t      RESERVED2[1];  /**< Reserved for future use **/
  volatile uint32_t EM4CONF;       /**< Energy mode 4 configuration register  */
  volatile uint32_t BUCTRL;        /**< Backup Power configuration register  */
  volatile uint32_t PWRCONF;       /**< Power connection configuration register  */
  volatile uint32_t BUINACT;       /**< Backup mode inactive configuration register  */
  volatile uint32_t BUACT;         /**< Backup mode active configuration register  */
  volatile const uint32_t  STATUS;        /**< Status register  */
  volatile uint32_t ROUTE;         /**< I/O Routing Register  */
  volatile const uint32_t  IF;            /**< Interrupt Flag Register  */
  volatile uint32_t IFS;           /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;           /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;           /**< Interrupt Enable Register  */
  volatile uint32_t BUBODBUVINCAL; /**< BU_VIN Backup BOD calibration  */
  volatile uint32_t BUBODUNREGCAL; /**< Unregulated power Backup BOD calibration  */
} EMU_TypeDef;                 /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_EMU_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for EMU CTRL */

/* Bit fields for EMU LOCK */

/* Bit fields for EMU AUXCTRL */

/* Bit fields for EMU EM4CONF */

/* Bit fields for EMU BUCTRL */

/* Bit fields for EMU PWRCONF */

/* Bit fields for EMU BUINACT */

/* Bit fields for EMU BUACT */

/* Bit fields for EMU STATUS */

/* Bit fields for EMU ROUTE */

/* Bit fields for EMU IF */

/* Bit fields for EMU IFS */

/* Bit fields for EMU IFC */

/* Bit fields for EMU IEN */

/* Bit fields for EMU BUBODBUVINCAL */

/* Bit fields for EMU BUBODUNREGCAL */

/** @} End of group EZR32WG_EMU */


/**************************************************************************//**
 * @file ezr32wg_rmu.h
 * @brief EZR32WG_RMU register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_RMU
 * @{
 * @brief EZR32WG_RMU Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Control Register  */
  volatile const uint32_t  RSTCAUSE; /**< Reset Cause Register  */
  volatile uint32_t  CMD;      /**< Command Register  */
} RMU_TypeDef;            /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_RMU_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for RMU CTRL */

/* Bit fields for RMU RSTCAUSE */

/* Bit fields for RMU CMD */

/** @} End of group EZR32WG_RMU */


/**************************************************************************//**
 * @file ezr32wg_cmu.h
 * @brief EZR32WG_CMU register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_CMU
 * @{
 * @brief EZR32WG_CMU Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< CMU Control Register  */
  volatile uint32_t HFCORECLKDIV; /**< High Frequency Core Clock Division Register  */
  volatile uint32_t HFPERCLKDIV;  /**< High Frequency Peripheral Clock Division Register  */
  volatile uint32_t HFRCOCTRL;    /**< HFRCO Control Register  */
  volatile uint32_t LFRCOCTRL;    /**< LFRCO Control Register  */
  volatile uint32_t AUXHFRCOCTRL; /**< AUXHFRCO Control Register  */
  volatile uint32_t CALCTRL;      /**< Calibration Control Register  */
  volatile uint32_t CALCNT;       /**< Calibration Counter Register  */
  volatile uint32_t OSCENCMD;     /**< Oscillator Enable/Disable Command Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile uint32_t LFCLKSEL;     /**< Low Frequency Clock Select Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile uint32_t HFCORECLKEN0; /**< High Frequency Core Clock Enable Register 0  */
  volatile uint32_t HFPERCLKEN0;  /**< High Frequency Peripheral Clock Enable Register 0  */
  uint32_t      RESERVED0[2]; /**< Reserved for future use **/
  volatile const uint32_t  SYNCBUSY;     /**< Synchronization Busy Register  */
  volatile uint32_t FREEZE;       /**< Freeze Register  */
  volatile uint32_t LFACLKEN0;    /**< Low Frequency A Clock Enable Register 0  (Async Reg)  */
  uint32_t      RESERVED1[1]; /**< Reserved for future use **/
  volatile uint32_t LFBCLKEN0;    /**< Low Frequency B Clock Enable Register 0 (Async Reg)  */

  uint32_t      RESERVED2[1]; /**< Reserved for future use **/
  volatile uint32_t LFAPRESC0;    /**< Low Frequency A Prescaler Register 0 (Async Reg)  */
  uint32_t      RESERVED3[1]; /**< Reserved for future use **/
  volatile uint32_t LFBPRESC0;    /**< Low Frequency B Prescaler Register 0  (Async Reg)  */
  uint32_t      RESERVED4[1]; /**< Reserved for future use **/
  volatile uint32_t PCNTCTRL;     /**< PCNT Control Register  */

  uint32_t      RESERVED5[1]; /**< Reserved for future use **/
  volatile uint32_t ROUTE;        /**< I/O Routing Register  */
  volatile uint32_t LOCK;         /**< Configuration Lock Register  */
} CMU_TypeDef;                /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_CMU_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for CMU CTRL */

/* Bit fields for CMU HFCORECLKDIV */

/* Bit fields for CMU HFPERCLKDIV */

/* Bit fields for CMU HFRCOCTRL */

/* Bit fields for CMU LFRCOCTRL */

/* Bit fields for CMU AUXHFRCOCTRL */

/* Bit fields for CMU CALCTRL */

/* Bit fields for CMU CALCNT */

/* Bit fields for CMU OSCENCMD */

/* Bit fields for CMU CMD */

/* Bit fields for CMU LFCLKSEL */

/* Bit fields for CMU STATUS */

/* Bit fields for CMU IF */

/* Bit fields for CMU IFS */

/* Bit fields for CMU IFC */

/* Bit fields for CMU IEN */

/* Bit fields for CMU HFCORECLKEN0 */

/* Bit fields for CMU HFPERCLKEN0 */

/* Bit fields for CMU SYNCBUSY */

/* Bit fields for CMU FREEZE */

/* Bit fields for CMU LFACLKEN0 */

/* Bit fields for CMU LFBCLKEN0 */

/* Bit fields for CMU LFAPRESC0 */

/* Bit fields for CMU LFBPRESC0 */

/* Bit fields for CMU PCNTCTRL */

/* Bit fields for CMU ROUTE */

/* Bit fields for CMU LOCK */

/** @} End of group EZR32WG_CMU */


/**************************************************************************//**
 * @file ezr32wg_lesense_st.h
 * @brief EZR32WG_LESENSE_ST register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief LESENSE_ST EZR32WG LESENSE ST
 *****************************************************************************/
typedef struct
{
  volatile uint32_t TCONFA; /**< State transition configuration A  */
  volatile uint32_t TCONFB; /**< State transition configuration B  */
} LESENSE_ST_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_lesense_buf.h
 * @brief EZR32WG_LESENSE_BUF register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief LESENSE_BUF EZR32WG LESENSE BUF
 *****************************************************************************/
typedef struct
{
  volatile uint32_t DATA; /**< Scan results  */
} LESENSE_BUF_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_lesense_ch.h
 * @brief EZR32WG_LESENSE_CH register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief LESENSE_CH EZR32WG LESENSE CH
 *****************************************************************************/
typedef struct
{
  volatile uint32_t TIMING;       /**< Scan configuration  */
  volatile uint32_t INTERACT;     /**< Scan configuration  */
  volatile uint32_t EVAL;         /**< Scan configuration  */
  uint32_t      RESERVED0[1]; /**< Reserved future */
} LESENSE_CH_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_lesense.h
 * @brief EZR32WG_LESENSE register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_LESENSE
 * @{
 * @brief EZR32WG_LESENSE Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t       CTRL;           /**< Control Register  */
  volatile uint32_t       TIMCTRL;        /**< Timing Control Register  */
  volatile uint32_t       PERCTRL;        /**< Peripheral Control Register  */
  volatile uint32_t       DECCTRL;        /**< Decoder control Register  */
  volatile uint32_t       BIASCTRL;       /**< Bias Control Register  */
  volatile uint32_t       CMD;            /**< Command Register  */
  volatile uint32_t       CHEN;           /**< Channel enable Register  */
  volatile const uint32_t        SCANRES;        /**< Scan result register  */
  volatile const uint32_t        STATUS;         /**< Status Register  */
  volatile const uint32_t        PTR;            /**< Result buffer pointers  */
  volatile const uint32_t        BUFDATA;        /**< Result buffer data register  */
  volatile const uint32_t        CURCH;          /**< Current channel index  */
  volatile uint32_t       DECSTATE;       /**< Current decoder state  */
  volatile uint32_t       SENSORSTATE;    /**< Decoder input register  */
  volatile uint32_t       IDLECONF;       /**< GPIO Idle phase configuration  */
  volatile uint32_t       ALTEXCONF;      /**< Alternative excite pin configuration  */
  volatile const uint32_t        IF;             /**< Interrupt Flag Register  */
  volatile uint32_t       IFC;            /**< Interrupt Flag Clear Register  */
  volatile uint32_t       IFS;            /**< Interrupt Flag Set Register  */
  volatile uint32_t       IEN;            /**< Interrupt Enable Register  */
  volatile const uint32_t        SYNCBUSY;       /**< Synchronization Busy Register  */
  volatile uint32_t       ROUTE;          /**< I/O Routing Register  */
  volatile uint32_t       POWERDOWN;      /**< LESENSE RAM power-down register  */

  uint32_t            RESERVED0[105]; /**< Reserved registers */
  LESENSE_ST_TypeDef  ST[16];         /**< Decoding states */

  LESENSE_BUF_TypeDef BUF[16];        /**< Scanresult */

  LESENSE_CH_TypeDef  CH[16];         /**< Scanconfig */
} LESENSE_TypeDef;                    /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_LESENSE_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for LESENSE CTRL */

/* Bit fields for LESENSE TIMCTRL */

/* Bit fields for LESENSE PERCTRL */

/* Bit fields for LESENSE DECCTRL */

/* Bit fields for LESENSE BIASCTRL */

/* Bit fields for LESENSE CMD */

/* Bit fields for LESENSE CHEN */

/* Bit fields for LESENSE SCANRES */

/* Bit fields for LESENSE STATUS */

/* Bit fields for LESENSE PTR */

/* Bit fields for LESENSE BUFDATA */

/* Bit fields for LESENSE CURCH */

/* Bit fields for LESENSE DECSTATE */

/* Bit fields for LESENSE SENSORSTATE */

/* Bit fields for LESENSE IDLECONF */

/* Bit fields for LESENSE ALTEXCONF */

/* Bit fields for LESENSE IF */

/* Bit fields for LESENSE IFC */

/* Bit fields for LESENSE IFS */

/* Bit fields for LESENSE IEN */

/* Bit fields for LESENSE SYNCBUSY */

/* Bit fields for LESENSE ROUTE */

/* Bit fields for LESENSE POWERDOWN */

/* Bit fields for LESENSE ST_TCONFA */

/* Bit fields for LESENSE ST_TCONFB */

/* Bit fields for LESENSE BUF_DATA */

/* Bit fields for LESENSE CH_TIMING */

/* Bit fields for LESENSE CH_INTERACT */

/* Bit fields for LESENSE CH_EVAL */

/** @} End of group EZR32WG_LESENSE */


/**************************************************************************//**
 * @file ezr32wg_fpueh.h
 * @brief EZR32WG_FPUEH register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_FPUEH
 * @{
 * @brief EZR32WG_FPUEH Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile const uint32_t  IF;  /**< Interrupt Flag Register  */
  volatile uint32_t IFS; /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC; /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN; /**< Interrupt Enable Register  */
} FPUEH_TypeDef;     /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_FPUEH_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for FPUEH IF */

/* Bit fields for FPUEH IFS */

/* Bit fields for FPUEH IFC */

/* Bit fields for FPUEH IEN */

/** @} End of group EZR32WG_FPUEH */


/**************************************************************************//**
 * @file ezr32wg_usart.h
 * @brief EZR32WG_USART register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_USART
 * @{
 * @brief EZR32WG_USART Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;       /**< Control Register  */
  volatile uint32_t FRAME;      /**< USART Frame Format Register  */
  volatile uint32_t TRIGCTRL;   /**< USART Trigger Control register  */
  volatile uint32_t CMD;        /**< Command Register  */
  volatile const uint32_t  STATUS;     /**< USART Status Register  */
  volatile uint32_t CLKDIV;     /**< Clock Control Register  */
  volatile const uint32_t  RXDATAX;    /**< RX Buffer Data Extended Register  */
  volatile const uint32_t  RXDATA;     /**< RX Buffer Data Register  */
  volatile const uint32_t  RXDOUBLEX;  /**< RX Buffer Double Data Extended Register  */
  volatile const uint32_t  RXDOUBLE;   /**< RX FIFO Double Data Register  */
  volatile const uint32_t  RXDATAXP;   /**< RX Buffer Data Extended Peek Register  */
  volatile const uint32_t  RXDOUBLEXP; /**< RX Buffer Double Data Extended Peek Register  */
  volatile uint32_t TXDATAX;    /**< TX Buffer Data Extended Register  */
  volatile uint32_t TXDATA;     /**< TX Buffer Data Register  */
  volatile uint32_t TXDOUBLEX;  /**< TX Buffer Double Data Extended Register  */
  volatile uint32_t TXDOUBLE;   /**< TX Buffer Double Data Register  */
  volatile const uint32_t  IF;         /**< Interrupt Flag Register  */
  volatile uint32_t IFS;        /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;        /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;        /**< Interrupt Enable Register  */
  volatile uint32_t IRCTRL;     /**< IrDA Control Register  */
  volatile uint32_t ROUTE;      /**< I/O Routing Register  */
  volatile uint32_t INPUT;      /**< USART Input Register  */
  volatile uint32_t I2SCTRL;    /**< I2S Control Register  */
} USART_TypeDef;            /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_USART_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for USART CTRL */

/* Bit fields for USART FRAME */

/* Bit fields for USART TRIGCTRL */

/* Bit fields for USART CMD */

/* Bit fields for USART STATUS */

/* Bit fields for USART CLKDIV */

/* Bit fields for USART RXDATAX */

/* Bit fields for USART RXDATA */

/* Bit fields for USART RXDOUBLEX */

/* Bit fields for USART RXDOUBLE */

/* Bit fields for USART RXDATAXP */

/* Bit fields for USART RXDOUBLEXP */

/* Bit fields for USART TXDATAX */

/* Bit fields for USART TXDATA */

/* Bit fields for USART TXDOUBLEX */

/* Bit fields for USART TXDOUBLE */

/* Bit fields for USART IF */

/* Bit fields for USART IFS */

/* Bit fields for USART IFC */

/* Bit fields for USART IEN */

/* Bit fields for USART IRCTRL */

/* Bit fields for USART ROUTE */

/* Bit fields for USART INPUT */

/* Bit fields for USART I2SCTRL */

/** @} End of group EZR32WG_USART */


/**************************************************************************//**
 * @file ezr32wg_timer_cc.h
 * @brief EZR32WG_TIMER_CC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief TIMER_CC EZR32WG TIMER CC
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL; /**< CC Channel Control Register  */
  volatile uint32_t CCV;  /**< CC Channel Value Register  */
  volatile const uint32_t  CCVP; /**< CC Channel Value Peek Register  */
  volatile uint32_t CCVB; /**< CC Channel Buffer Register  */
} TIMER_CC_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_timer.h
 * @brief EZR32WG_TIMER register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_TIMER
 * @{
 * @brief EZR32WG_TIMER Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t    CTRL;         /**< Control Register  */
  volatile uint32_t    CMD;          /**< Command Register  */
  volatile const uint32_t     STATUS;       /**< Status Register  */
  volatile uint32_t    IEN;          /**< Interrupt Enable Register  */
  volatile const uint32_t     IF;           /**< Interrupt Flag Register  */
  volatile uint32_t    IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t    IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t    TOP;          /**< Counter Top Value Register  */
  volatile uint32_t    TOPB;         /**< Counter Top Value Buffer Register  */
  volatile uint32_t    CNT;          /**< Counter Value Register  */
  volatile uint32_t    ROUTE;        /**< I/O Routing Register  */

  uint32_t         RESERVED0[1]; /**< Reserved registers */
  TIMER_CC_TypeDef CC[3];        /**< Compare/Capture Channel */

  uint32_t         RESERVED1[4]; /**< Reserved for future use **/
  volatile uint32_t    DTCTRL;       /**< DTI Control Register  */
  volatile uint32_t    DTTIME;       /**< DTI Time Control Register  */
  volatile uint32_t    DTFC;         /**< DTI Fault Configuration Register  */
  volatile uint32_t    DTOGEN;       /**< DTI Output Generation Enable Register  */
  volatile const uint32_t     DTFAULT;      /**< DTI Fault Register  */
  volatile uint32_t     DTFAULTC;     /**< DTI Fault Clear Register  */
  volatile uint32_t    DTLOCK;       /**< DTI Configuration Lock Register  */
} TIMER_TypeDef;                 /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_TIMER_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for TIMER CTRL */

/* Bit fields for TIMER CMD */

/* Bit fields for TIMER STATUS */

/* Bit fields for TIMER IEN */

/* Bit fields for TIMER IF */

/* Bit fields for TIMER IFS */

/* Bit fields for TIMER IFC */

/* Bit fields for TIMER TOP */

/* Bit fields for TIMER TOPB */

/* Bit fields for TIMER CNT */

/* Bit fields for TIMER ROUTE */

/* Bit fields for TIMER CC_CTRL */

/* Bit fields for TIMER CC_CCV */

/* Bit fields for TIMER CC_CCVP */

/* Bit fields for TIMER CC_CCVB */

/* Bit fields for TIMER DTCTRL */

/* Bit fields for TIMER DTTIME */

/* Bit fields for TIMER DTFC */

/* Bit fields for TIMER DTOGEN */

/* Bit fields for TIMER DTFAULT */

/* Bit fields for TIMER DTFAULTC */

/* Bit fields for TIMER DTLOCK */

/** @} End of group EZR32WG_TIMER */


/**************************************************************************//**
 * @file ezr32wg_acmp.h
 * @brief EZR32WG_ACMP register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_ACMP
 * @{
 * @brief EZR32WG_ACMP Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Control Register  */
  volatile uint32_t INPUTSEL; /**< Input Selection Register  */
  volatile const uint32_t  STATUS;   /**< Status Register  */
  volatile uint32_t IEN;      /**< Interrupt Enable Register  */
  volatile const uint32_t  IF;       /**< Interrupt Flag Register  */
  volatile uint32_t IFS;      /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;      /**< Interrupt Flag Clear Register  */
  volatile uint32_t ROUTE;    /**< I/O Routing Register  */
} ACMP_TypeDef;           /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_ACMP_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for ACMP CTRL */

/* Bit fields for ACMP INPUTSEL */

/* Bit fields for ACMP STATUS */

/* Bit fields for ACMP IEN */

/* Bit fields for ACMP IF */

/* Bit fields for ACMP IFS */

/* Bit fields for ACMP IFC */

/* Bit fields for ACMP ROUTE */

/** @} End of group EZR32WG_ACMP */


/**************************************************************************//**
 * @file ezr32wg_leuart.h
 * @brief EZR32WG_LEUART register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_LEUART
 * @{
 * @brief EZR32WG_LEUART Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;          /**< Control Register  */
  volatile uint32_t CMD;           /**< Command Register  */
  volatile const uint32_t  STATUS;        /**< Status Register  */
  volatile uint32_t CLKDIV;        /**< Clock Control Register  */
  volatile uint32_t STARTFRAME;    /**< Start Frame Register  */
  volatile uint32_t SIGFRAME;      /**< Signal Frame Register  */
  volatile const uint32_t  RXDATAX;       /**< Receive Buffer Data Extended Register  */
  volatile const uint32_t  RXDATA;        /**< Receive Buffer Data Register  */
  volatile const uint32_t  RXDATAXP;      /**< Receive Buffer Data Extended Peek Register  */
  volatile uint32_t TXDATAX;       /**< Transmit Buffer Data Extended Register  */
  volatile uint32_t TXDATA;        /**< Transmit Buffer Data Register  */
  volatile const uint32_t  IF;            /**< Interrupt Flag Register  */
  volatile uint32_t IFS;           /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;           /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;           /**< Interrupt Enable Register  */
  volatile uint32_t PULSECTRL;     /**< Pulse Control Register  */

  volatile uint32_t FREEZE;        /**< Freeze Register  */
  volatile const uint32_t  SYNCBUSY;      /**< Synchronization Busy Register  */

  uint32_t      RESERVED0[3];  /**< Reserved for future use **/
  volatile uint32_t ROUTE;         /**< I/O Routing Register  */
  uint32_t      RESERVED1[21]; /**< Reserved for future use **/
  volatile uint32_t INPUT;         /**< LEUART Input Register  */
} LEUART_TypeDef;              /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_LEUART_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for LEUART CTRL */

/* Bit fields for LEUART CMD */

/* Bit fields for LEUART STATUS */

/* Bit fields for LEUART CLKDIV */

/* Bit fields for LEUART STARTFRAME */

/* Bit fields for LEUART SIGFRAME */

/* Bit fields for LEUART RXDATAX */

/* Bit fields for LEUART RXDATA */

/* Bit fields for LEUART RXDATAXP */

/* Bit fields for LEUART TXDATAX */

/* Bit fields for LEUART TXDATA */

/* Bit fields for LEUART IF */

/* Bit fields for LEUART IFS */

/* Bit fields for LEUART IFC */

/* Bit fields for LEUART IEN */

/* Bit fields for LEUART PULSECTRL */

/* Bit fields for LEUART FREEZE */

/* Bit fields for LEUART SYNCBUSY */

/* Bit fields for LEUART ROUTE */

/* Bit fields for LEUART INPUT */

/** @} End of group EZR32WG_LEUART */


/**************************************************************************//**
 * @file ezr32wg_rtc.h
 * @brief EZR32WG_RTC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_RTC
 * @{
 * @brief EZR32WG_RTC Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Control Register  */
  volatile uint32_t CNT;      /**< Counter Value Register  */
  volatile uint32_t COMP0;    /**< Compare Value Register 0  */
  volatile uint32_t COMP1;    /**< Compare Value Register 1  */
  volatile const uint32_t  IF;       /**< Interrupt Flag Register  */
  volatile uint32_t IFS;      /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;      /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;      /**< Interrupt Enable Register  */

  volatile uint32_t FREEZE;   /**< Freeze Register  */
  volatile const uint32_t  SYNCBUSY; /**< Synchronization Busy Register  */
} RTC_TypeDef;            /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_RTC_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for RTC CTRL */

/* Bit fields for RTC CNT */

/* Bit fields for RTC COMP0 */

/* Bit fields for RTC COMP1 */

/* Bit fields for RTC IF */

/* Bit fields for RTC IFS */

/* Bit fields for RTC IFC */

/* Bit fields for RTC IEN */

/* Bit fields for RTC FREEZE */

/* Bit fields for RTC SYNCBUSY */

/** @} End of group EZR32WG_RTC */


/**************************************************************************//**
 * @file ezr32wg_letimer.h
 * @brief EZR32WG_LETIMER register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_LETIMER
 * @{
 * @brief EZR32WG_LETIMER Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Control Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile uint32_t CNT;          /**< Counter Value Register  */
  volatile uint32_t COMP0;        /**< Compare Value Register 0  */
  volatile uint32_t COMP1;        /**< Compare Value Register 1  */
  volatile uint32_t REP0;         /**< Repeat Counter Register 0  */
  volatile uint32_t REP1;         /**< Repeat Counter Register 1  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */

  volatile uint32_t FREEZE;       /**< Freeze Register  */
  volatile const uint32_t  SYNCBUSY;     /**< Synchronization Busy Register  */

  uint32_t      RESERVED0[2]; /**< Reserved for future use **/
  volatile uint32_t ROUTE;        /**< I/O Routing Register  */
} LETIMER_TypeDef;            /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_LETIMER_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for LETIMER CTRL */

/* Bit fields for LETIMER CMD */

/* Bit fields for LETIMER STATUS */

/* Bit fields for LETIMER CNT */

/* Bit fields for LETIMER COMP0 */

/* Bit fields for LETIMER COMP1 */

/* Bit fields for LETIMER REP0 */

/* Bit fields for LETIMER REP1 */

/* Bit fields for LETIMER IF */

/* Bit fields for LETIMER IFS */

/* Bit fields for LETIMER IFC */

/* Bit fields for LETIMER IEN */

/* Bit fields for LETIMER FREEZE */

/* Bit fields for LETIMER SYNCBUSY */

/* Bit fields for LETIMER ROUTE */

/** @} End of group EZR32WG_LETIMER */


/**************************************************************************//**
 * @file ezr32wg_pcnt.h
 * @brief EZR32WG_PCNT register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_PCNT
 * @{
 * @brief EZR32WG_PCNT Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Control Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile const uint32_t  CNT;          /**< Counter Value Register  */
  volatile const uint32_t  TOP;          /**< Top Value Register  */
  volatile uint32_t TOPB;         /**< Top Value Buffer Register  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile uint32_t ROUTE;        /**< I/O Routing Register  */

  volatile uint32_t FREEZE;       /**< Freeze Register  */
  volatile const uint32_t  SYNCBUSY;     /**< Synchronization Busy Register  */

  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t AUXCNT;       /**< Auxiliary Counter Value Register  */
  volatile uint32_t INPUT;        /**< PCNT Input Register  */
} PCNT_TypeDef;               /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_PCNT_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for PCNT CTRL */

/* Bit fields for PCNT CMD */

/* Bit fields for PCNT STATUS */

/* Bit fields for PCNT CNT */

/* Bit fields for PCNT TOP */

/* Bit fields for PCNT TOPB */

/* Bit fields for PCNT IF */

/* Bit fields for PCNT IFS */

/* Bit fields for PCNT IFC */

/* Bit fields for PCNT IEN */

/* Bit fields for PCNT ROUTE */

/* Bit fields for PCNT FREEZE */

/* Bit fields for PCNT SYNCBUSY */

/* Bit fields for PCNT AUXCNT */

/* Bit fields for PCNT INPUT */

/** @} End of group EZR32WG_PCNT */


/**************************************************************************//**
 * @file ezr32wg_i2c.h
 * @brief EZR32WG_I2C register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_I2C
 * @{
 * @brief EZR32WG_I2C Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;      /**< Control Register  */
  volatile uint32_t CMD;       /**< Command Register  */
  volatile const uint32_t  STATE;     /**< State Register  */
  volatile const uint32_t  STATUS;    /**< Status Register  */
  volatile uint32_t CLKDIV;    /**< Clock Division Register  */
  volatile uint32_t SADDR;     /**< Slave Address Register  */
  volatile uint32_t SADDRMASK; /**< Slave Address Mask Register  */
  volatile const uint32_t  RXDATA;    /**< Receive Buffer Data Register  */
  volatile const uint32_t  RXDATAP;   /**< Receive Buffer Data Peek Register  */
  volatile uint32_t TXDATA;    /**< Transmit Buffer Data Register  */
  volatile const uint32_t  IF;        /**< Interrupt Flag Register  */
  volatile uint32_t IFS;       /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;       /**< Interrupt Flag Clear Register  */
  volatile uint32_t IEN;       /**< Interrupt Enable Register  */
  volatile uint32_t ROUTE;     /**< I/O Routing Register  */
} I2C_TypeDef;             /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_I2C_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for I2C CTRL */

/* Bit fields for I2C CMD */

/* Bit fields for I2C STATE */

/* Bit fields for I2C STATUS */

/* Bit fields for I2C CLKDIV */

/* Bit fields for I2C SADDR */

/* Bit fields for I2C SADDRMASK */

/* Bit fields for I2C RXDATA */

/* Bit fields for I2C RXDATAP */

/* Bit fields for I2C TXDATA */

/* Bit fields for I2C IF */

/* Bit fields for I2C IFS */

/* Bit fields for I2C IFC */

/* Bit fields for I2C IEN */

/* Bit fields for I2C ROUTE */

/** @} End of group EZR32WG_I2C */


/**************************************************************************//**
 * @file ezr32wg_gpio_p.h
 * @brief EZR32WG_GPIO_P register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief GPIO_P EZR32WG GPIO P
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Port Control Register  */
  volatile uint32_t MODEL;    /**< Port Pin Mode Low Register  */
  volatile uint32_t MODEH;    /**< Port Pin Mode High Register  */
  volatile uint32_t DOUT;     /**< Port Data Out Register  */
  volatile uint32_t  DOUTSET;  /**< Port Data Out Set Register  */
  volatile uint32_t  DOUTCLR;  /**< Port Data Out Clear Register  */
  volatile uint32_t  DOUTTGL;  /**< Port Data Out Toggle Register  */
  volatile const uint32_t  DIN;      /**< Port Data In Register  */
  volatile uint32_t PINLOCKN; /**< Port Unlocked Pins Register  */
} GPIO_P_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_gpio.h
 * @brief EZR32WG_GPIO register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_GPIO
 * @{
 * @brief EZR32WG_GPIO Register Declaration
 *****************************************************************************/
typedef struct
{
  GPIO_P_TypeDef P[6];          /**< Port configuration bits */

  uint32_t       RESERVED0[10]; /**< Reserved for future use **/
  volatile uint32_t  EXTIPSELL;     /**< External Interrupt Port Select Low Register  */
  volatile uint32_t  EXTIPSELH;     /**< External Interrupt Port Select High Register  */
  volatile uint32_t  EXTIRISE;      /**< External Interrupt Rising Edge Trigger Register  */
  volatile uint32_t  EXTIFALL;      /**< External Interrupt Falling Edge Trigger Register  */
  volatile uint32_t  IEN;           /**< Interrupt Enable Register  */
  volatile const uint32_t   IF;            /**< Interrupt Flag Register  */
  volatile uint32_t  IFS;           /**< Interrupt Flag Set Register  */
  volatile uint32_t  IFC;           /**< Interrupt Flag Clear Register  */

  volatile uint32_t  ROUTE;         /**< I/O Routing Register  */
  volatile uint32_t  INSENSE;       /**< Input Sense Register  */
  volatile uint32_t  LOCK;          /**< Configuration Lock Register  */
  volatile uint32_t  CTRL;          /**< GPIO Control Register  */
  volatile uint32_t  CMD;           /**< GPIO Command Register  */
  volatile uint32_t  EM4WUEN;       /**< EM4 Wake-up Enable Register  */
  volatile uint32_t  EM4WUPOL;      /**< EM4 Wake-up Polarity Register  */
  volatile const uint32_t   EM4WUCAUSE;    /**< EM4 Wake-up Cause Register  */
} GPIO_TypeDef;                 /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_GPIO_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for GPIO P_CTRL */

/* Bit fields for GPIO P_MODEL */

/* Bit fields for GPIO P_MODEH */

/* Bit fields for GPIO P_DOUT */

/* Bit fields for GPIO P_DOUTSET */

/* Bit fields for GPIO P_DOUTCLR */

/* Bit fields for GPIO P_DOUTTGL */

/* Bit fields for GPIO P_DIN */

/* Bit fields for GPIO P_PINLOCKN */

/* Bit fields for GPIO EXTIPSELL */

/* Bit fields for GPIO EXTIPSELH */

/* Bit fields for GPIO EXTIRISE */

/* Bit fields for GPIO EXTIFALL */

/* Bit fields for GPIO IEN */

/* Bit fields for GPIO IF */

/* Bit fields for GPIO IFS */

/* Bit fields for GPIO IFC */

/* Bit fields for GPIO ROUTE */

/* Bit fields for GPIO INSENSE */

/* Bit fields for GPIO LOCK */

/* Bit fields for GPIO CTRL */

/* Bit fields for GPIO CMD */

/* Bit fields for GPIO EM4WUEN */

/* Bit fields for GPIO EM4WUPOL */

/* Bit fields for GPIO EM4WUCAUSE */

/** @} End of group EZR32WG_GPIO */


/**************************************************************************//**
 * @file ezr32wg_vcmp.h
 * @brief EZR32WG_VCMP register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_VCMP
 * @{
 * @brief EZR32WG_VCMP Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Control Register  */
  volatile uint32_t INPUTSEL; /**< Input Selection Register  */
  volatile const uint32_t  STATUS;   /**< Status Register  */
  volatile uint32_t IEN;      /**< Interrupt Enable Register  */
  volatile const uint32_t  IF;       /**< Interrupt Flag Register  */
  volatile uint32_t IFS;      /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;      /**< Interrupt Flag Clear Register  */
} VCMP_TypeDef;           /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_VCMP_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for VCMP CTRL */

/* Bit fields for VCMP INPUTSEL */

/* Bit fields for VCMP STATUS */

/* Bit fields for VCMP IEN */

/* Bit fields for VCMP IF */

/* Bit fields for VCMP IFS */

/* Bit fields for VCMP IFC */

/** @} End of group EZR32WG_VCMP */


/**************************************************************************//**
 * @file ezr32wg_prs_ch.h
 * @brief EZR32WG_PRS_CH register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief PRS_CH EZR32WG PRS CH
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL; /**< Channel Control Register  */
} PRS_CH_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_prs.h
 * @brief EZR32WG_PRS register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_PRS
 * @{
 * @brief EZR32WG_PRS Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t  SWPULSE;      /**< Software Pulse Register  */
  volatile uint32_t  SWLEVEL;      /**< Software Level Register  */
  volatile uint32_t  ROUTE;        /**< I/O Routing Register  */

  uint32_t       RESERVED0[1]; /**< Reserved registers */
  PRS_CH_TypeDef CH[12];       /**< Channel registers */
} PRS_TypeDef;                 /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_PRS_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for PRS SWPULSE */

/* Bit fields for PRS SWLEVEL */

/* Bit fields for PRS ROUTE */

/* Bit fields for PRS CH_CTRL */

/** @} End of group EZR32WG_PRS */


/**************************************************************************//**
 * @file ezr32wg_adc.h
 * @brief EZR32WG_ADC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_ADC
 * @{
 * @brief EZR32WG_ADC Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Control Register  */
  volatile uint32_t CMD;          /**< Command Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile uint32_t SINGLECTRL;   /**< Single Sample Control Register  */
  volatile uint32_t SCANCTRL;     /**< Scan Control Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile const uint32_t  SINGLEDATA;   /**< Single Conversion Result Data  */
  volatile const uint32_t  SCANDATA;     /**< Scan Conversion Result Data  */
  volatile const uint32_t  SINGLEDATAP;  /**< Single Conversion Result Data Peek Register  */
  volatile const uint32_t  SCANDATAP;    /**< Scan Sequence Result Data Peek Register  */
  volatile uint32_t CAL;          /**< Calibration Register  */

  uint32_t      RESERVED0[1]; /**< Reserved for future use **/
  volatile uint32_t BIASPROG;     /**< Bias Programming Register  */
} ADC_TypeDef;                /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_ADC_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for ADC CTRL */

/* Bit fields for ADC CMD */

/* Bit fields for ADC STATUS */

/* Bit fields for ADC SINGLECTRL */

/* Bit fields for ADC SCANCTRL */

/* Bit fields for ADC IEN */

/* Bit fields for ADC IF */

/* Bit fields for ADC IFS */

/* Bit fields for ADC IFC */

/* Bit fields for ADC SINGLEDATA */

/* Bit fields for ADC SCANDATA */

/* Bit fields for ADC SINGLEDATAP */

/* Bit fields for ADC SCANDATAP */

/* Bit fields for ADC CAL */

/* Bit fields for ADC BIASPROG */

/** @} End of group EZR32WG_ADC */


/**************************************************************************//**
 * @file ezr32wg_dac.h
 * @brief EZR32WG_DAC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_DAC
 * @{
 * @brief EZR32WG_DAC Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;         /**< Control Register  */
  volatile const uint32_t  STATUS;       /**< Status Register  */
  volatile uint32_t CH0CTRL;      /**< Channel 0 Control Register  */
  volatile uint32_t CH1CTRL;      /**< Channel 1 Control Register  */
  volatile uint32_t IEN;          /**< Interrupt Enable Register  */
  volatile const uint32_t  IF;           /**< Interrupt Flag Register  */
  volatile uint32_t IFS;          /**< Interrupt Flag Set Register  */
  volatile uint32_t IFC;          /**< Interrupt Flag Clear Register  */
  volatile uint32_t CH0DATA;      /**< Channel 0 Data Register  */
  volatile uint32_t CH1DATA;      /**< Channel 1 Data Register  */
  volatile uint32_t COMBDATA;     /**< Combined Data Register  */
  volatile uint32_t CAL;          /**< Calibration Register  */
  volatile uint32_t BIASPROG;     /**< Bias Programming Register  */
  uint32_t      RESERVED0[8]; /**< Reserved for future use **/
  volatile uint32_t OPACTRL;      /**< Operational Amplifier Control Register  */
  volatile uint32_t OPAOFFSET;    /**< Operational Amplifier Offset Register  */
  volatile uint32_t OPA0MUX;      /**< Operational Amplifier Mux Configuration Register  */
  volatile uint32_t OPA1MUX;      /**< Operational Amplifier Mux Configuration Register  */
  volatile uint32_t OPA2MUX;      /**< Operational Amplifier Mux Configuration Register  */
} DAC_TypeDef;                /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_DAC_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for DAC CTRL */

/* Bit fields for DAC STATUS */

/* Bit fields for DAC CH0CTRL */

/* Bit fields for DAC CH1CTRL */

/* Bit fields for DAC IEN */

/* Bit fields for DAC IF */

/* Bit fields for DAC IFS */

/* Bit fields for DAC IFC */

/* Bit fields for DAC CH0DATA */

/* Bit fields for DAC CH1DATA */

/* Bit fields for DAC COMBDATA */

/* Bit fields for DAC CAL */

/* Bit fields for DAC BIASPROG */

/* Bit fields for DAC OPACTRL */

/* Bit fields for DAC OPAOFFSET */

/* Bit fields for DAC OPA0MUX */

/* Bit fields for DAC OPA1MUX */

/* Bit fields for DAC OPA2MUX */

/** @} End of group EZR32WG_DAC */


/**************************************************************************//**
 * @file ezr32wg_burtc_ret.h
 * @brief EZR32WG_BURTC_RET register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @brief BURTC_RET EZR32WG BURTC RET
 *****************************************************************************/
typedef struct
{
  volatile uint32_t REG; /**< Retention Register  */
} BURTC_RET_TypeDef;

/**************************************************************************//**
 * @file ezr32wg_burtc.h
 * @brief EZR32WG_BURTC register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_BURTC
 * @{
 * @brief EZR32WG_BURTC Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t     CTRL;          /**< Control Register  */
  volatile uint32_t     LPMODE;        /**< Low power mode configuration  */
  volatile const uint32_t      CNT;           /**< Counter Value Register  */
  volatile uint32_t     COMP0;         /**< Counter Compare Value  */
  volatile const uint32_t      TIMESTAMP;     /**< Backup mode timestamp  */
  volatile uint32_t     LFXOFDET;      /**< LFXO   */
  volatile const uint32_t      STATUS;        /**< Status Register  */
  volatile uint32_t     CMD;           /**< Command Register  */
  volatile uint32_t     POWERDOWN;     /**< Retention RAM power-down Register  */
  volatile uint32_t     LOCK;          /**< Configuration Lock Register  */
  volatile const uint32_t      IF;            /**< Interrupt Flag Register  */
  volatile uint32_t     IFS;           /**< Interrupt Flag Set Register  */
  volatile uint32_t     IFC;           /**< Interrupt Flag Clear Register  */
  volatile uint32_t     IEN;           /**< Interrupt Enable Register  */

  volatile uint32_t     FREEZE;        /**< Freeze Register  */
  volatile const uint32_t      SYNCBUSY;      /**< Synchronization Busy Register  */

  uint32_t          RESERVED0[48]; /**< Reserved registers */
  BURTC_RET_TypeDef RET[128];      /**< RetentionReg */
} BURTC_TypeDef;                   /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_BURTC_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for BURTC CTRL */

/* Bit fields for BURTC LPMODE */

/* Bit fields for BURTC CNT */

/* Bit fields for BURTC COMP0 */

/* Bit fields for BURTC TIMESTAMP */

/* Bit fields for BURTC LFXOFDET */

/* Bit fields for BURTC STATUS */

/* Bit fields for BURTC CMD */

/* Bit fields for BURTC POWERDOWN */

/* Bit fields for BURTC LOCK */

/* Bit fields for BURTC IF */

/* Bit fields for BURTC IFS */

/* Bit fields for BURTC IFC */

/* Bit fields for BURTC IEN */

/* Bit fields for BURTC FREEZE */

/* Bit fields for BURTC SYNCBUSY */

/* Bit fields for BURTC RET_REG */

/** @} End of group EZR32WG_BURTC */


/**************************************************************************//**
 * @file ezr32wg_wdog.h
 * @brief EZR32WG_WDOG register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_WDOG
 * @{
 * @brief EZR32WG_WDOG Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t CTRL;     /**< Control Register  */
  volatile uint32_t CMD;      /**< Command Register  */

  volatile const uint32_t  SYNCBUSY; /**< Synchronization Busy Register  */
} WDOG_TypeDef;           /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_WDOG_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for WDOG CTRL */

/* Bit fields for WDOG CMD */

/* Bit fields for WDOG SYNCBUSY */

/** @} End of group EZR32WG_WDOG */


/**************************************************************************//**
 * @file ezr32wg_etm.h
 * @brief EZR32WG_ETM register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_ETM
 * @{
 * @brief EZR32WG_ETM Register Declaration
 *****************************************************************************/
typedef struct
{
  volatile uint32_t ETMCR;           /**< Main Control Register  */
  volatile const uint32_t  ETMCCR;          /**< Configuration Code Register  */
  volatile uint32_t ETMTRIGGER;      /**< ETM Trigger Event Register  */
  uint32_t      RESERVED0[1];    /**< Reserved for future use **/
  volatile uint32_t ETMSR;           /**< ETM Status Register  */
  volatile const uint32_t  ETMSCR;          /**< ETM System Configuration Register  */
  uint32_t      RESERVED1[2];    /**< Reserved for future use **/
  volatile uint32_t ETMTEEVR;        /**< ETM TraceEnable Event Register  */
  volatile uint32_t ETMTECR1;        /**< ETM Trace control Register  */
  uint32_t      RESERVED2[1];    /**< Reserved for future use **/
  volatile uint32_t ETMFFLR;         /**< ETM Fifo Full Level Register  */
  uint32_t      RESERVED3[68];   /**< Reserved for future use **/
  volatile uint32_t ETMCNTRLDVR1;    /**< Counter Reload Value  */
  uint32_t      RESERVED4[39];   /**< Reserved for future use **/
  volatile uint32_t ETMSYNCFR;       /**< Synchronisation Frequency Register  */
  volatile const uint32_t  ETMIDR;          /**< ID Register  */
  volatile const uint32_t  ETMCCER;         /**< Configuration Code Extension Register  */
  uint32_t      RESERVED5[1];    /**< Reserved for future use **/
  volatile uint32_t ETMTESSEICR;     /**< TraceEnable Start/Stop EmbeddedICE Control Register  */
  uint32_t      RESERVED6[1];    /**< Reserved for future use **/
  volatile uint32_t ETMTSEVR;        /**< Timestamp Event Register  */
  uint32_t      RESERVED7[1];    /**< Reserved for future use **/
  volatile uint32_t ETMTRACEIDR;     /**< CoreSight Trace ID Register  */
  uint32_t      RESERVED8[1];    /**< Reserved for future use **/
  volatile const uint32_t  ETMIDR2;         /**< ETM ID Register 2  */
  uint32_t      RESERVED9[66];   /**< Reserved for future use **/
  volatile const uint32_t  ETMPDSR;         /**< Device Power-down Status Register  */
  uint32_t      RESERVED10[754]; /**< Reserved for future use **/
  volatile uint32_t ETMISCIN;        /**< Integration Test Miscellaneous Inputs Register  */
  uint32_t      RESERVED11[1];   /**< Reserved for future use **/
  volatile uint32_t  ITTRIGOUT;       /**< Integration Test Trigger Out Register  */
  uint32_t      RESERVED12[1];   /**< Reserved for future use **/
  volatile const uint32_t  ETMITATBCTR2;    /**< ETM Integration Test ATB Control 2 Register  */
  uint32_t      RESERVED13[1];   /**< Reserved for future use **/
  volatile uint32_t  ETMITATBCTR0;    /**< ETM Integration Test ATB Control 0 Register  */
  uint32_t      RESERVED14[1];   /**< Reserved for future use **/
  volatile uint32_t ETMITCTRL;       /**< ETM Integration Control Register  */
  uint32_t      RESERVED15[39];  /**< Reserved for future use **/
  volatile uint32_t ETMCLAIMSET;     /**< ETM Claim Tag Set Register  */
  volatile uint32_t ETMCLAIMCLR;     /**< ETM Claim Tag Clear Register  */
  uint32_t      RESERVED16[2];   /**< Reserved for future use **/
  volatile uint32_t ETMLAR;          /**< ETM Lock Access Register  */
  volatile const uint32_t  ETMLSR;          /**< Lock Status Register  */
  volatile const uint32_t  ETMAUTHSTATUS;   /**< ETM Authentication Status Register  */
  uint32_t      RESERVED17[4];   /**< Reserved for future use **/
  volatile const uint32_t  ETMDEVTYPE;      /**< CoreSight Device Type Register  */
  volatile const uint32_t  ETMPIDR4;        /**< Peripheral ID4 Register  */
  volatile uint32_t  ETMPIDR5;        /**< Peripheral ID5 Register  */
  volatile uint32_t  ETMPIDR6;        /**< Peripheral ID6 Register  */
  volatile uint32_t  ETMPIDR7;        /**< Peripheral ID7 Register  */
  volatile const uint32_t  ETMPIDR0;        /**< Peripheral ID0 Register  */
  volatile const uint32_t  ETMPIDR1;        /**< Peripheral ID1 Register  */
  volatile const uint32_t  ETMPIDR2;        /**< Peripheral ID2 Register  */
  volatile const uint32_t  ETMPIDR3;        /**< Peripheral ID3 Register  */
  volatile const uint32_t  ETMCIDR0;        /**< Component ID0 Register  */
  volatile const uint32_t  ETMCIDR1;        /**< Component ID1 Register  */
  volatile const uint32_t  ETMCIDR2;        /**< Component ID2 Register  */
  volatile const uint32_t  ETMCIDR3;        /**< Component ID3 Register  */
} ETM_TypeDef;                   /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_ETM_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for ETM ETMCR */

/* Bit fields for ETM ETMCCR */

/* Bit fields for ETM ETMTRIGGER */

/* Bit fields for ETM ETMSR */

/* Bit fields for ETM ETMSCR */

/* Bit fields for ETM ETMTEEVR */

/* Bit fields for ETM ETMTECR1 */

/* Bit fields for ETM ETMFFLR */

/* Bit fields for ETM ETMCNTRLDVR1 */

/* Bit fields for ETM ETMSYNCFR */

/* Bit fields for ETM ETMIDR */

/* Bit fields for ETM ETMCCER */

/* Bit fields for ETM ETMTESSEICR */

/* Bit fields for ETM ETMTSEVR */

/* Bit fields for ETM ETMTRACEIDR */

/* Bit fields for ETM ETMIDR2 */

/* Bit fields for ETM ETMPDSR */

/* Bit fields for ETM ETMISCIN */

/* Bit fields for ETM ITTRIGOUT */

/* Bit fields for ETM ETMITATBCTR2 */

/* Bit fields for ETM ETMITATBCTR0 */

/* Bit fields for ETM ETMITCTRL */

/* Bit fields for ETM ETMCLAIMSET */

/* Bit fields for ETM ETMCLAIMCLR */

/* Bit fields for ETM ETMLAR */

/* Bit fields for ETM ETMLSR */

/* Bit fields for ETM ETMAUTHSTATUS */

/* Bit fields for ETM ETMDEVTYPE */

/* Bit fields for ETM ETMPIDR4 */

/* Bit fields for ETM ETMPIDR5 */

/* Bit fields for ETM ETMPIDR6 */

/* Bit fields for ETM ETMPIDR7 */

/* Bit fields for ETM ETMPIDR0 */

/* Bit fields for ETM ETMPIDR1 */

/* Bit fields for ETM ETMPIDR2 */

/* Bit fields for ETM ETMPIDR3 */

/* Bit fields for ETM ETMCIDR0 */

/* Bit fields for ETM ETMCIDR1 */

/* Bit fields for ETM ETMCIDR2 */

/* Bit fields for ETM ETMCIDR3 */

/** @} End of group EZR32WG_ETM */


/**************************************************************************//**
 * @file ezr32wg_dma_descriptor.h
 * @brief EZR32WG_DMA_DESCRIPTOR register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_DMA_DESCRIPTOR
 * @{
 *****************************************************************************/
typedef struct
{
  /* Note! Use of double __IO (volatile) qualifier to ensure that both */
  /* pointer and referenced memory are declared volatile. */
  volatile void * volatile SRCEND;     /**< DMA source address end */
  volatile void * volatile DSTEND;     /**< DMA destination address end */
  volatile uint32_t    CTRL;       /**< DMA control register */
  volatile uint32_t    USER;       /**< DMA padding register, available for user */
} DMA_DESCRIPTOR_TypeDef;      /** @} */

/**************************************************************************//**
 * @file ezr32wg_devinfo.h
 * @brief EZR32WG_DEVINFO register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_DEVINFO
 * @{
 *****************************************************************************/
typedef struct
{
  volatile const uint32_t RADIO0;       /**< Radio information 0 */
  volatile const uint32_t RADIO1;       /**< Radio information 1 */
  volatile const uint32_t CAL;          /**< Calibration temperature and checksum */
  volatile const uint32_t ADC0CAL0;     /**< ADC0 Calibration register 0 */
  volatile const uint32_t ADC0CAL1;     /**< ADC0 Calibration register 1 */
  volatile const uint32_t ADC0CAL2;     /**< ADC0 Calibration register 2 */
  uint32_t     RESERVED0[2]; /**< Reserved */
  volatile const uint32_t DAC0CAL0;     /**< DAC calibrartion register 0 */
  volatile const uint32_t DAC0CAL1;     /**< DAC calibrartion register 1 */
  volatile const uint32_t DAC0CAL2;     /**< DAC calibrartion register 2 */
  volatile const uint32_t AUXHFRCOCAL0; /**< AUXHFRCO calibration register 0 */
  volatile const uint32_t AUXHFRCOCAL1; /**< AUXHFRCO calibration register 1 */
  volatile const uint32_t HFRCOCAL0;    /**< HFRCO calibration register 0 */
  volatile const uint32_t HFRCOCAL1;    /**< HFRCO calibration register 1 */
  volatile const uint32_t MEMINFO;      /**< Memory information */
  uint32_t     RESERVED2;    /**< Reserved */
  volatile const uint32_t RADIO2;       /**< Radio information 2 */
  volatile const uint32_t UNIQUEL;      /**< Low 32 bits of device unique number */
  volatile const uint32_t UNIQUEH;      /**< High 32 bits of device unique number */
  volatile const uint32_t MSIZE;        /**< Flash and SRAM Memory size in KiloBytes */
  volatile const uint32_t PART;         /**< Part description */
} DEVINFO_TypeDef;           /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_DEVINFO_BitFields
 * @{
 *****************************************************************************/
/* Bit fields for EZR32WG_DEVINFO */
/* Legacy family #defines */
/* New style family #defines */

/** @} End of group EZR32WG_DEVINFO */


/**************************************************************************//**
 * @file ezr32wg_romtable.h
 * @brief EZR32WG_ROMTABLE register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_ROMTABLE
 * @{
 * @brief Chip Information, Revision numbers
 *****************************************************************************/
typedef struct
{
  volatile const uint32_t PID4; /**< JEP_106_BANK */
  volatile const uint32_t PID5; /**< Unused */
  volatile const uint32_t PID6; /**< Unused */
  volatile const uint32_t PID7; /**< Unused */
  volatile const uint32_t PID0; /**< Chip family LSB, chip major revision */
  volatile const uint32_t PID1; /**< JEP_106_NO, Chip family MSB */
  volatile const uint32_t PID2; /**< Chip minor rev MSB, JEP_106_PRESENT, JEP_106_NO */
  volatile const uint32_t PID3; /**< Chip minor rev LSB */
  volatile const uint32_t CID0; /**< Unused */
} ROMTABLE_TypeDef;  /** @} */

/**************************************************************************//**
 * @defgroup EZR32WG_ROMTABLE_BitFields
 * @{
 *****************************************************************************/
/* Bit fields for EZR32WG_ROMTABLE */

/** @} End of group EZR32WG_ROMTABLE */


/**************************************************************************//**
 * @file ezr32wg_calibrate.h
 * @brief EZR32WG_CALIBRATE register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_CALIBRATE
 * @{
 *****************************************************************************/

typedef struct
{
  volatile const uint32_t ADDRESS; /**< Address of calibration register */
  volatile const uint32_t VALUE;   /**< Default value for calibration register */
} CALIBRATE_TypeDef;    /** @} */


/** @} End of group EZR32WG330F256R60_Peripheral_TypeDefs */

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_Peripheral_Base EZR32WG330F256R60 Peripheral Memory Map
 * @{
 *****************************************************************************/


/** @} End of group EZR32WG330F256R60_Peripheral_Base */

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_Peripheral_Declaration  EZR32WG330F256R60 Peripheral Declarations
 * @{
 *****************************************************************************/


/** @} End of group EZR32WG330F256R60_Peripheral_Declaration */

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_BitFields EZR32WG330F256R60 Bit Fields
 * @{
 *****************************************************************************/

/**************************************************************************//**
 * @file ezr32wg_prs_signals.h
 * @brief EZR32WG_PRS_SIGNALS register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @addtogroup EZR32WG_PRS_Signals
 * @{
 * @brief PRS Signal names
 *****************************************************************************/

/** @} End of group EZR32WG_PRS */


/**************************************************************************//**
 * @file ezr32wg_dmareq.h
 * @brief EZR32WG_DMAREQ register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/

/**************************************************************************//**
 * @defgroup EZR32WG_DMAREQ_BitFields
 * @{
 *****************************************************************************/

/** @} End of group EZR32WG_DMAREQ */


/**************************************************************************//**
 * @file ezr32wg_dmactrl.h
 * @brief EZR32WG_DMACTRL register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/

/**************************************************************************//**
 * @defgroup EZR32WG_DMACTRL_BitFields
 * @{
 *****************************************************************************/

/** @} End of group EZR32WG_DMA */


/**************************************************************************//**
 * @file ezr32wg_usartrf.h
 * @brief EZR32WG_USARTRF register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/

/**************************************************************************//**
 * @defgroup EZR32WG_USARTRF_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for USARTRF CTRL */

/* Bit fields for USARTRF FRAME */

/* Bit fields for USARTRF TRIGCTRL */

/* Bit fields for USARTRF CMD */

/* Bit fields for USARTRF STATUS */

/* Bit fields for USARTRF CLKDIV */

/* Bit fields for USARTRF RXDATAX */

/* Bit fields for USARTRF RXDATA */

/* Bit fields for USARTRF RXDOUBLEX */

/* Bit fields for USARTRF RXDOUBLE */

/* Bit fields for USARTRF RXDATAXP */

/* Bit fields for USARTRF RXDOUBLEXP */

/* Bit fields for USARTRF TXDATAX */

/* Bit fields for USARTRF TXDATA */

/* Bit fields for USARTRF TXDOUBLEX */

/* Bit fields for USARTRF TXDOUBLE */

/* Bit fields for USARTRF IF */

/* Bit fields for USARTRF IFS */

/* Bit fields for USARTRF IFC */

/* Bit fields for USARTRF IEN */

/* Bit fields for USARTRF IRCTRL */

/* Bit fields for USARTRF ROUTE */

/* Bit fields for USARTRF INPUT */

/* Bit fields for USARTRF I2SCTRL */

/** @} End of group EZR32WG_USARTRF */


/**************************************************************************//**
 * @file ezr32wg_uart.h
 * @brief EZR32WG_UART register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/

/**************************************************************************//**
 * @defgroup EZR32WG_UART_BitFields
 * @{
 *****************************************************************************/

/* Bit fields for UART CTRL */

/* Bit fields for UART FRAME */

/* Bit fields for UART TRIGCTRL */

/* Bit fields for UART CMD */

/* Bit fields for UART STATUS */

/* Bit fields for UART CLKDIV */

/* Bit fields for UART RXDATAX */

/* Bit fields for UART RXDATA */

/* Bit fields for UART RXDOUBLEX */

/* Bit fields for UART RXDOUBLE */

/* Bit fields for UART RXDATAXP */

/* Bit fields for UART RXDOUBLEXP */

/* Bit fields for UART TXDATAX */

/* Bit fields for UART TXDATA */

/* Bit fields for UART TXDOUBLEX */

/* Bit fields for UART TXDOUBLE */

/* Bit fields for UART IF */

/* Bit fields for UART IFS */

/* Bit fields for UART IFC */

/* Bit fields for UART IEN */

/* Bit fields for UART IRCTRL */

/* Bit fields for UART ROUTE */

/* Bit fields for UART INPUT */

/* Bit fields for UART I2SCTRL */

/** @} End of group EZR32WG_UART */



/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_UNLOCK EZR32WG330F256R60 Unlock Codes
 * @{
 *****************************************************************************/

/** @} End of group EZR32WG330F256R60_UNLOCK */

/** @} End of group EZR32WG330F256R60_BitFields */

/**************************************************************************//**
 * @defgroup EZR32WG330F256R60_Alternate_Function EZR32WG330F256R60 Alternate Function
 * @{
 *****************************************************************************/

/**************************************************************************//**
 * @file ezr32wg_af_ports.h
 * @brief EZR32WG_AF_PORTS register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_AF_Ports
 * @{
 *****************************************************************************/

/** AF port number for location number i */

/** @} End of group EZR32WG_AF_Ports */


/**************************************************************************//**
 * @file ezr32wg_af_pins.h
 * @brief EZR32WG_AF_PINS register and bit field definitions
 * @version 4.0.0
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Laboratories, Inc. http://www.silabs.com</b>
 ******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.@n
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.@n
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Laboratories, Inc.
 * has no obligation to support this Software. Silicon Laboratories, Inc. is
 * providing the Software "AS IS", with no express or implied warranties of any
 * kind, including, but not limited to, any implied warranties of
 * merchantability or fitness for any particular purpose or warranties against
 * infringement of any proprietary rights of a third party.
 *
 * Silicon Laboratories, Inc. will not be liable for any consequential,
 * incidental, or special damages, or any other relief, or for any claim by
 * any third party, arising from your use of this Software.
 *
 *****************************************************************************/
/**************************************************************************//**
 * @defgroup EZR32WG_AF_Pins
 * @{
 *****************************************************************************/

/** AF pin number for location number i */

/** @} End of group EZR32WG_AF_Pins */



/** @} End of group EZR32WG330F256R60_Alternate_Function */

/**************************************************************************//**
 *  @brief Set the value of a bit field within a register.
 *
 *  @param REG
 *       The register to update
 *  @param MASK
 *       The mask for the bit field to update
 *  @param VALUE
 *       The value to write to the bit field
 *  @param OFFSET
 *       The number of bits that the field is offset within the register.
 *       0 (zero) means LSB.
 *****************************************************************************/

/** @} End of group EZR32WG330F256R60 */

/** @} End of group Parts */


/** @file hal/micro/cortexm3/efm32/regs.h
 *
 * @brief
 * This file pulls in the appropriate register
 * headers based on the specific Cortex-M3 being
 * compiled.
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2015 Silicon Laboratories, Inc.                        *80*-->
 */

      //EZR32WG
/** @file hal/micro/cortexm3/micro-features.h
 *
 * @brief
 * This file pulls in the appropriate feature
 * defines based on the specific Cortex-M3 being
 * compiled.
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2015 Silicon Laboratories, Inc.                        *80*-->
 */

/** @file hal/micro/cortexm3/efm32/ezr32lg230f256/micro-features.h
 *
 * @brief
 * Constants to indicate which features the ezr32lg230f256 has available
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2014 Silicon Laboratories, Inc.                        *80*-->
 */



// Masks of which GPIO this chip has on which ports

// Which physical serial ports are available


  //Provide a default NVIC configuration file.  The build process can
  //override this if it needs to.
//[[
//]]

// suppress warnings about unknown pragmas
//  (as they may be pragmas known to other platforms)
#pragma diag_suppress = pe161





/** \name Master Variable Types
 * These are a set of typedefs to make the size of all variable declarations
 * explicitly known.
 */
//@{
/**
 * @brief A typedef to make the size of the variable explicitly known.
 */
typedef _Bool boolean; /*To ease adoption of bool instead of boolean.*/
typedef unsigned char  int8u;
typedef signed   char  int8s;
typedef unsigned short int16u;
typedef signed   short int16s;
typedef unsigned int   int32u;
typedef signed   int   int32s;
typedef unsigned long long int64u;
typedef signed   long long int64s;
typedef unsigned int   PointerType;
//@} \\END MASTER VARIABLE TYPES

/**
 * @brief Denotes that this platform supports 64-bit data-types.
 */

/**
 * @brief Use the Master Program Memory Declarations from platform-common.h
 */



////////////////////////////////////////////////////////////////////////////////
/** \name Miscellaneous Macros
 */
////////////////////////////////////////////////////////////////////////////////
//@{

/**
 * @brief A convenient method for code to know what endiannes processor
 * it is running on.  For the Cortex-M3, we are little endian.
 */


/**
 * @brief Define intrinsics for NTOHL and NTOHS to save code space by
 * making endian.c compile to nothing.
 */


/**
 * @brief A friendlier name for the compiler's intrinsic for not
 * stripping.
 */


/**
 * @brief A friendlier name for the compiler's intrinsic for eeprom
 * reference.
 */


  /**
   * @brief The __SOURCEFILE__ macro is used by asserts to list the
   * filename if it isn't otherwise defined, set it to the compiler intrinsic
   * which specifies the whole filename and path of the sourcefile
   */


/**
 * @brief A prototype definition for use by the assert macro. (see
 * hal/micro/micro.h)
 */
void halInternalAssertFailed(const char *filename, int linenumber);

/**
 * @brief A custom implementation of the C language assert macro.
 * This macro implements the conditional evaluation and calls the function
 * halInternalAssertFailed(). (see hal/micro/micro.h)
 */
// Don't define PUSH_REGS_BEFORE_ASSERT if it causes problems with the compiler.
// For example, in some compilers any inline assembly disables all optimization.
//
// For IAR V5.30, inline assembly apparently does not affect compiler output.
//#define PUSH_REGS_BEFORE_ASSERT

/**
 * @brief Macro to reset the watchdog timer.  Note:  be very very
 * careful when using this as you can easily get into an infinite loop if you
 * are not careful.
 */
void halInternalResetWatchDog(void);

/**
 * @brief Define __attribute__ to nothing since it isn't handled by IAR.
 */


/**
 * @brief Declare a variable as unused to avoid a warning.  Has no effect
 * in IAR builds
 */

/**
 * @brief Some platforms need to cast enum values that have the high bit set.
 */


/**
 * @brief Define the magic value that is interpreted by IAR C-SPY's Stack View.
 */

/**
 * @brief Define a generic RAM function identifier to a compiler specific one.
 */

/**
 * @brief Define a generic no operation identifier to a compiler specific one.
 */

/**
 * @brief A convenience macro that makes it easy to change the field of a
 * register to any value.
 */

/**
 * @brief Stub for code not running in simulation.
 */
/**
 * @brief Stub for code not running in simulation.
 */
/**
 * @brief Stub for code not running in simulation.
 */


/**
 * @brief Use the Divide and Modulus Operations from platform-common.h
 */


/**
 * @brief Provide a portable way to specify the segment where a variable
 * lives.
 */

/**
 * @brief Convinience macro for turning a token into a string 
 */
    
/**
 * @brief Provide a portable way to align data.
 */

/**
 * @brief Provide a portable way to specify a symbol as weak
 */

/**
 * @brief Provide a portable way to specify a non initialized symbol
 */

////////////////////////////////////////////////////////////////////////////////
//@}  // end of Miscellaneous Macros
////////////////////////////////////////////////////////////////////////////////

/** @name Portable segment names
 *@{
 */
/**
 * @brief Portable segment names
 */


//=============================================================================
// The '#pragma segment=' declaration must be used before attempting to access
// the segments so the compiler properly handles the __segment_*() functions.
//
// The segment names used here are the default segment names used by IAR. Refer
// to the IAR Compiler Reference Guide for a proper description of these
// segments.
//=============================================================================
#pragma segment= ".noinit"
#pragma segment= "DEBUG_CHANNEL"
#pragma segment= ".intvec"
#pragma segment= "CSTACK"
#pragma segment= "RESETINFO"
#pragma segment= ".data_init"
#pragma segment= ".data"
#pragma segment= ".bss"
#pragma segment= "APP_RAM"
#pragma segment= ".rodata"
#pragma segment= ".text"
#pragma segment= ".textrw_init"
#pragma segment= ".textrw"
#pragma segment= "AAT"
#pragma segment= "BAT"
#pragma segment= "FAT"
#pragma segment= "RAT"
#pragma segment= "NVM"
#pragma segment= "SIMEE"
#pragma segment= "EMHEAP"
#pragma segment= "EMHEAP_overlay"
#pragma segment= "GUARD_REGION"
#pragma segment= "__DLIB_PERTHREAD_init"
#pragma segment= "DLIB_PERTHREAD_INITIALIZED_DATA"
#pragma segment= "DLIB_PERTHREAD_ZERO_DATA"
#pragma segment= "INTERNAL_STORAGE"
#pragma segment= "UNRETAINED_RAM"



/**@} */


//A utility function for inserting barrier instructions.  These
//instructions should be used whenever the MPU is enabled or disabled so
//that all memory/instruction accesses can complete before the MPU changes
//state.  
void _executeBarrierInstructions(void);

////////////////////////////////////////////////////////////////////////////////
/** \name Global Interrupt Manipulation Macros
 *
 * \b Note: The special purpose BASEPRI register is used to enable and disable
 * interrupts while permitting faults.
 * When BASEPRI is set to 1 no interrupts can trigger. The configurable faults
 * (usage, memory management, and bus faults) can trigger if enabled as well as 
 * the always-enabled exceptions (reset, NMI and hard fault).
 * When BASEPRI is set to 0, it is disabled, so any interrupt can triggger if 
 * its priority is higher than the current priority.
 */
////////////////////////////////////////////////////////////////////////////////
//@{


  
    // A series of macros for the diagnostics of the global interrupt state.
    // These macros either enable or disable the debugging code in the
    // Interrupt Manipulation Macros as well as define the two pins used for
    // indicating the entry and exit of critical sections.
    //UNCOMMENT the below #define to enable interrupt debugging.
    //#define INTERRUPT_DEBUGGING
        /**
         * @brief This macro should be called in the local variable
         * declarations section of any function which calls DISABLE_INTERRUPTS()
         * or RESTORE_INTERRUPTS().
         */

    
    // Prototypes for the BASEPRI and PRIMASK access functions.  They are very
    // basic and instantiated in assembly code in the file spmr.s37 (since
    // there are no C functions that cause the compiler to emit code to access
    // the BASEPRI/PRIMASK). This will inhibit the core from taking interrupts
    // with a priority equal to or less than the BASEPRI value.
    // Note that the priority values used by these functions are 5 bits and 
    // right-aligned
    extern uint8_t _readBasePri(void);
    extern void _writeBasePri(uint8_t priority);

    // Prototypes for BASEPRI functions used to disable and enable interrupts
    // while still allowing enabled faults to trigger.
    extern void _enableBasePri(void);
    extern uint8_t _disableBasePri(void);
    extern _Bool _basePriIsDisabled(void);
    
    // Prototypes for setting and clearing PRIMASK for global interrupt
    // enable/disable.
    extern void _setPriMask(void);
    extern void _clearPriMask(void);



  //The core Global Interrupt Manipulation Macros start here.
  
  // When building for an RTOS be sure to use compatible interrupt routines
    /**
     * @brief Disable interrupts, saving the previous state so it can be
     * later restored with RESTORE_INTERRUPTS().
     * \note Do not fail to call RESTORE_INTERRUPTS().
     * \note It is safe to nest this call.
     */
    
    
    /** 
     * @brief Restore the global interrupt state previously saved by
     * DISABLE_INTERRUPTS()
     * \note Do not call without having first called DISABLE_INTERRUPTS()
     * to have saved the state.
     * \note It is safe to nest this call.
     */
  
  /**
   * @brief Enable global interrupts without regard to the current or
   * previous state.
   */
  
  
  /**
   * @brief Disable global interrupts without regard to the current or
   * previous state.
   */
  
  
  /**
   * @returns true if global interrupts are disabled.
   */
  
  /**
   * @returns true if global interrupt flag was enabled when 
   * ::DISABLE_INTERRUPTS() was called.
   */
  
  /**
   * @brief A block of code may be made atomic by wrapping it with this
   * macro.  Something which is atomic cannot be interrupted by interrupts.
   */
  
  
  /**
   * @brief Allows any pending interrupts to be executed. Usually this
   * would be called at a safe point while interrupts are disabled (such as
   * within an ISR).
   * 
   * Takes no action if interrupts are already enabled.
   */
  
  
  /**
   * @brief Sets the base priority mask (BASEPRI) to the value passed,
   * bit shifted up by PRIGROUP_POSITION+1.  This will inhibit the core from
   * taking all interrupts with a preemptive priority equal to or less than
   * the BASEPRI mask.  This macro is dependent on the value of
   * PRIGROUP_POSITION in nvic-config.h. Note that the value 0 disables the
   * the base priority mask.
   *
   * Refer to the "PRIGROUP" table in nvic-config.h to know the valid values
   * for this macro depending on the value of PRIGROUP_POSITION.  With respect
   * to the table, this macro can only take the preemptive priority group
   * numbers denoted by the parenthesis.
   */
  
////////////////////////////////////////////////////////////////////////////////
//@}  // end of Global Interrupt Manipulation Macros
////////////////////////////////////////////////////////////////////////////////

/**
 * @brief If the line below is uncommented we will use Ember memory APIs,
 * otherwise, we will use the C Standard library (memset,memcpy,memmove) APIs.
 */

////////////////////////////////////////////////////////////////////////////////
/** \name External Declarations
 * These are routines that are defined in certain header files that we don't
 * want to include, e.g. stdlib.h
 */
////////////////////////////////////////////////////////////////////////////////
//@{

/**
 * @brief Returns the absolute value of I (also called the magnitude of I).
 * That is, if I is negative, the result is the opposite of I, but if I is
 * nonnegative the result is I.
 *
 * @param I  An integer.
 *
 * @return A nonnegative integer.
 */
int abs(int I);

////////////////////////////////////////////////////////////////////////////////
//@}  // end of External Declarations
////////////////////////////////////////////////////////////////////////////////


/**
 * @brief Include platform-common.h last to pick up defaults and common definitions.
 */
/** @file hal/micro/generic/compiler/platform-common.h
 * See @ref platform_common for detailed documentation.
 *
 * <!-- Copyright 2009 by Ember Corporation. All rights reserved.        *80*-->
 */

/** @addtogroup platform_common
 * @brief Compiler and Platform specific definitions and typedefs common to
 * all platforms.  
 *
 * platform-common.h provides PLATFORM_HEADER defaults and common definitions.
 * This head should never be included directly, it should only be included
 * by the specific PLATFORM_HEADER used by your platform.
 *
 * See platform-common.h for source code.
 *@{
 */
 

////////////////////////////////////////////////////////////////////////////////
// Many of the common definitions must be explicitly enabled by the 
//  particular PLATFORM_HEADER being used
////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////
// The XAP2b compiler uses these macros to enable and disable placement
// in zero-page memory.  All other platforms do not have zero-page memory
// so these macros define to nothing.
////////////////////////////////////////////////////////////////////////////////


////////////////////////////////////////////////////////////////////////////////
  /** \name Master Program Memory Declarations
   * These are a set of defines for simple declarations of program memory.
   */
  //@{
  /**
   * @brief Standard program memory delcaration.
   */

  /**
   * @brief Char pointer to program memory declaration.
   */

  /**
   * @brief Unsigned char pointer to program memory declaration.
   */


  /**
   * @brief Sometimes a second PGM is needed in a declaration.  Having two
   * 'const' declarations generates a warning so we have a second PGM that turns
   * into nothing under gcc.
   */
  //@} \\END MASTER PROGRAM MEMORY DECLARATIONS


////////////////////////////////////////////////////////////////////////////////
  /** \name Divide and Modulus Operations
   * Some platforms can perform divide and modulus operations on 32 bit 
   * quantities more efficiently when the divisor is only a 16 bit quantity.
   * C compilers will always promote the divisor to 32 bits before performing the
   * operation, so the following utility functions are instead required to take 
   * advantage of this optimisation.
   */
  //@{
  /**
   * @brief Provide a portable name for the uint32_t by uint16_t division
   * library function (which can perform the division with only a single 
   * assembly instruction on some platforms)
   */

  /**
   * @brief Provide a portable name for the int32_t by int16_t division
   * library function (which can perform the division with only a single
   * assembly instruction on some platforms)
   */

  /**
   * @brief Provide a portable name for the uint32_t by uint16_t modulo
   * library function (which can perform the division with only a single
   * assembly instruction on some platforms)
   */

  /**
   * @brief Provide a portable name for the int32_t by int16_t modulo
   * library function (which can perform the division with only a single
   * assembly instruction on some platforms)
   */
  //@} \\END DIVIDE and MODULUS OPERATIONS


////////////////////////////////////////////////////////////////////////////////
  /** \name C Standard Library Memory Utilities
   * These should be used in place of the standard library functions.
   * 
   * These functions have the same parameters and expected results as their C
   * Standard Library equivalents but may take advantage of certain implementation
   * optimizations.
   * 
   * Unless otherwise noted, these functions are utilized by the EmberStack and are 
   * therefore required to be implemented in the HAL. Additionally, unless otherwise
   * noted, applications that find these functions useful may utilze them.
   */
  //@{

  /**
   * @brief Refer to the C stdlib memmove().
   */
  void halCommonMemMove(void *dest, const void *src, uint16_t bytes);


  /**
   * @brief Refer to the C stdlib memset().
   */
  void halCommonMemSet(void *dest, uint8_t val, uint16_t bytes);


  /**
   * @brief Refer to the C stdlib memcmp().
   */
  int16_t halCommonMemCompare(const void *source0, const void *source1, uint16_t bytes);


  /**
   * @brief Works like C stdlib memcmp(), but takes a flash space source
   * parameter.
   */
  int8_t halCommonMemPGMCompare(const void *source0, const void  *source1, uint16_t bytes);

  /**
   * @brief Same as the C stdlib memcpy(), but handles copying from const 
   * program space.
   */
  void halCommonMemPGMCopy(void* dest, const void  *source, uint16_t bytes);

  /**
   * @brief Friendly convenience macro pointing to the full HAL function.
   */

  //@}  // end of C Standard Library Memory Utilities









////////////////////////////////////////////////////////////////////////////////
//  The following sections are common on all platforms
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
/**
 * @name Generic Types
 *@{
 */

/**
 * @brief An alias for one, used for clarity.
 */

/**
 * @brief An alias for zero, used for clarity.
 */


//@} \\END Generic Types


/**
 * @name  Bit Manipulation Macros
 */
//@{

/**
 * @brief Useful to reference a single bit of a byte.
 */

/**
 * @brief Useful to reference a single bit of an uint32_t type.
 */

/**
 * @brief Sets \c bit in the \c reg register or byte.
 * @note Assuming \c reg is an IO register, some platforms (such as the
 * AVR) can implement this in a single atomic operation.
*/

/**
 * @brief Sets the bits in the \c reg register or the byte 
 * as specified in the bitmask \c bits. 
 * @note This is never a single atomic operation.
 */

/**
 * @brief Clears a bit in the \c reg register or byte. 
 * @note Assuming \c reg is an IO register, some platforms (such as the AVR) 
 * can implement this in a single atomic operation.
 */

/**
 * @brief Clears the bits in the \c reg register or byte 
 * as specified in the bitmask \c bits. 
 * @note This is never a single atomic operation.
 */

/**
 * @brief Returns the value of \c bit within the register or byte \c reg.
*/

/**
 * @brief Returns the value of the bitmask \c bits within 
 * the register or byte \c reg.
 */

//@} \\END Bit Manipulation Macros


////////////////////////////////////////////////////////////////////////////////
/**
 * @name  Byte Manipulation Macros
 */
//@{

/**
 * @brief Returns the low byte of the 16-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the high byte of the 16-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the value built from the two \c uint8_t 
 * values \c high and \c low.
 */

/**
 * @brief Returns the low byte of the 32-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the second byte of the 32-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the third byte of the 32-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the high byte of the 32-bit value \c n as an \c uint8_t.
 */

/**
 * @brief Returns the number of entries in an array.
 */

//@} \\END Byte manipulation macros


////////////////////////////////////////////////////////////////////////////////
/**
 * @name  Time Manipulation Macros
 */
//@{

/**
 * @brief Returns the elapsed time between two 8 bit values.  
 *        Result may not be valid if the time samples differ by more than 127
 */

/**
 * @brief Returns the elapsed time between two 16 bit values.  
 *        Result may not be valid if the time samples differ by more than 32767
 */

/**
 * @brief Returns the elapsed time between two 32 bit values.  
 *   Result may not be valid if the time samples differ by more than 2147483647
 */

/**
 * @brief Returns true if t1 is greater than t2.  Can only account for 1 wrap
 * around of the variable before it is wrong.
 */

/**
 * @brief Returns true if t1 is greater than t2.  Can only account for 1 wrap
 * around of the variable before it is wrong.
 */

/**
 * @brief Returns true if t1 is greater than t2.  Can only account for 1 wrap
 * around of the variable before it is wrong.
 */

//@} \\END Time manipulation macros


////////////////////////////////////////////////////////////////////////////////
/**
 * @name Miscellaneous Macros
 */
//@{

/**
 * @description Useful macro for avoiding compiler warnings related to unused
 * function arguments or unused variables.
 */

/**
 * @brief Set debug level based on whether DEBUG or DEBUG_OFF are defined.
 */

//@} \\END Miscellaneous Macros


/** @}  END addtogroup */


/**
 * @brief The kind of arguments the main function takes
 */

/** @}  END addtogroup */

/***************************************************************************//**
 * @file em_mpu.h
 * @brief Memory protection unit (MPU) peripheral API
 * @version 4.0.0
 *******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Labs, http://www.silabs.com</b>
 *******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Labs has no
 * obligation to support this Software. Silicon Labs is providing the
 * Software "AS IS", with no express or implied warranties of any kind,
 * including, but not limited to, any implied warranties of merchantability
 * or fitness for any particular purpose or warranties against infringement
 * of any proprietary rights of a third party.
 *
 * Silicon Labs will not be liable for any consequential, incidental, or
 * special damages, or any other relief, or for any claim by any third party,
 * arising from your use of this Software.
 *
 ******************************************************************************/


      //EZR32WG

/***************************************************************************//**
 * @file em_assert.h
 * @brief Emlib peripheral API "assert" implementation.
 * @version 4.0.0
 *
 * @details
 * By default, emlib library assert usage is not included in order to reduce
 * footprint and processing overhead. Further, emlib assert usage is decoupled
 * from ISO C assert handling (NDEBUG usage), to allow a user to use ISO C
 * assert without including emlib assert statements.
 *
 * Below are available defines for controlling emlib assert inclusion. The defines
 * are typically defined for a project to be used by the preprocessor.
 *
 * @li If DEBUG_EFM is defined, the internal emlib library assert handling will
 * be used, which may be a quite rudimentary implementation.
 *
 * @li If DEBUG_EFM_USER is defined instead, the user must provide their own
 * assert handling routine (assertEFM()).
 *
 * As indicated above, if none of the above defines are used, emlib assert
 * statements are not compiled.
 *******************************************************************************
 * @section License
 * <b>(C) Copyright 2015 Silicon Labs, http://www.silabs.com</b>
 *******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Labs has no
 * obligation to support this Software. Silicon Labs is providing the
 * Software "AS IS", with no express or implied warranties of any kind,
 * including, but not limited to, any implied warranties of merchantability
 * or fitness for any particular purpose or warranties against infringement
 * of any proprietary rights of a third party.
 *
 * Silicon Labs will not be liable for any consequential, incidental, or
 * special damages, or any other relief, or for any claim by any third party,
 * arising from your use of this Software.
 *
 ******************************************************************************/



/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */




/** @endcond */





/***************************************************************************//**
 * @addtogroup EM_Library
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup MPU
 * @{
 ******************************************************************************/

/** @anchor MPU_CTRL_PRIVDEFENA
 *  Argument to MPU_enable(). Enables priviledged
 *  access to default memory map.                                            */

/** @anchor MPU_CTRL_HFNMIENA
 *  Argument to MPU_enable(). Enables MPU during hard fault,
 *  NMI, and FAULTMASK handlers.                                             */

/*******************************************************************************
 ********************************   ENUMS   ************************************
 ******************************************************************************/

/**
 * Size of an MPU region.
 */
typedef enum
{
  mpuRegionSize32b   = 4,        /**< 32   byte region size. */
  mpuRegionSize64b   = 5,        /**< 64   byte region size. */
  mpuRegionSize128b  = 6,        /**< 128  byte region size. */
  mpuRegionSize256b  = 7,        /**< 256  byte region size. */
  mpuRegionSize512b  = 8,        /**< 512  byte region size. */
  mpuRegionSize1Kb   = 9,        /**< 1K   byte region size. */
  mpuRegionSize2Kb   = 10,       /**< 2K   byte region size. */
  mpuRegionSize4Kb   = 11,       /**< 4K   byte region size. */
  mpuRegionSize8Kb   = 12,       /**< 8K   byte region size. */
  mpuRegionSize16Kb  = 13,       /**< 16K  byte region size. */
  mpuRegionSize32Kb  = 14,       /**< 32K  byte region size. */
  mpuRegionSize64Kb  = 15,       /**< 64K  byte region size. */
  mpuRegionSize128Kb = 16,       /**< 128K byte region size. */
  mpuRegionSize256Kb = 17,       /**< 256K byte region size. */
  mpuRegionSize512Kb = 18,       /**< 512K byte region size. */
  mpuRegionSize1Mb   = 19,       /**< 1M   byte region size. */
  mpuRegionSize2Mb   = 20,       /**< 2M   byte region size. */
  mpuRegionSize4Mb   = 21,       /**< 4M   byte region size. */
  mpuRegionSize8Mb   = 22,       /**< 8M   byte region size. */
  mpuRegionSize16Mb  = 23,       /**< 16M  byte region size. */
  mpuRegionSize32Mb  = 24,       /**< 32M  byte region size. */
  mpuRegionSize64Mb  = 25,       /**< 64M  byte region size. */
  mpuRegionSize128Mb = 26,       /**< 128M byte region size. */
  mpuRegionSize256Mb = 27,       /**< 256M byte region size. */
  mpuRegionSize512Mb = 28,       /**< 512M byte region size. */
  mpuRegionSize1Gb   = 29,       /**< 1G   byte region size. */
  mpuRegionSize2Gb   = 30,       /**< 2G   byte region size. */
  mpuRegionSize4Gb   = 31        /**< 4G   byte region size. */
} MPU_RegionSize_TypeDef;

/**
 * MPU region access permission attributes.
 */
typedef enum
{
  mpuRegionNoAccess     = 0,  /**< No access what so ever.                   */
  mpuRegionApPRw        = 1,  /**< Priviledged state R/W only.               */
  mpuRegionApPRwURo     = 2,  /**< Priviledged state R/W, User state R only. */
  mpuRegionApFullAccess = 3,  /**< R/W in Priviledged and User state.        */
  mpuRegionApPRo        = 5,  /**< Priviledged R only.                       */
  mpuRegionApPRo_URo    = 6   /**< R only in Priviledged and User state.     */
} MPU_RegionAp_TypeDef;


/*******************************************************************************
 *******************************   STRUCTS   ***********************************
 ******************************************************************************/

/** MPU Region init structure. */
typedef struct
{
  _Bool                   regionEnable;     /**< MPU region enable.                */
  uint8_t                regionNo;         /**< MPU region number.                */
  uint32_t               baseAddress;      /**< Region baseaddress.               */
  MPU_RegionSize_TypeDef size;             /**< Memory region size.               */
  MPU_RegionAp_TypeDef   accessPermission; /**< Memory access permissions.   */
  _Bool                   disableExec;      /**< Disable execution.                */
  _Bool                   shareable;        /**< Memory shareable attribute.       */
  _Bool                   cacheable;        /**< Memory cacheable attribute.       */
  _Bool                   bufferable;       /**< Memory bufferable attribute.      */
  uint8_t                srd;              /**< Memory subregion disable bits.    */
  uint8_t                tex;              /**< Memory type extension attributes. */
} MPU_RegionInit_TypeDef;

/** Default configuration of MPU region init structure for flash memory.     */


/** Default configuration of MPU region init structure for sram memory.      */


/** Default configuration of MPU region init structure for onchip peripherals.*/


/*******************************************************************************
 *****************************   PROTOTYPES   **********************************
 ******************************************************************************/


void MPU_ConfigureRegion(const MPU_RegionInit_TypeDef *init);


/***************************************************************************//**
 * @brief
 *   Disable the MPU
 * @details
 *   Disable MPU and MPU fault exceptions.
 ******************************************************************************/
static inline void MPU_Disable(void)
{
  ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->SHCSR &= ~(1UL << 16);      /* Disable fault exceptions */
  ((MPU_Type *) ((0xE000E000UL) + 0x0D90UL) )->CTRL  &= ~(1UL << 0);            /* Disable the MPU */
}


/***************************************************************************//**
 * @brief
 *   Enable the MPU
 * @details
 *   Enable MPU and MPU fault exceptions.
 * @param[in] flags
 *   Use a logical OR of @ref MPU_CTRL_PRIVDEFENA and
 *   @ref MPU_CTRL_HFNMIENA as needed.
 ******************************************************************************/
static inline void MPU_Enable(uint32_t flags)
{
  ((void)(!(flags & ~((1UL << 2) | (1UL << 1) | (1UL << 0)))));

  ((MPU_Type *) ((0xE000E000UL) + 0x0D90UL) )->CTRL   = flags | (1UL << 0);     /* Enable the MPU */
  ((SCB_Type *) ((0xE000E000UL) + 0x0D00UL) )->SHCSR |= (1UL << 16);       /* Enable fault exceptions */
}


/** @} (end addtogroup MPU) */
/** @} (end addtogroup EM_Library) */



/** @file hal/micro/cortexm3/mpu.h
 *
 * <!-- Copyright 2008 by Ember Corporation. All rights reserved.-->   
 */



// A region is defined by a struct with two parts, base address and attributes,
// that are loaded into the MPU_BASE and MPU_ATTR registers, respectively.
typedef struct mpu
{
  uint32_t base;
  uint32_t attr;
} mpu_t;

// Number of MPU regions on the Cortex M3

// Region size (SIZE) field values
// Size must be a power of two, from 32 bytes to 4 gigabytes.
// Regions less than 256 bytes cannot be divided into 8 sub regions


/** @file hal/micro/cortexm3/mpu-config.h
 *
 * @brief
 * This file pulls in the appropriate MPU
 * configuration based on the specific Cortex-M3
 * being compiled.
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2015 Silicon Laboratories, Inc.                        *80*-->
 */

/** @file hal/micro/cortexm3/efm32/ezr32lg230f256/mpu-config.h
 *
 * @brief MPU configuration for the ezr32lg230f256
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2014 Silicon Laboratories, Inc.                        *80*-->
 */



/** @file hal/micro/micro.h
 * 
 * @brief Full HAL functions common across all microcontroller-specific files.
 * See @ref micro for documentation.
 *
 * Some functions in this file return an ::EmberStatus value. 
 * See error-def.h for definitions of all ::EmberStatus return values.
 *
 * <!-- Copyright 2004-2011 by Ember Corporation. All rights reserved.   *80*-->
 */
 
/** @addtogroup micro
 * Many of the supplied example applications use these microcontroller functions.
 * See hal/micro/micro.h for source code.
 *
 * @note The term SFD refers to the Start Frame Delimiter.
 *@{
 */


/** @file hal/micro/generic/em2xx-reset-defs.h
 * @brief Definitions of reset types compatible with EM2xx usage.
 *
 * <!-- Copyright 2009 by Ember Corporation.             All rights reserved.-->
 */



/** @addtogroup em2xx_resets
 *@{
 */
/** @brief EM2xx-compatible reset code returned by halGetEm2xxResetInfo()
 *@{
 */
/**@} */

/**@}  // end of CRC Functions
 */

/** @file hal/micro/micro-types.h
 *
 * @brief
 * This file handles defines and enums related to all the micros.
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2015 Silicon Laboratories, Inc.                        *80*-->
 */



// Below is a list of PLATFORM and MICRO values that are used to define the
// chips our code runs on. These values are used in EBL headers, bootloader
// query response messages, and possibly other places in the code
// -----------------------------------------------------------------------------
// PLAT 1 was the AVR ATMega, no longer supported (still used for EMBER_TEST)
// for PLAT 1, MICRO 1 is the avr64
// for PLAT 1, MICRO 2 is the avr128
// for PLAT 1, MICRO 3 is the avr32

// PLAT 2 is the XAP2b
// for PLAT 2, MICRO 1 is the em250
// for PLAT 2, MICRO 2 is the em260

// PLAT 3 was the MSP 430, no longer supported

// PLAT 4 is the CortexM3
// for PLAT 4, MICRO 1 is the em350
// for PLAT 4, MICRO 2 is the em360
// for PLAT 4, MICRO 3 is the em357
// for PLAT 4, MICRO 4 is the em367
// for PLAT 4, MICRO 5 is the em351
// for PLAT 4, MICRO 6 is the em35x
// for PLAT 4, MICRO 7 is the stm32w108
// for PLAT 4, MICRO 8 is the em3588
// for PLAT 4, MICRO 9 is the em359
// for PLAT 4, MICRO 10 is the em3581
// for PLAT 4, MICRO 11 is the em3582
// for PLAT 4, MICRO 12 is the em3585
// for PLAT 4, MICRO 13 is the em3586
// for PLAT 4, MICRO 14 is the em3587
// for PLAT 4, MICRO 15 is the sky66107
// for PLAT 4, MICRO 16 is the em3597
// for PLAT 4, MICRO 17 is the em356
// for PLAT 4, MICRO 18 is the em3598
// for PLAT 4, MICRO 19 is the em3591
// for PLAT 4, MICRO 20 is the em3592
// for PLAT 4, MICRO 21 is the em3595
// for PLAT 4, MICRO 22 is the em3596
// for PLAT 4, MICRO 23 is the em317
// for PLAT 4, MICRO 24 is the efr32
// for PLAT 4, MICRO 25 is the em341
// for PLAT 4, MICRO 26 is the em342
// for PLAT 4, MICRO 27 is the em346
// for PLAT 4, MICRO 28 is the efm32lg990f256
// for PLAT 4, MICRO 29 is the ezr32lg230f256
// for PLAT 4, MICRO 30 is the em355
// for PLAT 4, MICRO 31 is the em3555

// PLAT 5 is the C8051
// for PLAT 5, MICRO 1 is the siF930
// for PLAT 5, MICRO 2 is the siF960
// for PLAT 5, MICRO 3 is the cobra
// for PLAT 5, MICRO 4 is the siF370
// for PLAT 5, MICRO 5 is the siF393

// PLAT 6 is the FFD
// for PLAT 6, MICRO 1 is the si4010

// -----------------------------------------------------------------------------

// Create an enum for the platform types
enum {
  EMBER_PLATFORM_UNKNOWN    = 0,
  EMBER_PLATFORM_AVR_ATMEGA = 1,
  EMBER_PLATFORM_XAP2B      = 2,
  EMBER_PLATFORM_MSP_430    = 3,
  EMBER_PLATFORM_CORTEXM3   = 4,
  EMBER_PLATFORM_C8051      = 5,
  EMBER_PLATFORM_FFD        = 6,
  EMBER_PLATFORM_MAX_VALUE
};
typedef uint16_t EmberPlatformEnum;


// Create an enum for all of the different AVR ATMega micros we support
enum {
  EMBER_MICRO_AVR_ATMEGA_UNKNOWN   = 0,
  EMBER_MICRO_AVR_ATMEGA_64        = 1,
  EMBER_MICRO_AVR_ATMEGA_128       = 2,
  EMBER_MICRO_AVR_ATMEGA_32        = 3,
  EMBER_MICRO_AVR_ATMEGA_MAX_VALUE
};
typedef uint16_t EmberMicroAvrAtmegaEnum;


// Create an enum for all of the different XAP2b micros we support
enum {
  EMBER_MICRO_XAP2B_UNKNOWN   = 0,
  EMBER_MICRO_XAP2B_EM250     = 1,
  EMBER_MICRO_XAP2B_EM260     = 2,
  EMBER_MICRO_XAP2B_MAX_VALUE
};
typedef uint16_t EmberMicroXap2bEnum;


// Create an enum for all of the different CortexM3 micros we support
enum {
  EMBER_MICRO_CORTEXM3_UNKNOWN        = 0,
  EMBER_MICRO_CORTEXM3_EM350          = 1,
  EMBER_MICRO_CORTEXM3_EM360          = 2,
  EMBER_MICRO_CORTEXM3_EM357          = 3,
  EMBER_MICRO_CORTEXM3_EM367          = 4,
  EMBER_MICRO_CORTEXM3_EM351          = 5,
  EMBER_MICRO_CORTEXM3_EM35X          = 6,
  EMBER_MICRO_CORTEXM3_STM32W108      = 7,
  EMBER_MICRO_CORTEXM3_EM3588         = 8,
  EMBER_MICRO_CORTEXM3_EM359          = 9,
  EMBER_MICRO_CORTEXM3_EM3581         = 10,
  EMBER_MICRO_CORTEXM3_EM3582         = 11,
  EMBER_MICRO_CORTEXM3_EM3585         = 12,
  EMBER_MICRO_CORTEXM3_EM3586         = 13,
  EMBER_MICRO_CORTEXM3_EM3587         = 14,
  EMBER_MICRO_CORTEXM3_SKY66107       = 15,
  EMBER_MICRO_CORTEXM3_EM3597         = 16,
  EMBER_MICRO_CORTEXM3_EM356          = 17,
  EMBER_MICRO_CORTEXM3_EM3598         = 18,
  EMBER_MICRO_CORTEXM3_EM3591         = 19,
  EMBER_MICRO_CORTEXM3_EM3592         = 20,
  EMBER_MICRO_CORTEXM3_EM3595         = 21,
  EMBER_MICRO_CORTEXM3_EM3596         = 22,
  EMBER_MICRO_CORTEXM3_EM317          = 23,
  EMBER_MICRO_CORTEXM3_EFR32          = 24,
  EMBER_MICRO_CORTEXM3_EM341          = 25,
  EMBER_MICRO_CORTEXM3_EM342          = 26,
  EMBER_MICRO_CORTEXM3_EM346          = 27,
  EMBER_MICRO_CORTEXM3_EFM32LG990F256 = 28,
  EMBER_MICRO_CORTEXM3_EZR32LG230F256 = 29,
  EMBER_MICRO_CORTEXM3_EM355          = 30,
  EMBER_MICRO_CORTEXM3_EM3555         = 31,
  EMBER_MICRO_CORTEXM3_EZR32LG330F256 = 32,
  EMBER_MICRO_CORTEXM3_EZR32WG230F256 = 33,
  EMBER_MICRO_CORTEXM3_EZR32WG330F256 = 34,
  EMBER_MICRO_CORTEXM3_EZR32HG230F256 = 35,
  EMBER_MICRO_CORTEXM3_EZR32HG330F256 = 36,
  EMBER_MICRO_CORTEXM3_MAX_VALUE
};
typedef uint16_t EmberMicroCortexM3Enum;


// Create an enum for all of the different C8051 micros we support
enum {
  EMBER_MICRO_C8051_UNKNOWN   = 0,
  EMBER_MICRO_C8051_SIF930    = 1,
  EMBER_MICRO_C8051_SIF960    = 2,
  EMBER_MICRO_C8051_COBRA     = 3,
  EMBER_MICRO_C8051_SIF370    = 4,
  EMBER_MICRO_C8051_SIF393    = 5,
  EMBER_MICRO_C8051_MAX_VALUE
};
typedef uint16_t EmberMicroC8051Enum;


// Create an enum for all of the different FFD micros we support
enum {
  EMBER_MICRO_FFD_UNKNOWN   = 0,
  EMBER_MICRO_FFD_SI4010    = 1,
  EMBER_MICRO_FFD_MAX_VALUE
};
typedef uint16_t EmberMicroFfdEnum;


// A dummy type declared to allow generically passing around this
// data type.  Micro specific enums (such as EmberMicroCortexM3Enum)
// are required to be the same size as this.
typedef uint16_t EmberMicroEnum;

// Determine what micro and platform that we're supposed to target using the
// defines passed in at build time. Then set the PLAT and MICRO defines based
// on what was passed in



// Define distinct literal values for each phy. These values are used in the
// bootloader query response message.
// PHY 0 is NULL
// PHY 1 is em2420 (no longer supported)
// PHY 2 is em250
// PHY 3 is em3XX
// PHY 4 is si446x
// PHY 5 is cobra
// PHY 6 is PRO2+
// PHY 7 is si4x55
// PHY 8 is si4010
// PHY 9 is efr32
// PHY 10 is pro2
// PHY 11 is ezr2

enum {
  EMBER_PHY_NULL      = 0,
  EMBER_PHY_EM2420    = 1,
  EMBER_PHY_EM250     = 2,
  EMBER_PHY_EM3XX     = 3,
  EMBER_PHY_SI446X    = 4,
  EMBER_PHY_COBRA     = 5,
  EMBER_PHY_PRO2PLUS  = 6,
  EMBER_PHY_SI4X55    = 7,
  EMBER_PHY_SI4010    = 8,
  EMBER_PHY_EFR32     = 9,
  EMBER_PHY_PRO2      = 10,
  EMBER_PHY_EZR2      = 11,
  EMBER_PHY_MAX_VALUE
};
typedef uint16_t EmberPhyEnum;



typedef struct {
  EmberPlatformEnum platform;
  EmberMicroEnum    micro;
  EmberPhyEnum      phy;
} EmberChipTypeStruct;

// load up any chip-specific feature defines
/** @file hal/micro/cortexm3/micro-features.h
 *
 * @brief
 * This file pulls in the appropriate feature
 * defines based on the specific Cortex-M3 being
 * compiled.
 *
 * THIS IS A GENERATED FILE.  DO NOT EDIT.
 *
 * <!-- Copyright 2015 Silicon Laboratories, Inc.                        *80*-->
 */





// Make sure that a proper plat/micro combination was selected if we aren't
// building for a host processor




/** @brief Called from emberInit and provides a means for the HAL
 * to increment a boot counter, most commonly in non-volatile memory.
 *
 * This is useful while debugging to determine the number of resets that might
 * be seen over a period of time.  Exposing this functionality allows the
 * application to disable or alter processing of the boot counter if, for
 * example, the application is expecting a lot of resets that could wear
 * out non-volatile storage or some
 *
 * @stackusage Called from emberInit only as helpful debugging information.
 * This should be left enabled by default, but this function can also be
 * reduced to a simple return statement if boot counting is not desired.
 */
void halStackProcessBootCount(void);

/** @brief Gets information about what caused the microcontroller to reset. 
 *
 * @return A code identifying the cause of the reset.
 */
uint8_t halGetResetInfo(void);

/** @brief Calls ::halGetResetInfo() and supplies a string describing it.
 *
 * @appusage Useful for diagnostic printing of text just after program 
 * initialization.
 *
 * @return A pointer to a program space string.
 */
const char * halGetResetString(void);

/** @brief Calls ::halGetExtendedResetInfo() and translates the EM35x or COBRA
 *  reset code to the corresponding value used by the EM2XX HAL. Any reset codes 
 * not present in the EM2XX are returned after being OR'ed with 0x80.
 *
 * @appusage Used by the EZSP host as a platform-independent NCP reset code.
 *
 * @return The EM2XX-compatible reset code. If not supported by the EM2XX,
 *         return the platform-specific code with B7 set.
 */
  uint8_t halGetEm2xxResetInfo(void);


/** @file hal/micro/micro-common.h
 * 
 * @brief Minimal Hal functions common across all microcontroller-specific files.
 * See @ref micro for documentation.
 *
 * <!-- Copyright 2009 by Ember Corporation. All rights reserved.-->   
 */
 
/** @addtogroup micro
 * Many of the supplied example applications use these microcontroller functions.
 * See hal/micro/micro-common.h for source code.
 *
 *@{
 */



/** @brief Initializes microcontroller-specific peripherals.
*/
void halInit(void);

/** @brief Restarts the microcontroller and therefore everything else.
*/
void halReboot(void);

/** @brief Powers up microcontroller peripherals and board peripherals.
*/
void halPowerUp(void);

/** @brief Powers down microcontroller peripherals and board peripherals.
*/
void halPowerDown(void);

/** @brief Resumes microcontroller peripherals and board peripherals.
*/
void halResume(void);

/** @brief Suspends microcontroller peripherals and board peripherals.
*/
void halSuspend(void);


/** @brief The value that must be passed as the single parameter to 
 *  ::halInternalDisableWatchDog() in order to successfully disable the watchdog 
 *  timer.
 */ 

/** @brief Enables the watchdog timer.
 */
void halInternalEnableWatchDog(void);

/** @brief Disables the watchdog timer.
 *
 * @note To prevent the watchdog from being disabled accidentally, 
 * a magic key must be provided.
 * 
 * @param magicKey  A value (::MICRO_DISABLE_WATCH_DOG_KEY) that enables the function.
 */
void halInternalDisableWatchDog(uint8_t magicKey);

/** @brief Determines whether the watchdog has been enabled or disabled.
 *
 * @return A bool value indicating if the watchdog is current enabled.
 */
_Bool halInternalWatchDogEnabled( void );

typedef uint8_t SleepModes;
enum
{
  SLEEPMODE_RUNNING = 0,
  SLEEPMODE_IDLE = 1,
  SLEEPMODE_WAKETIMER = 2,
  SLEEPMODE_MAINTAINTIMER = 3,
  SLEEPMODE_NOTIMER = 4,
  
  //The following SleepModes are deprecated on EM2xx and EM3xx chips.  Each
  //micro's halSleep() function will remap these modes to the appropriate
  //replacement, as necessary.
  SLEEPMODE_RESERVED = 6,
  SLEEPMODE_POWERDOWN = 7,
  SLEEPMODE_POWERSAVE = 8,
};



  typedef uint32_t WakeEvents;
  typedef uint32_t WakeMask;


/** @note The preprocessor symbol WAKE_EVENT_SIZE has been deprecated.
 * Please use WakeMask instead.
 */

/** @brief Puts the microcontroller to sleep in a specified mode.
 *
 * @note This routine always enables interrupts.
 *
 * @param sleepMode  A microcontroller sleep mode 
 * 
 * @sa ::SleepModes
 */
void halSleep(SleepModes sleepMode);

/** @brief Blocks the current thread of execution for the specified
 * amount of time, in microseconds.
 *
 * The function is implemented with cycle-counted busy loops
 * and is intended to create the short delays required when interfacing with
 * hardware peripherals.
 *
 * The accuracy of the timing provided by this function is not specified,
 * but a general rule is that when running off of a crystal oscillator it will
 * be within 10us.  If the micro is running off of another type of oscillator
 * (e.g. RC) the timing accuracy will potentially be much worse.
 *
 * @param us  The specified time, in microseconds. 
              Values should be between 1 and 65535 microseconds.
 */
void halCommonDelayMicroseconds(uint16_t us);




/**
 * @brief Helper variable to track the state of 1.8V regulator.
 *
 * @note: Only used when DISABLE_INTERNAL_1V8_REGULATOR is defined.
 */
extern volatile int8_t halCommonVreg1v8EnableCount;

/**
 * @brief Disable the 1.8V regulator.  This function is to be used when
 * the 1.8V supply is provided externally.  Disabling the regulator
 * saves current consumption.  Disabling the regulator will cause ADC readings
 * of external signals to be wrong.  These exteranl signals include analog
 * sources ADC0 thru ADC5 and VDD_PADS/4.
 *
 * @note: Only used when DISABLE_INTERNAL_1V8_REGULATOR is defined.
 */
void halCommonDisableVreg1v8(void);

/**
 * @brief Enable the 1.8V regulator.  Normally the 1.8V regulator is enabled
 * out of reset.  This function is only needed if the 1.8V regulator has been
 * disabled and ADC conversions on external signals are needed.  These
 * exteranl signals include analog sources ADC0 thru ADC5 and VDD_PADS/4.
 * The state of 1v8 survives deep sleep.
 * 
 * @note: Only used when DISABLE_INTERNAL_1V8_REGULATOR is defined.
 */
void halCommonEnableVreg1v8(void);



/** @} END micro group  */
  

/** @file hal/micro/cortexm3/efm/micro.h
 * @brief Utility and convenience functions for EM35x microcontroller.
 * See @ref micro for documentation.
 *
 * <!-- Copyright 2008 by Ember Corporation.             All rights reserved.-->
 */

/** @addtogroup micro
 * See also hal/micro/cortexm3/micro.h for source code.
 *@{
 */




  //This is necessary here because halSetRadioHoldOff returns an
  //EmberStatus and not adding this typedef to this file breaks a
  //whole lot of builds due to include mis-ordering
  typedef uint8_t EmberStatus;

      //EZR32WG

// Micro specific serial defines

// Define the priority registers of system handlers and interrupts.
// This example shows how to save the current ADC interrupt priority and 
// then set it to 24:
//    uint8_t oldAdcPriority = INTERRUPT_PRIORITY_REGISTER(ADC);
//    INTERRUPT_PRIORITY_REGISTER(ADC) = 24;

// For Cortex-M3 faults and exceptions

// For EM3XX-specific interrupts


// The reset types of the EM300 series have both a base type and an 
//  extended type.  The extended type is a 16-bit value which has the base
//  type in the upper 8-bits, and the extended classification in the 
//  lower 8-bits
// For backwards compatibility with other platforms, only the base type is 
//  returned by the halGetResetInfo() API.  For the full extended type, the
//  halGetExtendedResetInfo() API should be called.
 

// Define the base reset cause types
enum {
/** @file hal/micro/cortexm3/reset-def.h
 * @brief Definitions for all the reset cause types
 *
 * <!-- Copyright 2009 by Ember Corporation.             All rights reserved.-->
 */
 
/** @addtogroup reset_def
 * Definitions for all the reset cause types.
 *
 * Reset cause types are built from a base definition and an extended.
 * definition. The base definitions allow working with entire categories of
 * resets while the extended definitions allow drilling down to very
 * specific causes.  The macros for the base and extended definitions are
 * combined for use in the code and equated to their combined numberical
 * equivalents.  In addition, exach base and extended definition is given
 * a corresponding 3 letter ASCII string to facilitate printing.  The ASCII
 * strings are best use with ::halGetExtendedResetString.
 *
 * For example:
 * \code
 * RESET_BASE_DEF(EXTERNAL,            0x03,     "EXT")
 *   RESET_EXT_DEF(EXTERNAL, UNKNOWN,    0x00,     "UNK")
 *   RESET_EXT_DEF(EXTERNAL, PIN,        0x01,     "PIN")
 * \endcode
 * results in enums which includes the entries:
 * \code
 * RESET_EXTERNAL = 0x03
 * RESET_EXTERNAL_PIN = 0x0301
 * \endcode
 * 
 * For a complete listing of all reset base and extended definitions, see
 * reset-def.h for source code.
 */


// *******************
// This file is specifically kept wider than 80 columns in order to keep the information 
//   well organized and easy to read by glancing down the columns
// *******************

// The reset types of the EM300 series have both a base type and an 
//  extended type.  The extended type is a 16-bit value which has the base
//  type in the upper 8-bits, and the extended classification in the 
//  lower 8-bits
// For backwards compatibility with other platforms, only the base type is 
//  returned by the halGetResetInfo() API.  For the full extended type, the
//  halGetExtendedResetInfo() API should be called.


// RESET_BASE_DEF macros take the following parameters:
//    RESET_BASE_DEF(basename, value, string)  // description
//        basename - the name used in the enum definition, expanded as RESET_basename
//        value - the value of the enum definition
//        string - the reset string, must be 3 characters
//        description - a comment describing the cause

// RESET_EXT_DEF macros take the following parameters:
//    RESET_EXT_DEF(basename, extname, extvalue, string)  // description
//        basename - the base name used in the enum definition
//        extname - the extended name used in the enum definition, expanded as RESET_basename_extname
//        extvalue - the LSB value of the enum definition, combined with the value of the base value in the MSB
//        string - the reset string, must be 3 characters
//        description - a comment describing the cause

// *******************
// This file is specifically kept wider than 80 columns in order to keep the information 
//   well organized and easy to read by glancing down the columns
// (Yes, this comment is mentioned multiple times in the file)
// *******************

// This file wants to use the bareword BOOTLOADER, which is sometimes a symbol.
// To allow this we will undefine the symbol here and restore it at the end of
// this file.

//[[ 
//   The first 3 (unknown, fib, and bootloader) reset base types and their
//     extended values should never be changed, as they are used by 
//     bootloaders in the field which can never be changed.
//   The later reset base and extended types may be changed over time
//]]

RESET_UNKNOWN = 0x00,    // Underterminable cause
      // Undeterminable cause
  
RESET_FIB = 0x01,      // Reset originated from the FIB bootloader
        // FIB bootloader caused a reset to main flash 
        // FIB bootloader is instructing ember bootloader to run
        // GO2 (unused)
        // GO3 (unused)
        // GO4 (unused)
        // GO5 (unused)
        // GO6 (unused)
        // GO7 (unused)
        // GO8 (unused)
        // GO9 (unused)
        // GOA (unused)
        // GOB (unused)
        // GOC (unused)
        // GOD (unused)
        // GOE (unused)
        // GOF (unused)
        // FIB bootloader is jumping to a specific flash address
        // FIB bootloader detected a high baud rate, causes ember bootloader to run
        // Read protection disabled, flash should be erased
        // BOOTMODE was not held long enough
        // MISMATCHED FIB Bootloader & Part Data
        // FIB Fatal Error
   
RESET_BOOTLOADER = 0x02,    // Reset relates to an Ember bootloader
      // Unknown bootloader cause (should never occur)
      // Bootloader caused reset telling app to run
      // Application requested that bootloader runs
      // Application bootloader detect bad external upgrade image 
      // Fatal Error or assert in bootloader
      // Forced bootloader activation
      // OTA Bootloader mode activation
      // Bootloader initiated deep sleep

//[[ -- Reset types below here may be changed in the future if absolutely necessary -- ]]

RESET_EXTERNAL = 0x03,    // External reset trigger
      // Unknown external cause (should never occur)
      // External pin reset
      // Woken up from EM4 from a pin

RESET_POWERON = 0x04,    // Poweron reset type, supply voltage < power-on threshold
      // Unknown poweron reset (should never occur)
      // High voltage poweron

RESET_WATCHDOG = 0x05,    // Watchdog reset occurred
      // Unknown watchdog reset (should never occur)
      // Watchdog timer expired
      // Watchdog low watermark expired and caught extended info
  
RESET_SOFTWARE = 0x06,    // Software triggered reset
      // Unknown software cause
      // General software reboot
      // App initiated deep sleep
      // App has been in EM4

RESET_CRASH = 0x07,    // Software crash
      // Unknown crash
      // a self-check assert in the code failed
  
RESET_FLASH = 0x08,    // Flash failure cause reset
      // Unknown flash failure
      // Flash write verify failure
      // Flash write inhibited: already written
  
RESET_FATAL = 0x09,    // A non-recoverable fatal error occurred
      // Unknown fatal error (should never occur)
      // CPU Core locked up
      // 24MHz crystal failure
      // option byte complement error

RESET_FAULT = 0x0A,    // A access fault occurred
      // An unknown fault occurred
      // Hard fault
      // Memory protection violation
      // Bus fault
      // Usage fault
      // Debug monitor fault
      // DMA RAM protection violation
      // Uninitialized interrupt vector

RESET_BROWNOUT = 0x0B,    // Brown out
      // An unknown fault occurred
      // unregulated power.
      // regulated power.
      // Analog Power Domain 0 (AVDD0).
      // Analog Power Domain 1 (AVDD1).
      // Analog Power Domain (AVDD).
      // Digital Power Domain (DVDD).
      // Detector Decouple (DEC).
      // Backup BOD on VDD_DREG.
      // Backup BOD on BU_VIN.
      // Backup BOD on unregulated power
      // Backup BOD on regulated power.
      // Backup Mode
// Restore the value of the BOOTLOADER symbol if we had to save it off in this
// file so that the word BOOTLOADER could be used.


  NUM_RESET_BASE_TYPES
};

// Define the extended reset cause types
enum {
/** @file hal/micro/cortexm3/reset-def.h
 * @brief Definitions for all the reset cause types
 *
 * <!-- Copyright 2009 by Ember Corporation.             All rights reserved.-->
 */
 
/** @addtogroup reset_def
 * Definitions for all the reset cause types.
 *
 * Reset cause types are built from a base definition and an extended.
 * definition. The base definitions allow working with entire categories of
 * resets while the extended definitions allow drilling down to very
 * specific causes.  The macros for the base and extended definitions are
 * combined for use in the code and equated to their combined numberical
 * equivalents.  In addition, exach base and extended definition is given
 * a corresponding 3 letter ASCII string to facilitate printing.  The ASCII
 * strings are best use with ::halGetExtendedResetString.
 *
 * For example:
 * \code
 * RESET_BASE_DEF(EXTERNAL,            0x03,     "EXT")
 *   RESET_EXT_DEF(EXTERNAL, UNKNOWN,    0x00,     "UNK")
 *   RESET_EXT_DEF(EXTERNAL, PIN,        0x01,     "PIN")
 * \endcode
 * results in enums which includes the entries:
 * \code
 * RESET_EXTERNAL = 0x03
 * RESET_EXTERNAL_PIN = 0x0301
 * \endcode
 * 
 * For a complete listing of all reset base and extended definitions, see
 * reset-def.h for source code.
 */


// *******************
// This file is specifically kept wider than 80 columns in order to keep the information 
//   well organized and easy to read by glancing down the columns
// *******************

// The reset types of the EM300 series have both a base type and an 
//  extended type.  The extended type is a 16-bit value which has the base
//  type in the upper 8-bits, and the extended classification in the 
//  lower 8-bits
// For backwards compatibility with other platforms, only the base type is 
//  returned by the halGetResetInfo() API.  For the full extended type, the
//  halGetExtendedResetInfo() API should be called.


// RESET_BASE_DEF macros take the following parameters:
//    RESET_BASE_DEF(basename, value, string)  // description
//        basename - the name used in the enum definition, expanded as RESET_basename
//        value - the value of the enum definition
//        string - the reset string, must be 3 characters
//        description - a comment describing the cause

// RESET_EXT_DEF macros take the following parameters:
//    RESET_EXT_DEF(basename, extname, extvalue, string)  // description
//        basename - the base name used in the enum definition
//        extname - the extended name used in the enum definition, expanded as RESET_basename_extname
//        extvalue - the LSB value of the enum definition, combined with the value of the base value in the MSB
//        string - the reset string, must be 3 characters
//        description - a comment describing the cause

// *******************
// This file is specifically kept wider than 80 columns in order to keep the information 
//   well organized and easy to read by glancing down the columns
// (Yes, this comment is mentioned multiple times in the file)
// *******************

// This file wants to use the bareword BOOTLOADER, which is sometimes a symbol.
// To allow this we will undefine the symbol here and restore it at the end of
// this file.

//[[ 
//   The first 3 (unknown, fib, and bootloader) reset base types and their
//     extended values should never be changed, as they are used by 
//     bootloaders in the field which can never be changed.
//   The later reset base and extended types may be changed over time
//]]

    // Underterminable cause
  RESET_UNKNOWN_UNKNOWN = (((RESET_UNKNOWN)<<8) + 0x00),    // Undeterminable cause
  
      // Reset originated from the FIB bootloader
  RESET_FIB_GO = (((RESET_FIB)<<8) + 0x00),      // FIB bootloader caused a reset to main flash 
  RESET_FIB_BOOTLOADER = (((RESET_FIB)<<8) + 0x01),      // FIB bootloader is instructing ember bootloader to run
  RESET_FIB_GO2 = (((RESET_FIB)<<8) + 0x02),      // GO2 (unused)
  RESET_FIB_GO3 = (((RESET_FIB)<<8) + 0x03),      // GO3 (unused)
  RESET_FIB_GO4 = (((RESET_FIB)<<8) + 0x04),      // GO4 (unused)
  RESET_FIB_GO5 = (((RESET_FIB)<<8) + 0x05),      // GO5 (unused)
  RESET_FIB_GO6 = (((RESET_FIB)<<8) + 0x06),      // GO6 (unused)
  RESET_FIB_GO7 = (((RESET_FIB)<<8) + 0x07),      // GO7 (unused)
  RESET_FIB_GO8 = (((RESET_FIB)<<8) + 0x08),      // GO8 (unused)
  RESET_FIB_GO9 = (((RESET_FIB)<<8) + 0x09),      // GO9 (unused)
  RESET_FIB_GOA = (((RESET_FIB)<<8) + 0x0A),      // GOA (unused)
  RESET_FIB_GOB = (((RESET_FIB)<<8) + 0x0B),      // GOB (unused)
  RESET_FIB_GOC = (((RESET_FIB)<<8) + 0x0C),      // GOC (unused)
  RESET_FIB_GOD = (((RESET_FIB)<<8) + 0x0D),      // GOD (unused)
  RESET_FIB_GOE = (((RESET_FIB)<<8) + 0x0E),      // GOE (unused)
  RESET_FIB_GOF = (((RESET_FIB)<<8) + 0x0F),      // GOF (unused)
  RESET_FIB_JUMP = (((RESET_FIB)<<8) + 0x10),      // FIB bootloader is jumping to a specific flash address
  RESET_FIB_BAUDRATE = (((RESET_FIB)<<8) + 0x11),      // FIB bootloader detected a high baud rate, causes ember bootloader to run
  RESET_FIB_UNPROTECT = (((RESET_FIB)<<8) + 0x12),      // Read protection disabled, flash should be erased
  RESET_FIB_BOOTMODE = (((RESET_FIB)<<8) + 0x13),      // BOOTMODE was not held long enough
  RESET_FIB_MISMATCH = (((RESET_FIB)<<8) + 0x14),      // MISMATCHED FIB Bootloader & Part Data
  RESET_FIB_FATAL = (((RESET_FIB)<<8) + 0x15),      // FIB Fatal Error
   
    // Reset relates to an Ember bootloader
  RESET_BOOTLOADER_UNKNOWN = (((RESET_BOOTLOADER)<<8) + 0x00),    // Unknown bootloader cause (should never occur)
  RESET_BOOTLOADER_GO = (((RESET_BOOTLOADER)<<8) + 0x01),    // Bootloader caused reset telling app to run
  RESET_BOOTLOADER_BOOTLOAD = (((RESET_BOOTLOADER)<<8) + 0x02),    // Application requested that bootloader runs
  RESET_BOOTLOADER_BADIMAGE = (((RESET_BOOTLOADER)<<8) + 0x03),    // Application bootloader detect bad external upgrade image 
  RESET_BOOTLOADER_FATAL = (((RESET_BOOTLOADER)<<8) + 0x04),    // Fatal Error or assert in bootloader
  RESET_BOOTLOADER_FORCE = (((RESET_BOOTLOADER)<<8) + 0x05),    // Forced bootloader activation
  RESET_BOOTLOADER_OTAVALID = (((RESET_BOOTLOADER)<<8) + 0x06),    // OTA Bootloader mode activation
  RESET_BOOTLOADER_DEEPSLEEP = (((RESET_BOOTLOADER)<<8) + 0x07),    // Bootloader initiated deep sleep

//[[ -- Reset types below here may be changed in the future if absolutely necessary -- ]]

    // External reset trigger
  RESET_EXTERNAL_UNKNOWN = (((RESET_EXTERNAL)<<8) + 0x00),    // Unknown external cause (should never occur)
  RESET_EXTERNAL_PIN = (((RESET_EXTERNAL)<<8) + 0x01),    // External pin reset
  RESET_EXTERNAL_EM4PIN = (((RESET_EXTERNAL)<<8) + 0x02),    // Woken up from EM4 from a pin

    // Poweron reset type, supply voltage < power-on threshold
  RESET_POWERON_UNKNOWN = (((RESET_POWERON)<<8) + 0x00),    // Unknown poweron reset (should never occur)
  RESET_POWERON_HV = (((RESET_POWERON)<<8) + 0x01),    // High voltage poweron

    // Watchdog reset occurred
  RESET_WATCHDOG_UNKNWON = (((RESET_WATCHDOG)<<8) + 0x00),    // Unknown watchdog reset (should never occur)
  RESET_WATCHDOG_EXPIRED = (((RESET_WATCHDOG)<<8) + 0x01),    // Watchdog timer expired
  RESET_WATCHDOG_CAUGHT = (((RESET_WATCHDOG)<<8) + 0x02),    // Watchdog low watermark expired and caught extended info
  
    // Software triggered reset
  RESET_SOFTWARE_UNKNOWN = (((RESET_SOFTWARE)<<8) + 0x00),    // Unknown software cause
  RESET_SOFTWARE_REBOOT = (((RESET_SOFTWARE)<<8) + 0x01),    // General software reboot
  RESET_SOFTWARE_DEEPSLEEP = (((RESET_SOFTWARE)<<8) + 0x02),    // App initiated deep sleep
  RESET_SOFTWARE_EM4 = (((RESET_SOFTWARE)<<8) + 0x03),    // App has been in EM4

    // Software crash
  RESET_CRASH_UNKNOWN = (((RESET_CRASH)<<8) + 0x00),    // Unknown crash
  RESET_CRASH_ASSERT = (((RESET_CRASH)<<8) + 0x01),    // a self-check assert in the code failed
  
    // Flash failure cause reset
  RESET_FLASH_UNKNWON = (((RESET_FLASH)<<8) + 0x00),    // Unknown flash failure
  RESET_FLASH_VERIFY = (((RESET_FLASH)<<8) + 0x01),    // Flash write verify failure
  RESET_FLASH_INHIBIT = (((RESET_FLASH)<<8) + 0x02),    // Flash write inhibited: already written
  
    // A non-recoverable fatal error occurred
  RESET_FATAL_UNKNOWN = (((RESET_FATAL)<<8) + 0x00),    // Unknown fatal error (should never occur)
  RESET_FATAL_LOCKUP = (((RESET_FATAL)<<8) + 0x01),    // CPU Core locked up
  RESET_FATAL_CRYSTAL = (((RESET_FATAL)<<8) + 0x02),    // 24MHz crystal failure
  RESET_FATAL_OPTIONBYTE = (((RESET_FATAL)<<8) + 0x03),    // option byte complement error

    // A access fault occurred
  RESET_FAULT_UNKNOWN = (((RESET_FAULT)<<8) + 0x00),    // An unknown fault occurred
  RESET_FAULT_HARD = (((RESET_FAULT)<<8) + 0x01),    // Hard fault
  RESET_FAULT_MEM = (((RESET_FAULT)<<8) + 0x02),    // Memory protection violation
  RESET_FAULT_BUS = (((RESET_FAULT)<<8) + 0x03),    // Bus fault
  RESET_FAULT_USAGE = (((RESET_FAULT)<<8) + 0x04),    // Usage fault
  RESET_FAULT_DBGMON = (((RESET_FAULT)<<8) + 0x05),    // Debug monitor fault
  RESET_FAULT_PROTDMA = (((RESET_FAULT)<<8) + 0x06),    // DMA RAM protection violation
  RESET_FAULT_BADVECTOR = (((RESET_FAULT)<<8) + 0x07),    // Uninitialized interrupt vector

    // Brown out
  RESET_BROWNOUT_UNKNOWN = (((RESET_BROWNOUT)<<8) + 0x00),    // An unknown fault occurred
  RESET_BROWNOUT_UNREGPOWER = (((RESET_BROWNOUT)<<8) + 0x01),    // unregulated power.
  RESET_BROWNOUT_REGPOWER = (((RESET_BROWNOUT)<<8) + 0x02),    // regulated power.
  RESET_BROWNOUT_AVDD0 = (((RESET_BROWNOUT)<<8) + 0x03),    // Analog Power Domain 0 (AVDD0).
  RESET_BROWNOUT_AVDD1 = (((RESET_BROWNOUT)<<8) + 0x04),    // Analog Power Domain 1 (AVDD1).
  RESET_BROWNOUT_AVDD = (((RESET_BROWNOUT)<<8) + 0x05),    // Analog Power Domain (AVDD).
  RESET_BROWNOUT_DVDD = (((RESET_BROWNOUT)<<8) + 0x06),    // Digital Power Domain (DVDD).
  RESET_BROWNOUT_DEC = (((RESET_BROWNOUT)<<8) + 0x06),    // Detector Decouple (DEC).
  RESET_BROWNOUT_BACKUP_VDD_DREG = (((RESET_BROWNOUT)<<8) + 0x07),    // Backup BOD on VDD_DREG.
  RESET_BROWNOUT_BACKUP_BU_VIN = (((RESET_BROWNOUT)<<8) + 0x08),    // Backup BOD on BU_VIN.
  RESET_BROWNOUT_BACKUP_UNREGPOWER = (((RESET_BROWNOUT)<<8) + 0x09),    // Backup BOD on unregulated power
  RESET_BROWNOUT_BACKUP_REGPOWER = (((RESET_BROWNOUT)<<8) + 0x10),    // Backup BOD on regulated power.
  RESET_BROWNOUT_BACKUP_MODE = (((RESET_BROWNOUT)<<8) + 0x11),    // Backup Mode
// Restore the value of the BOOTLOADER symbol if we had to save it off in this
// file so that the word BOOTLOADER could be used.


};

// These define the size of the GUARD region configured in the MPU that
// sits between the heap and the stack

// Define a value to fill the guard region between the heap and stack.

// Resize the CSTACK to add space to the 'heap' that exists below it
uint32_t halStackModifyCStackSize(int32_t stackSizeDeltaWords);

// Initialize the CSTACK/Heap region and the guard page in between them
void halInternalInitCStackRegion(void);

// Helper functions to get the location of the stack/heap
uint32_t halInternalGetCStackBottom(void);
uint32_t halInternalGetHeapTop(void);
uint32_t halInternalGetHeapBottom(void);


/** @name Vector Table Index Definitions
 * These are numerical definitions for vector table. Indices 0 through 15 are
 * Cortex-M3 standard exception vectors and indices 16 through 35 are EM3XX
 * specific interrupt vectors.
 *
 *@{
 */

/**
 * @brief A numerical definition for a vector.
 */
/**
 * @brief Number of vectors.
 */
/** @}  Vector Table Index Definitions */

/**
 * @brief Records the specified reset cause then forces a reboot.
 */
void halInternalSysReset(uint16_t extendedCause);

/**
 * @brief Returns the Extended Reset Cause information
 *
 * @return A 16-bit code identifying the base and extended cause of the reset
 */
uint16_t halGetExtendedResetInfo(void);

/** @brief Calls ::halGetExtendedResetInfo() and supplies a string describing 
 *  the extended cause of the reset.  halGetResetString() should also be called
 *  to get the string for the base reset cause
 *
 * @appusage Useful for diagnostic printing of text just after program 
 * initialization.
 *
 * @return A pointer to a program space string.
 */
const char * halGetExtendedResetString(void);


//[[ ram vectors are not public

/** @brief Install the given address at the given vector number, overriding
 *  the default value found in Flash.
 *
 * The first RAM Vector to be Registered will automatically cause the RAM
 * Vector table to be filled from the Flash Vector table and the RAM table
 * will be enabled.
 *
 * @param vectorNumber  The vector number that is being changed.  There are
 * 31 valid vectors, 2-32, and the list can be found in nvic-config.h.
 * 
 * @param newVector  The 32-bit address to install into the vector.  This
 * is generally the address of the function that should be called when
 * the vector is triggered.
 *
 * @return The 32-bit address of the previous vector in the RAM Table that
 * is being replaced.
 */
uint32_t halRegisterRamVector(uint8_t vectorNumber, uint32_t newVector);


/** @brief Uninstall the given vector number, restoring the vector from the
 *  Flash vector table.
 *
 * The last RAM Vector to be UnRegistered will automatically cause the RAM
 * Vector table to be deactivated and Flash Vector table will regain control.
 *
 * @param vectorNumber  The vector number that is being changed.  There are
 * 31 valid vectors, 2-32, and the list can be found in nvic-config.h.
 * 
 * @return The 32-bit address of the previous vector in the RAM Table that
 * is being replaced.
 */
uint32_t halUnRegisterRamVector(uint8_t vectorNumber);


/** @brief Enables or disables Radio HoldOff support
 *
 * @param enable  When true, configures ::RHO_GPIO in BOARD_HEADER
 * as an input which, when asserted, will prevent the radio from
 * transmitting.  When false, configures ::RHO_GPIO for its original
 * purpose.
 */
EmberStatus halSetRadioHoldOff(_Bool enable);


/** @brief Returns whether Radio HoldOff has been enabled or not.
 *
 * @return true if Radio HoldOff has been enabled, false otherwise.
 */
_Bool halGetRadioHoldOff(void);


/** @brief To assist with saving power when the radio automatically powers
 * down, this function allows the stack to tell the HAL to put pins
 * specific to radio functionality in their powerdown state.  The pin
 * state used is the state used by halInternalPowerDownBoard, but applied
 * only to the pins identified in the global variable gpioRadioPowerBoardMask.
 * The stack will automatically call this function as needed, but it
 * will only change GPIO state based on gpioRadioPowerBoardMask.  Most
 * commonly, the bits set in gpioRadioPowerBoardMask petain to using a
 * Front End Module.
 */
void halStackRadioPowerDownBoard(void);


/** @brief To assist with saving power when the radio automatically powers
 * up, this function allows the stack to tell the HAL to put pins
 * specific to radio functionality in their powerup state.  The pin
 * state used is the state used by halInternalPowerUpBoard, but applied
 * only to the pins identified in the global variable gpioRadioPowerBoardMask.
 * The stack will automatically call this function as needed, but it
 * will only change GPIO state based on gpioRadioPowerBoardMask.  Most
 * commonly, the bits set in gpioRadioPowerBoardMask petain to using a
 * Front End Module.
 */
void halStackRadioPowerUpBoard(void);

//]]

/** @file hal/micro/cortexm3/micro-common.h
 * @brief Utility and convenience functions for EM35x microcontroller,
 *        common to both the full and minimal hal.
 * See @ref micro for documentation.
 *
 * <!-- Copyright 2013 Silicon Laboratories, Inc.                        *80*-->
 */

/** @addtogroup micro
 * See also hal/micro/cortexm3/micro.h for source code.
 *@{
 */



// Forward declarations of the handlers used in the vector table
// These declarations are extracted from the NVIC configuration file.
 /***************************************************************************//**
 * @file nvic-config.h
 * @brief NVIC Config Header
 * @version 0.01.0
 *******************************************************************************
 * @section License
 * <b>(C) Copyright 2014 Silicon Labs, http://www.silabs.com</b>
 *******************************************************************************
 *
 * This file is licensed under the Silabs License Agreement. See the file
 * "Silabs_License_Agreement.txt" for details. Before using this software for
 * any purpose, you must agree to the terms of that agreement.
 *

 ******************************************************************************/

 /***************************************************************************//**
 * @file nvic-config.h
 * @brief NVIC Config Header
 * @version 0.01.0
 *******************************************************************************
 * @section License
 * <b>(C) Copyright 2014 Silicon Labs, http://www.silabs.com</b>
 *******************************************************************************
 *
 * This file is licensed under the Silabs License Agreement. See the file
 * "Silabs_License_Agreement.txt" for details. Before using this software for
 * any purpose, you must agree to the terms of that agreement.
 *

 ******************************************************************************/
 
/** @addtogroup nvic_config
 * Nested Vectored Interrupt Controller configuration header.
 *
 * This header defines the functions called by all of the NVIC exceptions/
 * interrupts.  The following are the nine peripheral ISRs available for
 * modification.  To use one of these ISRs, it must be instantiated
 * somewhere in the HAL.  Each ISR may only be instantiated once.  It is
 * not necessary to instantiate all or any of these ISRs (a stub will
 * be automatically generated if an ISR is not instantiated).
 *
 * - \code void halTimer1Isr(void); \endcode
 * - \code void halTimer2Isr(void); \endcode
 * - \code void halSc1Isr(void);    \endcode
 * - \code void halSc1Isr(void);    \endcode
 * - \code void halAdcIsr(void);    \endcode
 * - \code void halIrqAIsr(void);   \endcode
 * - \code void halIrqBIsr(void);   \endcode
 * - \code void halIrqCIsr(void);   \endcode
 * - \code void halIrqDIsr(void);   \endcode
 *
 * @note This file should \b not be modified.
 */


// \b NOTE NOTE NOTE NOTE NOTE NOTE - The physical layout of this file, that
// means the white space, is CRITICAL!  Since this file is \#include'ed by
// the assembly file isr-stubs.s79, the white space in this file translates
// into the white space in that file and the assembler has strict requirements.
// Specifically, there must be white space *before* each "SEGMENT()" and there
// must be an *empty line* between each "EXCEPTION()" and "SEGMENT()".
//
// \b NOTE NOTE NOTE - The order of the EXCEPTIONS in this file is critical
// since it translates to the order they are placed into the vector table in
// cstartup.
//
// The purpose of this file is to consolidate NVIC configuration, this
// includes basic exception handler (ISR) function definitions, into a single
// place where it is easily tracked and changeable.
//
// We establish 8 levels of priority (3 bits), with 32 (5 bits) of tie break
// priority. Lower priority values are higher priorities. This means that 0
// is the highest and 7 is the lowest. The NVIC mapping is detailed below.
//

//The 'PRIGROUP' field is 3 bits within the AIRCR register and indicates the
//bit position within a given exception's 8-bit priority field to the left of
//which is the "binary point" separating the preemptive priority level (in the
//most-significant bits) from the subpriority (in the least-significant bits).
//The preemptive priority determines whether an interrupt can preempt an
//executing interrupt. The subpriority helps choose which interrupt to run if
//multiple interrupts with the same preemptive priority are active at the same
//time. If no supriority is given or there is a tie then the hardware defined
//exception number is used to break the tie.
//
// Pri.Sub  Purpose
//   0.0    faults (highest)
//   1.0    not used
//   2.0    SysTick for idling, MAC Tmr for idling
//          during TX, and management interrupt for XTAL biasing.
//   3.0    DISABLE_INTERRUPTS(), INTERRUPTS_OFF(), ATOMIC()
//   4.0    normal interrupts
//   5.0    not used
//   6.0    not used
//   7.0    debug backchannel, PendSV
//   7.31   reserved (lowest)

// Priority level used by DISABLE_INTERRUPTS() and INTERRUPTS_OFF()
// Must be lower priority than pendsv 
// NOTE!! IF THIS VALUE IS CHANGED, SPRM.S79 MUST ALSO BE UPDATED


//Exceptions with fixed priorities cannot be changed by software.  Simply make
//them 0 since they are high priorities anyways.
//Reserved exceptions are not instatiated in the hardware.  Therefore
//exception priorities don't exist so just default them to lowest level.


    // SEGMENT()
    //   **Place holder required by isr-stubs.s79 to define __CODE__**
    // SEGMENT2()
    //   **Place holder required by isr-stubs.s79 to define __THUMB__**
    // EXCEPTION(vectorNumber, functionName, priorityLevel, subpriority)
    //   vectorNumber = exception number defined by hardware (not used anywhere)
    //   functionName = name of the function that the exception should trigger
    //   priorityLevel = priority level of the function
    //   supriority = Used to break ties between exceptions at the same level
    // PERM_EXCEPTION
    //   is used to define an exception that should not be intercepted by the
    //   interrupt debugging logic, or that not should have a weak stub defined.  
    //   Otherwise the definition is the same as EXCEPTION

//INTENTIONALLY INDENTED AND SPACED APART! Keep it that way!  See comment above!
    
    
    void halEntryPoint(void);      //Reset Handler
    
    
    
    void halNmiIsr(void);  //NMI Handler
    
    
    
    void halHardFaultIsr(void);  //Hard Fault Handler
    
    
    
    void halMemoryFaultIsr(void);      //Memory Fault Handler 
    
    
    
    void halBusFaultIsr(void);      //Bus Fault Handler
    
    
    
    void halUsageFaultIsr(void);      //Usage Fault Handler
    
    
    
    void halReserved07Isr(void);   //Reserved
    
    
    
    void halReserved08Isr(void);   //Reserved
    
    
    
    void halReserved09Isr(void);   //Reserved
    
    
    
    void halReserved10Isr(void);   //Reserved
    
    
    
    void halSvCallIsr(void);      //SVCall Handler
    
    
    
    void halDebugMonitorIsr(void);      //Debug Monitor Handler
    
    
    
    void halReserved13Isr(void);   //Reserved
    
    
    
    void halPendSvIsr(void);      //PendSV Handler
    
    
    
    void halInternalSysTickIsr(void);      //SysTick Handler
    
    //The following handlers map to "External Interrupts 16 and above"
    //In the NVIC Interrupt registers, this corresponds to bits 16:0 with bit 0
    //being TIMER1 (exception 4) and bit 15 being IRQD (exception 15)
    
    
    void DMA_IRQHandler(void);    //DMA
    
    
    
    void GPIO_EVEN_IRQHandler(void);    //GPIO_EVEN
    
    
    
    void TIMER0_IRQHandler(void);    //TIMER0
    
    
    
    void USART0_RX_IRQHandler(void);    //USART0_RX
    
    
    
    void USART0_TX_IRQHandler(void);    //USART0_TX
    
    
    
    void USB_IRQHandler(void);    //USB
  
    
    
    void ACMP0_IRQHandler(void);    //ACMP0
    
    
    
    void ADC0_IRQHandler(void);    //ADC0
    
    
    
    void DAC0_IRQHandler(void);    //DAC0
    
    
    
    void I2C0_IRQHandler(void);    //I2C0
    
    
    
    void I2C1_IRQHandler(void);    //I2C1
    
    
    
    void GPIO_ODD_IRQHandler(void);    //GPIO_ODD
    
    
    
    void TIMER1_IRQHandler(void);    //TIMER1
    
    
    
    void TIMER2_IRQHandler(void);    //TIMER2
    
    
    
    void TIMER3_IRQHandler(void);    //TIMER3

    
    
    void USART1_RX_IRQHandler(void);    //USART1_RX

    
    
    void USART1_TX_IRQHandler(void);    //USART1_TX

    
    
    void LESENSE_IRQHandler(void);    //LESENSE

    
    
    void USART2_RX_IRQHandler(void);    //USART2_RX

    
    
    void USART2_TX_IRQHandler(void);    //USART2_TX

    
    
    void UART0_RX_IRQHandler(void);    //UART0_RX

    
    
    void UART0_TX_IRQHandler(void);    //UART0_TX

    
    
    void UART1_RX_IRQHandler(void);    //UART1_RX

    
    
    void UART1_TX_IRQHandler(void);    //UART1_TX

    
    
    void LEUART0_IRQHandler(void);    //LEUART0

    
    
    void LEUART1_IRQHandler(void);    //LEUART1

    
    
    void LETIMER0_IRQHandler(void);    //LETIMER0

    
    
    void PCNT0_IRQHandler(void);    //PCNT0

    
    
    void PCNT1_IRQHandler(void);    //PCNT1

    
    
    void PCNT2_IRQHandler(void);    //PCNT2

    
    
    void RTC_IRQHandler(void);   //RTC

    
    
    void BURTC_IRQHandler(void);    //BURTC

    
    
    void CMU_IRQHandler(void);    //CMU

    
    
    void VCMP_IRQHandler(void);    //VCMP

    
    
    void LCD_IRQHandler(void);    //LCD
    
    
    
    void MSC_IRQHandler(void);    //MSC

    
    
    void AES_IRQHandler(void);    //AES

    
    
    void halReserved37Isr(void);   //Reserved

    
    
    void EMU_IRQHandler(void);   //EMU




/**
 * @brief OSC32K_x values can be used in board headers to specify the
 * desired mode for system timekeeping.  Because preprocessor logic
 * is used to check validity, these have to be #defines and not an enum.
 */

/**
 * @brief Some registers and variables require identifying GPIO by
 * a single number instead of the port and pin.  This macro converts
 * Port A pins into a single number.
 */
/**
 * @brief Some registers and variables require identifying GPIO by
 * a single number instead of the port and pin.  This macro converts
 * Port B pins into a single number.
 */
/**
 * @brief Some registers and variables require identifying GPIO by
 * a single number instead of the port and pin.  This macro converts
 * Port C pins into a single number.
 */

/**
 * @brief Resets the watchdog timer.  This function is pointed
 * to by the macro ::halResetWatchdog().
 * @warning Be very careful when using this as you can easily get into an
 * infinite loop.
 */
void halInternalResetWatchDog( void );


/**
 * @brief Configure an IO pin's operating mode
 *
 * @param gpio   The IO pin to use, can be specified with the convenience macros
 *               PORTA_PIN(), PORTB_PIN(), PORTC_PIN(), etc.
 * @param config   The configuration mode to use.
 *
 */
void halGpioSetConfig(uint32_t gpio, uint32_t config);


/**
 * @brief Calibrates the internal SlowRC to generate a 1024 Hz (1kHz) clock.
 */
void halInternalCalibrateSlowRc( void );

/**
 * @brief Calibrates the internal FastRC to generate a 12MHz clock.
 */
void halInternalCalibrateFastRc(void);


/**
 * @brief Sets the trim values for the 1.8V and 1.2V regulators based upon
 * manufacturing configuration.
 *
 * @param boostMode  Alter the regulator trim based upon the state
 * of boost mode.  true if boost mode is active, false otherwise.
 */
void halInternalSetRegTrim(_Bool boostMode);

/** @brief Determine VREG_OUT in the current mode (normal or boost).
 *
 * @return VREG_OUT in millivolts, depending on normal or boost mode
 */
uint16_t halInternalGetVreg(void);

/**
 * @brief Calibrates the GPIO pads.  This function is called from within
 * the stack and HAL at appropriate times.
 */
void halCommonCalibratePads(void);

enum {
  SYSCLK_BOOT_START  = 1, // halCommonStartXtal()
  SYSCLK_BOOT_SWITCH = 2, // halCommonSwitchToXtal()
  SYSCLK_WAKE_START  = 3, // halInternalPowerUpKickXtal()
  SYSCLK_WAKE_SWITCH = 4, // halInternalBlockUntilXtal()
  SYSCLK_NEED_STABLE = 5, // halCommonBlockUntilXtal()
  SYSCLK_BIAS_EVENT  = 6, // Timed event occurred
};
typedef uint8_t SysClkCallbackContext;


/**
 * @brief This callback can be implemented outside of the HAL to activate
 * a non-crystal system clock, if such activation is not done purely by
 * hardware but needs software assist (e.g. enabling it via GPIO).
 * It is called from within halInit() during bootup and from within
 * halPowerUp() during sleep wakeup if the system clock has become
 * disabled or deselected.  In each case, if the callback returns a non-zero
 * value, therewill be more calls made to poll until 0 is returned.  The first
 * callback occurs prior to halInternalInitBoard() or halInternalPowerUpBoard()
 * with a context of SYSCLK_BOOT_START or SYSCLK_WAKE_START to "start" the
 * clock, and remaining callbacks, if needed, are made subsequently.
 * In the case of a non-Xtal, OSC24M_CTRL_OSC24M_EN will have been set
 * before this callback is issued, and OSC24M_CTRL_OSC24M_SEL will only
 * be set when the callback returns 0, allowing the system clock switch
 * to occur.
 *
 * @param context Is the situation for the callback, per the
 * SysClkCallbackContext enum above.
 *
 * @return Time, in microseconds, to idle-delay (while still running on
 * internal fast RC system clock), and be called back again with a
 * SYSCLK_BIAS_EVENT, or 0 if can switch immediately to the external clock.
 */
uint16_t halSystemClockEnableCallback(SysClkCallbackContext context);

/**
 * @brief This function can be used to determine the system clock frequency.
 *
 * @return The current system clock frequency, in kilohertz (1000 Hz).
 */
uint16_t halSystemClockKHz(void);

/**
 * @brief This function can be used to determine the MCU clock frequency.
 *
 * @return The current MCU clock frequency, in kilohertz (1000 Hz).
 */
uint16_t halMcuClockKHz(void);

/**
 * @brief This function can be used to determine the peripheral clock frequency.
 *
 * @return The current peripheral clock frequency, in kilohertz (1000 Hz).
 */
uint16_t halPeripheralClockKHz(void);

/**
 * @brief Convenience macro to convert microseconds to ticks of the MAC_TIMER,
 * which is designed to tick every 1 microsecond on a 12 MHz Periph clock.
 * (Because the PCLK might not evenly divide by 1000 or even 500, use quad
 * arithmetic, dividing it by 250.)
 */

/**
 * @brief Convenience macro to convert MAC_TIMER ticks to microseconds and
 * rounding to nearest microsecond.
 * (Because the PCLK might not evenly divide by 1000 or even 500, use quad
 * arithmetic, dividing it by 250.)
 */


/**
 * @brief This function can be used to configure an arbitrary baud rate
 * on a UART port, based on the current peripheral clock rate.
 *
 * @param port     Serial port number (0 or 1).
 *
 * @param baud     An arbitrary baud rate > 0.
 *
 * @return EMBER_SERIAL_INVALID_BAUD_RATE if the baud rate is out of range,
 * otherwise EMBER_SUCCESS.
 */
EmberStatus halInternalUartSetBaudRate(uint8_t port, uint32_t baud);

/**
 * @brief This function returns the current baud rate configured on
 * a UART port, based on the current peripheral clock rate.
 *
 * @param port     Serial port number (0 or 1).
 *
 * @return The port's baud rate, or 0 if not configured or no such port.
 */
uint32_t halInternalUartGetBaudRate(uint8_t port);

/**
 * @brief Convenience macro to get current TPIU speed in Hz
 */

/**
 * @brief Convenience macro to set current TPIU speed in Hz
 */

/**
 * @brief This is the core function for enabling the XTAL, biasing
 * the XTAL, checking the XTAL biasing, switching to the XTAL,
 * configuring FCLK, and configuring flash access settings.  The ultimate
 * result of calling this function until it returns true is the chip is
 * operating from the 24MHz XTAL, the XTAL is biased for lowest current
 * consumption, the CPU's FCLK is being sourced from SYSCLK, and the flash
 * is configured for optimal current consumption.
 *
 * The basic principle of this function is that it takes time for the
 * XTAL to stabilize whenever it is enabled and/or the biasing is change;
 * about 1.5ms every time the bias is changed.  This function will handle
 * the XTAL configuration, set an interrupt event to indicate when the
 * appropriate delay has elapsed, and return immediately.  This interrupt
 * event should not be monitored directly by any code other than the clock
 * module itself.  The state of the XTAL is learned by the return code
 * of this function.  As long as this function returns false, the XTAL
 * is unstable.  Calling code can perform other actions until the XTAL
 * is stable.
 *
 * The suggested use of the four XTAL API functions is as follows:
 *  - halCommonStartXtal() is called once as soon as possible to start
 *    the XTAL.  Other actions may be performed while waiting for the XTAL
 *    to stabilize.
 *  - halCommonTryToSwitchToXtal() is called repeatedly to drive
 *    the biasing and switch process.  Other actions that do not require
 *    a stable XTAL may be performed until this function returns 0.
 *  - halCommonSwitchToXtal() is called just once when a stable XTAL is
 *    required before moving on.  This function will block in the idle
 *    sleep state until the switch procedure has completed.
 *  - halCommonCheckXtalBiasTrim() is called periodically, after a switch
 *    has occurred, to check that the XTAL biasing is optimal and
 *    adjust if needed.
 *
 * halCommonTryToSwitchToXtal() function will return immediately.  This
 * function drives the switch process.  This function can be called
 * any number of times and at anytime.
 *
 * @param amBlocking true if being called in a blocking context (loop),
 * false otherwise.  Used to distinguish startup from waiting on Xtal.
 *
 * @return time, in microseconds, to delay until next bias event for crystal
 * stability.  If 0, the chip has switched to and is now using the XTAL.
 * No further bias events are in process.  If non-zero the Xtal is
 * <b>unstable<b> and the chip has not modified it's XTAL selection; it
 * remains on the same clock source (OSCHF or XTAL) and there is a bias event
 * in process.
 */
uint16_t halCommonTryToSwitchToXtal(SysClkCallbackContext context);

void halInternalPowerUpKickXtal(void);
void halInternalBlockUntilXtal(void);
void halCommonBlockUntilXtal(void);

enum {
  WAKEUP_XTAL_STATE_START          = 0,
  WAKEUP_XTAL_STATE_BEFORE_LO_EN   = 1,
  WAKEUP_XTAL_STATE_LO_EN          = 2,
  WAKEUP_XTAL_STATE_READY_SWITCH   = 3,
  WAKEUP_XTAL_STATE_WAITING_FINAL  = 4,
  WAKEUP_XTAL_STATE_FINAL          = 5,
};
typedef uint8_t WakeupXtalState;

extern volatile WakeupXtalState wakeupXtalState;

/**
 * @brief This function is intended to be called periodically, from the
 * HAL and application, to check the XTAL bias trim is within
 * appropriate levels and adjust if not.  It will return immediately.
 * This function can be called any number of times and at anytime.
 */
//Simply redirect to the primary switch function, which handles all XTAL
//switching and biasing activities.  We don't care about the return code.
//0 is ideal but we could get non-zero (even if on the XTAL) because there
//is a biasing event in process and the XTAL is unstable.

/**
 * @brief This function is intended to initiate the XTAL start, bias, and
 * switch procedure. It will return immediately.  This allows the calling
 * code to do other things while waiting for the XTAL to stabilize.  The
 * functions halCommonTryToSwitchToXtal() and halCommonSwitchToXtal() are
 * intended for completing the process.  This function can be called any
 * number of times and at anytime.
 */
//Simply redirect to the primary switch function, which handles all XTAL
//switching and biasing activities.  We don't care about the return code.
//0 is ideal but we could get non-zero (even if on the XTAL) because there
//is a biasing event in process and the XTAL is unstable.

/**
 * @brief This function switches the chip to using the XTAL.  This includes
 * biasing the XTAL and changing the CPU to 24MHz (FCLK sourced from SYSCLK).
 * This function <b>blocks</b> until the switch procedure has occurred.
 * While blocking, this function invokes idle sleep to reduce current
 * consumption.
 *
 * NOTE: It is possible to use this function as a replacement for
 * the three other XTAL APIs, including halCommonCheckXtalBiasTrim(), as
 * long as blocking is acceptable.
 *
 * This function can be called any number of times and at anytime.
 */
void halCommonSwitchToXtal(void);

/**
 * @brief This function configures flash access for optimal current.
 */
void halInternalConfigFlashAccess(void);

/** @brief Blocks the current thread of execution for the specified
 * amount of time, in milliseconds.
 *
 * The function is implemented with cycle-counted busy loops
 * and is intended to create the short delays required when interfacing with
 * hardware peripherals.  This function works by simply adding another
 * layer on top of halCommonDelayMicroseconds().
 *
 * @param ms  The specified time, in milliseconds.
 */
void halCommonDelayMilliseconds(uint16_t ms);


/** @brief Puts the microcontroller to sleep in a specified mode, allows
 * the GPIO wake sources to be determined at runtime.  The function halSleep()
 * requires the GPIO wake sources to be defined at compile time in the board
 * file.
 *
 * @note This routine always enables interrupts.
 *
 * @param sleepMode  A microcontroller sleep mode.
 *
 * @param gpioWakeBitMask  A bit mask of the GPIO that are allowed to wake
 * the chip from deep sleep.  A high bit in the mask will enable waking
 * the chip if the corresponding GPIO changes state.  bit0 is PA0, bit1 is
 * PA1, bit8 is PB0, bit16 is PCO, bit23 is PC7, bits[31:24] are ignored.
 *
 * @sa ::SleepModes
 */
void halSleepWithOptions(SleepModes sleepMode, WakeMask gpioWakeBitMask);


/**
 * @brief Uses the system timer to enter ::SLEEPMODE_WAKETIMER for
 * approximately the specified amount of time (provided in quarter seconds),
 * the GPIO wake sources can be provided at runtime.
 *
 * This function returns ::EMBER_SUCCESS and the duration parameter is
 * decremented to 0 after sleeping for the specified amount of time.  If an
 * interrupt occurs that brings the chip out of sleep, the function returns
 * ::EMBER_SLEEP_INTERRUPTED and the duration parameter reports the amount of
 * time remaining out of the original request.
 *
 * @note This routine always enables interrupts.
 *
 * @note The maximum sleep time of the hardware is limited on EM35x platforms
 * to 48.5 days.  Any sleep duration greater than this limit will wake up
 * briefly (e.g. 16 microseconds) to reenable another sleep cycle.
 *
 * @nostackusage
 *
 * @param duration The amount of time, expressed in quarter seconds, that the
 * micro should be placed into ::SLEEPMODE_WAKETIMER.  When the function returns,
 * this parameter provides the amount of time remaining out of the original
 * sleep time request (normally the return value will be 0).
 *
 * @param gpioWakeBitMask  A bit mask of the GPIO that are allowed to wake
 * the chip from deep sleep.  A high bit in the mask will enable waking
 * the chip if the corresponding GPIO changes state.  bit0 is PA0, bit1 is
 * PA1, bit8 is PB0, bit16 is PCO, bit23 is PC7, bits[31:24] are ignored.
 *
 * @return An EmberStatus value indicating the success or
 *  failure of the command.
 */
EmberStatus halSleepForQsWithOptions(uint32_t *duration, WakeMask gpioWakeBitMask);


/** 
 * @brief Provides access to assembly code that is used to save/restore
 * context when deep sleeping.
 */
void halInternalContextSaveRestore(uint32_t save);

/**
 * @brief Provides access to assembly code which triggers idle sleep.
 */
void halInternalIdleSleep(void);

/** @brief Puts the microcontroller to sleep in a specified mode.  This
 *  internal function performs the actual sleep operation.  This function
 *  assumes all of the wake source registers are configured properly.
 *
 * @note This routine always enables interrupts.
 *
 * @param sleepMode  A microcontroller sleep mode
 */
void halInternalSleep(SleepModes sleepMode);


/**
 * @brief Obtains the events that caused the last wake from sleep.  The
 * meaning of each bit is as follows:
 * - [31] = WakeInfoValid
 * - [30] = SleepSkipped
 * - [29] = CSYSPWRUPREQ
 * - [28] = CDBGPWRUPREQ
 * - [27] = PWRUP_WAKECORE
 * - [26] = PWRUP_SLEEPTMRWRAP
 * - [25] = PWRUP_SLEEPTMRCOMPB
 * - [24] = PWRUP_SLEEPTMRCOMPA
 * - [23:0] = corresponding GPIO activity
 *
 * WakeInfoValid means that ::halSleep (::halInternalSleep) has been called
 * at least once.  Since the power on state clears the wake event info,
 * this bit says the sleep code has been called since power on.
 *
 * SleepSkipped means that the chip never left the running state.  Sleep can
 * be skipped if any wake event occurs between going ::ATOMIC and transferring
 * control from the CPU to the power management state machine.  Sleep can
 * also be skipped if the debugger is connected (JTAG/SerialWire CSYSPWRUPREQ
 * signal is set).  The net affect of skipping sleep is the Low Voltage
 * domain never goes through a power/reset cycle.
 *
 * @return The events that caused the last wake from sleep.
 */
uint32_t halGetWakeInfo(void);




/**@} // END micro group
 */


/**@} // END micro group
 */


// the number of ticks (as returned from halCommonGetInt32uMillisecondTick)
// that represent an actual second. This can vary on different platforms.
// It must be defined by the host system.
// See bug 10232
//  #error "MILLISECOND_TICKS_PER_SECOND is not defined in micro.h!"








/** @} END micro group  */
  


// Define the address offsets for all of our MPU regions

//=============================================================================
// Define the data used to initialize the MPU. Each of the 8 MPU regions
// has a programmable size and various attributes. A region must be a power of
// two in size, and its base address must be a multiple of that size. Regions
// are divided into 8 equal-sized sub-regions that can be individually disabled.
// A region is defined by what is written to MPU_BASE and MPU_ATTR.
// MPU_BASE holds the region base address, with some low order bits ignored
// depending on the region size. If B4 is set, then B3:0 set the region number.
// The MPU_ATTR fields are:
// XN (1 bit) - set to disable instruction execution
// AP (2 bits) - selects Privilege & User access- None, Read-only or Read-Write
// TEX,S,C,B (6 bits) - configures memory type, write ordering, shareable, ...
// SRD (8 bits) - a set bit disables the corresponding sub-region
// SIZE (5 bits) - specifies the region size as a power of two
// ENABLE (1 bit) - set to enable the region, except any disabled sub-regions
//=============================================================================


// Region 0 - Flash, including main, fixed and customer info blocks: 
//            execute, normal, not shareable
// Enabled sub-regions: 08000000 - 0802FFFF
// #define FLASH_REGION_ATTR    MATTR(0, PRO_URO, MEM_NORMAL, 0xE8, SIZE_512K, 1)
/** Default configuration of MPU region init structure for onchip peripherals.*/

// Region 1 - System peripherals: no execute, non-shared device
// Enabled sub-regions: 40000000 - 40008000, 4000A000 - 4000FFFF
// #define PERIPH_REGION_ATTR   MATTR(1, PRW_URO, MEM_DEVICE, 0x10, SIZE_64K,  1)
/** Default configuration of MPU region init structure for onchip peripherals.*/


// Region 2 - User peripherals: no execute, non-shared device
// Enabled sub-regions: 4000A000 - 4000FFFF
// #define USERPER_REGION_ATTR  MATTR(1, PRW_URW, MEM_DEVICE, 0x03, SIZE_32K,  1)
/** Default configuration of MPU region init structure for onchip peripherals.*/

// Region 3 - SRAM: no execute, normal, not shareable
// Enabled sub-regions: 20000000 - 20002FFF
// #define SRAM_REGION_ATTR     MATTR(1, PRW_URW, MEM_NORMAL, 0xC0, SIZE_16K,  1)
/** Default configuration of MPU region init structure for sram memory.      */

// Region 4 - Guard region between the heap and stack
// #define GUARD_REGION_ATTR_EN    MATTR(1, PNA_UNA, MEM_NORMAL, 0x00, //                                       HEAP_GUARD_REGION_SIZE, 1)
// #define GUARD_REGION_ATTR_DIS   MATTR(1, PNA_UNA, MEM_NORMAL, 0x00, //                                       HEAP_GUARD_REGION_SIZE, 0)


// Map the regions defined above into more generic versions that are
// appropriate for mpu.c


//A simple utility macro for temporarily turning off the MPU.  Turning off
//the MPU is dangerous and should only be done in critical situations, such
//as executing from RAM and writing Flash.

void halInternalLoadMPU(MPU_RegionInit_TypeDef *mp);
void halInternalEnableMPU(void);
void halInternalDisableMPU(void);
void halInternalSetMPUGuardRegionStart(uint32_t baseAddress);

//[[
_Bool halInternalIAmAnEmulator(void);
//]]



// Define MPU regions - note that the default vector table at address 0 and
// the ARM PPB peripherals are always accessible in privileged mode.
static MPU_RegionInit_TypeDef mpuConfig[5] =
{
  { 1, 0, (0x00000000 + 0x10), mpuRegionSize256Kb, mpuRegionApPRwURo, 0, 0, 1, 1, 0xE8, 1 },
  { 0, 1, (0x40000000 + 0x11), mpuRegionSize64Kb, mpuRegionApPRwURo, 0, 0, 0, 0, 0x10, 2 },
  { 0, 2, (0x40008000 + 0x12), mpuRegionSize32Kb, mpuRegionApFullAccess, 0, 0, 0, 0, 0x03, 1 },
  { 1, 3, (0x20000000 + 0x13), mpuRegionSize32Kb, mpuRegionApFullAccess, 0, 0, 1, 1, 0xC0, 1 },
  { 0, 4, (0x20000000 + 0x14), (mpuRegionSize32b), mpuRegionNoAccess, 0, 0, 0, 0, 0x00, 1 }
};

// Load the base address and attributes of all 8 MPU regions, then enable
// the MPU. Even though interrupts should be disabled when this function is
// called, the region loading is performed in an atomic block in case they
// are not disabled. After the regions have been defined, the MPU is enabled.
// To be safe, memory barrier instructions are included to make sure that
// the new MPU setup is in effect before returning to the caller.
//
// Note that the PRIVDEFENA bit is not set in the MPU_CTRL register so the 
// default privileged memory map is not enabled. Disabling the default
// memory map enables faults on core accesses (other than vector reads) to 
// the address ranges shown below.
//
//  Address range
//  Flash (ICODE and DCODE)
//    00000000 to 07FFFFFF    no access allowed (read, write or execute)
//    08000000 to 0809FFFF    write not allowed
//    080A0000 to 1FFFFFFF    no access allowed (read, write or execute)
//  SRAM
//    20000000 to 2000FFFF    execute not allowed
//    20010000 to 3FFFFFFF    no access allowed (read, write or execute)
//  Peripheral
//    40020000 to 5FFFFFFF    no access allowed (read, write or execute)
//  External Device / External RAM
//    60000000 to DFFFFFFF    no access allowed (read, write or execute)

void halInternalEnableMPU(void)
{
  { uint8_t _emIsrState; do { _emIsrState = _disableBasePri();  } while(0); { MPU_Disable(); halInternalLoadMPU(mpuConfig); MPU_Enable((1UL << 2)); } do {  _writeBasePri(_emIsrState); } while(0); }
}

void halInternalLoadMPU(MPU_RegionInit_TypeDef *mp)
{

  uint8_t i;
  
  for (i = 0; i < 5; i++) 
  {
    MPU_ConfigureRegion(mp);
    mp++;
  }
   _executeBarrierInstructions();
}

void halInternalDisableMPU(void)
{
  MPU_Disable();
  _executeBarrierInstructions();
}

void halInternalSetMPUGuardRegionStart(uint32_t baseAddress)
{

  uint32_t enable = 0;

  // Clear the lower 5 bits of the base address to be sure that it's
  // properly aligned
  baseAddress &= 0xFFFFFFE0;

  // If the base address is below the reset info then something weird is
  // going on so just turn off the guard region
  if(baseAddress < (uint32_t)__segment_end("RESETINFO")) {
    enable = 0;
  }

  // Add in the guard region number so the MPU knows which region to configure
  baseAddress |= (0x20000000 + 0x14) & 0x0000001F;

  // Set the base address for the MPU guard region
  { uint8_t _emIsrState; do { _emIsrState = _disableBasePri();  } while(0); { mpuConfig[(0x20000000 + 0x14) & 0xF]. baseAddress = baseAddress; mpuConfig[(0x20000000 + 0x14) & 0xF]. regionEnable = enable; } do {  _writeBasePri(_emIsrState); } while(0); };
}

_Bool halInternalIAmAnEmulator(void)
{
  return 0;
}
