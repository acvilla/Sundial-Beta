/*----------------------------------------------------------------------------/
/  FatFs - FAT file system module  R0.09                  (C)ChaN, 2011
/-----------------------------------------------------------------------------/
/ FatFs module is a generic FAT file system module for small embedded systems.
/ This is a free software that opened for education, research and commercial
/ developments under license policy of following terms.
/
/  Copyright (C) 2011, ChaN, all right reserved.
/
/ * The FatFs module is a free software and there is NO WARRANTY.
/ * No restriction on use. You can use, modify and redistribute it for
/   personal, non-profit or commercial products UNDER YOUR RESPONSIBILITY.
/ * Redistributions of source code must retain the above copyright notice.
/
/-----------------------------------------------------------------------------/
/ Feb 26,'06 R0.00  Prototype.
/
/ Apr 29,'06 R0.01  First stable version.
/
/ Jun 01,'06 R0.02  Added FAT12 support.
/                   Removed unbuffered mode.
/                   Fixed a problem on small (<32M) partition.
/ Jun 10,'06 R0.02a Added a configuration option (_FS_MINIMUM).
/
/ Sep 22,'06 R0.03  Added f_rename().
/                   Changed option _FS_MINIMUM to _FS_MINIMIZE.
/ Dec 11,'06 R0.03a Improved cluster scan algorithm to write files fast.
/                   Fixed f_mkdir() creates incorrect directory on FAT32.
/
/ Feb 04,'07 R0.04  Supported multiple drive system.
/                   Changed some interfaces for multiple drive system.
/                   Changed f_mountdrv() to f_mount().
/                   Added f_mkfs().
/ Apr 01,'07 R0.04a Supported multiple partitions on a physical drive.
/                   Added a capability of extending file size to f_lseek().
/                   Added minimization level 3.
/                   Fixed an endian sensitive code in f_mkfs().
/ May 05,'07 R0.04b Added a configuration option _USE_NTFLAG.
/                   Added FSInfo support.
/                   Fixed DBCS name can result FR_INVALID_NAME.
/                   Fixed short seek (<= csize) collapses the file object.
/
/ Aug 25,'07 R0.05  Changed arguments of f_read(), f_write() and f_mkfs().
/                   Fixed f_mkfs() on FAT32 creates incorrect FSInfo.
/                   Fixed f_mkdir() on FAT32 creates incorrect directory.
/ Feb 03,'08 R0.05a Added f_truncate() and f_utime().
/                   Fixed off by one error at FAT sub-type determination.
/                   Fixed btr in f_read() can be mistruncated.
/                   Fixed cached sector is not flushed when create and close without write.
/
/ Apr 01,'08 R0.06  Added fputc(), fputs(), fprintf() and fgets().
/                   Improved performance of f_lseek() on moving to the same or following cluster.
/
/ Apr 01,'09 R0.07  Merged Tiny-FatFs as a configuration option. (_FS_TINY)
/                   Added long file name feature.
/                   Added multiple code page feature.
/                   Added re-entrancy for multitask operation.
/                   Added auto cluster size selection to f_mkfs().
/                   Added rewind option to f_readdir().
/                   Changed result code of critical errors.
/                   Renamed string functions to avoid name collision.
/ Apr 14,'09 R0.07a Separated out OS dependent code on reentrant cfg.
/                   Added multiple sector size feature.
/ Jun 21,'09 R0.07c Fixed f_unlink() can return FR_OK on error.
/                   Fixed wrong cache control in f_lseek().
/                   Added relative path feature.
/                   Added f_chdir() and f_chdrive().
/                   Added proper case conversion to extended char.
/ Nov 03,'09 R0.07e Separated out configuration options from ff.h to ffconf.h.
/                   Fixed f_unlink() fails to remove a sub-dir on _FS_RPATH.
/                   Fixed name matching error on the 13 char boundary.
/                   Added a configuration option, _LFN_UNICODE.
/                   Changed f_readdir() to return the SFN with always upper case on non-LFN cfg.
/
/ May 15,'10 R0.08  Added a memory configuration option. (_USE_LFN = 3)
/                   Added file lock feature. (_FS_SHARE)
/                   Added fast seek feature. (_USE_FASTSEEK)
/                   Changed some types on the API, XCHAR->TCHAR.
/                   Changed fname member in the FILINFO structure on Unicode cfg.
/                   String functions support UTF-8 encoding files on Unicode cfg.
/ Aug 16,'10 R0.08a Added f_getcwd(). (_FS_RPATH = 2)
/                   Added sector erase feature. (_USE_ERASE)
/                   Moved file lock semaphore table from fs object to the bss.
/                   Fixed a wrong directory entry is created on non-LFN cfg when the given name contains ';'.
/                   Fixed f_mkfs() creates wrong FAT32 volume.
/ Jan 15,'11 R0.08b Fast seek feature is also applied to f_read() and f_write().
/                   f_lseek() reports required table size on creating CLMP.
/                   Extended format syntax of f_printf function.
/                   Ignores duplicated directory separators in given path names.
/
/ Sep 06,'11 R0.09  f_mkfs() supports multiple partition to finish the multiple partition feature.
/                   Added f_fdisk(). (_MULTI_PARTITION = 2)
/---------------------------------------------------------------------------*/

/*---------------------------------------------------------------------------/
/  FatFs - FAT file system module include file  R0.09     (C)ChaN, 2011
/----------------------------------------------------------------------------/
/ FatFs module is a generic FAT file system module for small embedded systems.
/ This is a free software that opened for education, research and commercial
/ developments under license policy of following trems.
/
/  Copyright (C) 2011, ChaN, all right reserved.
/
/ * The FatFs module is a free software and there is NO WARRANTY.
/ * No restriction on use. You can use, modify and redistribute it for
/   personal, non-profit or commercial product UNDER YOUR RESPONSIBILITY.
/ * Redistributions of source code must retain the above copyright notice.
/
/----------------------------------------------------------------------------*/



/*-------------------------------------------*/
/* Integer type definitions for FatFs module */
/*-------------------------------------------*/



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


/* This struct definition must not be inside namespace std, or
   overloading will be wrong in full C++ */
  typedef struct __va_list
  {
    char  *_Ap;
  } __va_list;

  typedef __va_list __Va_list;


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

/* These types must be 16-bit, 32-bit or larger integer */
typedef int16_t 	INT;
typedef uint16_t	UINT;

/* These types must be 8-bit integer */
typedef int8_t		CHAR;
typedef uint8_t	        UCHAR;
typedef uint8_t	        BYTE;

/* These types must be 16-bit integer */
typedef int16_t		SHORT;
typedef uint16_t	USHORT;
typedef uint16_t	WORD;
typedef uint16_t	WCHAR;

/* These types must be 32-bit integer */
typedef int32_t		LONG;
typedef uint32_t	ULONG;
typedef uint32_t	DWORD;


/*---------------------------------------------------------------------------/
/  FatFs - FAT file system module configuration file  R0.09  (C)ChaN, 2011
/----------------------------------------------------------------------------/
/
/ CAUTION! Do not forget to make clean the project after any changes to
/ the configuration options.
/
/----------------------------------------------------------------------------*/


/*---------------------------------------------------------------------------/
/ Functions and Buffer Configurations
/----------------------------------------------------------------------------*/

/* When _FS_TINY is set to 1, FatFs uses the sector buffer in the file system
/  object instead of the sector buffer in the individual file object for file
/  data transfer. This reduces memory consumption 512 bytes each file object. */


/* Setting _FS_READONLY to 1 defines read only configuration. This removes
/  writing functions, f_write, f_sync, f_unlink, f_mkdir, f_chmod, f_rename,
/  f_truncate and useless f_getfree. */


/* The _FS_MINIMIZE option defines minimization level to remove some functions.
/
/   0: Full function.
/   1: f_stat, f_getfree, f_unlink, f_mkdir, f_chmod, f_truncate and f_rename
/      are removed.
/   2: f_opendir and f_readdir are removed in addition to 1.
/   3: f_lseek is removed in addition to 2. */


/* To enable string functions, set _USE_STRFUNC to 1 or 2. */


/* To enable f_mkfs function, set _USE_MKFS to 1 and set _FS_READONLY to 0 */


/* To enable f_forward function, set _USE_FORWARD to 1 and set _FS_TINY to 1. */


/* To enable fast seek feature, set _USE_FASTSEEK to 1. */



/*---------------------------------------------------------------------------/
/ Locale and Namespace Configurations
/----------------------------------------------------------------------------*/

/* The _CODE_PAGE specifies the OEM code page to be used on the target system.
/  Incorrect setting of the code page can cause a file open failure.
/
/   932  - Japanese Shift-JIS (DBCS, OEM, Windows)
/   936  - Simplified Chinese GBK (DBCS, OEM, Windows)
/   949  - Korean (DBCS, OEM, Windows)
/   950  - Traditional Chinese Big5 (DBCS, OEM, Windows)
/   1250 - Central Europe (Windows)
/   1251 - Cyrillic (Windows)
/   1252 - Latin 1 (Windows)
/   1253 - Greek (Windows)
/   1254 - Turkish (Windows)
/   1255 - Hebrew (Windows)
/   1256 - Arabic (Windows)
/   1257 - Baltic (Windows)
/   1258 - Vietnam (OEM, Windows)
/   437  - U.S. (OEM)
/   720  - Arabic (OEM)
/   737  - Greek (OEM)
/   775  - Baltic (OEM)
/   850  - Multilingual Latin 1 (OEM)
/   858  - Multilingual Latin 1 + Euro (OEM)
/   852  - Latin 2 (OEM)
/   855  - Cyrillic (OEM)
/   866  - Russian (OEM)
/   857  - Turkish (OEM)
/   862  - Hebrew (OEM)
/   874  - Thai (OEM, Windows)
/	1    - ASCII only (Valid for non LFN cfg.)
*/


/* The _USE_LFN option switches the LFN support.
/
/   0: Disable LFN feature. _MAX_LFN and _LFN_UNICODE have no effect.
/   1: Enable LFN with static working buffer on the BSS. Always NOT reentrant.
/   2: Enable LFN with dynamic working buffer on the STACK.
/   3: Enable LFN with dynamic working buffer on the HEAP.
/
/  The LFN working buffer occupies (_MAX_LFN + 1) * 2 bytes. To enable LFN,
/  Unicode handling functions ff_convert() and ff_wtoupper() must be added
/  to the project. When enable to use heap, memory control functions
/  ff_memalloc() and ff_memfree() must be added to the project. */


/* To switch the character code set on FatFs API to Unicode,
/  enable LFN feature and set _LFN_UNICODE to 1. */


/* The _FS_RPATH option configures relative path feature.
/
/   0: Disable relative path feature and remove related functions.
/   1: Enable relative path. f_chdrive() and f_chdir() are available.
/   2: f_getcwd() is available in addition to 1.
/
/  Note that output of the f_readdir fnction is affected by this option. */



/*---------------------------------------------------------------------------/
/ Physical Drive Configurations
/----------------------------------------------------------------------------*/

/* Number of volumes (logical drives) to be used. */


/* Maximum sector size to be handled.
/  Always set 512 for memory card and hard disk but a larger value may be
/  required for on-board flash memory, floppy disk and optical disk.
/  When _MAX_SS is larger than 512, it configures FatFs to variable sector size
/  and GET_SECTOR_SIZE command must be implememted to the disk_ioctl function. */


/* When set to 0, each volume is bound to the same physical drive number and
/ it can mount only first primaly partition. When it is set to 1, each volume
/ is tied to the partitions listed in VolToPart[]. */


/* To enable sector erase feature, set _USE_ERASE to 1. CTRL_ERASE_SECTOR command
/  should be added to the disk_ioctl functio. */



/*---------------------------------------------------------------------------/
/ System Configurations
/----------------------------------------------------------------------------*/

/* Set 0 first and it is always compatible with all platforms. The _WORD_ACCESS
/  option defines which access method is used to the word data on the FAT volume.
/
/   0: Byte-by-byte access.
/   1: Word access. Do not choose this unless following condition is met.
/
/  When the byte order on the memory is big-endian or address miss-aligned word
/  access results incorrect behavior, the _WORD_ACCESS must be set to 0.
/  If it is not the case, the value can also be set to 1 to improve the
/  performance and code size.
*/


/* A header file that defines sync object types on the O/S, such as
/  windows.h, ucos_ii.h and semphr.h, must be included prior to ff.h. */


/* The _FS_REENTRANT option switches the reentrancy (thread safe) of the FatFs module.
/
/   0: Disable reentrancy. _SYNC_t and _FS_TIMEOUT have no effect.
/   1: Enable reentrancy. Also user provided synchronization handlers,
/      ff_req_grant, ff_rel_grant, ff_del_syncobj and ff_cre_syncobj
/      function must be added to the project. */


/* To enable file shareing feature, set _FS_SHARE to 1 or greater. The value
   defines how many files can be opened simultaneously. */






/* Definitions of volume management */





/* Type of path name strings on FatFs API */

typedef char TCHAR;




/* File system object structure (FATFS) */

typedef struct {
	BYTE	fs_type;		/* FAT sub-type (0:Not mounted) */
	BYTE	drv;			/* Physical drive number */
	BYTE	csize;			/* Sectors per cluster (1,2,4...128) */
	BYTE	n_fats;			/* Number of FAT copies (1,2) */
	BYTE	wflag;			/* win[] dirty flag (1:must be written back) */
	BYTE	fsi_flag;		/* fsinfo dirty flag (1:must be written back) */
	WORD	id;				/* File system mount ID */
	WORD	n_rootdir;		/* Number of root directory entries (FAT12/16) */
	DWORD	last_clust;		/* Last allocated cluster */
	DWORD	free_clust;		/* Number of free clusters */
	DWORD	fsi_sector;		/* fsinfo sector (FAT32) */
	DWORD	cdir;			/* Current directory start cluster (0:root) */
	DWORD	n_fatent;		/* Number of FAT entries (= number of clusters + 2) */
	DWORD	fsize;			/* Sectors per FAT */
	DWORD	fatbase;		/* FAT start sector */
	DWORD	dirbase;		/* Root directory start sector (FAT32:Cluster#) */
	DWORD	database;		/* Data start sector */
	DWORD	winsect;		/* Current sector appearing in the win[] */
	BYTE	win[512];	/* Disk access window for Directory, FAT (and Data on tiny cfg) */
} FATFS;



/* File object structure (FIL) */

typedef struct {
	FATFS*	fs;				/* Pointer to the owner file system object */
	WORD	id;				/* Owner file system mount ID */
	BYTE	flag;			/* File status flags */
	BYTE	pad1;
	DWORD	fptr;			/* File read/write pointer (0 on file open) */
	DWORD	fsize;			/* File size */
	DWORD	sclust;			/* File start cluster (0 when fsize==0) */
	DWORD	clust;			/* Current cluster */
	DWORD	dsect;			/* Current data sector */
	DWORD	dir_sect;		/* Sector containing the directory entry */
	BYTE*	dir_ptr;		/* Ponter to the directory entry in the window */
	BYTE	buf[512];	/* File data read/write buffer */
} FIL;



/* Directory object structure (DIR) */

typedef struct {
	FATFS*	fs;				/* Pointer to the owner file system object */
	WORD	id;				/* Owner file system mount ID */
	WORD	index;			/* Current read/write index number */
	DWORD	sclust;			/* Table start cluster (0:Root dir) */
	DWORD	clust;			/* Current cluster */
	DWORD	sect;			/* Current sector */
	BYTE*	dir;			/* Pointer to the current SFN entry in the win[] */
	BYTE*	fn;				/* Pointer to the SFN (in/out) {file[8],ext[3],status[1]} */
} DIR;



/* File status structure (FILINFO) */

typedef struct {
	DWORD	fsize;			/* File size */
	WORD	fdate;			/* Last modified date */
	WORD	ftime;			/* Last modified time */
	BYTE	fattrib;		/* Attribute */
	TCHAR	fname[13];		/* Short file name (8.3 format) */
} FILINFO;



/* File function return code (FRESULT) */

typedef enum {
	FR_OK = 0,				/* (0) Succeeded */
	FR_DISK_ERR,			/* (1) A hard error occured in the low level disk I/O layer */
	FR_INT_ERR,				/* (2) Assertion failed */
	FR_NOT_READY,			/* (3) The physical drive cannot work */
	FR_NO_FILE,				/* (4) Could not find the file */
	FR_NO_PATH,				/* (5) Could not find the path */
	FR_INVALID_NAME,		/* (6) The path name format is invalid */
	FR_DENIED,				/* (7) Acces denied due to prohibited access or directory full */
	FR_EXIST,				/* (8) Acces denied due to prohibited access */
	FR_INVALID_OBJECT,		/* (9) The file/directory object is invalid */
	FR_WRITE_PROTECTED,		/* (10) The physical drive is write protected */
	FR_INVALID_DRIVE,		/* (11) The logical drive number is invalid */
	FR_NOT_ENABLED,			/* (12) The volume has no work area */
	FR_NO_FILESYSTEM,		/* (13) There is no valid FAT volume */
	FR_MKFS_ABORTED,		/* (14) The f_mkfs() aborted due to any parameter error */
	FR_TIMEOUT,				/* (15) Could not get a grant to access the volume within defined period */
	FR_LOCKED,				/* (16) The operation is rejected according to the file shareing policy */
	FR_NOT_ENOUGH_CORE,		/* (17) LFN working buffer could not be allocated */
	FR_TOO_MANY_OPEN_FILES,	/* (18) Number of open files > _FS_SHARE */
	FR_INVALID_PARAMETER	/* (19) Given parameter is invalid */
} FRESULT;



/*--------------------------------------------------------------*/
/* FatFs module application interface                           */

FRESULT f_mount (BYTE, FATFS*);						/* Mount/Unmount a logical drive */
FRESULT f_open (FIL*, const TCHAR*, BYTE);			/* Open or create a file */
FRESULT f_read (FIL*, void*, UINT, UINT*);			/* Read data from a file */
FRESULT f_lseek (FIL*, DWORD);						/* Move file pointer of a file object */
FRESULT f_close (FIL*);								/* Close an open file object */
FRESULT f_opendir (DIR*, const TCHAR*);				/* Open an existing directory */
FRESULT f_readdir (DIR*, FILINFO*);					/* Read a directory item */
FRESULT f_stat (const TCHAR*, FILINFO*);			/* Get file status */
FRESULT f_write (FIL*, const void*, UINT, UINT*);	/* Write data to a file */
FRESULT f_getfree (const TCHAR*, DWORD*, FATFS**);	/* Get number of free clusters on the drive */
FRESULT f_truncate (FIL*);							/* Truncate file */
FRESULT f_sync (FIL*);								/* Flush cached data of a writing file */
FRESULT f_unlink (const TCHAR*);					/* Delete an existing file or directory */
FRESULT	f_mkdir (const TCHAR*);						/* Create a new directory */
FRESULT f_chmod (const TCHAR*, BYTE, BYTE);			/* Change attriburte of the file/dir */
FRESULT f_utime (const TCHAR*, const FILINFO*);		/* Change timestamp of the file/dir */
FRESULT f_rename (const TCHAR*, const TCHAR*);		/* Rename/Move a file or directory */
FRESULT f_chdrive (BYTE);							/* Change current drive */
FRESULT f_chdir (const TCHAR*);						/* Change current directory */
FRESULT f_getcwd (TCHAR*, UINT);					/* Get current directory */
FRESULT f_forward (FIL*, UINT(*)(const BYTE*,UINT), UINT, UINT*);	/* Forward data to the stream */
FRESULT f_mkfs (BYTE, BYTE, UINT);					/* Create a file system on the drive */
FRESULT	f_fdisk (BYTE, const DWORD[], void*);		/* Divide a physical drive into some partitions */
int f_putc (TCHAR, FIL*);							/* Put a character to the file */
int f_puts (const TCHAR*, FIL*);					/* Put a string to the file */
int f_printf (FIL*, const TCHAR*, ...);				/* Put a formatted string to the file */
TCHAR* f_gets (TCHAR*, int, FIL*);					/* Get a string from the file */






/*--------------------------------------------------------------*/
/* Additional user defined functions                            */

/* RTC function */
DWORD get_fattime (void);

/* Unicode support functions */

/* Sync functions */




/*--------------------------------------------------------------*/
/* Flags and offset address                                     */


/* File access control and file status flags (FIL.flag) */




/* FAT sub type (FATFS.fs_type) */



/* File attribute bits for directory entry */



/* Fast seek feature */



/*--------------------------------*/
/* Multi-byte word access macros  */



/*-----------------------------------------------------------------------
/  Low level disk interface modlue include file
/-----------------------------------------------------------------------*/





/* Status of Disk Functions */
typedef BYTE	DSTATUS;

/* Results of Disk Functions */
typedef enum {
	RES_OK = 0,		/* 0: Successful */
	RES_ERROR,		/* 1: R/W Error */
	RES_WRPRT,		/* 2: Write Protected */
	RES_NOTRDY,		/* 3: Not Ready */
	RES_PARERR		/* 4: Invalid Parameter */
} DRESULT;


/*---------------------------------------*/
/* Prototypes for disk control functions. */

DSTATUS disk_initialize (BYTE);
DSTATUS disk_status (BYTE);
DRESULT disk_read (BYTE, BYTE*, DWORD, BYTE);
DRESULT disk_write (BYTE, const BYTE*, DWORD, BYTE);
DRESULT disk_ioctl (BYTE, BYTE, void*);


/* Disk Status Bits (DSTATUS) */



/* Command code for disk_ioctrl fucntion */

/* Generic command (defined for FatFs) */

/* Generic command */


/* MMC/SDC specific ioctl command */

/* ATA/CF specific ioctl command */

/* NAND specific ioctl command */

/* SD Card type definitions (CardType) */



/*--------------------------------------------------------------------------

   Module Private Definitions

---------------------------------------------------------------------------*/



/* Definitions on sector size */


/* Reentrancy related */



/* File shareing feature */


/* Misc definitions */


/* DBCS code ranges and SBCS extend char conversion table */




/* Character code support macros */






/* Name status flags */


/* FAT sub-type boundaries */
/* Note that the FAT spec by Microsoft says 4085 but Windows works with 4087! */


/* FatFs refers the members in the FAT structures as byte array instead of
/ structure member because the structure is not binary compatible between
/ different platforms */




/*------------------------------------------------------------*/
/* Module private work area                                   */
/*------------------------------------------------------------*/
/* Note that uninitialized variables with static duration are
/  zeroed/nulled at start-up. If not, the compiler or start-up
/  routine is out of ANSI-C standard.
*/

static
FATFS *FatFs[1];	/* Pointer to the file system objects (logical drives) */

static
WORD Fsid;				/* File system mount ID */

static
BYTE CurrVol;			/* Current drive */







/*--------------------------------------------------------------------------

   Module Private Functions

---------------------------------------------------------------------------*/


/*-----------------------------------------------------------------------*/
/* String functions                                                      */
/*-----------------------------------------------------------------------*/

/* Copy memory to memory */
static
void mem_cpy (void* dst, const void* src, UINT cnt) {
	BYTE *d = (BYTE*)dst;
	const BYTE *s = (const BYTE*)src;

	while (cnt--)
		*d++ = *s++;
}

/* Fill memory */
static
void mem_set (void* dst, int val, UINT cnt) {
	BYTE *d = (BYTE*)dst;

	while (cnt--)
		*d++ = (BYTE)val;
}

/* Compare memory to memory */
static
int mem_cmp (const void* dst, const void* src, UINT cnt) {
	const BYTE *d = (const BYTE *)dst, *s = (const BYTE *)src;
	int r = 0;

	while (cnt-- && (r = *d++ - *s++) == 0) ;
	return r;
}

/* Check if chr is contained in the string */
static
int chk_chr (const char* str, int chr) {
	while (*str && *str != chr) str++;
	return *str;
}



/*-----------------------------------------------------------------------*/
/* Request/Release grant to access the volume                            */
/*-----------------------------------------------------------------------*/



/*-----------------------------------------------------------------------*/
/* File shareing control functions                                       */
/*-----------------------------------------------------------------------*/



/*-----------------------------------------------------------------------*/
/* Change window offset                                                  */
/*-----------------------------------------------------------------------*/

static
FRESULT move_window (
	FATFS *fs,		/* File system object */
	DWORD sector	/* Sector number to make appearance in the fs->win[] */
)					/* Move to zero only writes back dirty window */
{
	DWORD wsect;


	wsect = fs->winsect;
	if (wsect != sector) {	/* Changed current window */
		if (fs->wflag) {	/* Write back dirty window if needed */
			if (disk_write(fs->drv, fs->win, wsect, 1) != RES_OK)
				return FR_DISK_ERR;
			fs->wflag = 0;
			if (wsect < (fs->fatbase + fs->fsize)) {	/* In FAT area */
				BYTE nf;
				for (nf = fs->n_fats; nf > 1; nf--) {	/* Reflect the change to all FAT copies */
					wsect += fs->fsize;
					disk_write(fs->drv, fs->win, wsect, 1);
				}
			}
		}
		if (sector) {
			if (disk_read(fs->drv, fs->win, sector, 1) != RES_OK)
				return FR_DISK_ERR;
			fs->winsect = sector;
		}
	}

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Clean-up cached data                                                  */
/*-----------------------------------------------------------------------*/
static
FRESULT sync (	/* FR_OK: successful, FR_DISK_ERR: failed */
	FATFS *fs	/* File system object */
)
{
	FRESULT res;


	res = move_window(fs, 0);
	if (res == FR_OK) {
		/* Update FSInfo sector if needed */
		if (fs->fs_type == 3 && fs->fsi_flag) {
			fs->winsect = 0;
			/* Create FSInfo structure */
			mem_set(fs->win, 0, 512);
			*(BYTE*)(fs->win+510)=(BYTE)(0xAA55); *((BYTE*)(fs->win+510)+1)=(BYTE)((WORD)(0xAA55)>>8);
			*(BYTE*)(fs->win+0)=(BYTE)(0x41615252); *((BYTE*)(fs->win+0)+1)=(BYTE)((WORD)(0x41615252)>>8); *((BYTE*)(fs->win+0)+2)=(BYTE)((DWORD)(0x41615252)>>16); *((BYTE*)(fs->win+0)+3)=(BYTE)((DWORD)(0x41615252)>>24);
			*(BYTE*)(fs->win+484)=(BYTE)(0x61417272); *((BYTE*)(fs->win+484)+1)=(BYTE)((WORD)(0x61417272)>>8); *((BYTE*)(fs->win+484)+2)=(BYTE)((DWORD)(0x61417272)>>16); *((BYTE*)(fs->win+484)+3)=(BYTE)((DWORD)(0x61417272)>>24);
			*(BYTE*)(fs->win+488)=(BYTE)(fs->free_clust); *((BYTE*)(fs->win+488)+1)=(BYTE)((WORD)(fs->free_clust)>>8); *((BYTE*)(fs->win+488)+2)=(BYTE)((DWORD)(fs->free_clust)>>16); *((BYTE*)(fs->win+488)+3)=(BYTE)((DWORD)(fs->free_clust)>>24);
			*(BYTE*)(fs->win+492)=(BYTE)(fs->last_clust); *((BYTE*)(fs->win+492)+1)=(BYTE)((WORD)(fs->last_clust)>>8); *((BYTE*)(fs->win+492)+2)=(BYTE)((DWORD)(fs->last_clust)>>16); *((BYTE*)(fs->win+492)+3)=(BYTE)((DWORD)(fs->last_clust)>>24);
			/* Write it into the FSInfo sector */
			disk_write(fs->drv, fs->win, fs->fsi_sector, 1);
			fs->fsi_flag = 0;
		}
		/* Make sure that no pending write process in the physical drive */
		if (disk_ioctl(fs->drv, 0, 0) != RES_OK)
			res = FR_DISK_ERR;
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Get sector# from cluster#                                             */
/*-----------------------------------------------------------------------*/


DWORD clust2sect (	/* !=0: Sector number, 0: Failed - invalid cluster# */
	FATFS *fs,		/* File system object */
	DWORD clst		/* Cluster# to be converted */
)
{
	clst -= 2;
	if (clst >= (fs->n_fatent - 2)) return 0;		/* Invalid cluster# */
	return clst * fs->csize + fs->database;
}




/*-----------------------------------------------------------------------*/
/* FAT access - Read value of a FAT entry                                */
/*-----------------------------------------------------------------------*/


DWORD get_fat (	/* 0xFFFFFFFF:Disk error, 1:Internal error, Else:Cluster status */
	FATFS *fs,	/* File system object */
	DWORD clst	/* Cluster# to get the link information */
)
{
	UINT wc, bc;
	BYTE *p;


	if (clst < 2 || clst >= fs->n_fatent)	/* Chack range */
		return 1;

	switch (fs->fs_type) {
	case 1 :
		bc = (UINT)clst; bc += bc / 2;
		if (move_window(fs, fs->fatbase + (bc / 512U))) break;
		wc = fs->win[bc % 512U]; bc++;
		if (move_window(fs, fs->fatbase + (bc / 512U))) break;
		wc |= fs->win[bc % 512U] << 8;
		return (clst & 1) ? (wc >> 4) : (wc & 0xFFF);

	case 2 :
		if (move_window(fs, fs->fatbase + (clst / (512U / 2)))) break;
		p = &fs->win[clst * 2 % 512U];
		return (WORD)(((WORD)*((BYTE*)(p)+1)<<8)|(WORD)*(BYTE*)(p));

	case 3 :
		if (move_window(fs, fs->fatbase + (clst / (512U / 4)))) break;
		p = &fs->win[clst * 4 % 512U];
		return (DWORD)(((DWORD)*((BYTE*)(p)+3)<<24)|((DWORD)*((BYTE*)(p)+2)<<16)|((WORD)*((BYTE*)(p)+1)<<8)| *(BYTE*)(p)) & 0x0FFFFFFF;
	}

	return 0xFFFFFFFF;	/* An error occurred at the disk I/O layer */
}




/*-----------------------------------------------------------------------*/
/* FAT access - Change value of a FAT entry                              */
/*-----------------------------------------------------------------------*/

FRESULT put_fat (
	FATFS *fs,	/* File system object */
	DWORD clst,	/* Cluster# to be changed in range of 2 to fs->n_fatent - 1 */
	DWORD val	/* New value to mark the cluster */
)
{
	UINT bc;
	BYTE *p;
	FRESULT res;


	if (clst < 2 || clst >= fs->n_fatent) {	/* Check range */
		res = FR_INT_ERR;

	} else {
		switch (fs->fs_type) {
		case 1 :
			bc = clst; bc += bc / 2;
			res = move_window(fs, fs->fatbase + (bc / 512U));
			if (res != FR_OK) break;
			p = &fs->win[bc % 512U];
			*p = (clst & 1) ? ((*p & 0x0F) | ((BYTE)val << 4)) : (BYTE)val;
			bc++;
			fs->wflag = 1;
			res = move_window(fs, fs->fatbase + (bc / 512U));
			if (res != FR_OK) break;
			p = &fs->win[bc % 512U];
			*p = (clst & 1) ? (BYTE)(val >> 4) : ((*p & 0xF0) | ((BYTE)(val >> 8) & 0x0F));
			break;

		case 2 :
			res = move_window(fs, fs->fatbase + (clst / (512U / 2)));
			if (res != FR_OK) break;
			p = &fs->win[clst * 2 % 512U];
			*(BYTE*)(p)=(BYTE)((WORD)val); *((BYTE*)(p)+1)=(BYTE)((WORD)((WORD)val)>>8);
			break;

		case 3 :
			res = move_window(fs, fs->fatbase + (clst / (512U / 4)));
			if (res != FR_OK) break;
			p = &fs->win[clst * 4 % 512U];
			val |= (DWORD)(((DWORD)*((BYTE*)(p)+3)<<24)|((DWORD)*((BYTE*)(p)+2)<<16)|((WORD)*((BYTE*)(p)+1)<<8)| *(BYTE*)(p)) & 0xF0000000;
			*(BYTE*)(p)=(BYTE)(val); *((BYTE*)(p)+1)=(BYTE)((WORD)(val)>>8); *((BYTE*)(p)+2)=(BYTE)((DWORD)(val)>>16); *((BYTE*)(p)+3)=(BYTE)((DWORD)(val)>>24);
			break;

		default :
			res = FR_INT_ERR;
		}
		fs->wflag = 1;
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* FAT handling - Remove a cluster chain                                 */
/*-----------------------------------------------------------------------*/
static
FRESULT remove_chain (
	FATFS *fs,			/* File system object */
	DWORD clst			/* Cluster# to remove a chain from */
)
{
	FRESULT res;
	DWORD nxt;

	if (clst < 2 || clst >= fs->n_fatent) {	/* Check range */
		res = FR_INT_ERR;

	} else {
		res = FR_OK;
		while (clst < fs->n_fatent) {			/* Not a last link? */
			nxt = get_fat(fs, clst);			/* Get cluster status */
			if (nxt == 0) break;				/* Empty cluster? */
			if (nxt == 1) { res = FR_INT_ERR; break; }	/* Internal error? */
			if (nxt == 0xFFFFFFFF) { res = FR_DISK_ERR; break; }	/* Disk error? */
			res = put_fat(fs, clst, 0);			/* Mark the cluster "empty" */
			if (res != FR_OK) break;
			if (fs->free_clust != 0xFFFFFFFF) {	/* Update FSInfo */
				fs->free_clust++;
				fs->fsi_flag = 1;
			}
			clst = nxt;	/* Next cluster */
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* FAT handling - Stretch or Create a cluster chain                      */
/*-----------------------------------------------------------------------*/
static
DWORD create_chain (	/* 0:No free cluster, 1:Internal error, 0xFFFFFFFF:Disk error, >=2:New cluster# */
	FATFS *fs,			/* File system object */
	DWORD clst			/* Cluster# to stretch. 0 means create a new chain. */
)
{
	DWORD cs, ncl, scl;
	FRESULT res;


	if (clst == 0) {		/* Create a new chain */
		scl = fs->last_clust;			/* Get suggested start point */
		if (!scl || scl >= fs->n_fatent) scl = 1;
	}
	else {					/* Stretch the current chain */
		cs = get_fat(fs, clst);			/* Check the cluster status */
		if (cs < 2) return 1;			/* It is an invalid cluster */
		if (cs < fs->n_fatent) return cs;	/* It is already followed by next cluster */
		scl = clst;
	}

	ncl = scl;				/* Start cluster */
	for (;;) {
		ncl++;							/* Next cluster */
		if (ncl >= fs->n_fatent) {		/* Wrap around */
			ncl = 2;
			if (ncl > scl) return 0;	/* No free cluster */
		}
		cs = get_fat(fs, ncl);			/* Get the cluster status */
		if (cs == 0) break;				/* Found a free cluster */
		if (cs == 0xFFFFFFFF || cs == 1)/* An error occurred */
			return cs;
		if (ncl == scl) return 0;		/* No free cluster */
	}

	res = put_fat(fs, ncl, 0x0FFFFFFF);	/* Mark the new cluster "last link" */
	if (res == FR_OK && clst != 0) {
		res = put_fat(fs, clst, ncl);	/* Link it to the previous one if needed */
	}
	if (res == FR_OK) {
		fs->last_clust = ncl;			/* Update FSINFO */
		if (fs->free_clust != 0xFFFFFFFF) {
			fs->free_clust--;
			fs->fsi_flag = 1;
		}
	} else {
		ncl = (res == FR_DISK_ERR) ? 0xFFFFFFFF : 1;
	}

	return ncl;		/* Return new cluster number or error code */
}



/*-----------------------------------------------------------------------*/
/* FAT handling - Convert offset into cluster with link map table        */
/*-----------------------------------------------------------------------*/




/*-----------------------------------------------------------------------*/
/* Directory handling - Set directory index                              */
/*-----------------------------------------------------------------------*/

static
FRESULT dir_sdi (
	DIR *dj,		/* Pointer to directory object */
	WORD idx		/* Directory index number */
)
{
	DWORD clst;
	WORD ic;


	dj->index = idx;
	clst = dj->sclust;
	if (clst == 1 || clst >= dj->fs->n_fatent)	/* Check start cluster range */
		return FR_INT_ERR;
	if (!clst && dj->fs->fs_type == 3)	/* Replace cluster# 0 with root cluster# if in FAT32 */
		clst = dj->fs->dirbase;

	if (clst == 0) {	/* Static table (root-dir in FAT12/16) */
		dj->clust = clst;
		if (idx >= dj->fs->n_rootdir)		/* Index is out of range */
			return FR_INT_ERR;
		dj->sect = dj->fs->dirbase + idx / (512U / 32);	/* Sector# */
	}
	else {				/* Dynamic table (sub-dirs or root-dir in FAT32) */
		ic = 512U / 32 * dj->fs->csize;	/* Entries per cluster */
		while (idx >= ic) {	/* Follow cluster chain */
			clst = get_fat(dj->fs, clst);				/* Get next cluster */
			if (clst == 0xFFFFFFFF) return FR_DISK_ERR;	/* Disk error */
			if (clst < 2 || clst >= dj->fs->n_fatent)	/* Reached to end of table or int error */
				return FR_INT_ERR;
			idx -= ic;
		}
		dj->clust = clst;
		dj->sect = clust2sect(dj->fs, clst) + idx / (512U / 32);	/* Sector# */
	}

	dj->dir = dj->fs->win + (idx % (512U / 32)) * 32;	/* Ptr to the entry in the sector */

	return FR_OK;	/* Seek succeeded */
}




/*-----------------------------------------------------------------------*/
/* Directory handling - Move directory index next                        */
/*-----------------------------------------------------------------------*/

static
FRESULT dir_next (	/* FR_OK:Succeeded, FR_NO_FILE:End of table, FR_DENIED:EOT and could not stretch */
	DIR *dj,		/* Pointer to directory object */
	int stretch		/* 0: Do not stretch table, 1: Stretch table if needed */
)
{
	DWORD clst;
	WORD i;


	stretch = stretch;		/* To suppress warning on read-only cfg. */
	i = dj->index + 1;
	if (!i || !dj->sect)	/* Report EOT when index has reached 65535 */
		return FR_NO_FILE;

	if (!(i % (512U / 32))) {	/* Sector changed? */
		dj->sect++;					/* Next sector */

		if (dj->clust == 0) {	/* Static table */
			if (i >= dj->fs->n_rootdir)	/* Report EOT when end of table */
				return FR_NO_FILE;
		}
		else {					/* Dynamic table */
			if (((i / (512U / 32)) & (dj->fs->csize - 1)) == 0) {	/* Cluster changed? */
				clst = get_fat(dj->fs, dj->clust);				/* Get next cluster */
				if (clst <= 1) return FR_INT_ERR;
				if (clst == 0xFFFFFFFF) return FR_DISK_ERR;
				if (clst >= dj->fs->n_fatent) {					/* When it reached end of dynamic table */
					BYTE c;
					if (!stretch) return FR_NO_FILE;			/* When do not stretch, report EOT */
					clst = create_chain(dj->fs, dj->clust);		/* Stretch cluster chain */
					if (clst == 0) return FR_DENIED;			/* No free cluster */
					if (clst == 1) return FR_INT_ERR;
					if (clst == 0xFFFFFFFF) return FR_DISK_ERR;
					/* Clean-up stretched table */
					if (move_window(dj->fs, 0)) return FR_DISK_ERR;	/* Flush active window */
					mem_set(dj->fs->win, 0, 512U);			/* Clear window buffer */
					dj->fs->winsect = clust2sect(dj->fs, clst);	/* Cluster start sector */
					for (c = 0; c < dj->fs->csize; c++) {		/* Fill the new cluster with 0 */
						dj->fs->wflag = 1;
						if (move_window(dj->fs, 0)) return FR_DISK_ERR;
						dj->fs->winsect++;
					}
					dj->fs->winsect -= c;						/* Rewind window address */
				}
				dj->clust = clst;				/* Initialize data for new cluster */
				dj->sect = clust2sect(dj->fs, clst);
			}
		}
	}

	dj->index = i;
	dj->dir = dj->fs->win + (i % (512U / 32)) * 32;

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* LFN handling - Test/Pick/Fit an LFN segment from/to directory entry   */
/*-----------------------------------------------------------------------*/



/*-----------------------------------------------------------------------*/
/* Create numbered name                                                  */
/*-----------------------------------------------------------------------*/




/*-----------------------------------------------------------------------*/
/* Calculate sum of an SFN                                               */
/*-----------------------------------------------------------------------*/




/*-----------------------------------------------------------------------*/
/* Directory handling - Find an object in the directory                  */
/*-----------------------------------------------------------------------*/

static
FRESULT dir_find (
	DIR *dj			/* Pointer to the directory object linked to the file name */
)
{
	FRESULT res;
	BYTE c, *dir;

	res = dir_sdi(dj, 0);			/* Rewind directory object */
	if (res != FR_OK) return res;

	do {
		res = move_window(dj->fs, dj->sect);
		if (res != FR_OK) break;
		dir = dj->dir;					/* Ptr to the directory entry of current index */
		c = dir[0];
		if (c == 0) { res = FR_NO_FILE; break; }	/* Reached to end of table */
		if (!(dir[11] & 0x08) && !mem_cmp(dir, dj->fn, 11)) /* Is it a valid entry? */
			break;
		res = dir_next(dj, 0);		/* Next entry */
	} while (res == FR_OK);

	return res;
}




/*-----------------------------------------------------------------------*/
/* Read an object from the directory                                     */
/*-----------------------------------------------------------------------*/
static
FRESULT dir_read (
	DIR *dj			/* Pointer to the directory object that pointing the entry to be read */
)
{
	FRESULT res;
	BYTE c, *dir;

	res = FR_NO_FILE;
	while (dj->sect) {
		res = move_window(dj->fs, dj->sect);
		if (res != FR_OK) break;
		dir = dj->dir;					/* Ptr to the directory entry of current index */
		c = dir[0];
		if (c == 0) { res = FR_NO_FILE; break; }	/* Reached to end of table */
		if (c != 0xE5 && (1 || c != '.') && !(dir[11] & 0x08))	/* Is it a valid entry? */
			break;
		res = dir_next(dj, 0);				/* Next entry */
		if (res != FR_OK) break;
	}

	if (res != FR_OK) dj->sect = 0;

	return res;
}



/*-----------------------------------------------------------------------*/
/* Register an object to the directory                                   */
/*-----------------------------------------------------------------------*/
static
FRESULT dir_register (	/* FR_OK:Successful, FR_DENIED:No free entry or too many SFN collision, FR_DISK_ERR:Disk error */
	DIR *dj				/* Target directory with object name to be created */
)
{
	FRESULT res;
	BYTE c, *dir;
	res = dir_sdi(dj, 0);
	if (res == FR_OK) {
		do {	/* Find a blank entry for the SFN */
			res = move_window(dj->fs, dj->sect);
			if (res != FR_OK) break;
			c = *dj->dir;
			if (c == 0xE5 || c == 0) break;	/* Is it a blank entry? */
			res = dir_next(dj, 1);			/* Next entry with table stretch */
		} while (res == FR_OK);
	}

	if (res == FR_OK) {		/* Initialize the SFN entry */
		res = move_window(dj->fs, dj->sect);
		if (res == FR_OK) {
			dir = dj->dir;
			mem_set(dir, 0, 32);	/* Clean the entry */
			mem_cpy(dir, dj->fn, 11);	/* Put SFN */
			dj->fs->wflag = 1;
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Remove an object from the directory                                   */
/*-----------------------------------------------------------------------*/
static
FRESULT dir_remove (	/* FR_OK: Successful, FR_DISK_ERR: A disk error */
	DIR *dj				/* Directory object pointing the entry to be removed */
)
{
	FRESULT res;
	res = dir_sdi(dj, dj->index);
	if (res == FR_OK) {
		res = move_window(dj->fs, dj->sect);
		if (res == FR_OK) {
			*dj->dir = 0xE5;			/* Mark the entry "deleted" */
			dj->fs->wflag = 1;
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Pick a segment and create the object name in directory form           */
/*-----------------------------------------------------------------------*/

static
FRESULT create_name (
	DIR *dj,			/* Pointer to the directory object */
	const TCHAR **path	/* Pointer to pointer to the segment in the path string */
)
{

	BYTE b, c, d, *sfn;
	UINT ni, si, i;
	const char *p;

	/* Create file name in directory form */
	for (p = *path; *p == '/' || *p == '\\'; p++) ;	/* Strip duplicated separator */
	sfn = dj->fn;
	mem_set(sfn, ' ', 11);
	si = i = b = 0; ni = 8;
	if (p[si] == '.') { /* Is this a dot entry? */
		for (;;) {
			c = (BYTE)p[si++];
			if (c != '.' || si >= 3) break;
			sfn[i++] = c;
		}
		if (c != '/' && c != '\\' && c > ' ') return FR_INVALID_NAME;
		*path = &p[si];									/* Return pointer to the next segment */
		sfn[11] = (c <= ' ') ? 0x04 | 0x20 : 0x20;	/* Set last segment flag if end of path */
		return FR_OK;
	}
	for (;;) {
		c = (BYTE)p[si++];
		if (c <= ' ' || c == '/' || c == '\\') break;	/* Break on end of segment */
		if (c == '.' || i >= ni) {
			if (ni != 8 || c != '.') return FR_INVALID_NAME;
			i = 8; ni = 11;
			b <<= 2; continue;
		}
		if (c >= 0x80) {				/* Extended char? */
			b |= 3;						/* Eliminate NT flag */
		}
		if ((((BYTE)(c) >= 0x81 && (BYTE)(c) <= 0x9F) || ((BYTE)(c) >= 0xE0 && (BYTE)(c) <= 0xFC))) {				/* Check if it is a DBC 1st byte (always false on SBCS cfg) */
			d = (BYTE)p[si++];			/* Get 2nd byte */
			if (!(((BYTE)(d) >= 0x40 && (BYTE)(d) <= 0x7E) || ((BYTE)(d) >= 0x80 && (BYTE)(d) <= 0xFC)) || i >= ni - 1)	/* Reject invalid DBC */
				return FR_INVALID_NAME;
			sfn[i++] = c;
			sfn[i++] = d;
		} else {						/* Single byte code */
			if (chk_chr("\"*+,:;<=>\?[]|\x7F", c))	/* Reject illegal chrs for SFN */
				return FR_INVALID_NAME;
			if ((((c)>= 'A')&&((c)<= 'Z'))) {			/* ASCII large capital? */
				b |= 2;
			} else {
				if ((((c)>= 'a')&&((c)<= 'z'))) {		/* ASCII small capital? */
					b |= 1; c -= 0x20;
				}
			}
			sfn[i++] = c;
		}
	}
	*path = &p[si];						/* Return pointer to the next segment */
	c = (c <= ' ') ? 0x04 : 0;		/* Set last segment flag if end of path */

	if (!i) return FR_INVALID_NAME;		/* Reject nul string */
	if (sfn[0] == 0xE5) sfn[0] = 0x05;	/* When first char collides with DDE, replace it with 0x05 */

	if (ni == 8) b <<= 2;
	if ((b & 0x03) == 0x01) c |= 0x10;	/* NT flag (Name extension has only small capital) */
	if ((b & 0x0C) == 0x04) c |= 0x08;	/* NT flag (Name body has only small capital) */

	sfn[11] = c;		/* Store NT flag, File name is created */

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Get file information from directory entry                             */
/*-----------------------------------------------------------------------*/
static
void get_fileinfo (		/* No return code */
	DIR *dj,			/* Pointer to the directory object */
	FILINFO *fno	 	/* Pointer to the file information to be filled */
)
{
	UINT i;
	BYTE nt, *dir;
	TCHAR *p, c;


	p = fno->fname;
	if (dj->sect) {
		dir = dj->dir;
		nt = dir[12];		/* NT flag */
		for (i = 0; i < 8; i++) {	/* Copy name body */
			c = dir[i];
			if (c == ' ') break;
			if (c == 0x05) c = (TCHAR)0xE5;
			if (0 && (nt & 0x08) && (((c)>= 'A')&&((c)<= 'Z'))) c += 0x20;
			*p++ = c;
		}
		if (dir[8] != ' ') {		/* Copy name extension */
			*p++ = '.';
			for (i = 8; i < 11; i++) {
				c = dir[i];
				if (c == ' ') break;
				if (0 && (nt & 0x10) && (((c)>= 'A')&&((c)<= 'Z'))) c += 0x20;
				*p++ = c;
			}
		}
		fno->fattrib = dir[11];				/* Attribute */
		fno->fsize = (DWORD)(((DWORD)*((BYTE*)(dir+28)+3)<<24)|((DWORD)*((BYTE*)(dir+28)+2)<<16)|((WORD)*((BYTE*)(dir+28)+1)<<8)| *(BYTE*)(dir+28));	/* Size */
		fno->fdate = (WORD)(((WORD)*((BYTE*)(dir+24)+1)<<8)|(WORD)*(BYTE*)(dir+24));		/* Date */
		fno->ftime = (WORD)(((WORD)*((BYTE*)(dir+22)+1)<<8)|(WORD)*(BYTE*)(dir+22));		/* Time */
	}
	*p = 0;		/* Terminate SFN str by a \0 */

}




/*-----------------------------------------------------------------------*/
/* Follow a file path                                                    */
/*-----------------------------------------------------------------------*/

static
FRESULT follow_path (	/* FR_OK(0): successful, !=0: error code */
	DIR *dj,			/* Directory object to return last directory and found object */
	const TCHAR *path	/* Full-path string to find a file or directory */
)
{
	FRESULT res;
	BYTE *dir, ns;


	if (*path == '/' || *path == '\\') { /* There is a heading separator */
		path++;	dj->sclust = 0;		/* Strip it and start from the root dir */
	} else {							/* No heading separator */
		dj->sclust = dj->fs->cdir;	/* Start from the current dir */
	}

	if ((UINT)*path < ' ') {			/* Nul path means the start directory itself */
		res = dir_sdi(dj, 0);
		dj->dir = 0;

	} else {							/* Follow path */
		for (;;) {
			res = create_name(dj, &path);	/* Get a segment */
			if (res != FR_OK) break;
			res = dir_find(dj);				/* Find it */
			ns = *(dj->fn+11);
			if (res != FR_OK) {				/* Failed to find the object */
				if (res != FR_NO_FILE) break;	/* Abort if any hard error occured */
				/* Object not found */
				if (1 && (ns & 0x20)) {	/* If dot entry is not exit */
					dj->sclust = 0; dj->dir = 0;	/* It is the root dir */
					res = FR_OK;
					if (!(ns & 0x04)) continue;
				} else {							/* Could not find the object */
					if (!(ns & 0x04)) res = FR_NO_PATH;
				}
				break;
			}
			if (ns & 0x04) break;			/* Last segment match. Function completed. */
			dir = dj->dir;						/* There is next segment. Follow the sub directory */
			if (!(dir[11] & 0x10)) {	/* Cannot follow because it is a file */
				res = FR_NO_PATH; break;
			}
			dj->sclust = (((DWORD)(WORD)(((WORD)*((BYTE*)(dir+20)+1)<<8)|(WORD)*(BYTE*)(dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dir+26)+1)<<8)|(WORD)*(BYTE*)(dir+26)));
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Load a sector and check if it is an FAT Volume Boot Record            */
/*-----------------------------------------------------------------------*/

static
BYTE check_fs (	/* 0:FAT-VBR, 1:Valid BR but not FAT, 2:Not a BR, 3:Disk error */
	FATFS *fs,	/* File system object */
	DWORD sect	/* Sector# (lba) to check if it is an FAT boot record or not */
)
{
	if (disk_read(fs->drv, fs->win, sect, 1) != RES_OK)	/* Load boot record */
		return 3;
	if ((WORD)(((WORD)*((BYTE*)(&fs->win[510])+1)<<8)|(WORD)*(BYTE*)(&fs->win[510])) != 0xAA55)		/* Check record signature (always placed at offset 510 even if the sector size is >512) */
		return 2;

	if (((DWORD)(((DWORD)*((BYTE*)(&fs->win[54])+3)<<24)|((DWORD)*((BYTE*)(&fs->win[54])+2)<<16)|((WORD)*((BYTE*)(&fs->win[54])+1)<<8)| *(BYTE*)(&fs->win[54])) & 0xFFFFFF) == 0x544146)	/* Check "FAT" string */
		return 0;
	if (((DWORD)(((DWORD)*((BYTE*)(&fs->win[82])+3)<<24)|((DWORD)*((BYTE*)(&fs->win[82])+2)<<16)|((WORD)*((BYTE*)(&fs->win[82])+1)<<8)| *(BYTE*)(&fs->win[82])) & 0xFFFFFF) == 0x544146)
		return 0;

	return 1;
}




/*-----------------------------------------------------------------------*/
/* Check if the file system object is valid or not                       */
/*-----------------------------------------------------------------------*/

static
FRESULT chk_mounted (	/* FR_OK(0): successful, !=0: any error occurred */
	const TCHAR **path,	/* Pointer to pointer to the path name (drive number) */
	FATFS **rfs,		/* Pointer to pointer to the found file system object */
	BYTE chk_wp			/* !=0: Check media write protection for write access */
)
{
	BYTE fmt, b, pi, *tbl;
	UINT vol;
	DSTATUS stat;
	DWORD bsect, fasize, tsect, sysect, nclst, szbfat;
	WORD nrsv;
	const TCHAR *p = *path;
	FATFS *fs;

	/* Get logical drive number from the path name */
	vol = p[0] - '0';					/* Is there a drive number? */
	if (vol <= 9 && p[1] == ':') {		/* Found a drive number, get and strip it */
		p += 2; *path = p;				/* Return pointer to the path name */
	} else {							/* No drive number is given */
		vol = CurrVol;					/* Use current drive */
	}

	/* Check if the file system object is valid or not */
	if (vol >= 1) 				/* Is the drive number valid? */
		return FR_INVALID_DRIVE;
	*rfs = fs = FatFs[vol];				/* Return pointer to the corresponding file system object */
	if (!fs) return FR_NOT_ENABLED;		/* Is the file system object available? */

	;						/* Lock file system */

	if (fs->fs_type) {					/* If the logical drive has been mounted */
		stat = disk_status(fs->drv);
		if (!(stat & 0x01)) {		/* and the physical drive is kept initialized (has not been changed), */
			if (!0 && chk_wp && (stat & 0x04))	/* Check write protection if needed */
				return FR_WRITE_PROTECTED;
			return FR_OK;				/* The file system object is valid */
		}
	}

	/* The file system object is not valid. */
	/* Following code attempts to mount the volume. (analyze BPB and initialize the fs object) */

	fs->fs_type = 0;					/* Clear the file system object */
	fs->drv = (vol);				/* Bind the logical drive and a physical drive */
	stat = disk_initialize(fs->drv);	/* Initialize low level disk I/O layer */
	if (stat & 0x01)				/* Check if the initialization succeeded */
		return FR_NOT_READY;			/* Failed to initialize due to no media or hard error */
	if (!0 && chk_wp && (stat & 0x04))	/* Check disk write protection if needed */
		return FR_WRITE_PROTECTED;
	/* Search FAT partition on the drive. Supports only generic partitionings, FDISK and SFD. */
	fmt = check_fs(fs, bsect = 0);		/* Load sector 0 and check if it is an FAT-VBR (in SFD) */
	if (0 && !fmt) fmt = 1;	/* Force non-SFD if the volume is forced partition */
	if (fmt == 1) {						/* Not an FAT-VBR, the physical drive can be partitioned */
		/* Check the partition listed in the partition table */
		pi = 0;
		if (pi) pi--;
		tbl = &fs->win[446 + pi * 16];/* Partition table */
		if (tbl[4]) {						/* Is the partition existing? */
			bsect = (DWORD)(((DWORD)*((BYTE*)(&tbl[8])+3)<<24)|((DWORD)*((BYTE*)(&tbl[8])+2)<<16)|((WORD)*((BYTE*)(&tbl[8])+1)<<8)| *(BYTE*)(&tbl[8]));		/* Partition offset in LBA */
			fmt = check_fs(fs, bsect);		/* Check the partition */
		}
	}
	if (fmt == 3) return FR_DISK_ERR;
	if (fmt) return FR_NO_FILESYSTEM;		/* No FAT volume is found */

	/* An FAT volume is found. Following code initializes the file system object */

	if ((WORD)(((WORD)*((BYTE*)(fs->win+11)+1)<<8)|(WORD)*(BYTE*)(fs->win+11)) != 512U)		/* (BPB_BytsPerSec must be equal to the physical sector size) */
		return FR_NO_FILESYSTEM;

	fasize = (WORD)(((WORD)*((BYTE*)(fs->win+22)+1)<<8)|(WORD)*(BYTE*)(fs->win+22));				/* Number of sectors per FAT */
	if (!fasize) fasize = (DWORD)(((DWORD)*((BYTE*)(fs->win+36)+3)<<24)|((DWORD)*((BYTE*)(fs->win+36)+2)<<16)|((WORD)*((BYTE*)(fs->win+36)+1)<<8)| *(BYTE*)(fs->win+36));
	fs->fsize = fasize;

	fs->n_fats = b = fs->win[16];				/* Number of FAT copies */
	if (b != 1 && b != 2) return FR_NO_FILESYSTEM;		/* (Must be 1 or 2) */
	fasize *= b;										/* Number of sectors for FAT area */

	fs->csize = b = fs->win[13];			/* Number of sectors per cluster */
	if (!b || (b & (b - 1))) return FR_NO_FILESYSTEM;	/* (Must be power of 2) */

	fs->n_rootdir = (WORD)(((WORD)*((BYTE*)(fs->win+17)+1)<<8)|(WORD)*(BYTE*)(fs->win+17));	/* Number of root directory entries */
	if (fs->n_rootdir % (512U / 32)) return FR_NO_FILESYSTEM;	/* (BPB_RootEntCnt must be sector aligned) */

	tsect = (WORD)(((WORD)*((BYTE*)(fs->win+19)+1)<<8)|(WORD)*(BYTE*)(fs->win+19));				/* Number of sectors on the volume */
	if (!tsect) tsect = (DWORD)(((DWORD)*((BYTE*)(fs->win+32)+3)<<24)|((DWORD)*((BYTE*)(fs->win+32)+2)<<16)|((WORD)*((BYTE*)(fs->win+32)+1)<<8)| *(BYTE*)(fs->win+32));

	nrsv = (WORD)(((WORD)*((BYTE*)(fs->win+14)+1)<<8)|(WORD)*(BYTE*)(fs->win+14));				/* Number of reserved sectors */
	if (!nrsv) return FR_NO_FILESYSTEM;					/* (BPB_RsvdSecCnt must not be 0) */

	/* Determine the FAT sub type */
	sysect = nrsv + fasize + fs->n_rootdir / (512U / 32);	/* RSV+FAT+DIR */
	if (tsect < sysect) return FR_NO_FILESYSTEM;		/* (Invalid volume size) */
	nclst = (tsect - sysect) / fs->csize;				/* Number of clusters */
	if (!nclst) return FR_NO_FILESYSTEM;				/* (Invalid volume size) */
	fmt = 1;
	if (nclst >= 4086) fmt = 2;
	if (nclst >= 65526) fmt = 3;

	/* Boundaries and Limits */
	fs->n_fatent = nclst + 2;							/* Number of FAT entries */
	fs->database = bsect + sysect;						/* Data start sector */
	fs->fatbase = bsect + nrsv; 						/* FAT start sector */
	if (fmt == 3) {
		if (fs->n_rootdir) return FR_NO_FILESYSTEM;		/* (BPB_RootEntCnt must be 0) */
		fs->dirbase = (DWORD)(((DWORD)*((BYTE*)(fs->win+44)+3)<<24)|((DWORD)*((BYTE*)(fs->win+44)+2)<<16)|((WORD)*((BYTE*)(fs->win+44)+1)<<8)| *(BYTE*)(fs->win+44));	/* Root directory start cluster */
		szbfat = fs->n_fatent * 4;						/* (Required FAT size) */
	} else {
		if (!fs->n_rootdir)	return FR_NO_FILESYSTEM;	/* (BPB_RootEntCnt must not be 0) */
		fs->dirbase = fs->fatbase + fasize;				/* Root directory start sector */
		szbfat = (fmt == 2) ?					/* (Required FAT size) */
			fs->n_fatent * 2 : fs->n_fatent * 3 / 2 + (fs->n_fatent & 1);
	}
	if (fs->fsize < (szbfat + (512U - 1)) / 512U)	/* (BPB_FATSz must not be less than required) */
		return FR_NO_FILESYSTEM;

	/* Initialize cluster allocation information */
	fs->free_clust = 0xFFFFFFFF;
	fs->last_clust = 0;

	/* Get fsinfo if available */
	if (fmt == 3) {
	 	fs->fsi_flag = 0;
		fs->fsi_sector = bsect + (WORD)(((WORD)*((BYTE*)(fs->win+48)+1)<<8)|(WORD)*(BYTE*)(fs->win+48));
		if (disk_read(fs->drv, fs->win, fs->fsi_sector, 1) == RES_OK &&
			(WORD)(((WORD)*((BYTE*)(fs->win+510)+1)<<8)|(WORD)*(BYTE*)(fs->win+510)) == 0xAA55 &&
			(DWORD)(((DWORD)*((BYTE*)(fs->win+0)+3)<<24)|((DWORD)*((BYTE*)(fs->win+0)+2)<<16)|((WORD)*((BYTE*)(fs->win+0)+1)<<8)| *(BYTE*)(fs->win+0)) == 0x41615252 &&
			(DWORD)(((DWORD)*((BYTE*)(fs->win+484)+3)<<24)|((DWORD)*((BYTE*)(fs->win+484)+2)<<16)|((WORD)*((BYTE*)(fs->win+484)+1)<<8)| *(BYTE*)(fs->win+484)) == 0x61417272) {
				fs->last_clust = (DWORD)(((DWORD)*((BYTE*)(fs->win+492)+3)<<24)|((DWORD)*((BYTE*)(fs->win+492)+2)<<16)|((WORD)*((BYTE*)(fs->win+492)+1)<<8)| *(BYTE*)(fs->win+492));
				fs->free_clust = (DWORD)(((DWORD)*((BYTE*)(fs->win+488)+3)<<24)|((DWORD)*((BYTE*)(fs->win+488)+2)<<16)|((WORD)*((BYTE*)(fs->win+488)+1)<<8)| *(BYTE*)(fs->win+488));
		}
	}
	fs->fs_type = fmt;		/* FAT sub-type */
	fs->id = ++Fsid;		/* File system mount ID */
	fs->winsect = 0;		/* Invalidate sector cache */
	fs->wflag = 0;
	fs->cdir = 0;			/* Current directory (root dir) */

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Check if the file/dir object is valid or not                          */
/*-----------------------------------------------------------------------*/

static
FRESULT validate (	/* FR_OK(0): The object is valid, !=0: Invalid */
	FATFS *fs,		/* Pointer to the file system object */
	WORD id			/* Member id of the target object to be checked */
)
{
	if (!fs || !fs->fs_type || fs->id != id)
		return FR_INVALID_OBJECT;

	;		/* Lock file system */

	if (disk_status(fs->drv) & 0x01)
		return FR_NOT_READY;

	return FR_OK;
}




/*--------------------------------------------------------------------------

   Public Functions

--------------------------------------------------------------------------*/

DWORD get_fattime(void)
{
	  /*RTC must be initialized before this function is called*/

	DWORD time = RTCDRV_GetWallClock(); //returns an unsigned 32 bit integer
	
         return time;

}

/*-----------------------------------------------------------------------*/
/* Mount/Unmount a Logical Drive                                         */
/*-----------------------------------------------------------------------*/

FRESULT f_mount (
	BYTE vol,		/* Logical drive number to be mounted/unmounted */
	FATFS *fs		/* Pointer to new file system object (NULL for unmount)*/
)
{
	FATFS *rfs;


	if (vol >= 1)		/* Check if the drive number is valid */
		return FR_INVALID_DRIVE;
	rfs = FatFs[vol];			/* Get current fs object */

	if (rfs) {
		rfs->fs_type = 0;		/* Clear old fs object */
	}

	if (fs) {
		fs->fs_type = 0;		/* Clear new fs object */
	}
	else /* Unmount, Added by Energy Micro AS. */
	{
	  disk_ioctl(fs->drv, 8, (void*)0);
	}
	FatFs[vol] = fs;			/* Register new fs object */

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Open or Create a File                                                 */
/*-----------------------------------------------------------------------*/

FRESULT f_open (
	FIL *fp,			/* Pointer to the blank file object */
	const TCHAR *path,	/* Pointer to the file name */
	BYTE mode			/* Access mode and file open mode flags */
)
{
	FRESULT res;
	DIR dj;
	BYTE *dir;
	BYTE sfn[12];


	fp->fs = 0;			/* Clear file object */

	mode &= 0x01 | 0x02 | 0x08 | 0x10 | 0x04;
	res = chk_mounted(&path, &dj.fs, (BYTE)(mode & ~0x01));
	(dj). fn = sfn;
	if (res == FR_OK)
		res = follow_path(&dj, path);	/* Follow the file path */
	dir = dj.dir;

	if (res == FR_OK) {
		if (!dir)	/* Current dir itself */
			res = FR_INVALID_NAME;
	}
	/* Create or Open a file */
	if (mode & (0x08 | 0x10 | 0x04)) {
		DWORD dw, cl;

		if (res != FR_OK) {					/* No file, create new */
			if (res == FR_NO_FILE)			/* There is no file to open, create a new entry */
				res = dir_register(&dj);
			mode |= 0x08;		/* File is created */
			dir = dj.dir;					/* New entry */
		}
		else {								/* Any object is already existing */
			if (dir[11] & (0x01 | 0x10)) {	/* Cannot overwrite it (R/O or DIR) */
				res = FR_DENIED;
			} else {
				if (mode & 0x04)	/* Cannot create as new file */
					res = FR_EXIST;
			}
		}
		if (res == FR_OK && (mode & 0x08)) {	/* Truncate it if overwrite mode */
			dw = get_fattime();					/* Created time */
			*(BYTE*)(dir+14)=(BYTE)(dw); *((BYTE*)(dir+14)+1)=(BYTE)((WORD)(dw)>>8); *((BYTE*)(dir+14)+2)=(BYTE)((DWORD)(dw)>>16); *((BYTE*)(dir+14)+3)=(BYTE)((DWORD)(dw)>>24);
			dir[11] = 0;					/* Reset attribute */
			*(BYTE*)(dir+28)=(BYTE)(0); *((BYTE*)(dir+28)+1)=(BYTE)((WORD)(0)>>8); *((BYTE*)(dir+28)+2)=(BYTE)((DWORD)(0)>>16); *((BYTE*)(dir+28)+3)=(BYTE)((DWORD)(0)>>24);		/* size = 0 */
			cl = (((DWORD)(WORD)(((WORD)*((BYTE*)(dir+20)+1)<<8)|(WORD)*(BYTE*)(dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dir+26)+1)<<8)|(WORD)*(BYTE*)(dir+26)));					/* Get start cluster */
			{*(BYTE*)(dir+26)=(BYTE)(0); *((BYTE*)(dir+26)+1)=(BYTE)((WORD)(0)>>8); *(BYTE*)(dir+20)=(BYTE)((DWORD)0>>16); *((BYTE*)(dir+20)+1)=(BYTE)((WORD)((DWORD)0>>16)>>8);};					/* cluster = 0 */
			dj.fs->wflag = 1;
			if (cl) {							/* Remove the cluster chain if exist */
				dw = dj.fs->winsect;
				res = remove_chain(dj.fs, cl);
				if (res == FR_OK) {
					dj.fs->last_clust = cl - 1;	/* Reuse the cluster hole */
					res = move_window(dj.fs, dw);
				}
			}
		}
	}
	else {	/* Open an existing file */
		if (res == FR_OK) {						/* Follow succeeded */
			if (dir[11] & 0x10) {		/* It is a directory */
				res = FR_NO_FILE;
			} else {
				if ((mode & 0x02) && (dir[11] & 0x01)) /* R/O violation */
					res = FR_DENIED;
			}
		}
	}
	if (res == FR_OK) {
		if (mode & 0x08)			/* Set file change flag if created or overwritten */
			mode |= 0x20;
		fp->dir_sect = dj.fs->winsect;			/* Pointer to the directory entry */
		fp->dir_ptr = dir;
	}

	;

	if (res == FR_OK) {
		fp->flag = mode;					/* File access mode */
		fp->sclust = (((DWORD)(WORD)(((WORD)*((BYTE*)(dir+20)+1)<<8)|(WORD)*(BYTE*)(dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dir+26)+1)<<8)|(WORD)*(BYTE*)(dir+26)));			/* File start cluster */
		fp->fsize = (DWORD)(((DWORD)*((BYTE*)(dir+28)+3)<<24)|((DWORD)*((BYTE*)(dir+28)+2)<<16)|((WORD)*((BYTE*)(dir+28)+1)<<8)| *(BYTE*)(dir+28));	/* File size */
		fp->fptr = 0;						/* File pointer */
		fp->dsect = 0;
		fp->fs = dj.fs; fp->id = dj.fs->id;	/* Validate file object */
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Read File                                                             */
/*-----------------------------------------------------------------------*/

FRESULT f_read (
	FIL *fp, 		/* Pointer to the file object */
	void *buff,		/* Pointer to data buffer */
	UINT btr,		/* Number of bytes to read */
	UINT *br		/* Pointer to number of bytes read */
)
{
	FRESULT res;
	DWORD clst, sect, remain;
	UINT rcnt, cc;
	BYTE csect, *rbuff = buff;


	*br = 0;	/* Initialize byte counter */

	res = validate(fp->fs, fp->id);				/* Check validity */
	if (res != FR_OK) return res;
	if (fp->flag & 0x80)					/* Aborted file? */
		return FR_INT_ERR;
	if (!(fp->flag & 0x01)) 					/* Check access mode */
		return FR_DENIED;
	remain = fp->fsize - fp->fptr;
	if (btr > remain) btr = (UINT)remain;		/* Truncate btr by remaining bytes */

	for ( ;  btr;								/* Repeat until all data read */
		rbuff += rcnt, fp->fptr += rcnt, *br += rcnt, btr -= rcnt) {
		if ((fp->fptr % 512U) == 0) {		/* On the sector boundary? */
			csect = (BYTE)(fp->fptr / 512U & (fp->fs->csize - 1));	/* Sector offset in the cluster */
			if (!csect) {						/* On the cluster boundary? */
				if (fp->fptr == 0) {			/* On the top of the file? */
					clst = fp->sclust;			/* Follow from the origin */
				} else {						/* Middle or end of the file */
						clst = get_fat(fp->fs, fp->clust);	/* Follow cluster chain on the FAT */
				}
				if (clst < 2) { fp->flag |= 0x80; return FR_INT_ERR; };
				if (clst == 0xFFFFFFFF) { fp->flag |= 0x80; return FR_DISK_ERR; };
				fp->clust = clst;				/* Update current cluster */
			}
			sect = clust2sect(fp->fs, fp->clust);	/* Get current sector */
			if (!sect) { fp->flag |= 0x80; return FR_INT_ERR; };
			sect += csect;
			cc = btr / 512U;				/* When remaining bytes >= sector size, */
			if (cc) {							/* Read maximum contiguous sectors directly */
				if (csect + cc > fp->fs->csize)	/* Clip at cluster boundary */
					cc = fp->fs->csize - csect;
				if (disk_read(fp->fs->drv, rbuff, sect, (BYTE)cc) != RES_OK)
					{ fp->flag |= 0x80; return FR_DISK_ERR; };
				if ((fp->flag & 0x40) && fp->dsect - sect < cc)
					mem_cpy(rbuff + ((fp->dsect - sect) * 512U), fp->buf, 512U);
				rcnt = 512U * cc;			/* Number of bytes transferred */
				continue;
			}
			if (fp->dsect != sect) {			/* Load data sector if not in cache */
				if (fp->flag & 0x40) {		/* Write-back dirty sector cache */
					if (disk_write(fp->fs->drv, fp->buf, fp->dsect, 1) != RES_OK)
						{ fp->flag |= 0x80; return FR_DISK_ERR; };
					fp->flag &= ~0x40;
				}
				if (disk_read(fp->fs->drv, fp->buf, sect, 1) != RES_OK)	/* Fill sector cache */
					{ fp->flag |= 0x80; return FR_DISK_ERR; };
			}
			fp->dsect = sect;
		}
		rcnt = 512U - (fp->fptr % 512U);	/* Get partial sector data from sector buffer */
		if (rcnt > btr) rcnt = btr;
		mem_cpy(rbuff, &fp->buf[fp->fptr % 512U], rcnt);	/* Pick partial sector */
	}

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Write File                                                            */
/*-----------------------------------------------------------------------*/

FRESULT f_write (
	FIL *fp,			/* Pointer to the file object */
	const void *buff,	/* Pointer to the data to be written */
	UINT btw,			/* Number of bytes to write */
	UINT *bw			/* Pointer to number of bytes written */
)
{
	FRESULT res;
	DWORD clst, sect;
	UINT wcnt, cc;
	const BYTE *wbuff = buff;
	BYTE csect;


	*bw = 0;	/* Initialize byte counter */

	res = validate(fp->fs, fp->id);			/* Check validity */
	if (res != FR_OK) return res;
	if (fp->flag & 0x80)				/* Aborted file? */
		return FR_INT_ERR;
	if (!(fp->flag & 0x02))				/* Check access mode */
		return FR_DENIED;
	if ((DWORD)(fp->fsize + btw) < fp->fsize) btw = 0;	/* File size cannot reach 4GB */

	for ( ;  btw;							/* Repeat until all data written */
		wbuff += wcnt, fp->fptr += wcnt, *bw += wcnt, btw -= wcnt) {
		if ((fp->fptr % 512U) == 0) {	/* On the sector boundary? */
			csect = (BYTE)(fp->fptr / 512U & (fp->fs->csize - 1));	/* Sector offset in the cluster */
			if (!csect) {					/* On the cluster boundary? */
				if (fp->fptr == 0) {		/* On the top of the file? */
					clst = fp->sclust;		/* Follow from the origin */
					if (clst == 0)			/* When no cluster is allocated, */
						fp->sclust = clst = create_chain(fp->fs, 0);	/* Create a new cluster chain */
				} else {					/* Middle or end of the file */
						clst = create_chain(fp->fs, fp->clust);	/* Follow or stretch cluster chain on the FAT */
				}
				if (clst == 0) break;		/* Could not allocate a new cluster (disk full) */
				if (clst == 1) { fp->flag |= 0x80; return FR_INT_ERR; };
				if (clst == 0xFFFFFFFF) { fp->flag |= 0x80; return FR_DISK_ERR; };
				fp->clust = clst;			/* Update current cluster */
			}
			if (fp->flag & 0x40) {		/* Write-back sector cache */
				if (disk_write(fp->fs->drv, fp->buf, fp->dsect, 1) != RES_OK)
					{ fp->flag |= 0x80; return FR_DISK_ERR; };
				fp->flag &= ~0x40;
			}
			sect = clust2sect(fp->fs, fp->clust);	/* Get current sector */
			if (!sect) { fp->flag |= 0x80; return FR_INT_ERR; };
			sect += csect;
			cc = btw / 512U;			/* When remaining bytes >= sector size, */
			if (cc) {						/* Write maximum contiguous sectors directly */
				if (csect + cc > fp->fs->csize)	/* Clip at cluster boundary */
					cc = fp->fs->csize - csect;
				if (disk_write(fp->fs->drv, wbuff, sect, (BYTE)cc) != RES_OK)
					{ fp->flag |= 0x80; return FR_DISK_ERR; };
				if (fp->dsect - sect < cc) { /* Refill sector cache if it gets invalidated by the direct write */
					mem_cpy(fp->buf, wbuff + ((fp->dsect - sect) * 512U), 512U);
					fp->flag &= ~0x40;
				}
				wcnt = 512U * cc;		/* Number of bytes transferred */
				continue;
			}
			if (fp->dsect != sect) {		/* Fill sector cache with file data */
				if (fp->fptr < fp->fsize &&
					disk_read(fp->fs->drv, fp->buf, sect, 1) != RES_OK)
						{ fp->flag |= 0x80; return FR_DISK_ERR; };
			}
			fp->dsect = sect;
		}
		wcnt = 512U - (fp->fptr % 512U);/* Put partial sector into file I/O buffer */
		if (wcnt > btw) wcnt = btw;
		mem_cpy(&fp->buf[fp->fptr % 512U], wbuff, wcnt);	/* Fit partial sector */
		fp->flag |= 0x40;
	}

	if (fp->fptr > fp->fsize) fp->fsize = fp->fptr;	/* Update file size if needed */
	fp->flag |= 0x20;						/* Set file change flag */

	return FR_OK;
}




/*-----------------------------------------------------------------------*/
/* Synchronize the File Object                                           */
/*-----------------------------------------------------------------------*/

FRESULT f_sync (
	FIL *fp		/* Pointer to the file object */
)
{
	FRESULT res;
	DWORD tim;
	BYTE *dir;


	res = validate(fp->fs, fp->id);		/* Check validity of the object */
	if (res == FR_OK) {
		if (fp->flag & 0x20) {	/* Has the file been written? */
			if (fp->flag & 0x40) {
				if (disk_write(fp->fs->drv, fp->buf, fp->dsect, 1) != RES_OK)
					return FR_DISK_ERR;
				fp->flag &= ~0x40;
			}
			/* Update the directory entry */
			res = move_window(fp->fs, fp->dir_sect);
			if (res == FR_OK) {
				dir = fp->dir_ptr;
				dir[11] |= 0x20;					/* Set archive bit */
				*(BYTE*)(dir+28)=(BYTE)(fp->fsize); *((BYTE*)(dir+28)+1)=(BYTE)((WORD)(fp->fsize)>>8); *((BYTE*)(dir+28)+2)=(BYTE)((DWORD)(fp->fsize)>>16); *((BYTE*)(dir+28)+3)=(BYTE)((DWORD)(fp->fsize)>>24);		/* Update file size */
				{*(BYTE*)(dir+26)=(BYTE)(fp->sclust); *((BYTE*)(dir+26)+1)=(BYTE)((WORD)(fp->sclust)>>8); *(BYTE*)(dir+20)=(BYTE)((DWORD)fp->sclust>>16); *((BYTE*)(dir+20)+1)=(BYTE)((WORD)((DWORD)fp->sclust>>16)>>8);};					/* Update start cluster */
				tim = get_fattime();						/* Update updated time */
				*(BYTE*)(dir+22)=(BYTE)(tim); *((BYTE*)(dir+22)+1)=(BYTE)((WORD)(tim)>>8); *((BYTE*)(dir+22)+2)=(BYTE)((DWORD)(tim)>>16); *((BYTE*)(dir+22)+3)=(BYTE)((DWORD)(tim)>>24);
				fp->flag &= ~0x20;
				fp->fs->wflag = 1;
				res = sync(fp->fs);
			}
		}
	}

	return res;
}





/*-----------------------------------------------------------------------*/
/* Close File                                                            */
/*-----------------------------------------------------------------------*/

FRESULT f_close (
	FIL *fp		/* Pointer to the file object to be closed */
)
{
	FRESULT res;

	res = f_sync(fp);		/* Flush cached data */
	if (res == FR_OK) fp->fs = 0;	/* Discard file object */
	return res;
}




/*-----------------------------------------------------------------------*/
/* Current Drive/Directory Handlings                                     */
/*-----------------------------------------------------------------------*/


FRESULT f_chdrive (
	BYTE drv		/* Drive number */
)
{
	if (drv >= 1) return FR_INVALID_DRIVE;

	CurrVol = drv;

	return FR_OK;
}



FRESULT f_chdir (
	const TCHAR *path	/* Pointer to the directory path */
)
{
	FRESULT res;
	DIR dj;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 0);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);		/* Follow the path */
		;
		if (res == FR_OK) {					/* Follow completed */
			if (!dj.dir) {
				dj.fs->cdir = dj.sclust;	/* Start directory itself */
			} else {
				if (dj.dir[11] & 0x10)	/* Reached to the directory */
					dj.fs->cdir = (((DWORD)(WORD)(((WORD)*((BYTE*)(dj . dir+20)+1)<<8)|(WORD)*(BYTE*)(dj . dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dj . dir+26)+1)<<8)|(WORD)*(BYTE*)(dj . dir+26)));
				else
					res = FR_NO_PATH;		/* Reached but a file */
			}
		}
		if (res == FR_NO_FILE) res = FR_NO_PATH;
	}

	return res;
}





/*-----------------------------------------------------------------------*/
/* Seek File R/W Pointer                                                 */
/*-----------------------------------------------------------------------*/

FRESULT f_lseek (
	FIL *fp,		/* Pointer to the file object */
	DWORD ofs		/* File pointer from top of file */
)
{
	FRESULT res;


	res = validate(fp->fs, fp->id);		/* Check validity of the object */
	if (res != FR_OK) return res;
	if (fp->flag & 0x80)			/* Check abort flag */
		return FR_INT_ERR;


	/* Normal Seek */
	{
		DWORD clst, bcs, nsect, ifptr;

		if (ofs > fp->fsize					/* In read-only mode, clip offset with the file size */
			 && !(fp->flag & 0x02)
			) ofs = fp->fsize;

		ifptr = fp->fptr;
		fp->fptr = nsect = 0;
		if (ofs) {
			bcs = (DWORD)fp->fs->csize * 512U;	/* Cluster size (byte) */
			if (ifptr > 0 &&
				(ofs - 1) / bcs >= (ifptr - 1) / bcs) {	/* When seek to same or following cluster, */
				fp->fptr = (ifptr - 1) & ~(bcs - 1);	/* start from the current cluster */
				ofs -= fp->fptr;
				clst = fp->clust;
			} else {									/* When seek to back cluster, */
				clst = fp->sclust;						/* start from the first cluster */
				if (clst == 0) {						/* If no cluster chain, create a new chain */
					clst = create_chain(fp->fs, 0);
					if (clst == 1) { fp->flag |= 0x80; return FR_INT_ERR; };
					if (clst == 0xFFFFFFFF) { fp->flag |= 0x80; return FR_DISK_ERR; };
					fp->sclust = clst;
				}
				fp->clust = clst;
			}
			if (clst != 0) {
				while (ofs > bcs) {						/* Cluster following loop */
					if (fp->flag & 0x02) {			/* Check if in write mode or not */
						clst = create_chain(fp->fs, clst);	/* Force stretch if in write mode */
						if (clst == 0) {				/* When disk gets full, clip file size */
							ofs = bcs; break;
						}
					} else
						clst = get_fat(fp->fs, clst);	/* Follow cluster chain if not in write mode */
					if (clst == 0xFFFFFFFF) { fp->flag |= 0x80; return FR_DISK_ERR; };
					if (clst <= 1 || clst >= fp->fs->n_fatent) { fp->flag |= 0x80; return FR_INT_ERR; };
					fp->clust = clst;
					fp->fptr += bcs;
					ofs -= bcs;
				}
				fp->fptr += ofs;
				if (ofs % 512U) {
					nsect = clust2sect(fp->fs, clst);	/* Current sector */
					if (!nsect) { fp->flag |= 0x80; return FR_INT_ERR; };
					nsect += ofs / 512U;
				}
			}
		}
		if (fp->fptr % 512U && nsect != fp->dsect) {	/* Fill sector cache if needed */
			if (fp->flag & 0x40) {			/* Write-back dirty sector cache */
				if (disk_write(fp->fs->drv, fp->buf, fp->dsect, 1) != RES_OK)
					{ fp->flag |= 0x80; return FR_DISK_ERR; };
				fp->flag &= ~0x40;
			}
			if (disk_read(fp->fs->drv, fp->buf, nsect, 1) != RES_OK)	/* Fill sector cache */
				{ fp->flag |= 0x80; return FR_DISK_ERR; };
			fp->dsect = nsect;
		}
		if (fp->fptr > fp->fsize) {			/* Set file change flag if the file size is extended */
			fp->fsize = fp->fptr;
			fp->flag |= 0x20;
		}
	}

	return res;
}



/*-----------------------------------------------------------------------*/
/* Create a Directroy Object                                             */
/*-----------------------------------------------------------------------*/

FRESULT f_opendir (
	DIR *dj,			/* Pointer to directory object to create */
	const TCHAR *path	/* Pointer to the directory path */
)
{
	FRESULT res;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj->fs, 0);
	if (res == FR_OK) {
		(*dj). fn = sfn;
		res = follow_path(dj, path);			/* Follow the path to the directory */
		;
		if (res == FR_OK) {						/* Follow completed */
			if (dj->dir) {						/* It is not the root dir */
				if (dj->dir[11] & 0x10) {	/* The object is a directory */
					dj->sclust = (((DWORD)(WORD)(((WORD)*((BYTE*)(dj->dir+20)+1)<<8)|(WORD)*(BYTE*)(dj->dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dj->dir+26)+1)<<8)|(WORD)*(BYTE*)(dj->dir+26)));
				} else {						/* The object is not a directory */
					res = FR_NO_PATH;
				}
			}
			if (res == FR_OK) {
				dj->id = dj->fs->id;
				res = dir_sdi(dj, 0);			/* Rewind dir */
			}
		}
		if (res == FR_NO_FILE) res = FR_NO_PATH;
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Read Directory Entry in Sequense                                      */
/*-----------------------------------------------------------------------*/

FRESULT f_readdir (
	DIR *dj,			/* Pointer to the open directory object */
	FILINFO *fno		/* Pointer to file information to return */
)
{
	FRESULT res;
	BYTE sfn[12];


	res = validate(dj->fs, dj->id);			/* Check validity of the object */
	if (res == FR_OK) {
		if (!fno) {
			res = dir_sdi(dj, 0);			/* Rewind the directory object */
		} else {
			(*dj). fn = sfn;
			res = dir_read(dj);				/* Read an directory item */
			if (res == FR_NO_FILE) {		/* Reached end of dir */
				dj->sect = 0;
				res = FR_OK;
			}
			if (res == FR_OK) {				/* A valid entry is found */
				get_fileinfo(dj, fno);		/* Get the object information */
				res = dir_next(dj, 0);		/* Increment index for next */
				if (res == FR_NO_FILE) {
					dj->sect = 0;
					res = FR_OK;
				}
			}
			;
		}
	}

	return res;
}



/*-----------------------------------------------------------------------*/
/* Get File Status                                                       */
/*-----------------------------------------------------------------------*/

FRESULT f_stat (
	const TCHAR *path,	/* Pointer to the file path */
	FILINFO *fno		/* Pointer to file information to return */
)
{
	FRESULT res;
	DIR dj;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 0);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);	/* Follow the file path */
		if (res == FR_OK) {				/* Follow completed */
			if (dj.dir)		/* Found an object */
				get_fileinfo(&dj, fno);
			else			/* It is root dir */
				res = FR_INVALID_NAME;
		}
		;
	}

	return res;
}



/*-----------------------------------------------------------------------*/
/* Get Number of Free Clusters                                           */
/*-----------------------------------------------------------------------*/

FRESULT f_getfree (
	const TCHAR *path,	/* Pointer to the logical drive number (root dir) */
	DWORD *nclst,		/* Pointer to the variable to return number of free clusters */
	FATFS **fatfs		/* Pointer to pointer to corresponding file system object to return */
)
{
	FRESULT res;
	DWORD n, clst, sect, stat;
	UINT i;
	BYTE fat, *p;


	/* Get drive number */
	res = chk_mounted(&path, fatfs, 0);
	if (res == FR_OK) {
		/* If free_clust is valid, return it without full cluster scan */
		if ((*fatfs)->free_clust <= (*fatfs)->n_fatent - 2) {
			*nclst = (*fatfs)->free_clust;
		} else {
			/* Get number of free clusters */
			fat = (*fatfs)->fs_type;
			n = 0;
			if (fat == 1) {
				clst = 2;
				do {
					stat = get_fat(*fatfs, clst);
					if (stat == 0xFFFFFFFF) { res = FR_DISK_ERR; break; }
					if (stat == 1) { res = FR_INT_ERR; break; }
					if (stat == 0) n++;
				} while (++clst < (*fatfs)->n_fatent);
			} else {
				clst = (*fatfs)->n_fatent;
				sect = (*fatfs)->fatbase;
				i = 0; p = 0;
				do {
					if (!i) {
						res = move_window(*fatfs, sect++);
						if (res != FR_OK) break;
						p = (*fatfs)->win;
						i = 512U;
					}
					if (fat == 2) {
						if ((WORD)(((WORD)*((BYTE*)(p)+1)<<8)|(WORD)*(BYTE*)(p)) == 0) n++;
						p += 2; i -= 2;
					} else {
						if (((DWORD)(((DWORD)*((BYTE*)(p)+3)<<24)|((DWORD)*((BYTE*)(p)+2)<<16)|((WORD)*((BYTE*)(p)+1)<<8)| *(BYTE*)(p)) & 0x0FFFFFFF) == 0) n++;
						p += 4; i -= 4;
					}
				} while (--clst);
			}
			(*fatfs)->free_clust = n;
			if (fat == 3) (*fatfs)->fsi_flag = 1;
			*nclst = n;
		}
	}
	return res;
}




/*-----------------------------------------------------------------------*/
/* Truncate File                                                         */
/*-----------------------------------------------------------------------*/

FRESULT f_truncate (
	FIL *fp		/* Pointer to the file object */
)
{
	FRESULT res;
	DWORD ncl;


	res = validate(fp->fs, fp->id);		/* Check validity of the object */
	if (res == FR_OK) {
		if (fp->flag & 0x80) {			/* Check abort flag */
			res = FR_INT_ERR;
		} else {
			if (!(fp->flag & 0x02))		/* Check access mode */
				res = FR_DENIED;
		}
	}
	if (res == FR_OK) {
		if (fp->fsize > fp->fptr) {
			fp->fsize = fp->fptr;	/* Set file size to current R/W point */
			fp->flag |= 0x20;
			if (fp->fptr == 0) {	/* When set file size to zero, remove entire cluster chain */
				res = remove_chain(fp->fs, fp->sclust);
				fp->sclust = 0;
			} else {				/* When truncate a part of the file, remove remaining clusters */
				ncl = get_fat(fp->fs, fp->clust);
				res = FR_OK;
				if (ncl == 0xFFFFFFFF) res = FR_DISK_ERR;
				if (ncl == 1) res = FR_INT_ERR;
				if (res == FR_OK && ncl < fp->fs->n_fatent) {
					res = put_fat(fp->fs, fp->clust, 0x0FFFFFFF);
					if (res == FR_OK) res = remove_chain(fp->fs, ncl);
				}
			}
		}
		if (res != FR_OK) fp->flag |= 0x80;
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Delete a File or Directory                                            */
/*-----------------------------------------------------------------------*/

FRESULT f_unlink (
	const TCHAR *path		/* Pointer to the file or directory path */
)
{
	FRESULT res;
	DIR dj, sdj;
	BYTE *dir;
	DWORD dclst;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 1);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);		/* Follow the file path */
		if (1 && res == FR_OK && (dj.fn[11] & 0x20))
			res = FR_INVALID_NAME;			/* Cannot remove dot entry */
		if (res == FR_OK) {					/* The object is accessible */
			dir = dj.dir;
			if (!dir) {
				res = FR_INVALID_NAME;		/* Cannot remove the start directory */
			} else {
				if (dir[11] & 0x01)
					res = FR_DENIED;		/* Cannot remove R/O object */
			}
			dclst = (((DWORD)(WORD)(((WORD)*((BYTE*)(dir+20)+1)<<8)|(WORD)*(BYTE*)(dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dir+26)+1)<<8)|(WORD)*(BYTE*)(dir+26)));
			if (res == FR_OK && (dir[11] & 0x10)) {	/* Is it a sub-dir? */
				if (dclst < 2) {
					res = FR_INT_ERR;
				} else {
					mem_cpy(&sdj, &dj, sizeof(DIR));	/* Check if the sub-dir is empty or not */
					sdj.sclust = dclst;
					res = dir_sdi(&sdj, 2);		/* Exclude dot entries */
					if (res == FR_OK) {
						res = dir_read(&sdj);
						if (res == FR_OK			/* Not empty dir */
						|| dclst == sdj.fs->cdir	/* Current dir */
						) res = FR_DENIED;
						if (res == FR_NO_FILE) res = FR_OK;	/* Empty */
					}
				}
			}
			if (res == FR_OK) {
				res = dir_remove(&dj);		/* Remove the directory entry */
				if (res == FR_OK) {
					if (dclst)				/* Remove the cluster chain if exist */
						res = remove_chain(dj.fs, dclst);
					if (res == FR_OK) res = sync(dj.fs);
				}
			}
		}
		;
	}
	return res;
}




/*-----------------------------------------------------------------------*/
/* Create a Directory                                                    */
/*-----------------------------------------------------------------------*/

FRESULT f_mkdir (
	const TCHAR *path		/* Pointer to the directory path */
)
{
	FRESULT res;
	DIR dj;
	BYTE *dir, n;
	DWORD dsc, dcl, pcl, tim = get_fattime();
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 1);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);			/* Follow the file path */
		if (res == FR_OK) res = FR_EXIST;		/* Any object with same name is already existing */
		if (1 && res == FR_NO_FILE && (dj.fn[11] & 0x20))
			res = FR_INVALID_NAME;
		if (res == FR_NO_FILE) {				/* Can create a new directory */
			dcl = create_chain(dj.fs, 0);		/* Allocate a cluster for the new directory table */
			res = FR_OK;
			if (dcl == 0) res = FR_DENIED;		/* No space to allocate a new cluster */
			if (dcl == 1) res = FR_INT_ERR;
			if (dcl == 0xFFFFFFFF) res = FR_DISK_ERR;
			if (res == FR_OK)					/* Flush FAT */
				res = move_window(dj.fs, 0);
			if (res == FR_OK) {					/* Initialize the new directory table */
				dsc = clust2sect(dj.fs, dcl);
				dir = dj.fs->win;
				mem_set(dir, 0, 512U);
				mem_set(dir+0, ' ', 8+3);	/* Create "." entry */
				dir[0] = '.';
				dir[11] = 0x10;
				*(BYTE*)(dir+22)=(BYTE)(tim); *((BYTE*)(dir+22)+1)=(BYTE)((WORD)(tim)>>8); *((BYTE*)(dir+22)+2)=(BYTE)((DWORD)(tim)>>16); *((BYTE*)(dir+22)+3)=(BYTE)((DWORD)(tim)>>24);
				{*(BYTE*)(dir+26)=(BYTE)(dcl); *((BYTE*)(dir+26)+1)=(BYTE)((WORD)(dcl)>>8); *(BYTE*)(dir+20)=(BYTE)((DWORD)dcl>>16); *((BYTE*)(dir+20)+1)=(BYTE)((WORD)((DWORD)dcl>>16)>>8);};
				mem_cpy(dir+32, dir, 32); 	/* Create ".." entry */
				dir[33] = '.'; pcl = dj.sclust;
				if (dj.fs->fs_type == 3 && pcl == dj.fs->dirbase)
					pcl = 0;
				{*(BYTE*)(dir+32+26)=(BYTE)(pcl); *((BYTE*)(dir+32+26)+1)=(BYTE)((WORD)(pcl)>>8); *(BYTE*)(dir+32+20)=(BYTE)((DWORD)pcl>>16); *((BYTE*)(dir+32+20)+1)=(BYTE)((WORD)((DWORD)pcl>>16)>>8);};
				for (n = dj.fs->csize; n; n--) {	/* Write dot entries and clear following sectors */
					dj.fs->winsect = dsc++;
					dj.fs->wflag = 1;
					res = move_window(dj.fs, 0);
					if (res != FR_OK) break;
					mem_set(dir, 0, 512U);
				}
			}
			if (res == FR_OK) res = dir_register(&dj);	/* Register the object to the directoy */
			if (res != FR_OK) {
				remove_chain(dj.fs, dcl);			/* Could not register, remove cluster chain */
			} else {
				dir = dj.dir;
				dir[11] = 0x10;				/* Attribute */
				*(BYTE*)(dir+22)=(BYTE)(tim); *((BYTE*)(dir+22)+1)=(BYTE)((WORD)(tim)>>8); *((BYTE*)(dir+22)+2)=(BYTE)((DWORD)(tim)>>16); *((BYTE*)(dir+22)+3)=(BYTE)((DWORD)(tim)>>24);		/* Created time */
				{*(BYTE*)(dir+26)=(BYTE)(dcl); *((BYTE*)(dir+26)+1)=(BYTE)((WORD)(dcl)>>8); *(BYTE*)(dir+20)=(BYTE)((DWORD)dcl>>16); *((BYTE*)(dir+20)+1)=(BYTE)((WORD)((DWORD)dcl>>16)>>8);};					/* Table start cluster */
				dj.fs->wflag = 1;
				res = sync(dj.fs);
			}
		}
		;
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Change Attribute                                                      */
/*-----------------------------------------------------------------------*/

FRESULT f_chmod (
	const TCHAR *path,	/* Pointer to the file path */
	BYTE value,			/* Attribute bits */
	BYTE mask			/* Attribute mask to change */
)
{
	FRESULT res;
	DIR dj;
	BYTE *dir;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 1);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);		/* Follow the file path */
		;
		if (1 && res == FR_OK && (dj.fn[11] & 0x20))
			res = FR_INVALID_NAME;
		if (res == FR_OK) {
			dir = dj.dir;
			if (!dir) {						/* Is it a root directory? */
				res = FR_INVALID_NAME;
			} else {						/* File or sub directory */
				mask &= 0x01|0x02|0x04|0x20;	/* Valid attribute mask */
				dir[11] = (value & mask) | (dir[11] & (BYTE)~mask);	/* Apply attribute change */
				dj.fs->wflag = 1;
				res = sync(dj.fs);
			}
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Change Timestamp                                                      */
/*-----------------------------------------------------------------------*/

FRESULT f_utime (
	const TCHAR *path,	/* Pointer to the file/directory name */
	const FILINFO *fno	/* Pointer to the time stamp to be set */
)
{
	FRESULT res;
	DIR dj;
	BYTE *dir;
	BYTE sfn[12];


	res = chk_mounted(&path, &dj.fs, 1);
	if (res == FR_OK) {
		(dj). fn = sfn;
		res = follow_path(&dj, path);	/* Follow the file path */
		;
		if (1 && res == FR_OK && (dj.fn[11] & 0x20))
			res = FR_INVALID_NAME;
		if (res == FR_OK) {
			dir = dj.dir;
			if (!dir) {					/* Root directory */
				res = FR_INVALID_NAME;
			} else {					/* File or sub-directory */
				*(BYTE*)(dir+22)=(BYTE)(fno->ftime); *((BYTE*)(dir+22)+1)=(BYTE)((WORD)(fno->ftime)>>8);
				*(BYTE*)(dir+24)=(BYTE)(fno->fdate); *((BYTE*)(dir+24)+1)=(BYTE)((WORD)(fno->fdate)>>8);
				dj.fs->wflag = 1;
				res = sync(dj.fs);
			}
		}
	}

	return res;
}




/*-----------------------------------------------------------------------*/
/* Rename File/Directory                                                 */
/*-----------------------------------------------------------------------*/

FRESULT f_rename (
	const TCHAR *path_old,	/* Pointer to the old name */
	const TCHAR *path_new	/* Pointer to the new name */
)
{
	FRESULT res;
	DIR djo, djn;
	BYTE buf[21], *dir;
	DWORD dw;
	BYTE sfn[12];


	res = chk_mounted(&path_old, &djo.fs, 1);
	if (res == FR_OK) {
		djn.fs = djo.fs;
		(djo). fn = sfn;
		res = follow_path(&djo, path_old);		/* Check old object */
		if (1 && res == FR_OK && (djo.fn[11] & 0x20))
			res = FR_INVALID_NAME;
		if (res == FR_OK) {						/* Old object is found */
			if (!djo.dir) {						/* Is root dir? */
				res = FR_NO_FILE;
			} else {
				mem_cpy(buf, djo.dir+11, 21);		/* Save the object information except for name */
				mem_cpy(&djn, &djo, sizeof(DIR));		/* Check new object */
				res = follow_path(&djn, path_new);
				if (res == FR_OK) res = FR_EXIST;		/* The new object name is already existing */
				if (res == FR_NO_FILE) { 				/* Is it a valid path and no name collision? */
/* Start critical section that any interruption or error can cause cross-link */
					res = dir_register(&djn);			/* Register the new entry */
					if (res == FR_OK) {
						dir = djn.dir;					/* Copy object information except for name */
						mem_cpy(dir+13, buf+2, 19);
						dir[11] = buf[0] | 0x20;
						djo.fs->wflag = 1;
						if (djo.sclust != djn.sclust && (dir[11] & 0x10)) {		/* Update .. entry in the directory if needed */
							dw = clust2sect(djn.fs, (((DWORD)(WORD)(((WORD)*((BYTE*)(dir+20)+1)<<8)|(WORD)*(BYTE*)(dir+20))<<16) | (WORD)(((WORD)*((BYTE*)(dir+26)+1)<<8)|(WORD)*(BYTE*)(dir+26))));
							if (!dw) {
								res = FR_INT_ERR;
							} else {
								res = move_window(djn.fs, dw);
								dir = djn.fs->win+32;	/* .. entry */
								if (res == FR_OK && dir[1] == '.') {
									dw = (djn.fs->fs_type == 3 && djn.sclust == djn.fs->dirbase) ? 0 : djn.sclust;
									{*(BYTE*)(dir+26)=(BYTE)(dw); *((BYTE*)(dir+26)+1)=(BYTE)((WORD)(dw)>>8); *(BYTE*)(dir+20)=(BYTE)((DWORD)dw>>16); *((BYTE*)(dir+20)+1)=(BYTE)((WORD)((DWORD)dw>>16)>>8);};
									djn.fs->wflag = 1;
								}
							}
						}
						if (res == FR_OK) {
							res = dir_remove(&djo);		/* Remove old entry */
							if (res == FR_OK)
								res = sync(djo.fs);
						}
					}
/* End critical section */
				}
			}
		}
		;
	}
	return res;
}




/*-----------------------------------------------------------------------*/
/* Forward data to the stream directly (available on only tiny cfg)      */
/*-----------------------------------------------------------------------*/



/*-----------------------------------------------------------------------*/
/* Create File System on the Drive                                       */
/*-----------------------------------------------------------------------*/


FRESULT f_mkfs (
	BYTE drv,		/* Logical drive number */
	BYTE sfd,		/* Partitioning rule 0:FDISK, 1:SFD */
	UINT au			/* Allocation unit size [bytes] */
)
{
	static const WORD vst[] = { 1024,   512,  256,  128,   64,    32,   16,    8,    4,    2,   0};
	static const WORD cst[] = {32768, 16384, 8192, 4096, 2048, 16384, 8192, 4096, 2048, 1024, 512};
	BYTE fmt, md, sys, *tbl, pdrv, part;
	DWORD n_clst, vs, n, wsect;
	UINT i;
	DWORD b_vol, b_fat, b_dir, b_data;	/* LBA */
	DWORD n_vol, n_rsv, n_fat, n_dir;	/* Size */
	FATFS *fs;
	DSTATUS stat;


	/* Check mounted drive and clear work area */
	if (drv >= 1) return FR_INVALID_DRIVE;
	if (sfd > 1) return FR_INVALID_PARAMETER;
	if (au & (au - 1)) return FR_INVALID_PARAMETER;
	fs = FatFs[drv];
	if (!fs) return FR_NOT_ENABLED;
	fs->fs_type = 0;
	pdrv = (drv);	/* Physical drive */
	part = 0;	/* Partition (0:auto detect, 1-4:get from partition table)*/

	/* Get disk statics */
	stat = disk_initialize(pdrv);
	if (stat & 0x01) return FR_NOT_READY;
	if (stat & 0x04) return FR_WRITE_PROTECTED;
	if (0 && part) {
		/* Get partition information from partition table in the MBR */
		if (disk_read(pdrv, fs->win, 0, 1) != RES_OK) return FR_DISK_ERR;
		if ((WORD)(((WORD)*((BYTE*)(fs->win+510)+1)<<8)|(WORD)*(BYTE*)(fs->win+510)) != 0xAA55) return FR_MKFS_ABORTED;
		tbl = &fs->win[446 + (part - 1) * 16];
		if (!tbl[4]) return FR_MKFS_ABORTED;	/* No partition? */
		b_vol = (DWORD)(((DWORD)*((BYTE*)(tbl+8)+3)<<24)|((DWORD)*((BYTE*)(tbl+8)+2)<<16)|((WORD)*((BYTE*)(tbl+8)+1)<<8)| *(BYTE*)(tbl+8));	/* Volume start sector */
		n_vol = (DWORD)(((DWORD)*((BYTE*)(tbl+12)+3)<<24)|((DWORD)*((BYTE*)(tbl+12)+2)<<16)|((WORD)*((BYTE*)(tbl+12)+1)<<8)| *(BYTE*)(tbl+12));	/* Volume size */
	} else {
		/* Create a partition in this function */
		if (disk_ioctl(pdrv, 1, &n_vol) != RES_OK || n_vol < 128)
			return FR_DISK_ERR;
		b_vol = (sfd) ? 0 : 63;		/* Volume start sector */
		n_vol -= b_vol;				/* Volume size */
	}

	if (!au) {				/* AU auto selection */
		vs = n_vol / (2000 / (512U / 512));
		for (i = 0; vs < vst[i]; i++) ;
		au = cst[i];
	}
	au /= 512U;		/* Number of sectors per cluster */
	if (au == 0) au = 1;
	if (au > 128) au = 128;

	/* Pre-compute number of clusters and FAT syb-type */
	n_clst = n_vol / au;
	fmt = 1;
	if (n_clst >= 4086) fmt = 2;
	if (n_clst >= 65526) fmt = 3;

	/* Determine offset and size of FAT structure */
	if (fmt == 3) {
		n_fat = ((n_clst * 4) + 8 + 512U - 1) / 512U;
		n_rsv = 32;
		n_dir = 0;
	} else {
		n_fat = (fmt == 1) ? (n_clst * 3 + 1) / 2 + 3 : (n_clst * 2) + 4;
		n_fat = (n_fat + 512U - 1) / 512U;
		n_rsv = 1;
		n_dir = (DWORD)512 * 32 / 512U;
	}
	b_fat = b_vol + n_rsv;				/* FAT area start sector */
	b_dir = b_fat + n_fat * 1;		/* Directory area start sector */
	b_data = b_dir + n_dir;				/* Data area start sector */
	if (n_vol < b_data + au - b_vol) return FR_MKFS_ABORTED;	/* Too small volume */

	/* Align data start sector to erase block boundary (for flash memory media) */
	if (disk_ioctl(pdrv, 3, &n) != RES_OK || !n || n > 32768) n = 1;
	n = (b_data + n - 1) & ~(n - 1);	/* Next nearest erase block from current data start */
	n = (n - b_data) / 1;
	if (fmt == 3) {		/* FAT32: Move FAT offset */
		n_rsv += n;
		b_fat += n;
	} else {					/* FAT12/16: Expand FAT size */
		n_fat += n;
	}

	/* Determine number of clusters and final check of validity of the FAT sub-type */
	n_clst = (n_vol - n_rsv - n_fat * 1 - n_dir) / au;
	if (   (fmt == 2 && n_clst < 4086)
		|| (fmt == 3 && n_clst < 65526))
		return FR_MKFS_ABORTED;

	switch (fmt) {	/* Determine system ID for partition table */
	case 1:	sys = 0x01; break;
	case 2:	sys = (n_vol < 0x10000) ? 0x04 : 0x06; break;
	default: 		sys = 0x0C;
	}

	if (0 && part) {
		/* Update system ID in the partition table */
		tbl = &fs->win[446 + (part - 1) * 16];
		tbl[4] = sys;
		if (disk_write(pdrv, fs->win, 0, 1) != RES_OK) return FR_DISK_ERR;
		md = 0xF8;
	} else {
		if (sfd) {	/* No patition table (SFD) */
			md = 0xF0;
		} else {	/* Create partition table (FDISK) */
			mem_set(fs->win, 0, 512U);
			tbl = fs->win+446;	/* Create partiton table for single partition in the drive */
			tbl[1] = 1;						/* Partition start head */
			tbl[2] = 1;						/* Partition start sector */
			tbl[3] = 0;						/* Partition start cylinder */
			tbl[4] = sys;					/* System type */
			tbl[5] = 254;					/* Partition end head */
			n = (b_vol + n_vol) / 63 / 255;
			tbl[6] = (BYTE)((n >> 2) | 63);	/* Partiiton end sector */
			tbl[7] = (BYTE)n;				/* End cylinder */
			*(BYTE*)(tbl+8)=(BYTE)(63); *((BYTE*)(tbl+8)+1)=(BYTE)((WORD)(63)>>8); *((BYTE*)(tbl+8)+2)=(BYTE)((DWORD)(63)>>16); *((BYTE*)(tbl+8)+3)=(BYTE)((DWORD)(63)>>24);			/* Partition start in LBA */
			*(BYTE*)(tbl+12)=(BYTE)(n_vol); *((BYTE*)(tbl+12)+1)=(BYTE)((WORD)(n_vol)>>8); *((BYTE*)(tbl+12)+2)=(BYTE)((DWORD)(n_vol)>>16); *((BYTE*)(tbl+12)+3)=(BYTE)((DWORD)(n_vol)>>24);		/* Partition size in LBA */
			*(BYTE*)(fs->win+510)=(BYTE)(0xAA55); *((BYTE*)(fs->win+510)+1)=(BYTE)((WORD)(0xAA55)>>8);	/* MBR signature */
			if (disk_write(pdrv, fs->win, 0, 1) != RES_OK)	/* Write it to the MBR sector */
				return FR_DISK_ERR;
			md = 0xF8;
		}
	}

	/* Create BPB in the VBR */
	tbl = fs->win;							/* Clear sector */
	mem_set(tbl, 0, 512U);
	mem_cpy(tbl, "\xEB\xFE\x90" "MSDOS5.0", 11);/* Boot jump code, OEM name */
	i = 512U;								/* Sector size */
	*(BYTE*)(tbl+11)=(BYTE)(i); *((BYTE*)(tbl+11)+1)=(BYTE)((WORD)(i)>>8);
	tbl[13] = (BYTE)au;			/* Sectors per cluster */
	*(BYTE*)(tbl+14)=(BYTE)(n_rsv); *((BYTE*)(tbl+14)+1)=(BYTE)((WORD)(n_rsv)>>8);		/* Reserved sectors */
	tbl[16] = 1;				/* Number of FATs */
	i = (fmt == 3) ? 0 : 512;	/* Number of rootdir entries */
	*(BYTE*)(tbl+17)=(BYTE)(i); *((BYTE*)(tbl+17)+1)=(BYTE)((WORD)(i)>>8);
	if (n_vol < 0x10000) {					/* Number of total sectors */
		*(BYTE*)(tbl+19)=(BYTE)(n_vol); *((BYTE*)(tbl+19)+1)=(BYTE)((WORD)(n_vol)>>8);
	} else {
		*(BYTE*)(tbl+32)=(BYTE)(n_vol); *((BYTE*)(tbl+32)+1)=(BYTE)((WORD)(n_vol)>>8); *((BYTE*)(tbl+32)+2)=(BYTE)((DWORD)(n_vol)>>16); *((BYTE*)(tbl+32)+3)=(BYTE)((DWORD)(n_vol)>>24);
	}
	tbl[21] = md;					/* Media descriptor */
	*(BYTE*)(tbl+24)=(BYTE)(63); *((BYTE*)(tbl+24)+1)=(BYTE)((WORD)(63)>>8);			/* Number of sectors per track */
	*(BYTE*)(tbl+26)=(BYTE)(255); *((BYTE*)(tbl+26)+1)=(BYTE)((WORD)(255)>>8);			/* Number of heads */
	*(BYTE*)(tbl+28)=(BYTE)(b_vol); *((BYTE*)(tbl+28)+1)=(BYTE)((WORD)(b_vol)>>8); *((BYTE*)(tbl+28)+2)=(BYTE)((DWORD)(b_vol)>>16); *((BYTE*)(tbl+28)+3)=(BYTE)((DWORD)(b_vol)>>24);		/* Hidden sectors */
	n = get_fattime();						/* Use current time as VSN */
	if (fmt == 3) {
		*(BYTE*)(tbl+67)=(BYTE)(n); *((BYTE*)(tbl+67)+1)=(BYTE)((WORD)(n)>>8); *((BYTE*)(tbl+67)+2)=(BYTE)((DWORD)(n)>>16); *((BYTE*)(tbl+67)+3)=(BYTE)((DWORD)(n)>>24);		/* VSN */
		*(BYTE*)(tbl+36)=(BYTE)(n_fat); *((BYTE*)(tbl+36)+1)=(BYTE)((WORD)(n_fat)>>8); *((BYTE*)(tbl+36)+2)=(BYTE)((DWORD)(n_fat)>>16); *((BYTE*)(tbl+36)+3)=(BYTE)((DWORD)(n_fat)>>24);	/* Number of sectors per FAT */
		*(BYTE*)(tbl+44)=(BYTE)(2); *((BYTE*)(tbl+44)+1)=(BYTE)((WORD)(2)>>8); *((BYTE*)(tbl+44)+2)=(BYTE)((DWORD)(2)>>16); *((BYTE*)(tbl+44)+3)=(BYTE)((DWORD)(2)>>24);		/* Root directory start cluster (2) */
		*(BYTE*)(tbl+48)=(BYTE)(1); *((BYTE*)(tbl+48)+1)=(BYTE)((WORD)(1)>>8);			/* FSInfo record offset (VBR+1) */
		*(BYTE*)(tbl+50)=(BYTE)(6); *((BYTE*)(tbl+50)+1)=(BYTE)((WORD)(6)>>8);		/* Backup boot record offset (VBR+6) */
		tbl[64] = 0x80;			/* Drive number */
		tbl[66] = 0x29;			/* Extended boot signature */
		mem_cpy(tbl+71, "NO NAME    " "FAT32   ", 19);	/* Volume label, FAT signature */
	} else {
		*(BYTE*)(tbl+39)=(BYTE)(n); *((BYTE*)(tbl+39)+1)=(BYTE)((WORD)(n)>>8); *((BYTE*)(tbl+39)+2)=(BYTE)((DWORD)(n)>>16); *((BYTE*)(tbl+39)+3)=(BYTE)((DWORD)(n)>>24);			/* VSN */
		*(BYTE*)(tbl+22)=(BYTE)(n_fat); *((BYTE*)(tbl+22)+1)=(BYTE)((WORD)(n_fat)>>8);	/* Number of sectors per FAT */
		tbl[36] = 0x80;				/* Drive number */
		tbl[38] = 0x29;				/* Extended boot signature */
		mem_cpy(tbl+43, "NO NAME    " "FAT     ", 19);	/* Volume label, FAT signature */
	}
	*(BYTE*)(tbl+510)=(BYTE)(0xAA55); *((BYTE*)(tbl+510)+1)=(BYTE)((WORD)(0xAA55)>>8);			/* Signature (Offset is fixed here regardless of sector size) */
	if (disk_write(pdrv, tbl, b_vol, 1) != RES_OK)	/* Write it to the VBR sector */
		return FR_DISK_ERR;
	if (fmt == 3)							/* Write backup VBR if needed (VBR+6) */
		disk_write(pdrv, tbl, b_vol + 6, 1);

	/* Initialize FAT area */
	wsect = b_fat;
	for (i = 0; i < 1; i++) {		/* Initialize each FAT copy */
		mem_set(tbl, 0, 512U);			/* 1st sector of the FAT  */
		n = md;								/* Media descriptor byte */
		if (fmt != 3) {
			n |= (fmt == 1) ? 0x00FFFF00 : 0xFFFFFF00;
			*(BYTE*)(tbl+0)=(BYTE)(n); *((BYTE*)(tbl+0)+1)=(BYTE)((WORD)(n)>>8); *((BYTE*)(tbl+0)+2)=(BYTE)((DWORD)(n)>>16); *((BYTE*)(tbl+0)+3)=(BYTE)((DWORD)(n)>>24);				/* Reserve cluster #0-1 (FAT12/16) */
		} else {
			n |= 0xFFFFFF00;
			*(BYTE*)(tbl+0)=(BYTE)(n); *((BYTE*)(tbl+0)+1)=(BYTE)((WORD)(n)>>8); *((BYTE*)(tbl+0)+2)=(BYTE)((DWORD)(n)>>16); *((BYTE*)(tbl+0)+3)=(BYTE)((DWORD)(n)>>24);				/* Reserve cluster #0-1 (FAT32) */
			*(BYTE*)(tbl+4)=(BYTE)(0xFFFFFFFF); *((BYTE*)(tbl+4)+1)=(BYTE)((WORD)(0xFFFFFFFF)>>8); *((BYTE*)(tbl+4)+2)=(BYTE)((DWORD)(0xFFFFFFFF)>>16); *((BYTE*)(tbl+4)+3)=(BYTE)((DWORD)(0xFFFFFFFF)>>24);
			*(BYTE*)(tbl+8)=(BYTE)(0x0FFFFFFF); *((BYTE*)(tbl+8)+1)=(BYTE)((WORD)(0x0FFFFFFF)>>8); *((BYTE*)(tbl+8)+2)=(BYTE)((DWORD)(0x0FFFFFFF)>>16); *((BYTE*)(tbl+8)+3)=(BYTE)((DWORD)(0x0FFFFFFF)>>24);	/* Reserve cluster #2 for root dir */
		}
		if (disk_write(pdrv, tbl, wsect++, 1) != RES_OK)
			return FR_DISK_ERR;
		mem_set(tbl, 0, 512U);			/* Fill following FAT entries with zero */
		for (n = 1; n < n_fat; n++) {		/* This loop may take a time on FAT32 volume due to many single sector writes */
			if (disk_write(pdrv, tbl, wsect++, 1) != RES_OK)
				return FR_DISK_ERR;
		}
	}

	/* Initialize root directory */
	i = (fmt == 3) ? au : n_dir;
	do {
		if (disk_write(pdrv, tbl, wsect++, 1) != RES_OK)
			return FR_DISK_ERR;
	} while (--i);


	/* Create FSInfo if needed */
	if (fmt == 3) {
		*(BYTE*)(tbl+0)=(BYTE)(0x41615252); *((BYTE*)(tbl+0)+1)=(BYTE)((WORD)(0x41615252)>>8); *((BYTE*)(tbl+0)+2)=(BYTE)((DWORD)(0x41615252)>>16); *((BYTE*)(tbl+0)+3)=(BYTE)((DWORD)(0x41615252)>>24);
		*(BYTE*)(tbl+484)=(BYTE)(0x61417272); *((BYTE*)(tbl+484)+1)=(BYTE)((WORD)(0x61417272)>>8); *((BYTE*)(tbl+484)+2)=(BYTE)((DWORD)(0x61417272)>>16); *((BYTE*)(tbl+484)+3)=(BYTE)((DWORD)(0x61417272)>>24);
		*(BYTE*)(tbl+488)=(BYTE)(n_clst - 1); *((BYTE*)(tbl+488)+1)=(BYTE)((WORD)(n_clst - 1)>>8); *((BYTE*)(tbl+488)+2)=(BYTE)((DWORD)(n_clst - 1)>>16); *((BYTE*)(tbl+488)+3)=(BYTE)((DWORD)(n_clst - 1)>>24);	/* Number of free clusters */
		*(BYTE*)(tbl+492)=(BYTE)(2); *((BYTE*)(tbl+492)+1)=(BYTE)((WORD)(2)>>8); *((BYTE*)(tbl+492)+2)=(BYTE)((DWORD)(2)>>16); *((BYTE*)(tbl+492)+3)=(BYTE)((DWORD)(2)>>24);				/* Last allocated cluster# */
		*(BYTE*)(tbl+510)=(BYTE)(0xAA55); *((BYTE*)(tbl+510)+1)=(BYTE)((WORD)(0xAA55)>>8);
		disk_write(pdrv, tbl, b_vol + 1, 1);	/* Write original (VBR+1) */
		disk_write(pdrv, tbl, b_vol + 7, 1);	/* Write backup (VBR+7) */
	}

	return (disk_ioctl(pdrv, 0, 0) == RES_OK) ? FR_OK : FR_DISK_ERR;
}






/*-----------------------------------------------------------------------*/
/* Get a string from the file                                            */
/*-----------------------------------------------------------------------*/
TCHAR* f_gets (
	TCHAR* buff,	/* Pointer to the string buffer to read */
	int len,		/* Size of string buffer (characters) */
	FIL* fil		/* Pointer to the file object */
)
{
	int n = 0;
	TCHAR c, *p = buff;
	BYTE s[2];
	UINT rc;


	while (n < len - 1) {			/* Read bytes until buffer gets filled */
		f_read(fil, s, 1, &rc);
		if (rc != 1) break;			/* Break on EOF or error */
		c = s[0];
		if (c == '\r') continue;	/* Strip '\r' */
		*p++ = c;
		n++;
		if (c == '\n') break;		/* Break on EOL */
	}
	*p = 0;
	return n ? buff : 0;			/* When no data read (eof or error), return with error. */
}



#include <stdarg.h>
/*-----------------------------------------------------------------------*/
/* Put a character to the file                                           */
/*-----------------------------------------------------------------------*/
int f_putc (
	TCHAR c,	/* A character to be output */
	FIL* fil	/* Pointer to the file object */
)
{
	UINT bw, btw;
	BYTE s[3];


	if (c == '\n') f_putc ('\r', fil);	/* LF -> CRLF conversion */

	s[0] = (BYTE)c;
	btw = 1;
	f_write(fil, s, btw, &bw);		/* Write the char to the file */
	return (bw == btw) ? 1 : (-1);	/* Return the result */
}




/*-----------------------------------------------------------------------*/
/* Put a string to the file                                              */
/*-----------------------------------------------------------------------*/
int f_puts (
	const TCHAR* str,	/* Pointer to the string to be output */
	FIL* fil			/* Pointer to the file object */
)
{
	int n;


	for (n = 0; *str; str++, n++) {
		if (f_putc(*str, fil) == (-1)) return (-1);
	}
	return n;
}




/*-----------------------------------------------------------------------*/
/* Put a formatted string to the file                                    */
/*-----------------------------------------------------------------------*/
int f_printf (
	FIL* fil,			/* Pointer to the file object */
	const TCHAR* str,	/* Pointer to the format string */
	...					/* Optional arguments... */
)
{
	va_list arp;
	BYTE f, r;
	UINT i, j, w;
	ULONG v;
	TCHAR c, d, s[16], *p;
	int res, chc, cc;


	va_start(arp, str);

	for (cc = res = 0; cc != (-1); res += cc) {
		c = *str++;
		if (c == 0) break;			/* End of string */
		if (c != '%') {				/* Non escape character */
			cc = f_putc(c, fil);
			if (cc != (-1)) cc = 1;
			continue;
		}
		w = f = 0;
		c = *str++;
		if (c == '0') {				/* Flag: '0' padding */
			f = 1; c = *str++;
		} else {
			if (c == '-') {			/* Flag: left justified */
				f = 2; c = *str++;
			}
		}
		while ((((c)>= '0')&&((c)<= '9'))) {		/* Precision */
			w = w * 10 + c - '0';
			c = *str++;
		}
		if (c == 'l' || c == 'L') {	/* Prefix: Size is long int */
			f |= 4; c = *str++;
		}
		if (!c) break;
		d = c;
		if ((((d)>= 'a')&&((d)<= 'z'))) d -= 0x20;
		switch (d) {				/* Type is... */
		case 'S' :					/* String */
			p = va_arg(arp, TCHAR*);
			for (j = 0; p[j]; j++) ;
			chc = 0;
			if (!(f & 2)) {
				while (j++ < w) chc += (cc = f_putc(' ', fil));
			}
			chc += (cc = f_puts(p, fil));
			while (j++ < w) chc += (cc = f_putc(' ', fil));
			if (cc != (-1)) cc = chc;
			continue;
		case 'C' :					/* Character */
			cc = f_putc((TCHAR)va_arg(arp, int), fil); continue;
		case 'B' :					/* Binary */
			r = 2; break;
		case 'O' :					/* Octal */
			r = 8; break;
		case 'D' :					/* Signed decimal */
		case 'U' :					/* Unsigned decimal */
			r = 10; break;
		case 'X' :					/* Hexdecimal */
			r = 16; break;
		default:					/* Unknown type (passthrough) */
			cc = f_putc(c, fil); continue;
		}

		/* Get an argument and put it in numeral */
		v = (f & 4) ? (ULONG)va_arg(arp, long) : ((d == 'D') ? (ULONG)(long)va_arg(arp, int) : (ULONG)va_arg(arp, unsigned int));
		if (d == 'D' && (v & 0x80000000)) {
			v = 0 - v;
			f |= 8;
		}
		i = 0;
		do {
			d = (TCHAR)(v % r); v /= r;
			if (d > 9) d += (c == 'x') ? 0x27 : 0x07;
			s[i++] = d + '0';
		} while (v && i < sizeof(s) / sizeof(s[0]));
		if (f & 8) s[i++] = '-';
		j = i; d = (f & 1) ? '0' : ' ';
		res = 0;
		while (!(f & 2) && j++ < w) res += (cc = f_putc(d, fil));
		do res += (cc = f_putc(s[--i], fil)); while(i);
		while (j++ < w) res += (cc = f_putc(' ', fil));
		if (cc != (-1)) cc = res;
	}

	va_end(arp);
	return (cc == (-1)) ? cc : res;
}

