/* stdio.h standard header */
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




/* ystdio.h internal header */
/* Copyright 2009-2010 IAR Systems AB. */

  #pragma system_include



  
/* File system functions that have debug variants. They are agnostic on 
   whether the library is full or normal. */

__intrinsic __nounwind int remove(const char *);
__intrinsic __nounwind int rename(const char *, const char *);






/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.042:0576 */



/* Module consistency. */
#pragma rtmodel="__dlib_file_descriptor","0"

                /* macros */









                /* type definitions */
typedef _Fpost fpos_t;

                /* printf and scanf pragma support */
#pragma language=save
#pragma language=extended




             /* Corresponds to fgets(char *, int, stdin); */
_Pragma("function_effects = no_read(1), always_returns")    __intrinsic __nounwind char * __gets(char *, int);
_Pragma("function_effects = no_read(1), always_returns")    __intrinsic __nounwind char * gets(char *);
_Pragma("function_effects = no_write(1), always_returns")    __intrinsic __nounwind void perror(const char *);
_Pragma("function_effects = no_write(1), always_returns")    _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int printf(const char *, ...);
_Pragma("function_effects = no_write(1), always_returns")    __intrinsic __nounwind int puts(const char *);
_Pragma("function_effects = no_write(1), always_returns")    _Pragma("__scanf_args") _Pragma("library_default_requirements _Scanf = unknown")  __intrinsic __nounwind int scanf(const char *, ...);
_Pragma("function_effects = no_read(1), no_write(2), always_returns") _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int sprintf(char *, 
                                                 const char *, ...);
_Pragma("function_effects = no_write(1,2), always_returns") _Pragma("__scanf_args") _Pragma("library_default_requirements _Scanf = unknown")  __intrinsic __nounwind int sscanf(const char *, 
                                                const char *, ...);
             __intrinsic __nounwind char * tmpnam(char *);
             /* Corresponds to "ungetc(c, stdout)" */
             __intrinsic __nounwind int __ungetchar(int);
_Pragma("function_effects = no_write(1), always_returns")    _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int vprintf(const char *,
                                                 __Va_list);
  _Pragma("function_effects = no_write(1), always_returns")    _Pragma("__scanf_args") _Pragma("library_default_requirements _Scanf = unknown")  __intrinsic __nounwind int vscanf(const char *, 
                                                  __Va_list);
  _Pragma("function_effects = no_write(1,2), always_returns") _Pragma("__scanf_args") _Pragma("library_default_requirements _Scanf = unknown")  __intrinsic __nounwind int vsscanf(const char *, 
                                                   const char *, 
                                                   __Va_list);
_Pragma("function_effects = no_read(1), no_write(2), always_returns")  _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int vsprintf(char *, 
                                                   const char *,
                                                   __Va_list);
              /* Corresponds to fwrite(p, x, y, stdout); */
_Pragma("function_effects = no_write(1), always_returns")      __intrinsic __nounwind size_t __write_array(const void *, size_t, size_t);
  _Pragma("function_effects = no_read(1), no_write(3), always_returns") _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int snprintf(char *, size_t, 
                                                    const char *, ...);
  _Pragma("function_effects = no_read(1), no_write(3), always_returns") _Pragma("__printf_args") _Pragma("library_default_requirements _Printf = unknown") __intrinsic __nounwind int vsnprintf(char *, size_t,
                                                     const char *, 
                                                     __Va_list);

              __intrinsic __nounwind int getchar(void);
              __intrinsic __nounwind int putchar(int);



#pragma language=restore





/*
 * Copyright (c) 1992-2002 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
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



/***************************************************************************//**
 * @file em_usb.h
 * @brief USB protocol stack library API for EFM32/EZR32.
 * @version 4.0.0
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
 * @file usbconfig.h
 * @brief USB protocol stack library, application supplied configuration options.
 * @version 4.0.0
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




/****************************************************************************
**                                                                         **
** Specify total number of endpoints used (in addition to EP0).            **
**                                                                         **
*****************************************************************************/
/* Defined in plugin */

/****************************************************************************
**                                                                         **
** Specify number of application timers you need.                          **
**                                                                         **
*****************************************************************************/
/* Defined in plugin */

/****************************************************************************
**                                                                         **
** USB HID keyboard class device driver definitions.                       **
**                                                                         **
*****************************************************************************/

/* Define interface numbers */



/* Define timer ID's */
                                        /* rate defined in the HID class spec.*/
                                        /* interrupt IN endpoint descriptor.  */

/****************************************************************************
**                                                                         **
** Configuration options for the CDC driver.                               **
**                                                                         **
*****************************************************************************/

/* Define interface numbers */


/* Define USB endpoint addresses for the interfaces */



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
/* stddef.h standard header */
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






                /* macros */


                /* type definitions */
  typedef _Ptrdifft ptrdiff_t;

  typedef _Wchart wchar_t;




/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
/***************************************************************************//**
 * @file em_common.h
 * @brief Emlib general purpose utilities.
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
/* stdbool.h header */
/* Copyright 2003-2010 IAR Systems AB.  */

/* NOTE: IAR Extensions must be enabled in order to use the bool type! */


  #pragma system_include







/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */


/***************************************************************************//**
 * @addtogroup EM_Library
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup COMMON
 * @brief Emlib general purpose utilities.
 * @{
 ******************************************************************************/


/** Macro for getting minimum value. */
/** Macro for getting maximum value. */

/** Macros for handling packed structs. */

/** Macros for handling aligned structs. */


/***************************************************************************//**
 * @brief
 *   Count trailing number of zero's.
 *
 * @note
 *   Disabling SWDClk will disable the debug interface, which may result in
 *   a lockout if done early in startup (before debugger is able to halt core).
 *
 * @param[in] value
 *   Data value to check for number of trailing zero bits.
 *
 * @return
 *   Number of trailing zero's in value.
 ******************************************************************************/
static inline uint32_t EFM32_CTZ(uint32_t value)
{
  return __CLZ(__RBIT(value));

}

/** @} (end addtogroup COMMON) */
/** @} (end addtogroup EM_Library) */


/***************************************************************************//**
 * @file em_int.h
 * @brief Interrupt enable/disable unit API
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

extern uint32_t INT_LockCnt;


/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */
/** @endcond */

/***************************************************************************//**
 * @addtogroup EM_Library
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup INT
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @brief
 *   Disable interrupts.
 *
 * @details
 *   Disable interrupts and increment lock level counter.
 *
 * @return
 *   The resulting interrupt nesting level.
 *
 ******************************************************************************/
static inline uint32_t INT_Disable(void)
{
  __disable_interrupt();
  if (INT_LockCnt < 0xffffffffU)
  {
    INT_LockCnt++;
  }

  return INT_LockCnt;
}

/***************************************************************************//**
 * @brief
 *   Enable interrupts.
 *
 * @return
 *   The resulting interrupt nesting level.
 *
 * @details
 *   Decrement interrupt lock level counter and enable interrupts if counter
 *   reached zero.
 *
 ******************************************************************************/
static inline uint32_t INT_Enable(void)
{
  uint32_t retVal;

  if (INT_LockCnt > 0)
  {
    INT_LockCnt--;
    retVal = INT_LockCnt;
    if (retVal == 0)
    {
      __enable_interrupt();
    }
    return retVal;
  }
  else
  {
    return 0;
  }
}

/** @} (end addtogroup INT) */
/** @} (end addtogroup EM_Library) */






/***************************************************************************//**
 * @addtogroup USB
 * @brief USB HOST and DEVICE protocol stacks.
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup USB_COMMON
 * @brief Common parts for both HOST and DEVICE USB stacks, see @ref usb_device
 *        and @ref usb_host pages for device and host library documentation.
 * @{
 ******************************************************************************/


/* SETUP request, direction of data stage */

/* SETUP request type */

/* SETUP request recipient */

/* SETUP standard request codes for Full Speed devices */

/* SETUP class request codes */

/* SETUP command GET/SET_DESCRIPTOR decriptor types */


/* Misc. USB definitions */









/*** Triplet for the device descriptor of a composite device using IAD descriptors. ***/


/* uchar.h added header for TR 19769 */
/* Copyright 2009-2010 IAR Systems AB.  */

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






                /* macros */

/* Values of char16_t are UTF-16 encoded */
/* Values of char32_t are UTF-32 encoded */


                /* TYPE DEFINITIONS */
typedef _Mbstatet mbstate_t;
typedef unsigned short char16_t;
typedef unsigned long char32_t;

                /* declarations */
__intrinsic __nounwind size_t mbrtoc16(char16_t *, const char *,
                             size_t, mbstate_t *);
__intrinsic __nounwind size_t c16rtomb(char *, char16_t,
                             mbstate_t *);

__intrinsic __nounwind size_t mbrtoc32(char32_t *, const char *,
                             size_t, mbstate_t *);
__intrinsic __nounwind size_t c32rtomb(char *, char32_t,
                             mbstate_t *);





/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */


/** Macro for creating USB compliant UTF-16LE UNICODE string descriptors.
 *  @n Example: STATIC_CONST_STRING_DESC( iManufacturer, 'E','n','e','r','g','y',' ','M','i','c','r','o',' ','A','S' );
 *  @note The size of the resulting struct will be two byte larger than a USB string
 *        descriptor. This is to accommodate a terminating null char for the string.
 *        The value assigned to the 'len' member does not take this into account
 *        and is therefore correct usb wise.
 */

/** Macro for creating USB compliant language string descriptors.
 *  @n Example: STATIC_CONST_STRING_DESC_LANGID( langID, 0x04, 0x09 );
 */

/** Macro for creating WORD (4 byte) aligned uint8_t array with size which
 *  is a multiple of WORD size.
 *  @n Example: @n UBUF( rxBuffer, 37 );  =>  uint8_t rxBuffer[ 40 ];
 */


/** @brief USB transfer status enumerator. */
typedef enum
{
  /* NOTE: Please keep in sync with table errMsg[] in em_usbhal.c */
  USB_STATUS_OK              = 0,               /**< No errors detected.                               */
  USB_STATUS_REQ_ERR         = -1,              /**< Setup request error.                              */
  USB_STATUS_EP_BUSY         = -2,              /**< Endpoint is busy.                                 */
  USB_STATUS_REQ_UNHANDLED   = -3,              /**< Setup request not handled.                        */
  USB_STATUS_ILLEGAL         = -4,              /**< Illegal operation attempted.                      */
  USB_STATUS_EP_STALLED      = -5,              /**< Endpoint is stalled.                              */
  USB_STATUS_EP_ABORTED      = -6,              /**< Endpoint transfer was aborted.                    */
  USB_STATUS_EP_ERROR        = -7,              /**< Endpoint transfer error.                          */
  USB_STATUS_EP_NAK          = -8,              /**< Endpoint NAK'ed transfer request.                 */
  USB_STATUS_DEVICE_UNCONFIGURED = -9,          /**< Device is unconfigured.                           */
  USB_STATUS_DEVICE_SUSPENDED    = -10,         /**< Device is suspended.                              */
  USB_STATUS_DEVICE_RESET    = -11,             /**< Device is/was reset.                              */
  USB_STATUS_TIMEOUT         = -12,             /**< Transfer timeout.                                 */
  USB_STATUS_DEVICE_REMOVED  = -13,             /**< Device was removed.                               */
  USB_STATUS_HC_BUSY         = -14,             /**< Host channel is busy.                             */
  USB_STATUS_DEVICE_MALFUNCTION = -15,          /**< Malfunctioning device attached.                   */
  USB_STATUS_PORT_OVERCURRENT = -16,            /**< VBUS shortcircuit/overcurrent failure.            */
} USB_Status_TypeDef;
/** @} (end addtogroup USB_COMMON) */


/***************************************************************************//**
 * @addtogroup USB_DEVICE
 * @brief USB DEVICE protocol stack, see @ref usb_device page for detailed documentation.
 * @{
 ******************************************************************************/



/** @brief USB device state enumerator. */
typedef enum
{
  USBD_STATE_NONE       = 0,                    /**< Device state is undefined/unknown.                */
  USBD_STATE_ATTACHED   = 1,                    /**< Device state is ATTACHED.                         */
  USBD_STATE_POWERED    = 2,                    /**< Device state is POWERED.                          */
  USBD_STATE_DEFAULT    = 3,                    /**< Device state is DEFAULT.                          */
  USBD_STATE_ADDRESSED  = 4,                    /**< Device state is ADDRESSED.                        */
  USBD_STATE_CONFIGURED = 5,                    /**< Device state is CONFIGURED.                       */
  USBD_STATE_SUSPENDED  = 6,                    /**< Device state is SUSPENDED.                        */
  USBD_STATE_LASTMARKER = 7,                    /**< Device state enum end marker.                     */
} USBD_State_TypeDef;
/** @} (end addtogroup USB_DEVICE) */

/** @addtogroup USB_COMMON
 *  @{*/

/** @brief USB Setup request package. */
_Pragma( "pack( 1 )" )
typedef struct
{
  union
  {
    struct
    {
      union
      {
        struct
        {
          uint8_t Recipient : 5;                /**< Request recipient (device, interface, endpoint or other).*/
          uint8_t Type      : 2;                /**< Request type (standard, class or vendor).         */
          uint8_t Direction : 1;                /**< Transfer direction of SETUP data phase.           */
        };
        uint8_t bmRequestType;                  /**< Request characteristics.                          */
      };
      uint8_t   bRequest;                       /**< Request code.                                     */
      uint16_t  wValue;                         /**< Varies according to request.                      */
      uint16_t  wIndex;                         /**< Index or offset, varies according to request.     */
      uint16_t  wLength;                        /**< Number of bytes to transfer if there is a data stage.*/
    };
    uint32_t  dw[2];
  };
}  USB_Setup_TypeDef;
_Pragma( "pack()" )


/** @brief USB Device Descriptor. */
_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t  bLength;                             /**< Size of this descriptor in bytes                  */
  uint8_t  bDescriptorType;                     /**< Constant DEVICE Descriptor Type                   */
  uint16_t bcdUSB;                              /**< USB Specification Release Number in Binary-Coded
                                                     Decimal                                           */
  uint8_t  bDeviceClass;                        /**< Class code (assigned by the USB-IF)               */
  uint8_t  bDeviceSubClass;                     /**< Subclass code (assigned by the USB-IF)            */
  uint8_t  bDeviceProtocol;                     /**< Protocol code (assigned by the USB-IF)            */
  uint8_t  bMaxPacketSize0;                     /**< Maximum packet size for endpoint zero             */
  uint16_t idVendor;                            /**< Vendor ID (assigned by the USB-IF)                */
  uint16_t idProduct;                           /**< Product ID (assigned by the manufacturer)         */
  uint16_t bcdDevice;                           /**< Device release number in binary-coded decimal     */
  uint8_t  iManufacturer;                       /**< Index of string descriptor describing manufacturer*/
  uint8_t  iProduct;                            /**< Index of string descriptor describing product     */
  uint8_t  iSerialNumber;                       /**< Index of string descriptor describing the device
                                                     serialnumber                                      */
  uint8_t  bNumConfigurations;                  /**< Number of possible configurations                 */
}  USB_DeviceDescriptor_TypeDef;
_Pragma( "pack()" )


/** @brief USB Configuration Descriptor. */
_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t  bLength;                             /**< Size of this descriptor in bytes                  */
  uint8_t  bDescriptorType;                     /**< Constant CONFIGURATION Descriptor Type            */
  uint16_t wTotalLength;                        /**< Total length of data returned for this
                                                     configuration. Includes the combined length of all
                                                     descriptors (configuration, interface, endpoint,
                                                     and class- or vendor-specific) returned for this
                                                     configuration.                                    */
  uint8_t  bNumInterfaces;                      /**< Number of interfaces supported by this
                                                     configuration                                     */
  uint8_t  bConfigurationValue;                 /**< Value to use as an argument to the
                                                     SetConfiguration request to select this
                                                     configuration.                                    */
  uint8_t  iConfiguration;                      /**< Index of string descriptor describing this
                                                     configuration.                                    */
  uint8_t  bmAttributes;                        /**< Configuration characteristics.
                                                     @n D7: Reserved (set to one)
                                                     @n D6: Self-powered
                                                     @n D5: Remote Wakeup
                                                     @n D4...0: Reserved (reset to zero)               */
  uint8_t  bMaxPower;                           /**< Maximum power consumption of the USB device, unit
                                                     is 2mA per LSB                                    */
}  USB_ConfigurationDescriptor_TypeDef;
_Pragma( "pack()" )


/** @brief USB Interface Descriptor. */
_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t bLength;                              /**< Size of this descriptor in bytes.                 */
  uint8_t bDescriptorType;                      /**< Constant INTERFACE Descriptor Type.               */
  uint8_t bInterfaceNumber;                     /**< Number of this interface. Zero-based value
                                                     identifying the index in the array of concurrent
                                                     interfaces supported by this configuration.       */
  uint8_t bAlternateSetting;                    /**< Value used to select this alternate setting for
                                                     the interface identified in the prior field.      */
  uint8_t bNumEndpoints;                        /**< Number of endpoints used by this interface
                                                     (excluding endpoint zero). If this value is zero,
                                                     this interface only uses the Default Control Pipe.*/
  uint8_t bInterfaceClass;                      /**< Class code (assigned by the USB-IF). A value
                                                     of zero is reserved for future standardization. If
                                                     this field is set to FFH, the interface class is
                                                     vendor-specific. All other values are reserved for
                                                     assignment by the USB-IF.                         */
  uint8_t bInterfaceSubClass;                   /**< Subclass code (assigned by the USB-IF). These codes
                                                     are qualified by the value of the bInterfaceClass
                                                     field. If the bInterfaceClass field is reset to
                                                     zero, this field must also be reset to zero. If
                                                     the bInterfaceClass field is not set to FFH, all
                                                     values are reserved forassignment by the USB-IF.  */
  uint8_t bInterfaceProtocol;                   /**< Protocol code (assigned by the USB). These codes
                                                     are qualified by the value of the bInterfaceClass
                                                     and the bInterfaceSubClass fields. If an interface
                                                     supports class-specific requests, this code
                                                     identifies the protocols that the device uses as
                                                     defined by the specification of the device class.
                                                     If this field is reset to zero, the device does
                                                     not use a class-specific protocol on this
                                                     interface. If this field is set to FFH, the device
                                                     uses a vendor-specific protocol for this interface*/
  uint8_t iInterface;                           /**< Index of string descriptor describing this
                                                     interface.                                        */
}  USB_InterfaceDescriptor_TypeDef;
_Pragma( "pack()" )


/** @brief USB Endpoint Descriptor. */
_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t   bLength;                            /**< Size of this descriptor in bytes                  */
  uint8_t   bDescriptorType;                    /**< Constant ENDPOINT Descriptor Type                 */
  uint8_t   bEndpointAddress;                   /**< The address of the endpoint                       */
  uint8_t   bmAttributes;                       /**< This field describes the endpoint attributes      */
  uint16_t  wMaxPacketSize;                     /**< Maximum packet size for the endpoint              */
  uint8_t   bInterval;                          /**< Interval for polling EP for data transfers        */
}  USB_EndpointDescriptor_TypeDef;
_Pragma( "pack()" )


/** @brief USB String Descriptor. */
_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t len;                                  /**< Size of this descriptor in bytes.                 */
  uint8_t type;                                 /**< Constant STRING Descriptor Type.                  */
  char16_t name[];                              /**< The string encoded with UTF-16LE UNICODE charset. */
}  USB_StringDescriptor_TypeDef;
_Pragma( "pack()" )

/** @} (end addtogroup USB_COMMON) */

/*** -------------------- Serial port debug configuration ---------------- ***/


/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */

/* Hardware constraint, do not change. */

/* The DMA engine use one FIFO ram word for each host channel. */




/** @endcond */

/*** -------------------- Common API definitions ------------------------- ***/

/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */

/** @endcond */

/** @addtogroup USB_COMMON
 *  @{*/

/***************************************************************************//**
 * @brief
 *  USB transfer callback function.
 *
 * @details
 *  The callback function is called when a transfer has completed. An application
 *  should check the status, xferred and optionally the remaining parameters
 *  before deciding if the transfer is usable. In the case where the transfer
 *  is part of a control request data stage, the callback function should
 *  return an appropriate @ref USB_Status_TypeDef status.
 *
 * @param[in] status
 *   The transfer status. See @ref USB_Status_TypeDef.
 *
 * @param[in] xferred
 *   Number of bytes actually transferred.
 *
 * @param[in] remaining
 *   Number of bytes not transferred.
 *
 * @return
 *   @ref USB_STATUS_OK on success, else an appropriate error code.
 ******************************************************************************/
typedef int  (*USB_XferCompleteCb_TypeDef)( USB_Status_TypeDef status, uint32_t xferred, uint32_t remaining );

/***************************************************************************//**
 * @brief
 *  USBTIMER callback function.
 *
 * @details
 *  The callback function is called when an USBTIMER has expired. The callback
 *  is done with interrupts disabled.
 ******************************************************************************/
typedef void (*USBTIMER_Callback_TypeDef)(  void );

char *USB_GetErrorMsgString(            int error );


void  USBTIMER_DelayMs(                 uint32_t msec );
void  USBTIMER_DelayUs(                 uint32_t usec );
void  USBTIMER_Init(                    void );

/** @} (end addtogroup USB_COMMON) */

/** @addtogroup USB_DEVICE
 *  @{*/
/*** -------------------- DEVICE mode API definitions -------------------- ***/

/***************************************************************************//**
 * @brief
 *  USB Reset callback function.
 * @details
 *  Called whenever USB reset signalling is detected on the USB port.
 ******************************************************************************/
typedef void (*USBD_UsbResetCb_TypeDef)( void );

/***************************************************************************//**
 * @brief
 *  USB Start Of Frame (SOF) interrupt callback function.
 *
 * @details
 *  Called at each SOF interrupt (if enabled),
 *
 * @param[in] sofNr
 *   Current frame number. The value rolls over to 0 after 16383 (0x3FFF).
 ******************************************************************************/
typedef void (*USBD_SofIntCb_TypeDef)( uint16_t sofNr );

/***************************************************************************//**
 * @brief
 *  USB State change callback function.
 *
 * @details
 *  Called whenever the device change state.
 *
 * @param[in] oldState
 *   The device USB state just leaved. See @ref USBD_State_TypeDef.
 *
 * @param[in] newState
 *   New (the current) USB device state. See @ref USBD_State_TypeDef.
 ******************************************************************************/
typedef void (*USBD_DeviceStateChangeCb_TypeDef)( USBD_State_TypeDef oldState, USBD_State_TypeDef newState );

/***************************************************************************//**
 * @brief
 *  USB power mode callback function.
 *
 * @details
 *  Called whenever the device stack needs to query if the device is currently
 *  self- or bus-powered. Typically when host has issued an @ref GET_STATUS
 *  setup command.
 *
 * @return
 *  True if self-powered, false otherwise.
 ******************************************************************************/
typedef _Bool (*USBD_IsSelfPoweredCb_TypeDef)( void );

/***************************************************************************//**
 * @brief
 *  USB setup request callback function.
 *
 * @details
 *  Called on each setup request received from host. This gives the application a
 *  possibility to extend or override standard requests, and to implement class
 *  or vendor specific requests. Return @ref USB_STATUS_OK if the request is
 *  handled, return @ref USB_STATUS_REQ_ERR if it is an illegal request or
 *  return @ref USB_STATUS_REQ_UNHANDLED to pass the request on to the default
 *  request handler.
 *
 * @param[in] setup
 *  Pointer to an USB setup packet. See @ref USB_Setup_TypeDef.
 *
 * @return
 *  An appropriate status/error code. See @ref USB_Status_TypeDef.
 ******************************************************************************/
typedef int  (*USBD_SetupCmdCb_TypeDef)( const USB_Setup_TypeDef *setup );

/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */
struct USBD_Callbacks_TypeDef;
typedef struct USBD_Callbacks_TypeDef const *USBD_Callbacks_TypeDef_Pointer;
/** @endcond */


/** @brief USB Device stack initialization structure.
 *  @details This structure is passed to @ref USBD_Init() when starting up
 *  the device.                                                             */
typedef struct
{
  const USB_DeviceDescriptor_TypeDef      *deviceDescriptor;      /**< Pointer to a device descriptor.                */
  const uint8_t                           *configDescriptor;      /**< Pointer to a configuration descriptor.         */
  const void * const                      *stringDescriptors;     /**< Pointer to an array of string descriptor pointers.*/
  const uint8_t                           numberOfStrings;        /**< Number of strings in string descriptor array.  */
  const uint8_t                           *bufferingMultiplier;   /**< Pointer to an array defining the size of the
                                                                       endpoint buffers. The size is given in
                                                                       multiples of endpoint size. Generally a value
                                                                       of 1 (single) or 2 (double) buffering should be
                                                                       used.                                          */
  USBD_Callbacks_TypeDef_Pointer          callbacks;              /**< Pointer to struct with callbacks
                                                                       (@ref USBD_Callbacks_TypeDef). These callbacks
                                                                       are used by the device stack to signal events
                                                                       to or query the application.                   */
  const uint32_t                          reserved;               /**< Reserved for future use.                       */
} USBD_Init_TypeDef;


/** @brief USB Device stack callback structure.
 *  @details Callback functions used by the device stack to signal events or
 *  query status to/from the application. See @ref USBD_Init_TypeDef. Assign
 *  members to NULL if your application don't need a specific callback. */
typedef struct USBD_Callbacks_TypeDef
{
  const USBD_UsbResetCb_TypeDef           usbReset;               /**< Called whenever USB reset signalling is detected
                                                                       on the USB port.                                */
  const USBD_DeviceStateChangeCb_TypeDef  usbStateChange;         /**< Called whenever the device change state.        */
  const USBD_SetupCmdCb_TypeDef           setupCmd;               /**< Called on each setup request received from host.*/
  const USBD_IsSelfPoweredCb_TypeDef      isSelfPowered;          /**< Called whenever the device stack needs to query
                                                                       if the device is currently self- or bus-powered.
                                                                       Applies to devices which can operate in both modes.*/
  const USBD_SofIntCb_TypeDef             sofInt;                 /**< Called at each SOF interrupt. If NULL, the device
                                                                       stack will not enable the SOF interrupt.        */
} USBD_Callbacks_TypeDef;


/*** -------------------- DEVICE mode API -------------------------------- ***/

void                USBD_AbortAllTransfers( void );
int                 USBD_AbortTransfer(     int epAddr );
void                USBD_Connect(           void );
void                USBD_Disconnect(        void );
_Bool                USBD_EpIsBusy(          int epAddr );
USBD_State_TypeDef  USBD_GetUsbState(       void );
const char *        USBD_GetUsbStateName(   USBD_State_TypeDef state );
int                 USBD_Init(              const USBD_Init_TypeDef *p );
int                 USBD_Read(              int epAddr, void *data, int byteCount, USB_XferCompleteCb_TypeDef callback );
int                 USBD_RemoteWakeup(      void );
_Bool                USBD_SafeToEnterEM2(    void );
int                 USBD_StallEp(           int epAddr );
void                USBD_Stop(              void );
int                 USBD_UnStallEp(         int epAddr );
int                 USBD_Write(             int epAddr, void *data, int byteCount, USB_XferCompleteCb_TypeDef callback );

/** @} (end addtogroup USB_DEVICE) */


/** @} (end addtogroup USB) */


/***************************************************************************//**
 * @file em_cmu.h
 * @brief Clock management unit (CMU) API
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
 * @file em_bus.h
 * @brief RAM and peripheral bit-field set and clear API
 * @version 3.20.2
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
 * @addtogroup EM_Library
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup BUS
 * @brief BUS RAM and register bit/field read/write API
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @brief
 *   Perform a single-bit write operation on a 32-bit word in RAM
 *
 * @details
 *   This function uses Cortex-M bit-banding hardware to perform an atomic
 *   read-modify-write operation on a single bit write on a 32-bit word in RAM.
 *   Please refer to the reference manual for further details about bit-banding.
 *
 * @note
 *   This function is atomic on Cortex-M cores with bit-banding support. Bit-
 *   banding is a multicycle read-modify-write bus operation. RAM bit-banding is
 *   performed using the memory alias region at BITBAND_RAM_BASE.
 *
 * @param[in] addr Address of 32-bit word in RAM
 *
 * @param[in] bit Bit position to write, 0-31
 *
 * @param[in] val Value to set bit to, 0 or 1
 ******************************************************************************/
static inline void BUS_RamBitWrite(volatile uint32_t* const addr,
                                     unsigned int bit,
                                     unsigned int val)
{
  uint32_t aliasAddr =
    ((uint32_t) 0x22000000UL) + (((uint32_t)addr - (0x20000000UL)) * 32) + (bit * 4);

  *(volatile uint32_t *)aliasAddr = (uint32_t)val;
}


/***************************************************************************//**
 * @brief
 *   Perform a single-bit read operation on a 32-bit word in RAM
 *
 * @details
 *   This function uses Cortex-M bit-banding hardware to perform an atomic
 *   read operation on a single register bit. Please refer to the
 *   reference manual for further details about bit-banding.
 *
 * @note
 *   This function is atomic on Cortex-M cores with bit-banding support.
 *   RAM bit-banding is performed using the memory alias region
 *   at BITBAND_RAM_BASE.
 *
 * @param[in] addr RAM address
 *
 * @param[in] bit Bit position to read, 0-31
 *
 * @return
 *     The requested bit shifted to bit position 0 in the return value
 ******************************************************************************/
static inline unsigned int BUS_RamBitRead(volatile const uint32_t* const addr,
                                            unsigned int bit)
{
  uint32_t aliasAddr =
    ((uint32_t) 0x22000000UL) + (((uint32_t)addr - (0x20000000UL)) * 32) + (bit * 4);

  return *(volatile uint32_t *)aliasAddr;
}


/***************************************************************************//**
 * @brief
 *   Perform a single-bit write operation on a peripheral register
 *
 * @details
 *   This function uses Cortex-M bit-banding hardware to perform an atomic
 *   read-modify-write operation on a single register bit. Please refer to the
 *   reference manual for further details about bit-banding.
 *
 * @note
 *   This function is atomic on Cortex-M cores with bit-banding support. Bit-
 *   banding is a multicycle read-modify-write bus operation. Peripheral register
 *   bit-banding is performed using the memory alias region at BITBAND_PER_BASE.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] bit Bit position to write, 0-31
 *
 * @param[in] val Value to set bit to, 0 or 1
 ******************************************************************************/
static inline void BUS_RegBitWrite(volatile uint32_t* const addr,
                                     unsigned int bit,
                                     unsigned int val)
{
  uint32_t aliasAddr =
    ((uint32_t) 0x42000000UL) + (((uint32_t)addr - ((uint32_t) 0x40000000UL)) * 32) + (bit * 4);

  *(volatile uint32_t *)aliasAddr = (uint32_t)val;
}


/***************************************************************************//**
 * @brief
 *   Perform a single-bit read operation on a peripheral register
 *
 * @details
 *   This function uses Cortex-M bit-banding hardware to perform an atomic
 *   read operation on a single register bit. Please refer to the
 *   reference manual for further details about bit-banding.
 *
 * @note
 *   This function is atomic on Cortex-M cores with bit-banding support.
 *   Peripheral register bit-banding is performed using the memory alias
 *   region at BITBAND_PER_BASE.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] bit Bit position to read, 0-31
 *
 * @return
 *     The requested bit shifted to bit position 0 in the return value
 ******************************************************************************/
static inline unsigned int BUS_RegBitRead(volatile const uint32_t* const addr,
                                            unsigned int bit)
{
  uint32_t aliasAddr =
    ((uint32_t) 0x42000000UL) + (((uint32_t)addr - ((uint32_t) 0x40000000UL)) * 32) + (bit * 4);

  return *(volatile uint32_t *)aliasAddr;
}


/***************************************************************************//**
 * @brief
 *   Perform a masked set operation on peripheral register address.
 *
 * @details
 *   Peripheral register masked set provides a single-cycle and atomic set
 *   operation of a bit-mask in a peripheral register. All 1's in the mask are
 *   set to 1 in the register. All 0's in the mask are not changed in the
 *   register.
 *   RAMs and special peripherals are not supported. Please refer to the
 *   reference manual for further details about peripheral register field set.
 *
 * @note
 *   This function is single-cycle and atomic on cores with peripheral bit set
 *   and clear support. It uses the memory alias region at PER_BITSET_MEM_BASE.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] mask Mask to set
 ******************************************************************************/
static inline void BUS_RegMaskedSet(volatile uint32_t* const addr,
                                      const uint32_t mask)
{
  *addr |= mask;
}


/***************************************************************************//**
 * @brief
 *   Perform a masked clear operation on peripheral register address.
 *
 * @details
 *   Peripheral register masked clear provides a single-cycle and atomic clear
 *   operation of a bit-mask in a peripheral register. All 1's in the mask are
 *   set to 0 in the register.
 *   All 0's in the mask are not changed in the register.
 *   RAMs and special peripherals are not supported. Please refer to the
 *   reference manual for further details about peripheral register field clear.
 *
 * @note
 *   This function is single-cycle and atomic on cores with peripheral bit set
 *   and clear support. It uses the memory alias region at PER_BITCLR_MEM_BASE.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] mask Mask to clear
 ******************************************************************************/
static inline void BUS_RegMaskedClear(volatile uint32_t* const addr,
                                        const uint32_t mask)
{
  *addr &= ~mask;
}


/***************************************************************************//**
 * @brief
 *   Perform peripheral register masked clear and value write.
 *
 * @details
 *   This function first clears the mask in the peripheral register, then
 *   writes the value. Typically the mask is a bit-field in the register, and
 *   the value val is within the mask.
 *
 * @note
 *   This operation is not atomic. Note that the mask is first set to 0 before
 *   the val is set.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] mask Peripheral register mask
 *
 * @param[in] val Peripheral register value. The value must be shifted to the
                  correct bit position in the register.
 ******************************************************************************/
static inline void BUS_RegMaskedWrite(volatile uint32_t* const addr,
                                        const uint32_t mask,
                                        uint32_t val)
{
  *addr = (*addr & ~mask) | val;
}


/***************************************************************************//**
 * @brief
 *   Perform a peripheral register masked read
 *
 * @details
 *   Read an unshifted and masked value from a peripheral register.
 *
 * @note
 *   This operation is not hardware accelerated.
 *
 * @param[in] addr Peripheral register address
 *
 * @param[in] mask Peripheral register mask
 *
 * @return
 *   Unshifted and masked register value
 ******************************************************************************/
static inline uint32_t BUS_RegMaskedRead(volatile const uint32_t* const addr,
                                           const uint32_t mask)
{
  return *addr & mask;
}


/** @} (end addtogroup BUS) */
/** @} (end addtogroup EM_Library) */




/***************************************************************************//**
 * @addtogroup EM_Library
 * @{
 ******************************************************************************/

/***************************************************************************//**
 * @addtogroup CMU
 * @{
 ******************************************************************************/

/** @cond DO_NOT_INCLUDE_WITH_DOXYGEN */

/* Select register id's, for internal use. */


/* Divisor/prescaler register id's, for internal use. */


/* Enable register id's, for internal use. */


/* Enable register bit positions, for internal use. */

/* Clock branch bitfield positions, for internal use. */


/** @endcond */

/*******************************************************************************
 ********************************   ENUMS   ************************************
 ******************************************************************************/

/** Clock divisors. These values are valid for prescalers. */

/** Clock divider configuration */
typedef uint32_t CMU_ClkDiv_TypeDef;


/** High frequency system RCO bands */
typedef enum
{
  cmuHFRCOBand_1MHz  = 0x00000000UL,      /**< 1MHz HFRCO band  */
  cmuHFRCOBand_7MHz  = 0x00000001UL,      /**< 7MHz HFRCO band  */
  cmuHFRCOBand_11MHz = 0x00000002UL,     /**< 11MHz HFRCO band */
  cmuHFRCOBand_14MHz = 0x00000003UL,     /**< 14MHz HFRCO band */
  cmuHFRCOBand_21MHz = 0x00000004UL,     /**< 21MHz HFRCO band */
  cmuHFRCOBand_28MHz = 0x00000005UL,     /**< 28MHz HFRCO band */
} CMU_HFRCOBand_TypeDef;

/** AUX High frequency RCO bands */
typedef enum
{
  cmuAUXHFRCOBand_1MHz  = 0x00000003UL,  /**< 1MHz RC band  */
  cmuAUXHFRCOBand_7MHz  = 0x00000002UL,  /**< 7MHz RC band  */
  cmuAUXHFRCOBand_11MHz = 0x00000001UL, /**< 11MHz RC band */
  cmuAUXHFRCOBand_14MHz = 0x00000000UL, /**< 14MHz RC band */
  cmuAUXHFRCOBand_21MHz = 0x00000007UL, /**< 21MHz RC band */
  cmuAUXHFRCOBand_28MHz = 0x00000006UL, /**< 28MHz RC band */
} CMU_AUXHFRCOBand_TypeDef;





/** Clock points in CMU. Please refer to CMU overview in reference manual. */
typedef enum
{
  /*******************/
  /* HF clock branch */
  /*******************/

  /** High frequency clock */
  cmuClock_HF = (1 << 4)
                | (1 << 0)
                | (0 << 8)
                | (0 << 12)
                | (0 << 17),

  /** Debug clock */
  cmuClock_DBG = (0 << 4)
                 | (6 << 0)
                 | (0 << 8)
                 | (0 << 12)
                 | (6 << 17),

  /** AUX clock */
  cmuClock_AUX = (0 << 4)
                 | (0 << 0)
                 | (0 << 8)
                 | (0 << 12)
                 | (7 << 17),



  /**********************************/
  /* HF peripheral clock sub-branch */
  /**********************************/

  /** High frequency peripheral clock */
  cmuClock_HFPER = (4 << 4)
                   | (0 << 0)
                   | (1 << 8)
                   | (8 << 12)
                   | (2 << 17),


  /** Universal sync/async receiver/transmitter 0 clock. */
  cmuClock_USARTRF0 = (0 << 4)
                      | (0 << 0)
                      | (2 << 8)
                      | (0 << 12)
                      | (2 << 17),

  /** Universal sync/async receiver/transmitter 1 clock. */
  cmuClock_USART1 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (1 << 12)
                    | (2 << 17),

  /** Universal sync/async receiver/transmitter 2 clock. */
  cmuClock_USART2 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (2 << 12)
                    | (2 << 17),





  /** Universal async receiver/transmitter 0 clock. */
  cmuClock_UART0 = (0 << 4)
                   | (0 << 0)
                   | (2 << 8)
                   | (3 << 12)
                   | (2 << 17),

  /** Universal async receiver/transmitter 1 clock. */
  cmuClock_UART1 = (0 << 4)
                   | (0 << 0)
                   | (2 << 8)
                   | (4 << 12)
                   | (2 << 17),

  /** Timer 0 clock. */
  cmuClock_TIMER0 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (5 << 12)
                    | (2 << 17),

  /** Timer 1 clock. */
  cmuClock_TIMER1 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (6 << 12)
                    | (2 << 17),

  /** Timer 2 clock. */
  cmuClock_TIMER2 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (7 << 12)
                    | (2 << 17),

  /** Timer 3 clock. */
  cmuClock_TIMER3 = (0 << 4)
                    | (0 << 0)
                    | (2 << 8)
                    | (8 << 12)
                    | (2 << 17),


  /** Analog comparator 0 clock. */
  cmuClock_ACMP0 = (0 << 4)
                   | (0 << 0)
                   | (2 << 8)
                   | (9 << 12)
                   | (2 << 17),

  /** Analog comparator 1 clock. */
  cmuClock_ACMP1 = (0 << 4)
                   | (0 << 0)
                   | (2 << 8)
                   | (10 << 12)
                   | (2 << 17),

  /** Peripheral reflex system clock. */
  cmuClock_PRS = (0 << 4)
                 | (0 << 0)
                 | (2 << 8)
                 | (15 << 12)
                 | (2 << 17),

  /** Digital to analog converter 0 clock. */
  cmuClock_DAC0 = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (17 << 12)
                  | (2 << 17),


  /** General purpose input/output clock. */
  cmuClock_GPIO = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (13 << 12)
                  | (2 << 17),

  /** Voltage comparator clock. */
  cmuClock_VCMP = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (14 << 12)
                  | (2 << 17),

  /** Analog to digital converter 0 clock. */
  cmuClock_ADC0 = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (16 << 12)
                  | (2 << 17),

  /** I2C 0 clock. */
  cmuClock_I2C0 = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (11 << 12)
                  | (2 << 17),

  /** I2C 1 clock. */
  cmuClock_I2C1 = (0 << 4)
                  | (0 << 0)
                  | (2 << 8)
                  | (12 << 12)
                  | (2 << 17),


  /**********************/
  /* HF core sub-branch */
  /**********************/

  /** Core clock */
  cmuClock_CORE = (5 << 4)
                  | (0 << 0)
                  | (0 << 8)
                  | (0 << 12)
                  | (1 << 17),

  /** Advanced encryption standard accelerator clock. */
  cmuClock_AES = (0 << 4)
                 | (0 << 0)
                 | (3 << 8)
                 | (1 << 12)
                 | (1 << 17),

  /** Direct memory access controller clock. */
  cmuClock_DMA = (0 << 4)
                 | (0 << 0)
                 | (3 << 8)
                 | (0 << 12)
                 | (1 << 17),

/** Low energy clocking module clock. */
  cmuClock_CORELE = (0 << 4)
                    | (0 << 0)
                    | (3 << 8)
                    | (4 << 12)
                    | (1 << 17),


  /** USB Core clock. */
  cmuClock_USBC = (0 << 4)
                  | (7 << 0)
                  | (3 << 8)
                  | (2 << 12)
                  | (16 << 17),


  /** USB clock. */
  cmuClock_USB = (0 << 4)
                 | (0 << 0)
                 | (3 << 8)
                 | (3 << 12)
                 | (1 << 17),


  /***************/
  /* LF A branch */
  /***************/

  /** Low frequency A clock */
  cmuClock_LFA = (0 << 4)
                 | (2 << 0)
                 | (0 << 8)
                 | (0 << 12)
                 | (12 << 17),

  /** Real time counter clock. */
  cmuClock_RTC = (7 << 4)
                 | (0 << 0)
                 | (6 << 8)
                 | (1 << 12)
                 | (8 << 17),

  /** Low energy timer 0 clock. */
  cmuClock_LETIMER0 = (7 << 4)
                      | (0 << 0)
                      | (6 << 8)
                      | (2 << 12)
                      | (9 << 17),


  /** Pulse counter 0 clock. */
  cmuClock_PCNT0 = (0 << 4)
                   | (0 << 0)
                   | (10 << 8)
                   | (0 << 12)
                   | (12 << 17),

  /** Pulse counter 1 clock. */
  cmuClock_PCNT1 = (0 << 4)
                   | (0 << 0)
                   | (10 << 8)
                   | (2 << 12)
                   | (12 << 17),

  /** Pulse counter 2 clock. */
  cmuClock_PCNT2 = (0 << 4)
                   | (0 << 0)
                   | (10 << 8)
                   | (4 << 12)
                   | (12 << 17),
  /** LESENSE clock. */
  cmuClock_LESENSE = (7 << 4)
                     | (0 << 0)
                     | (6 << 8)
                     | (0 << 12)
                     | (20 << 17),

  /***************/
  /* LF B branch */
  /***************/

  /** Low frequency B clock */
  cmuClock_LFB = (0 << 4)
                 | (3 << 0)
                 | (0 << 8)
                 | (0 << 12)
                 | (13 << 17),

  /** Low energy universal asynchronous receiver/transmitter 0 clock. */
  cmuClock_LEUART0 = (8 << 4)
                     | (0 << 0)
                     | (7 << 8)
                     | (0 << 12)
                     | (10 << 17),

  /** Low energy universal asynchronous receiver/transmitter 1 clock. */
  cmuClock_LEUART1 = (8 << 4)
                     | (0 << 0)
                     | (7 << 8)
                     | (1 << 12)
                     | (11 << 17),



} CMU_Clock_TypeDef;


/** Oscillator types. */
typedef enum
{
  cmuOsc_LFXO,     /**< Low frequency crystal oscillator. */
  cmuOsc_LFRCO,    /**< Low frequency RC oscillator. */
  cmuOsc_HFXO,     /**< High frequency crystal oscillator. */
  cmuOsc_HFRCO,    /**< High frequency RC oscillator. */
  cmuOsc_AUXHFRCO, /**< Auxiliary high frequency RC oscillator. */
  cmuOsc_ULFRCO    /**< Ultra low frequency RC oscillator. */
} CMU_Osc_TypeDef;


/** Selectable clock sources. */
typedef enum
{
  cmuSelect_Error,      /**< Usage error. */
  cmuSelect_Disabled,   /**< Clock selector disabled. */
  cmuSelect_LFXO,       /**< Low frequency crystal oscillator. */
  cmuSelect_LFRCO,      /**< Low frequency RC oscillator. */
  cmuSelect_HFXO,       /**< High frequency crystal oscillator. */
  cmuSelect_HFRCO,      /**< High frequency RC oscillator. */
  cmuSelect_CORELEDIV2, /**< Core low energy clock divided by 2. */
  cmuSelect_AUXHFRCO,   /**< Auxilliary clock source can be used for debug clock */
  cmuSelect_HFCLK,      /**< Divided HFCLK on Giant for debug clock, undivided on Tiny Gecko and for USBC (not used on Gecko) */
  cmuSelect_ULFRCO,     /**< Ultra low frequency RC oscillator. */
} CMU_Select_TypeDef;


/*******************************************************************************
 *******************************   STRUCTS   ***********************************
 ******************************************************************************/




/*******************************************************************************
 *****************************   PROTOTYPES   **********************************
 ******************************************************************************/

CMU_AUXHFRCOBand_TypeDef  CMU_AUXHFRCOBandGet(void);
void                      CMU_AUXHFRCOBandSet(CMU_AUXHFRCOBand_TypeDef band);


uint32_t              CMU_Calibrate(uint32_t HFCycles, CMU_Osc_TypeDef reference);

void                  CMU_CalibrateConfig(uint32_t downCycles, CMU_Osc_TypeDef downSel,
                                          CMU_Osc_TypeDef upSel);

uint32_t              CMU_CalibrateCountGet(void);
void                  CMU_ClockEnable(CMU_Clock_TypeDef clock, _Bool enable);
CMU_ClkDiv_TypeDef    CMU_ClockDivGet(CMU_Clock_TypeDef clock);
void                  CMU_ClockDivSet(CMU_Clock_TypeDef clock, CMU_ClkDiv_TypeDef div);
uint32_t              CMU_ClockFreqGet(CMU_Clock_TypeDef clock);


void                  CMU_ClockSelectSet(CMU_Clock_TypeDef clock, CMU_Select_TypeDef ref);
CMU_Select_TypeDef    CMU_ClockSelectGet(CMU_Clock_TypeDef clock);
void                  CMU_FreezeEnable(_Bool enable);

CMU_HFRCOBand_TypeDef CMU_HFRCOBandGet(void);
void                  CMU_HFRCOBandSet(CMU_HFRCOBand_TypeDef band);


uint32_t              CMU_HFRCOStartupDelayGet(void);
void                  CMU_HFRCOStartupDelaySet(uint32_t delay);




uint32_t              CMU_LCDClkFDIVGet(void);
void                  CMU_LCDClkFDIVSet(uint32_t div);


void                  CMU_OscillatorEnable(CMU_Osc_TypeDef osc, _Bool enable, _Bool wait);
uint32_t              CMU_OscillatorTuningGet(CMU_Osc_TypeDef osc);
void                  CMU_OscillatorTuningSet(CMU_Osc_TypeDef osc, uint32_t val);
_Bool                  CMU_PCNTClockExternalGet(unsigned int instance);
void                  CMU_PCNTClockExternalSet(unsigned int instance, _Bool external);



/***************************************************************************//**
 * @brief
 *   Configures continuous calibration mode
 * @param[in] enable
 *   If true, enables continuous calibration, if false disables continuous
 *   calibrartion
 ******************************************************************************/
static inline void CMU_CalibrateCont(_Bool enable)
{
  BUS_RegBitWrite(&(((CMU_TypeDef *) (0x400C8000UL))->CALCTRL), 6, enable);
}


/***************************************************************************//**
 * @brief
 *   Starts calibration
 * @note
 *   This call is usually invoked after CMU_CalibrateConfig() and possibly
 *   CMU_CalibrateCont()
 ******************************************************************************/
static inline void CMU_CalibrateStart(void)
{
  ((CMU_TypeDef *) (0x400C8000UL))->CMD = (0x1UL << 3);
}


/***************************************************************************//**
 * @brief
 *   Stop the calibration counters
 ******************************************************************************/
static inline void CMU_CalibrateStop(void)
{
  ((CMU_TypeDef *) (0x400C8000UL))->CMD = (0x1UL << 4);
}


/***************************************************************************//**
 * @brief
 *   Convert dividend to logarithmic value. Only works for even
 *   numbers equal to 2^n.
 *
 * @param[in] div
 *   Unscaled dividend.
 *
 * @return
 *   Logarithm of 2, as used by fixed prescalers.
 ******************************************************************************/
static inline uint32_t CMU_DivToLog2(CMU_ClkDiv_TypeDef div)
{
  uint32_t log2;

  /* Fixed 2^n prescalers take argument of 32768 or less. */
  ((void)((div > 0U) && (div <= 32768U)));

  /* Count leading zeroes and "reverse" result */
  log2 = (31U - __CLZ(div));

  return log2;
}


/***************************************************************************//**
 * @brief
 *   Clear one or more pending CMU interrupts.
 *
 * @param[in] flags
 *   CMU interrupt sources to clear.
 ******************************************************************************/
static inline void CMU_IntClear(uint32_t flags)
{
  ((CMU_TypeDef *) (0x400C8000UL))->IFC = flags;
}


/***************************************************************************//**
 * @brief
 *   Disable one or more CMU interrupts.
 *
 * @param[in] flags
 *   CMU interrupt sources to disable.
 ******************************************************************************/
static inline void CMU_IntDisable(uint32_t flags)
{
  ((CMU_TypeDef *) (0x400C8000UL))->IEN &= ~flags;
}


/***************************************************************************//**
 * @brief
 *   Enable one or more CMU interrupts.
 *
 * @note
 *   Depending on the use, a pending interrupt may already be set prior to
 *   enabling the interrupt. Consider using CMU_IntClear() prior to enabling
 *   if such a pending interrupt should be ignored.
 *
 * @param[in] flags
 *   CMU interrupt sources to enable.
 ******************************************************************************/
static inline void CMU_IntEnable(uint32_t flags)
{
  ((CMU_TypeDef *) (0x400C8000UL))->IEN |= flags;
}


/***************************************************************************//**
 * @brief
 *   Get pending CMU interrupts.
 *
 * @return
 *   CMU interrupt sources pending.
 ******************************************************************************/
static inline uint32_t CMU_IntGet(void)
{
  return ((CMU_TypeDef *) (0x400C8000UL))->IF;
}


/***************************************************************************//**
 * @brief
 *   Get enabled and pending CMU interrupt flags.
 *
 * @details
 *   Useful for handling more interrupt sources in the same interrupt handler.
 *
 * @note
 *   The event bits are not cleared by the use of this function.
 *
 * @return
 *   Pending and enabled CMU interrupt sources
 *   The return value is the bitwise AND of
 *   - the enabled interrupt sources in CMU_IEN and
 *   - the pending interrupt flags CMU_IF
 ******************************************************************************/
static inline uint32_t CMU_IntGetEnabled(void)
{
  uint32_t ien;

  ien = ((CMU_TypeDef *) (0x400C8000UL))->IEN;
  return ((CMU_TypeDef *) (0x400C8000UL))->IF & ien;
}


/**************************************************************************//**
 * @brief
 *   Set one or more pending CMU interrupts.
 *
 * @param[in] flags
 *   CMU interrupt sources to set to pending.
 *****************************************************************************/
static inline void CMU_IntSet(uint32_t flags)
{
  ((CMU_TypeDef *) (0x400C8000UL))->IFS = flags;
}


/***************************************************************************//**
 * @brief
 *   Lock the CMU in order to protect some of its registers against unintended
 *   modification.
 *
 * @details
 *   Please refer to the reference manual for CMU registers that will be
 *   locked.
 *
 * @note
 *   If locking the CMU registers, they must be unlocked prior to using any
 *   CMU API functions modifying CMU registers protected by the lock.
 ******************************************************************************/
static inline void CMU_Lock(void)
{
  ((CMU_TypeDef *) (0x400C8000UL))->LOCK = (0x00000000UL << 0);
}


/***************************************************************************//**
 * @brief
 *   Convert logarithm of 2 prescaler to division factor.
 *
 * @param[in] log2
 *   Logarithm of 2, as used by fixed prescalers.
 *
 * @return
 *   Dividend.
 ******************************************************************************/
static inline uint32_t CMU_Log2ToDiv(uint32_t log2)
{
  return 1 << log2;
}




/***************************************************************************//**
 * @brief
 *   Unlock the CMU so that writing to locked registers again is possible.
 ******************************************************************************/
static inline void CMU_Unlock(void)
{
  ((CMU_TypeDef *) (0x400C8000UL))->LOCK = (0x0000580EUL << 0);
}

/** @} (end addtogroup CMU) */
/** @} (end addtogroup EM_Library) */



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





  #include <stdarg.h>
/* stdint.h standard header */
/* Copyright 2003-2010 IAR Systems AB.  */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
/* string.h standard header */
/* Copyright 2009-2010 IAR Systems AB. */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */
    // EFR32, EZR32
      //EZR32WG
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

// This file is generated by Ember Desktop.  Please do not edit manually.
//
//

// Enclosing macro to prevent multiple inclusion




// Top level macros


// Generated setup headers that are included automatically
// This file is generated by Ember Desktop.  Please do not edit manually.
//
//

// Enclosing macro to prevent multiple inclusion




// This file contains the generated macros for the debug printing
// Global macro, if this is commented out, there is no printing



// Generated bit array and name array that is used by thedebug printing library.


// Generated functions for use within plugin Command Interpreter


// Generated functions for use within plugin Debug Print


// Generated functions for use within plugin Diagnostic


// Generated functions for use within plugin HAL library


// Generated functions for use within plugin Heartbeat


// Generated functions for use within plugin Idle/Sleep


// Generated functions for use within plugin Main


// Generated functions for use within plugin EzRadio PHY


// Generated functions for use within plugin Poll


// Generated functions for use within plugin Serial


// Generated functions for use within plugin Simulated EEPROM version 1 Library


// Generated functions for use within plugin Security AES


// Generated functions for use within plugin Stack Common


// Generated functions for use within plugin Stack packet counters


// Generated functions for use within plugin Form and Join


// Generated functions for use within plugin MAC Packet Queue


// Generated functions for use within plugin Parent Support


// Generated functions for use within plugin Security XXTEA


// Generated functions for use within plugin USB CDC


// Generated functions for use within plugin USB Common


// Generated functions for use within plugin WSTK Sensors


// Generated functions for use within area Core
// Blocking IO is enabled for all serial ports, therefore flush calls are unnecessary.


// Generated functions for use within area Debug


// Generated functions for use within area Application
// Blocking IO is enabled for all serial ports, therefore flush calls are unnecessary.


// Generated functions for use within area Custom messages (1)


// Generated functions for use within area Custom messages (2)


// Generated functions for use within area Custom messages (3)




// Generated plugin macros

// Use this macro to check if Command Interpreter plugin is included

// Use this macro to check if Debug Print plugin is included
// User options for plugin Debug Print

// Use this macro to check if Diagnostic plugin is included

// Use this macro to check if HAL library plugin is included

// Use this macro to check if Heartbeat plugin is included
// User options for plugin Heartbeat

// Use this macro to check if Idle/Sleep plugin is included
// User options for plugin Idle/Sleep

// Use this macro to check if Main plugin is included

// Use this macro to check if EzRadio PHY plugin is included
// User options for plugin EzRadio PHY

// Use this macro to check if Poll plugin is included
// User options for plugin Poll

// Use this macro to check if Serial plugin is included

// Use this macro to check if Simulated EEPROM version 1 Library plugin is included

// Use this macro to check if Security AES plugin is included

// Use this macro to check if Stack Common plugin is included
// User options for plugin Stack Common

// Use this macro to check if Stack packet counters plugin is included

// Use this macro to check if Form and Join plugin is included

// Use this macro to check if MAC Packet Queue plugin is included
// User options for plugin MAC Packet Queue

// Use this macro to check if Parent Support plugin is included
// User options for plugin Parent Support

// Use this macro to check if Security XXTEA plugin is included

// Use this macro to check if USB CDC plugin is included
// User options for plugin USB CDC

// Use this macro to check if USB Common plugin is included

// Use this macro to check if WSTK Sensors plugin is included


// Generated API headers

// API command-interpreter2 from Command Interpreter plugin

// API debug-print from Debug Print plugin

// API diagnostic from Diagnostic plugin

// API diagnostic-cortexm3 from Diagnostic plugin

// API poll from Poll plugin

// API serial from Serial plugin

// API sim-eeprom from Simulated EEPROM version 1 Library plugin

// API usb-cdc from USB CDC plugin


// Custom macros












/**
 * @file ember.h
 * @brief The master include file for the Ember Connect API.
 *
 *  See @ref ember for documentation.
 *
 * <!--Copyright 2014 by Silicon Laboratories. All rights reserved.      *80*-->
 */


      //EZR32WG

/**
 * @file stack/include/ember-types.h
 * @brief Ember Connect data type definitions.
 *
 * <!--Copyright 2014 by Silicon Laboratories. All rights reserved.      *80*-->
 */

/**
 * @addtogroup ember_types
 *
 * See ember-types.h for source code.
 * @{
 */


/* stdint.h standard header */
/* Copyright 2003-2010 IAR Systems AB.  */


/*
 * Copyright (c) 1992-2009 by P.J. Plauger.  ALL RIGHTS RESERVED.
 * Consult your license regarding permissions and restrictions.
V5.04:0576 */

/** @file ember-configuration-defaults.h
 * @brief User-configurable stack memory allocation defaults
 *
 * @note Application developers should \b not modify any portion
 * of this file. Doing so may cause mysterious bugs. Allocations should be
 * adjusted only by defining the appropriate macros in the application's
 * CONFIGURATION_HEADER.
 *
 * See @ref configuration for documentation.
 * <!--Copyright 2014 by Silicon Laboratories. All rights reserved.      *80*-->
 */

/**
 * @addtogroup configuration
 *
 * All configurations have defaults, therefore many applications may not need
 * to do anything special.  However, you can override these defaults
 * by creating a CONFIGURATION_HEADER and within this header,
 * defining the appropriate macro to a different size.
 *
 * See ember-configuration-defaults.h for source code.

 * @{
 */

 	

/** @brief The number of event tasks that can be tracked for the purpose of
 *  processor idling.
 */

/** @brief The size of the Ember heap. This is set to default to 0. If the
 * application includes the optional stack features that require dynamic memory
 * allocation, this should adjusted accordingly.
 */

/** @brief The maximum number of children that a node may have. This is set to
 * default to 0. If the application includes the optional parent support stack
 * feature, this should be adjusted accordingly.
 */


/** @brief Every child should exchange regularly some sort of traffic with the
 * parent. Eventually, if traffic is not exchanged for a prolonged period of
 * time, the parent will remove the child from the child table.
 * Range extenders periodically exchange network-level commands with the
 * coordinator. End devices and sleepy end devices can use ::emberPollForData()
 * as keep alive mechanism.
 */

/** @brief The maximum number of pending indirect packets. This is set to
 * default to 0. If the application includes the optional parent support stack
 * feature, this should be adjusted accordingly.
 */

/** @brief The maximum number of packets in the outgoing MAC queue. This is set
 * to default to 0. If the application includes the optional MAC queue stack
 * feature, this should be adjusted accordingly.
 */

/** @brief The maximum amount of time (in milliseconds) that the MAC
 * will hold a message for indirect transmission to a child.
 *
 * The default is 8000 milliseconds (8 sec).
 * The maximum value is 30 seconds (30000 milliseconds).larger values
 * will cause rollover confusion.
 */

/** @brief The period in seconds a range extender sends an update command to the
 * coordinator containing the list of its children.
 */

/** @brief The ACK timeout in milliseconds. This can be fine-tuned to reduce
 * energy consumption at sleepy devices. This parameter depends on the data rate
 * of the PHY configuration being used.
 */

/** @brief The CCA threshold used at the MAC layer.
 */

/** @} END addtogroup */


/**
 * @brief Size of EUI64 (an IEEE address) in bytes (8).
 */

/**
 * @brief Size of an encryption key in bytes (16).
 */

/**
 * @brief EUI 64-bit ID (an IEEE address).
 */
typedef uint8_t EmberEUI64[8];

/**
 * @brief 802.15.4 node ID.
 */
typedef uint16_t EmberNodeId;

/**
 * @brief 802.15.4 PAN ID.
 */
typedef uint16_t EmberPanId;

/**
 * @brief A distinguished network ID that will never be assigned
 * to any node.  Used to indicate the absence of a node ID.
 */

/** Broadcast address. */

/** The coordinator short address. */

/**
 * @brief The maximum allowed length in bytes of the PHY payload.
 */

typedef uint8_t EmberMessageLength;

/**
 * @brief Defines the possible types of nodes and the roles that a
 * node might play in a network.
 */
typedef uint8_t EmberNodeType;
enum
{
  /** Device is not joined */
  EMBER_UNKNOWN_DEVICE = 0,
  /** Star or extended star topology device: will relay messages and can act as
   * a parent to range extender and  end device nodes.
   */
  EMBER_STAR_COORDINATOR = 1,
  /** Star or extended star topology device: will relay messages and can act as
   * a parent to end device nodes.
   */
  EMBER_STAR_RANGE_EXTENDER = 2,
  /** Star or extended star topology device: communicates only with its parent
   * and will not relay messages.
   */
  EMBER_STAR_END_DEVICE = 3,
  /** Star or extended star topology device: an end device whose radio can be
   * turned off to save power. The application must call ::emberPollForData() to
   * receive messages.
   */
  EMBER_STAR_SLEEPY_END_DEVICE = 4,
  /** A device able to send and receive messages from other devices  in range on
   * the same PAN ID, with no star topology restrictions. Such device does not
   * relay messages. A node can be started as direct device by using the
   * ::emberJoinCommissioned() API.
   */
  EMBER_DIRECT_DEVICE = 5,
};

/**
 * @brief Defines the possible join states for a node.
 */
typedef uint8_t EmberNetworkStatus;
enum
{
  /** The node is not associated with a network in any way. */
  EMBER_NO_NETWORK,
  /** The node is currently attempting to join a network. */
  EMBER_JOINING_NETWORK,
  /** The node is joined to a network. */
  EMBER_JOINED_NETWORK,
};

/** @brief Holds network parameters.
 *
 * For information about power settings and radio channels,
 * see the technical specification for the
 * RF communication module in your Developer Kit.
 */
typedef struct {
  /** The network's PAN identifier.*/
  uint16_t  panId;
  /** A power setting, in dBm.*/
  int8_t   radioTxPower;
  /** A radio channel. Be sure to specify a channel supported by the radio. */
  uint8_t   radioChannel;
} EmberNetworkParameters;

/**
 * @brief Packet options.
 */
typedef uint8_t EmberMessageOptions;
enum
{
  /** No options. */
  EMBER_OPTIONS_NONE                     = 0x00,
  /** The packet should be sent out encrypted. */
  EMBER_OPTIONS_SECURITY_ENABLED         = 0x01,
  /** An acknowledgment should be requested for the outgoing packet. */
  EMBER_OPTIONS_ACK_REQUESTED            = 0x02,
  /** The packet should be sent with high priority. */
  EMBER_OPTIONS_HIGH_PRIORITY            = 0x04,
};

/**
 * @brief An instance of this struct is passed to emberIncomingMessageHandler().
 * It describe the incoming message.
 */
typedef struct {
  /**
   * An ::EmberMessageOptions value indicating the options used for the incoming
   * packet.
   */
  EmberMessageOptions options;
  /**
   * An ::EmberNodeId value indicating source node ID.
   */
  EmberNodeId source;
  /**
   * The endpoint the message is destined to.
   */
  uint8_t endpoint;
  /**
   * The RSSI the packet was received with.
   */
  int8_t rssi;
  /**
   * An ::EmberMessageLength value indicating the length in bytes of the
   * incoming message.
   */
  EmberMessageLength length;
  /**
   * A pointer to the message payload.
   */
  uint8_t *payload;
} EmberIncomingMessage;

/**
 * @brief An instance of this struct is passed to emberMessageSentHandler().
 * It describes the outgoing packet.
 */
typedef struct {
  /**
   * An ::EmberMessageOptions value indicating the options used for transmitting
   * the outgoing message.
   */
  EmberMessageOptions options;
  /**
   * An ::EmberNodeId value indicating the destination short ID.
   */
  EmberNodeId destination;
  /**
   * The endpoint the message is destined to.
   */
  uint8_t endpoint;
  /**
   * A tag value the application can use to match ::emberMessageSend() calls to
   * the corresponding ::emberMessageSentHandler() calls.
   */
  uint8_t tag;
  /**
   * An ::EmberMessageLength value indicating the length in bytes of the
   * incoming message.
   */
  EmberMessageLength length;
  /**
   * A pointer to the message payload.
   */
  uint8_t *payload;
} EmberOutgoingMessage;

/** @brief This data structure contains the key data that is passed
 *   into various other functions. */
typedef struct {
  /** This is the key byte data. */
  uint8_t contents[16];
} EmberKeyData;

/** @brief This function allows the programmer to gain access
 *  to the actual key data bytes of the EmberKeyData struct.
 *
 * @param key  A Pointer to an EmberKeyData structure.
 *
 * @return uint8_t* Returns a pointer to the first byte of the Key data.
 */

/**
 * @brief Either marks an event as inactive or specifies the units for the
 * event execution time.
 */
typedef uint8_t EmberEventUnits;
enum
{
  /** The event is not scheduled to run. */
  EMBER_EVENT_INACTIVE = 0,
  /** The execution time is in approximate milliseconds.  */
  EMBER_EVENT_MS_TIME,
  /** The execution time is in 'binary' quarter seconds (256 approximate
      milliseconds each). */
  EMBER_EVENT_QS_TIME,
  /** The execution time is in 'binary' minutes (65536 approximate milliseconds
      each). */
  EMBER_EVENT_MINUTE_TIME,
  /** The event is scheduled to run at the earliest opportunity. */
  EMBER_EVENT_ZERO_DELAY
};

/** brief An identifier for a task */
typedef uint8_t EmberTaskId;

/** @brief Control structure for events.
 *
 * This structure should not be accessed directly.
 * This holds the event status (one of the @e EMBER_EVENT_ values)
 * and the time left before the event fires.
 */
typedef struct {
  /** The event's status, either inactive or the units for timeToExecute. */
  EmberEventUnits status;
  /** The id of the task this event belongs to. */
  EmberTaskId taskid;
  /** How long before the event fires.
   *  Units are always in milliseconds
   */
  uint32_t timeToExecute;
} EmberEventControl;

/** @brief Complete events with a control and a handler procedure.
 *
 * An application typically creates an array of events
 * along with their handlers.
 * The main loop passes the array to ::emberRunEvents() in order to call
 * the handlers of any events whose time has arrived.
 */
typedef const struct EmberEventData_S {
  /** The control structure for the event. */
  EmberEventControl *control;
  /** The procedure to call when the event fires. */
  void (*handler)(void);
} EmberEventData;

/** @brief Control structure for tasks.
 *
 * This structure should not be accessed directly.
 */
typedef struct {
  // The time when the next event associated with this task will fire
  uint32_t nextEventTime;
  // The list of events associated with this task
  EmberEventData *events;
  // A flag that indicates the task has something to do other than events
  _Bool busy;
} EmberTaskControl;

/** @brief Defines tasks that prevent the stack from sleeping.
 */
enum
{
   /** There are messages waiting for transmission. */
   EMBER_OUTGOING_MESSAGES = 0x0001,
   /** One or more incoming messages are being processed. */
   EMBER_INCOMING_MESSAGES = 0x0002,
   /** The radio is currently powered on.  On sleepy devices the radio is
    *  turned off when not in use.  On non-sleepy devices, i.e.,
    *  ::EMBER_STAR_COORDINATOR, ::EMBER_STAR_RANGE_EXTENDER,
    *  ::EMBER_STAR_END_DEVICE, or ::EMBER_DIRECT_DEVICE, the radio is always
    *  on.
    */
   EMBER_RADIO_IS_ON = 0x0004,
   /** The node is currently trying to associate to a Connect network. */
   EMBER_ASSOCIATING = 0x0008,
   /** The node is currently performing a MAC level scanning procedure. */
   EMBER_SCANNING = 0x0010,
};

/**
 * @brief Defines the events reported to the application
 * by the ::emberCounterHandler().
 */
typedef uint8_t EmberCounterType;
enum
{
  /** Every packet that comes in over the radio (except mac acks). */
  EMBER_COUNTER_PHY_IN_PACKETS,

  /** Every packet that goes out over the radio (except mac acks). */
  EMBER_COUNTER_PHY_OUT_PACKETS,

  /** Incoming mac unicasts. */
  EMBER_COUNTER_MAC_IN_UNICAST,

  /** Incoming mac broadcasts. */
  EMBER_COUNTER_MAC_IN_BROADCAST,

  /** Outgoing mac unicasts that do not require an ack. */
  EMBER_COUNTER_MAC_OUT_UNICAST_NO_ACK,

  /** Outgoing mac unicasts that require an ack for which we received an ack,
   * possibly after retrying. */
  EMBER_COUNTER_MAC_OUT_UNICAST_ACK_SUCCESS,

  /** Outgoing unicasts for which we never received an ack even
   * after retrying. */
  EMBER_COUNTER_MAC_OUT_UNICAST_ACK_FAIL,

  /** Outgoing mac packets which were never transmitted because
   * clear channel assessment always returned busy. */
  EMBER_COUNTER_MAC_OUT_UNICAST_CCA_FAIL,

  /** Outgoing unicast retries.  This does not count the initial
   * transmission.  Note a single mac transmission can result in
   * multiple retries. */
  EMBER_COUNTER_MAC_OUT_UNICAST_RETRY,

  EMBER_COUNTER_MAC_OUT_BROADCAST,

  EMBER_COUNTER_MAC_OUT_BROADCAST_CCA_FAIL,

  /** Dropped incoming MAC packets (out of memory) */
  EMBER_COUNTER_MAC_DROP_IN_MEMORY,

  /** Dropped incoming MAC packets (invalid frame counter) */
  EMBER_COUNTER_MAC_DROP_IN_FRAME_COUNTER,

  /** Dropped incoming MAC packets (can't decrypt) */
  EMBER_COUNTER_MAC_DROP_IN_DECRYPT,

  /** Outgoing nwk forwarded packets */
  EMBER_COUNTER_NWK_OUT_FORWARDING,

  /** Incoming nwk data frames correctly processed */
  EMBER_COUNTER_NWK_IN_SUCCESS,

  /** Dropped incoming nwk packets (wrong source node) */
  EMBER_COUNTER_NWK_DROP_IN_WRONG_SOURCE,

  /** Dropped incoming nwk packets (can't forward) */
  EMBER_COUNTER_NWK_DROP_IN_FORWARDING,

  /** A placeholder giving the number of Ember counter types. */
  EMBER_COUNTER_TYPE_COUNT
};

/**
 * @brief  Buffers used by the memory buffer system.
 */
typedef uint16_t EmberBuffer;

/**
 * @brief  Return type for Ember functions.
 */
  typedef uint8_t EmberStatus;

//------------------------------------------------------------------------------
// INTERNAL TYPES AND DEFINES
//------------------------------------------------------------------------------


typedef uint16_t Buffer;
typedef uint16_t EmberMessageBuffer;


typedef struct {
  EmberNodeId source;
  EmberNodeId destination;
  uint8_t endpoint;
  uint8_t tag;
  Buffer payload;
  EmberMessageOptions txOptions;
} EmOutgoingPacket;


enum {
  /* RX status codes */
  EMBER_PACKET_TRACE_RX_STATUS_SUCCESS      = 0x00,
  EMBER_PACKET_TRACE_RX_STATUS_CRC_FAILED   = 0x01,
  EMBER_PACKET_TRACE_RX_STATUS_MAC_FILTERED = 0x02,
  /* TX status codes */
  EMBER_PACKET_TRACE_TX_STATUS_SUCCESS      = 0x80
};

typedef struct {
  uint8_t status;
  int8_t rssi;
  uint8_t channel;
  EmberMessageLength packetLength;
  uint8_t *packet;
} EmberMessageTrace;

typedef struct {
  uint32_t lastSeen;
  uint32_t frameCounter;
  EmberNodeId shortId;
  EmberEUI64 longId;
  uint8_t flags;
} EmberChildEntry;

typedef uint8_t EmberLibraryStatus;



/** @} // END addtogroup
*/
/**
 * @file error.h
 * @brief Return codes for Ember Connect API functions and module definitions.
 *
 * See @ref status_codes for documentation.
 *
 * <!--Copyright 2014 by Silicon Labs. All rights reserved.              *80*-->
 */


/**
 * @brief  Return type for Ember functions.
 */

/**
 * @addtogroup status_codes
 * @{
 */

/**
 * @brief Macro used by error-def.h to define all of the return codes.
 *
 * @param symbol  The name of the constant being defined. All Ember returns
 *                begin with EMBER_. For example, ::EMBER_CONNECTION_OPEN.
 *
 * @param value   The value of the return code. For example, 0x61.
 */


enum {
/**
 * @file error-def.h
 * @brief Return-code definitions for Ember Connect stack API functions.
 *
 * See @ref status_codes for documentation.
 *
 * <!--Copyright 2014 by Silicon Laboratories. All rights reserved.      *80*-->
*/

/**
 * @addtogroup status_codes
 *
 * Many Ember Connect API functions return an ::EmberStatus value to indicate
 * the success or failure of the call.
 * Return codes are one byte long.
 * This page documents the possible status codes and their meanings.
 *
 * See error-def.h for source code.
 *
 * See also error.h for information on how the values for the return codes are
 * built up from these definitions.
 * The file error-def.h is separated from error.h because utilities will use
 * this file to parse the return codes.
 *
 * @note Do not include error-def.h directly. It is included by
 * error.h inside an enum typedef, which is in turn included by ember.h.
 *
 * @{
 */

/**
 * @name Generic Messages
 * These messages are system wide.
 */
//@{

EMBER_SUCCESS = 0,


EMBER_ERR_FATAL = 0x01,


EMBER_BAD_ARGUMENT = 0x02,


EMBER_INVALID_CALL = 0x70,

EMBER_EEPROM_STACK_VERSION_MISMATCH = 0x07,

//@} // END Generic Messages

/**
 * @name Packet Buffer Module Errors
 */
//@{

EMBER_NO_BUFFERS = 0x18,

//@} / END Packet Buffer Module Errors

/**
 * @name Serial Manager Errors
 */
//@{

EMBER_SERIAL_INVALID_BAUD_RATE = 0x20,


EMBER_SERIAL_INVALID_PORT = 0x21,


EMBER_SERIAL_TX_OVERFLOW = 0x22,


EMBER_SERIAL_RX_OVERFLOW = 0x23,


EMBER_SERIAL_RX_FRAME_ERROR = 0x24,


EMBER_SERIAL_RX_PARITY_ERROR = 0x25,


EMBER_SERIAL_RX_EMPTY = 0x26,


EMBER_SERIAL_RX_OVERRUN_ERROR = 0x27,

//@}

/**
 * @name MAC Errors
 */
//@{

EMBER_MAC_NO_DATA = 0x31,


EMBER_MAC_JOINED_NETWORK = 0x32,

EMBER_MAC_SECURITY_FAILED = 0x35,

EMBER_MAC_COMMAND_TRANSMIT_FAILURE = 0x36,

EMBER_MAC_UNKNOWN_DESTINATION = 0x37,

EMBER_MAC_SECURITY_NOT_SUPPORTED = 0x38,

// Internal
EMBER_MAC_TRANSMIT_QUEUE_FULL = 0x39,


EMBER_MAC_UNKNOWN_HEADER_TYPE = 0x3A,

EMBER_MAC_ACK_HEADER_TYPE = 0x3B,


EMBER_MAC_SCANNING = 0x3D,

EMBER_MAC_NO_ACK_RECEIVED = 0x40,

EMBER_MAC_INDIRECT_TIMEOUT = 0x41,

EMBER_MAC_INDIRECT_MESSAGE_PURGED = 0x42,

//@}


/**
 * @name  Simulated EEPROM Errors
 */  
//@{


EMBER_SIM_EEPROM_ERASE_PAGE_GREEN = 0x43,


EMBER_SIM_EEPROM_ERASE_PAGE_RED = 0x44,


EMBER_SIM_EEPROM_FULL = 0x45,


//  Errors 46 and 47 are now defined below in the 
//    flash error block (was attempting to prevent renumbering)


EMBER_SIM_EEPROM_INIT_1_FAILED = 0x48,


EMBER_SIM_EEPROM_INIT_2_FAILED = 0x49,


EMBER_SIM_EEPROM_INIT_3_FAILED = 0x4A,


EMBER_SIM_EEPROM_REPAIRING = 0x4D,

//@}


/**
 * @name  Flash Errors
 */  
//@{

EMBER_ERR_FLASH_WRITE_INHIBITED = 0x46,


EMBER_ERR_FLASH_VERIFY_FAILED = 0x47,


EMBER_ERR_FLASH_PROG_FAIL = 0x4B,


EMBER_ERR_FLASH_ERASE_FAIL = 0x4C,

//@}


/**
 * @name  Bootloader Errors
 */  
//@{


EMBER_ERR_BOOTLOADER_TRAP_TABLE_BAD = 0x58,


EMBER_ERR_BOOTLOADER_TRAP_UNKNOWN = 0x59,


EMBER_ERR_BOOTLOADER_NO_IMAGE = 0x5A,

//@}


/**
 * @name  Transport Errors
 */  
//@{

EMBER_MESSAGE_TOO_LONG = 0x74,

//@}

/**
 * @name  HAL Module Errors
 */
//@{


EMBER_ADC_CONVERSION_DONE = 0x80,


EMBER_ADC_CONVERSION_BUSY = 0x81,


EMBER_ADC_CONVERSION_DEFERRED = 0x82,


EMBER_ADC_NO_CONVERSION_PENDING = 0x84,


EMBER_SLEEP_INTERRUPTED = 0x85,

//@}

/**
 * @name  PHY Errors
 */
//@{


EMBER_PHY_TX_UNDERFLOW = 0x88,


EMBER_PHY_TX_INCOMPLETE = 0x89,


EMBER_PHY_INVALID_CHANNEL = 0x8A,


EMBER_PHY_INVALID_POWER = 0x8B,


EMBER_PHY_TX_BUSY = 0x8C,


EMBER_PHY_TX_CCA_FAIL = 0x8D,


EMBER_PHY_ACK_RECEIVED = 0x8F,

//@}

/**
 * @name  Return Codes Passed to emberStackStatusHandler()
 * See also ::emberStackStatusHandler().
 */
//@{

EMBER_NETWORK_UP = 0x90,


EMBER_NETWORK_DOWN = 0x91,

EMBER_JOIN_SCAN_FAILED = 0x93,

EMBER_JOIN_FAILED = 0x94,

EMBER_JOIN_DENIED = 0x95,

EMBER_JOIN_TIMEOUT = 0x96,

EMBER_CHANNEL_CHANGED = 0x9B,

EMBER_NO_VALID_BEACONS = 0xAB,


//@}

/**
 * @name  Security Errors
 */
EMBER_KEY_INVALID = 0xB2,

     EMBER_SECURITY_DATA_INVALID = 0xBD,

//@}


/**
 * @name  Miscellaneous Network Errors
 */
//@{


EMBER_NOT_JOINED = 0x93,

//@}

/**
 * @name  Miscellaneous Utility Errors
 */
//@{

EMBER_INDEX_OUT_OF_RANGE = 0xB1,

EMBER_TABLE_FULL = 0xB4,

EMBER_TABLE_ENTRY_ERASED = 0xB6,

EMBER_LIBRARY_NOT_PRESENT = 0xB5,

EMBER_OPERATION_IN_PROGRESS = 0xBA,

//@}

/**
 * @name  Application Errors
 * These error codes are available for application use.
 */
//@{

EMBER_APPLICATION_ERROR_0 = 0xF0,
EMBER_APPLICATION_ERROR_1 = 0xF1,
EMBER_APPLICATION_ERROR_2 = 0xF2,
EMBER_APPLICATION_ERROR_3 = 0xF3,
EMBER_APPLICATION_ERROR_4 = 0xF4,
EMBER_APPLICATION_ERROR_5 = 0xF5,
EMBER_APPLICATION_ERROR_6 = 0xF6,
EMBER_APPLICATION_ERROR_7 = 0xF7,
EMBER_APPLICATION_ERROR_8 = 0xF8,
EMBER_APPLICATION_ERROR_9 = 0xF9,
EMBER_APPLICATION_ERROR_10 = 0xFA,
EMBER_APPLICATION_ERROR_11 = 0xFB,
EMBER_APPLICATION_ERROR_12 = 0xFC,
EMBER_APPLICATION_ERROR_13 = 0xFD,
EMBER_APPLICATION_ERROR_14 = 0xFE,
EMBER_APPLICATION_ERROR_15 = 0xFF,

//@} // END name group

/** @} END addtogroup */
  /** Gets defined as a count of all the possible return codes in the
  * Ember stack API.
  */
  EMBER_ERROR_CODE_COUNT

};



/**@} // End of addtogroup
 */


/**
 * @file memory-buffer.h
 * @brief Ember Connect API dynamically allocate and free memory.
 * See @ref memory_buffer for documentation.
 *
 * <!--Copyright 2015 by Silicon Labs. All rights reserved.              *80*-->
 */

/**
 * @addtogroup memory_buffer
 *
 * See memory-buffer.h for source code.
 * @{
 */

/** @brief A special ::EmberBuffer ID indicating that no memory is currently
 * allocated.
 */

/** @name Handlers*/
//@{

/** @brief This handler is invoked by the memory buffers system garbage
 * collector and allows the application to properly mark the application-defined
 * ::EmberBuffer variables.
 */
void emberMarkApplicationBuffersHandler(void);

//@}//END Handlers

/** @name APIs*/
//@{

/** @brief An API for dynamically allocating memory.
 *
 * @param dataSizeInBytes   The size in bytes of the memory to be allocated.
 *
 * @return An ::EmberBuffer value of ::EMBER_NULL_BUFFER if the memory
 * management system could not allocate the requested memory, or any other
 * ::EmberBuffer value indicating that the requested memory was successfully
 * allocated.
 * The allocated memory can easily be freed by assigning an ::EmberBuffer
 * variable to EMBER_NULL_BUFFER. The memory will be freed by the garbage
 * collector during the next ::emberTick() call.
 */
EmberBuffer emberAllocateBuffer(uint16_t dataSizeInBytes);

/** @brief This API prevents the garbage collector to reclaim the memory
 * associated with the passed ::EmberBuffer. The application should call
 * this API within the ::emberMarkApplicationBuffersHandler() stack handler
 * for each ::EmberBuffer object.
 *
 * @param buffer   A pointer to the ::EmberBuffer buffer to be marked.
 */
void emberMarkBuffer(EmberBuffer *buffer);

/** @brief An API that returns a pointer to the memory segment corresponding to
 * the passed ::EmberBuffer buffer. Notice that the garbage collector can move
 * memory segments to defragment the available memory. As result, the
 * application should always use this API to obtain an updated pointer prior to
 * accessing the memory.
 *
 * @param buffer   A pointer to the ::EmberBuffer buffer for which the
 * corresponding memory pointer should be returned.
 *
 * @return  A NULL pointer if the passed ::EmberBuffer value is
 * ::EMBER_NULL_BUFFER. Otherwise, a pointer to the corresponding memory
 * segment.
 */
uint8_t *emberGetBufferPointer(EmberBuffer buffer);

/** @brief An API that returns the length in bytes of the passed ::EmberBuffer
 * buffer.
 *
 * @param buffer   A pointer to the ::EmberBuffer buffer for which the
 * corresponding length in bytes should be returned.
 *
 * @return  The length in bytes of memory segment corresponding to the passed
 * ::EmberBuffer buffer.
 */
uint16_t emberGetBufferLength(EmberBuffer buffer);

//@}//END APIs

/** @} // END addtogroup
*/
/**
 * @file event.h
 * @brief Scheduling events for future execution.
 * See @ref event for documentation.
 *
 * <!--Copyright 2014 Silicon Laboratories, Inc.                         *80*-->
 */


/**
 * @addtogroup event
 *
 * These macros implement an event abstraction that allows the application
 * to schedule code to run after some specified time interval.  An event
 * consists of a procedure to be called at some point in the future and
 * a control object that determines the procedure should be called.  Events
 * are also useful for when an ISR needs to initiate an action that should
 * run outside of ISR context.
 *
 * See event.h for source code.
 *
 * Note that while not required, it is recommended that the event-handling
 * procedure explicitly define the recurrence of the next event, either by
 * rescheduling it via some kind of @e emberEventControlSetDelayXX() call or by
 * deactivating it via a call to ::emberEventControlSetInactive().
 * In cases where the handler does not explicitly reschedule or cancel the
 * event, the default behavior of the event control system is to keep the
 * event immediately active as if the handler function had called
 * ::emberEventControlSetActive(someEvent) or
 * ::emberEventControlSetDelayMS(someEvent, 0)
 *
 * The base time units for events are ticks.  Each tick is approximately equal
 * to a millisecond, but the true duration depends on the platform.  The
 * duration of a tick is 1000 / ::MILLISECOND_TICKS_PER_SECOND, where 1000 is
 * the number of milliseconds per second and ::MILLISECOND_TICKS_PER_SECOND is
 * the platform-specific number of ticks per second.  For example,
 * ::MILLISECOND_TICKS_PER_SECOND on the EM357 SoC is 1024, so each tick is
 * therefore 1000 / 1024 = ~0.98 milliseconds.  Calling
 * ::emberEventControlSetDelayMS(someEvent, 100) on the EM357 SoC will schedule
 * the event for 100 ticks * (1000 milliseconds / 1024 ticks) =
 * ~97.7 milliseconds.  Note however that the accuracy of the base tick depends
 * on your timer source.  Further, the scheduled delay is the minimum delay.
 * If ::emberRunEvents or ::emberRunTask are not called frequently enough, the
 * actual delay may be longer than the scheduled delay.
 *
 * Additionally, the APIs for quarter second and minute delays
 * (::emberEventControlSetDelayQS and ::emberEventControlSetDelayMinutes) use
 * "binary" units.  One quarter second is 256 ticks and one minute is 65536
 * ticks.  Calling ::emberEventControlSetDelayMinutes(someEvent, 3) on the
 * EM357 SoC will schedule the event for 3 minutes * (65536 ticks / minute) *
 * (1000 milliseconds / 1024 ticks) = ~3.2 minutes.  It is possible to avoid
 * these binary units by using ::emberEventControlSetDelayMS and the various
 * MILLISECOND_TICKS_PER_XXX multipliers.  For example, calling
 * ::emberEventControlSetDelayMS(someEvent, 3 * MILLISECOND_TICKS_PER_MINUTE)
 * will delay for 3 minutes on any platform.  Be aware of
 * ::EMBER_MAX_EVENT_CONTROL_DELAY_MS when using this approach.
 *
 * Following are some brief usage examples.
 * @code
 * EmberEventControl delayEvent;
 * EmberEventControl signalEvent;
 * EmberEventControl periodicEvent;
 *
 * void delayEventHandler(void)
 * {
 *   // Disable this event until its next use.
 *   emberEventControlSetInactive(delayEvent);
 * }
 *
 * void signalEventHandler(void)
 * {
 *   // Disable this event until its next use.
 *   emberEventControlSetInactive(signalEvent);
 *
 *   // Sometimes we need to do something 100 ms later.
 *   if (somethingIsExpected)
 *     emberEventControlSetDelayMS(delayEvent, 100);
 * }
 *
 * void periodicEventHandler(void)
 * {
 *   emberEventControlSetDelayQS(periodicEvent, 4);
 * }
 *
 * void someIsr(void)
 * {
 *   // Set the signal event to run at the first opportunity.
 *   emberEventControlSetActive(signalEvent);
 * }
 *
 * // Put the controls and handlers in an array.  They will be run in
 * // this order.
 * EmberEventData events[] =
 *  {
 *    { &delayEvent,    delayEventHandler },
 *    { &signalEvent,   signalEentHandler },
 *    { &periodicEvent, periodicEventHandler },
 *    { NULL, NULL }                            // terminator
 *  };
 *
 * void main(void)
 * {
 *   // Cause the periodic event to occur once a second.
 *   emberEventControlSetDelayQS(periodicEvent, 4);
 *
 *   while (TRUE) {
 *     emberRunEvents(events);
 *   }
 * }
 * @endcode
 *
 * @{
 */

// Controlling events

// Possible event status values.  Having zero as the 'inactive' value
// causes events to initially be inactive.
//

/** @brief Sets this ::EmberEventControl as inactive (no pending event).
 */

/** @brief Returns TRUE if the event is active, FALSE otherwise.
 */

/** @brief Sets this ::EmberEventControl to run at the next available
    opportunity.
 */

/** @brief Sets this ::EmberEventControl to run at the next available
    opportunity.
 */
void emEventControlSetActive(EmberEventControl *event);

/** @brief The maximum delay that may be passed to
 * ::emberEventControlSetDelayMS.
 */

/** @brief Sets this ::EmberEventControl to run "delay" milliseconds in the
 *  future.
 *  NOTE: To avoid rollover errors in event calculation, the delay must be
 *  less than ::EMBER_MAX_EVENT_CONTROL_DELAY_MS.
 */

/** @brief Sets this ::EmberEventControl to run "delay" milliseconds in the
 *  future.
 *  NOTE: To avoid rollover errors in event calculation, the delay must be
 *  less than ::EMBER_MAX_EVENT_CONTROL_DELAY_MS.
 */
void emEventControlSetDelayMS(EmberEventControl*event, uint32_t delay);

/** @brief The maximum delay that may be passed to
 * ::emberEventControlSetDelayQS.
 */

/** @brief Sets this ::EmberEventControl to run "delay" quarter seconds
 *  in the future. The 'quarter seconds' are actually 256 milliseconds long.
 *  NOTE: To avoid rollover errors in event calculation, the delay must be
 *  less than ::EMBER_MAX_EVENT_CONTROL_DELAY_QS.
 */

/** @brief The maximum delay that may be passed to
 * ::emberEventControlSetDelayMinutes.
 */

/** @brief Sets this ::EmberEventControl to run "delay" minutes in the future.
 *  The 'minutes' are actually 65536 (0x10000) milliseconds long.
 *  NOTE: To avoid rollover errors in event calculation, the delay must be
 *  less than ::EMBER_MAX_EVENT_CONTROL_DELAY_MINUTES.
 */

/** @brief Returns The amount of milliseconds remaining before the event is
 *  scheduled to run.  If the event is inactive, MAX_INT32U_VALUE is returned.
 */

/** @brief Returns The amount of milliseconds remaining before the event is
 *  scheduled to run.  If the event is inactive, MAX_INT32U_VALUE is returned.
 */
uint32_t emEventControlGetRemainingMS(EmberEventControl *event);


// Running events

/** @brief An application typically creates an array of events
 * along with their handlers.
 *
 * The main loop passes the array to ::emberRunEvents() in order to call
 * the handlers of any events whose time has arrived.
 */
void emberRunEvents(EmberEventData *events);

/** @brief If an application has initialized a task via emberTaskInit, to
 *  run the events associated with that task, it should could ::emberRunTask()
 *  instead of ::emberRunEvents().
 */
void emberRunTask(EmberTaskId taskid);

/** @brief Returns the number of milliseconds before the next event
 *  is scheduled to expire, or maxMs if no event is scheduled to expire
 *  within that time.
 *  NOTE: If any events are modified within an interrupt, in order to guarantee
 *  the accuracy of this API, it must be called with interrupts disabled or
 *  from within an ATOMIC() block.
 */
uint32_t emberMsToNextEvent(EmberEventData *events, uint32_t maxMs);

/** @brief This function does the same as emberMsToNextEvent() with the
 *  following addition.  If the returnIndex is non-NULL, it will set the value
 *  pointed to by the pointer to be equal to the index of the event that is
 *  ready to fire next.  If no events are active, then it returns 0xFF.
 */
uint32_t emberMsToNextEventExtended(EmberEventData *events, uint32_t maxMs, uint8_t* returnIndex);

/** @brief Returns the number of milliseconds before the next stack event is
 * scheduled to expire.
 */
uint32_t emberMsToNextStackEvent(void);


/** @brief Initializes a task to be used for managing events and processor
 *  idling state.
 *  Returns the ::EmberTaskId which represents the newly created task
 */
EmberTaskId emberTaskInit(EmberEventData *events);

/** @brief Indicates that a task has nothing to do (unless any events are
 *   pending) and that it would be safe to idle the CPU if all other tasks
 *   also have nothing to do.
 *  This API should always be called with interrupts disabled.  It will forcibly
 *   re-enable interrupts before returning
 *  Returns TRUE if the processor was idled, FALSE if idling wasn't permitted
 *   because some other task has something to do.
 */
_Bool emberMarkTaskIdle(EmberTaskId taskid);

  /** @brief Call this to indicate that an application supports processor idling
   */

  void emTaskEnableIdling(_Bool allow);

  /** @brief Indicates that a task has something to do, so the CPU should not be
   *   idled until emberMarkTaskIdle is next called on this task.
   */

  void emMarkTaskActive(EmberTaskId taskid);


// @} END addtogroup


/**
 * @file network-management.h
 * See @ref network_management for documentation.
 *
 * <!--Copyright 2014 by Silicon Labs. All rights reserved.              *80*-->
 */

/**
 * @addtogroup network_management
 * @brief Ember Connect API for finding, forming, joining, and leaving Connect
 * networks.
 *
 * See network-management.h for source code.
 * @{
 */


/** @brief The maximum length in bytes of the application beacon payload.
 */

/** @name Handlers*/
//@{

/** @brief This stack handler is invoked if a beacon is received during the
 *  scanning procedure, if this was initiated by the application with the
 *  ::emberStartActiveScan stack APIs.
 *
 * @param panId   The source pan ID of the received beacon.
 *
 * @param nodeId  The source node ID of the received beacon.
 *
 * @param payloadLength  The length in bytes of the application beacon payload
 *   of the received beacon.
 *
 * @param payload   A pointer to the application beacon payload of the received
 *   beacon.
 */
void emberIncomingBeaconHandler(EmberPanId panId,
                                EmberNodeId nodeId,
                                uint8_t payloadLength,
                                uint8_t *payload);

/** @brief This stack handler is invoked after the application has called the
 *  ::emberStartActiveScan stack API to inform the application that the scanning
 *  procedure has completed.
 */
void emberActiveScanCompleteHandler(void);

/** @brief This stack handler is invoked after the application has called the
 *  ::emberStartEnergyScan stack API to inform the application that the energy
 *  scan procedure has completed and to provide statistics.
 *
 *  params mean        The average energy detected.
 *  params min         The minimum energy detected.
 *  params max         The maximum energy detected.
 *  params variance    The variance of the energy detected.
 */
void emberEnergyScanCompleteHandler(int8_t mean,
                                    int8_t min,
                                    int8_t max,
                                    uint16_t variance);

//@}//END Handlers

/** @name APIs*/
//@{

/** @brief Initializes the radio and the Ember stack.
 *
 * Device configuration functions must be called before ::emberInit()
 * is called.
 *
 * @note The application must check the return value of this function. If the
 * initialization fails, normal messaging functions will not be available.
 * Some failure modes are not fatal, but the application must follow certain
 * procedures to permit recovery.
 * Ignoring the return code will result in unpredictable radio and API behavior.
 * (In particular, problems with association will occur.)
 *
 * @return An ::EmberStatus value indicating successful initialization or the
 *   reason for failure.
 */
EmberStatus emberInit(void);

/** @brief A periodic tick routine that should be called:
 * - in the application's main event loop,
 * - as soon as possible after any radio interrupts, and
 * - after ::emberInit().
 */
void emberTick(void);

/** @brief Resume network operation after a reboot.
 *
 * It is required that this be called on boot prior to ANY network operations.
 * This will initialize the networking system and attempt to resume the
 * previous network identity and configuration.  If the node was not previously
 * joined, this routine should still be called.
 *
 * If the node was previously joined to a network it will retain its original
 * type (e.g. coordinator, router, end device, etc.)
 *
 * ::EMBER_NOT_JOINED is returned if the node is not part of a network.
 *
 * @return An ::EmberStatus value that indicates one of the following:
 *   - successful initialization,
 *   - ::EMBER_NOT_JOINED if the node is not part of a network, or
 *   - the reason for failure.
 */
EmberStatus emberNetworkInit(void);

/** @brief This function will start an active scan. ::EMBER_SUCCESS signals that
 * the scan successfully started.  Note that while a scan can be initiated
 * while the node is currently joined to a network, the node will generally
 * be unable to communicate with its PAN during the scan period, so care
 * should be taken when performing scans of any significant duration while
 * presently joined to an existing PAN. Upon receiving a beacon, the
 * ::emberIncomingBeaconHandler stack handler shall be called. At the end of
 * the scanning procedure the ::emberActiveScanCompleteHandler stack handler
 * shall be called.
 *
 * Possible error responses and their meanings:
 * - ::EMBER_MAC_SCANNING, we are already scanning.
 * - ::EMBER_PHY_INVALID_CHANNEL, the specified channel is not a valid channel
 *   on the current platform.
 *
 * @param channel  The channel to scan.
 */
EmberStatus emberStartActiveScan(uint8_t channel);

/** @brief This function will kick off an energy scan. ::EMBER_SUCCESS signals
 * that the scan successfully started.  Note that while a scan can be initiated
 * while the node is currently joined to a network, the node will generally
 * be unable to communicate with its PAN during the scan period, so care
 * should be taken when performing scans of any significant duration while
 * presently joined to an existing PAN. At the end of the scanning procedure the
 * ::emberEnergyScanCompleteHandler stack handler shall be called.
 *
 * Possible error responses and their meanings:
 * - ::EMBER_MAC_SCANNING, we are already scanning.
 * - ::EMBER_PHY_INVALID_CHANNEL, the specified channel is not a valid channel
 *   on the current platform.
 * - ::EMBER_NO_BUFFERS, the stack doesn't have enough memory at the moment to
 *   perform the requested scan.
 *
 * @param channel  The channel to scan.
 *
 * @param samples   The number of energy samples to be produced. Each sample is
 * performed averaging the detected energy over 8 symbols time (the actual
 * length depends on the selected PHY configuration).
 */
EmberStatus emberStartEnergyScan(uint8_t channel, uint8_t samples);


/** @brief This API allows the application to set the application portion of the
 * beacon payload. This is by default set to the empty string.
 *
 * @param payloadLength  The length in bytes of the application beacon payload
 *   to be set. This value can not exceed
 *   ::EMBER_MAC_MAX_APP_BEACON_PAYLOAD_LENGTH.
 *
 * @param payload   A pointer to the application beacon payload to be set.
 *
 * @return an ::EmberStatus value of ::EMBER_SUCCESS if the application beacon
 * payload was successfully set, otherwise an ::EmberStatus value indicating
 * the reason of failure.
 */
EmberStatus emberSetApplicationBeaconPayload(uint8_t payloadLength,
                                             uint8_t *payload);

/** @brief Forms a new network by becoming the coordinator.
 *
 * @param parameters  An ::EmberNetworkParameters value that specifies the
 *   network parameters of the network to be formed.
 *
 * @return An ::EmberStatus value that indicates either the successful formation
 *   of the new network, or the reason that the network formation failed.
 */
EmberStatus emberFormNetwork(EmberNetworkParameters *parameters);

/** @brief Causes the stack to associate with the network using the
 * specified network parameters. It can take several seconds for the stack to
 * associate with the local network. Do not send messages until a call to the
 * ::emberStackStatusHandler() callback informs you that the stack is up.
 *
 * @param nodeType    Specification of the role that this node will have in
 *   the network. This role can be ::EMBER_STAR_RANGE_EXTENDER,
 *   ::EMBER_STAR_END_DEVICE or ::EMBER_STAR_SLEEPY_END_DEVICE.
 *
 * @param nodeId    An ::EmberNodeId value indicating the short ID the node
 * intends to use for addressing purposes. If this value is ::EMBER_NULL_NODE_ID
 * the network coordinator will allocate a new short address. Addresses should
 * be allocated by the coordinator unless there is a specific need to join a
 * network with a specific ID. If a specific ID is used, uniqueness should be
 * guaranteed across the entire network by the application, via some out of band
 * means.
 *
 * @param parameters  An ::EmberNetworkParameters value that specifies the
 * network parameters of the network with which the node should associate.
 *
 * @return An ::EmberStatus value that indicates either:
 * - that the association process began successfully, or
 * - the reason for failure.
 */
EmberStatus emberJoinNetworkExtended(EmberNodeType nodeType,
                                     EmberNodeId nodeId,
                                     EmberNetworkParameters *parameters);


/** @brief Tells the stack to allow other nodes to join the network
  * with this node as their parent.  Joining is initially disabled by default.
  * This function may only be called after the node is part of a network
  * and the stack is up.
  *
  * @param duration  A value of 0x00 disables joining. A value of 0xFF enables
  *   joining indefinitely.  Any other value enables joining for that number of
  *   seconds.
  *
  * @return an ::EmberStatus value of ::EMBER_SUCCESS if the permit joining
  *   was successfully set, otherwise an ::EmberStatus value indicating the
  *   reason of failure.
  */
EmberStatus emberPermitJoining(uint8_t duration);

/** @brief Causes the stack to go up with the passed network parameters without
 * performing any over-the-air message exchange.
 *
 * @param nodeType    Specification of the role that this node will have in
 *   the network. For now, the only role allowed in the commissioning API is
 *   ::EMBER_DIRECT_DEVICE.
 *
 * @param nodeId  An ::EmberNodeId value that specifies the short ID the node
 * shall have. The passed node ID must be a valid short address
 * (any value other than ::EMBER_NULL_NODE_ID or ::EMBER_BROADCAST_ADDRESS).
 *
 * @param parameters  An ::EmberNetworkParameters value that specifies the
 *   network parameters of the network the node should participate in.
 *
 * @return An ::EmberStatus value that indicates either:
 *   - that the node successfully commissioned the passed network parameters
 *   - the reason for failure.
 */
EmberStatus emberJoinCommissioned(EmberNodeType nodeType,
                                  EmberNodeId nodeId,
                                  EmberNetworkParameters *parameters);

/** @brief Forgets the current network and reverts to a network status of
 * ::EMBER_NO_NETWORK.
 */
void emberResetNetworkState(void);

//@}//END APIs


/** @} // END addtogroup
 */
/**
 * @file message.h
 * @brief Ember Connect APIs and handlers for sending and receiving messages.
 * See @ref message for documentation.
 *
 * <!--Copyright 2015 by Silicon Labs. All rights reserved.              *80*-->
 */

/**
 * @addtogroup message
 * @brief Ember Connect APIs sending and receiving messages.
 *
 * See message.h for source code.
 * @{
 */


/** @brief The maximum length in bytes of the application payload for an
 * unsecured message.
 */

/** @brief The maximum length in bytes of the application payload for a
 * secured message.
 */

/** @brief The maximum allowed endpoint value.
 */

/** @name Handlers*/
//@{

/** @brief A callback invoked when the stack has completed sending a message.
 *
 * @param status   An ::EmberStatus value of ::EMBER_SUCCESS if an ACK was
 *  received from the destination or no ACK was requested, a value of
 *  ::EMBER_MAC_NO_ACK_RECEIVED if an ACK was requested and no ACK was received,
 *  a value of ::EMBER_MAC_INDIRECT_TIMEOUT is the destination is a sleepy node
 *  and the packet timed-out before the sleepy node sent a data request, a value
 *  of ::EMBER_MAC_INDIRECT_MESSAGE_PURGED is the destination is a sleepy node
 *  and it was removed from the child table while the packet was stored in the
 *  indirect queue, a value of ::EMBER_PHY_TX_CCA_FAIL if the node failed all
 *  the clear channel assessment attempts.
 *
 * @param message  An ::EmberOutgoingMessage describing the outgoing packet.
 */
void emberMessageSentHandler(EmberStatus status, EmberOutgoingMessage *message);

/** @brief A callback invoked when a packet has been received.
 *
 * @param message  An ::EmberIncomingMessage describing the incoming packet.
 */
void emberIncomingMessageHandler(EmberIncomingMessage *message);

//@}//END Handlers

/** @name APIs*/
//@{

/** @brief Sends a message to the passed destination short ID.
 *
 * @param destination The destination node short ID.
 *
 * @param endpoint        The destination endpoint of the outgoing message. This
 *                        value can not exceed ::EMBER_MAX_ENDPOINT.
 *
 * @param messageTag      A value chosen by the application. This value will be
 *                        passed in the corresponding
 *                        ::emberMessageSentHandler() call.
 *
 * @param messageLength The size in bytes of the message payload. Please refer
 * to ::EMBER_MAX_UNSECURED_APPLICATION_PAYLOAD_LENGTH or
 * ::EMBER_MAX_SECURED_APPLICATION_PAYLOAD_LENGTH for the maximum message length
 * allowed.
 *
 * @param message A pointer to an array of bytes containing the message payload.
 *
 * @param options  Specifies the ::EmberMessageOptions for the outgoing message.
 *
 * @return an ::EmberStatus value of ::EMBER_SUCCESS if the message was accepted
 * by the stack, a value of ::EMBER_INVALID_CALL if the node is not joined to a
 * network, the packet length is 0, the passed TX options indicates some feature
 * feature that is not supported or the passed endpoint exceeds
 * ::EMBER_MAX_ENDPOINT, a value of ::EMBER_MESSAGE_TOO_LONG if the
 * message does not fit in a single frame, a value of ::EMBER_PHY_TX_BUSY if the
 * message cannot be sent since the node does not support MAC queuing and the
 * radio is currently busy. If a success status is returned, the
 * ::emberMessageSentHandler() callback will be invoked by the stack to indicate
 * whether the message was successfully delivered or the reason of failure.
 */
EmberStatus emberMessageSend(EmberNodeId destination,
                             uint8_t endpoint,
                             uint8_t messageTag,
                             EmberMessageLength messageLength,
                             uint8_t *message,
                             EmberMessageOptions options);

/** @brief Sends a data request command to the parent node.
 *
 * @return and ::EmberStatus value of ::EMBER_SUCCESS if the data poll was sent
 * out successfully, a value of ::EMBER_INVALID_CALL if the node is not joined
 * to a network, or the node is not an end device.
 */
EmberStatus emberPollForData(void);

//@}//END APIs


/** @} // END addtogroup
 */
/**
 * @file stack-info.h
 * @brief Ember Connect API for accessing and setting stack information.
 * See @ref stack_info for documentation.
 *
 * <!--Copyright 2014 by Silicon Labs. All rights reserved.              *80*-->
 */

/**
 * @addtogroup stack_info
 *
 * See stack-info.h for source code.
 * @{
 */

/** @brief A mask of the tasks that prevent a device from sleeping.
 */

/** @name Handlers*/
//@{

/** @brief A callback invoked when the status of the stack changes.
 *
 * The application is free to begin messaging once it receives the
 * ::EMBER_NETWORK_UP status.
 *
 * @param status  Stack status. One of the following:
 * - ::EMBER_NETWORK_UP
 * - ::EMBER_NETWORK_DOWN
 * - ::EMBER_NO_VALID_BEACONS
 * - ::EMBER_JOIN_SCAN_FAILED
 * - ::EMBER_JOIN_FAILED
 * - ::EMBER_JOIN_DENIED
 * - ::EMBER_JOIN_TIMEOUT
 * - ::EMBER_CHANNEL_CHANGED
 */
void emberStackStatusHandler(EmberStatus status);

/** @brief This handler is invoked at coordinator or range extender nodes when
 * a new child has joined the device.
 *
 * @param nodeType  The role of the joining device (::EMBER_STAR_RANGE_EXTENDER,
 * ::EMBER_STAR_END_DEVICE or ::EMBER_STAR_SLEEPY_END_DEVICE).
 *
 * @param nodeId    The node ID of the joining device.
 */
void emberChildJoinHandler(EmberNodeType nodeType,
                           EmberNodeId nodeId);

/** @brief This handler is invoked in ISR context whenever a stack-related ISR
 * routine fires.
 */
void emberStackIsrHandler(void);

//@}//END Handlers

/** @name APIs*/
//@{

/** @brief Immediately turns the radio power completely off.
 *
 * After calling this function, you must not call any other stack function
 * except emberStackPowerUp(). This is because all other stack
 * functions require that the radio is powered on for their
 * proper operation.
 */
void emberStackPowerDown(void);

/** @brief Powers up the radio.  Typically called coming out of sleep.
 *
 * For non-sleepy devices, also turns the radio on and leaves it in rx mode.
 */
void emberStackPowerUp(void);

/** @brief Returns the current join status.
 *
 *   Returns a value indicating whether the node is joining, joined to, or
 *   leaving a network.
 *
 * @return An ::EmberNetworkStatus value indicating the current join status.
 */
EmberNetworkStatus emberNetworkState(void);

/** @brief Indicates whether the stack is currently up.
 *
 *   Returns true if the stack is joined to a network and ready to send and
 *   receive messages.  This reflects only the state of the local node; it does
 *   not indicate whether or not other nodes are able to communicate with this
 *   node.
 *
 * @return TRUE if the stack is up, false otherwise.
 */
_Bool emberStackIsUp(void);

/** @brief Sets the security key.
 *
 * @param key   An ::EmberKeyData value containing the security key to be set.
 *
 * @return An EmberStatus value of ::EMBER_SUCCESS if the key was successfully
 *   set. Otherwise it returns an EmberStatus value of ::EMBER_INVALID_CALL.
 */
EmberStatus emberSetSecurityKey(EmberKeyData *key);

/** @brief Retrieves the stack counter corresponding to the passed counter type.
 *
 * @param counterType   An ::EmberCounterType value indicating the stack counter
 * to be retrieved.
 *
 * @return An EmberStatus value of ::EMBER_SUCCESS if the stack counter was
 * successfully retrieved. An EmberStatus value of ::EMBER_INVALID_CALL if the
 * passed counterType is invalid. An EmberStatus value of
 * ::EMBER_LIBRARY_NOT_PRESENT if the stack counter library is not present.
 */
EmberStatus emberGetCounter(EmberCounterType counterType, uint32_t *count);

/** @brief Sets the channel to use for sending and receiving messages on the
 * current logical network. For a list of available radio channels, see the
 * technical specification for the RF communication module in your Developer
 * Kit.
 *
 * Note: Care should be taken when using this API,
 * as all devices on a network must use the same channel.
 *
 * @param channel  Desired radio channel.
 *
 * @return An ::EmberStatus value indicating the success or
 *  failure of the command.
 */
EmberStatus emberSetRadioChannel(uint8_t channel);

/** @brief Gets the radio channel to which a node is set on the current
 * logical network. The possible return values depend on the radio in use.
 * For a list of available radio channels, see the technical specification
 * for the RF communication module in your Developer Kit.
 *
 * @return Current radio channel.
 */
uint8_t emberGetRadioChannel(void);

/** @brief Sets the radio output power at which a node is to operate for the
 * current logical network. Ember radios have discrete power settings. For a
 * list of available power settings, see the technical specification for the RF
 * communication module in your Developer Kit.
 * Note: Care should be taken when using this API on a running network,
 * as it will directly impact the established link qualities neighboring nodes
 * have with the node on which it is called.  This can lead to disruption of
 * existing routes and erratic network behavior.
 * Note: If the requested power level is not available on a given radio, this
 * function will use the next higher available power level.
 *
 * @param power  Desired radio output power, in dBm.
 *
 * @return An ::EmberStatus value indicating the success or failure of the
 * command.  Failure indicates that the requested power level is out of range.
 */
EmberStatus emberSetRadioPower(int8_t power);

/** @brief Gets the radio output power of the current logical network at which
 * a node is operating. Ember radios have discrete power settings. For a list of
 * available power settings, see the technical specification for the RF
 * communication module in your Developer Kit.
 *
 * @return Current radio output power, in dBm.
 */
int8_t emberGetRadioPower(void);

/** @brief This API allows the application to turn the radio on/off. This API is
 * intended to be used with direct devices only.
 *
 * @param radioOn  If this parameter is true, the radio shall be turned on,
 * otherwise it shall be turned off.
 *
 * @return An ::EmberStatus value indicating the success or failure of the
 * command.  Failure indicates that the node type is a type other than
 * ::EMBER_DIRECT_DEVICE.
 */
EmberStatus emberSetRadioPowerMode(_Bool radioOn);

/** @brief Sets the MAC layer transmission parameters.
 *
 * @param checkCca   If this is set to TRUE, the node will perform a clear
 *                   channel assessment prior to transmit a packet. If the
 *                   channel is not clear, a random backoff shall be performed.
 *                   If this is set to FALSE, no clear channel assessment is
 *                   performed and the packet shall be transmitted right away.
 *                   This parameter is set by default to TRUE.
 *
 * @param maxCcaAttempts   The maximum number of clear channel assessment
 *                         attempts that shall be performed prior to fail to
 *                         transmit a packet with ::EMBER_PHY_TX_CCA_FAIL
 *                         status. This parameter is set by default to 4.
 *                         Note: this is meaningful only if the checkCca
 *                         parameter is set to TRUE.
 *
 * @param minBackoffExp   The backoff exponent to be used if the initial channel
 *                        clear assessment fails. This parameter is set by
 *                        default to 3.
 *                        Note: this is meaningful only if the checkCca
 *                        parameter is set to TRUE.
 *
 * @param maxBackoffExp   The backoff exponent to be used if the final channel
 *                        clear assessment fails. This parameter is set by
 *                        default to 5.
 *                        Note: this is meaningful only if the checkCca
 *                        parameter is set to TRUE.
 *
 * @param maxRetries      The number of transmission retries that shall be
 *                        performed in case no acknowledgement was received.
 *                        This parameter is set by default to 3 (which means
 *                        that a total of 4 transmission attempts shall per
 *                        performed).
 *
 * @return An ::EmberStatus value indicating whether the MAC parameters were
 * successfully set or the reason of failure.
 */
EmberStatus emberSetMacParams(_Bool checkCca,
                              uint8_t maxCcaAttempts,
                              uint8_t minBackoffExp,
                              uint8_t maxBackoffExp,
                              uint8_t maxRetries);

/** @brief Returns a bitmask indicating the stack's current tasks.
 *
 *  The mask ::EMBER_HIGH_PRIORITY_TASKS defines which tasks are high
 *  priority.  Devices should not sleep if any high priority tasks are active.
 *  Active tasks that are not high priority are waiting for
 *  messages to arrive from other devices.  If there are active tasks,
 *  but no high priority ones, the device may sleep but should periodically
 *  wake up and call ::emberPollForData() in order to receive messages.  Parents
 *  will hold messages for ::EMBER_INDIRECT_TRANSMISSION_TIMEOUT_MS milliseconds
 *  before discarding them.
 *
 * @return A bitmask of the stack's active tasks.
 */
uint16_t emberCurrentStackTasks(void);

/** @brief Indicates whether the stack is currently in a state where
 * there are no high priority tasks and may sleep.
 *
 * There may be tasks expecting incoming messages, in which case the device
 * should periodically wake up and call ::emberPollForData() in order to receive
 * messages. This function can only be called when the node type is
 * ::EMBER_STAR_SLEEPY_END_DEVICE.
 *
 * @return TRUE if the application may sleep but the stack may be expecting
 * incoming messages.
 */

/** @brief Indicates whether the stack currently has any tasks pending.
 *
 * If there are no pending tasks then ::emberTick() does not need to be called
 * until the next time a stack API function is called. This function can only be
 * called when the node type is ::EMBER_STAR_SLEEPY_END_DEVICE.
 *
 * @return TRUE if the application may sleep for as long as it wishes.
 */

extern EmberNodeId emLocalNodeId;
extern EmberPanId emLocalPanId;
extern EmberNodeId emParentId;
extern EmberNodeType emNodeType;
extern EmberEUI64 emLocalEui64;


//@}//END APIs

/** @} // END addtogroup
*/
/**
 * @file ember-debug.h
 * See @ref debug for documentation.
 *
 * <!--Copyright 2014 by Silicon Laboratories. All rights reserved.      *80*-->
 */


// We currently don't have debug support in Connect.

// Define the values for DEBUG_LEVEL




/** @file command-interpreter.h
* @brief Processes commands coming from the serial port.
* See @ref command_interpreter for documentation.
*
* <!-- Culprit(s): Richard Kelsey, Matteo Paris -->
*
* <!-- Copyright 2013 Silicon Laboratories, Inc.                        *80* -->
*/


/** @addtogroup command_interpreter
* Interpret serial port commands. See command-interpreter.c for source code.
*
* See the following application usage example followed by a brief explanation. 
* @code
*
* // Usage: network form 22 0xAB12 -3 { 00 01 02 A3 A4 A5 A6 A7 }
* void formCommand(void)
* {
*   uint8_t channel = emberUnsignedCommandArgument(0);
*   uint16_t panId  = emberUnsignedCommandArgument(1);
*   int8_t power   = emberSignedCommandArgument(2);
*   uint8_t length;
*   uint8_t *eui64  = emberStringCommandArgument(3, &length);
*   ... 
*   ... call emberFormNetwork() etc
*   ...
* }
* 
* // The main command table.
* EmberCommandEntry emberCommandTable[] = {
*   emberCommandEntrySubMenu("network",  networkCommands, "Network form/join commands"),
*   emberCommandEntryAction("status",    statusCommand,   "Prints application status), 
*   ...
*   emberCommandEntryTerminator()
  };
*
* // The table of network commands.
* EmberCommandEntry networkCommands[] = {
*   emberCommandEntryAction("form", formCommand, "uvsh", "Form a network"),
*   emberCommandEntryAction("join", joinCommand, "uvsh", "Join a network"),
*   ...
*   emberCommandEntryTerminator()
  };
*
* void main(void)
* {
*    emberCommandReaderInit();
*    while(1) {
*      ...
*      // Process input and print prompt if it returns TRUE.
*      if (emberProcessCommandInput()) {
*         emberSerialPrintf("%p>", PROMPT);
*      }
*      ...
*    }
* }
* @endcode
*
* -# Applications specify the commands that can be interpreted
*    by defining the emberCommandTable array of type ::EmberCommandEntry.
*    The table includes the following information for each command:
*   -# The full command name.
*   -# Your application's function name that implements the command.
*   -# An ::EmberCommandEntry::argumentTypes string specifies the number and types of arguments
*      the command accepts.  See ::argumentTypes for details.
*   -# A description string explains the command.
*   .
* -# A default error handler ::emberCommandErrorHandler() is provided to
*    deal with incorrect command input. Applications may override it.
* -# The application calls ::emberCommandReaderInit() to initalize, and
*    ::emberProcessCommandInput() in its main loop.
* -# Within the application's command functions, use emberXXXCommandArgument()
*    functions to retrieve command arguments.
*
* The command interpreter does extensive processing and validation of the
* command input before calling the function that implements the command.
* It checks that the number, type, syntax, and range of all arguments
* are correct.  It performs any conversions necessary (for example, 
* converting integers and strings input in hexadecimal notation into
* the corresponding bytes), so that no additional parsing is necessary
* within command functions.  If there is an error in the command input,
* ::emberCommandErrorHandler() is called rather than a command function.
*
* The command interpreter allows inexact matches of command names.  The
* input command may be either shorter or longer than the actual command.
* However, if more than one inexact match is found and there is no exact
* match, an error of type EMBER_CMD_ERR_NO_SUCH_COMMAND will be generated.
* To disable this feature, define EMBER_REQUIRE_EXACT_COMMAND_NAME in the
* application configuration header.
*
*@{
*/

/** @name Command Table Settings
 *@{
 */
/** The maximum number of arguments a command can have.  A nested command
 * counts as an argument.
 */


/** Whether or not the command entry structure will include descriptions for
 *  the commands.  This consumes additional CONST space, which is expensive 
 *  on the XAP.  By default descriptions are not included.
 */

/** @} // END name group
 */

// The (+ 1) takes into account the leading command.

typedef void (*CommandAction)(void);

typedef const struct {
  /** Use letters, digits, and underscores, '_', for the command name.
   * Command names are case-sensitive.
   */
  const char * name;
  /** A reference to a function in the application that implements the 
   *  command.
   *  If this entry refers to a nested command, then action field
   *  has to be set to NULL.
   */
  CommandAction action;
  /** 
   * In case of normal (non-nested) commands, argumentTypes is a 
   * string that specifies the number and types of arguments the
   *  command accepts.  The argument specifiers are:
   *  - u:   one-byte unsigned integer.
   *  - v:   two-byte unsigned integer
   *  - w:   four-byte unsigned integer
   *  - s:   one-byte signed integer
   *  - b:   string.  The argument can be entered in ascii by using 
   *         quotes, for example: "foo".  Or it may be entered
   *         in hex by using curly braces, for example: { 08 A1 f2 }.
   *         There must be an even number of hex digits, and spaces
   *         are ignored.
   *  - *:   zero or more of the previous type.  
   *         If used, this must be the last specifier.
   *  - ?:   Unknown number of arguments. If used this must be the only
   *         character. This means, that command interpreter will not
   *         perform any validation of arguments, and will call the 
   *         action directly, trusting it that it will handle with 
   *         whatever arguments are passed in.
   *  Integer arguments can be either decimal or hexidecimal.
   *  A 0x prefix indicates a hexidecimal integer.  Example: 0x3ed.
   *
   *  In case of a nested command (action is NULL), then this field
   *  contains a pointer to the nested EmberCommandEntry array.
   */
  const char * argumentTypes;
  /** A description of the command.
   */

  const char * description;
} EmberCommandEntry;


  /* @brief Macro to define a CLI action */

  /* @brief Macro to define a CLI sub-menu (nested command) */

  /* @briefy Macro to define a command entry array terminator.*/


/** 
 * A pointer to the currently matching command entry.  
 * Only valid from within a command function.
 * If the original command was nested, points to the
 * final (non-nested) command entry.
 */
extern EmberCommandEntry *emberCurrentCommand;

extern EmberCommandEntry emberCommandTable[];

/** 
 * Configuration byte. 
 */
extern uint8_t emberCommandInterpreter2Configuration;


typedef uint8_t EmberCommandStatus;
enum
{
  EMBER_CMD_SUCCESS,                          
  EMBER_CMD_ERR_PORT_PROBLEM,                 
  EMBER_CMD_ERR_NO_SUCH_COMMAND,              
  EMBER_CMD_ERR_WRONG_NUMBER_OF_ARGUMENTS,   
  EMBER_CMD_ERR_ARGUMENT_OUT_OF_RANGE,        
  EMBER_CMD_ERR_ARGUMENT_SYNTAX_ERROR,        
  EMBER_CMD_ERR_STRING_TOO_LONG,              
  EMBER_CMD_ERR_INVALID_ARGUMENT_TYPE
};

/** @name Functions to Retrieve Arguments
 * Use the following functions in your functions that process commands to
 * retrieve arguments from the command interpreter.
 * These functions pull out unsigned integers, signed integers, and strings,
 * and hex strings.  Index 0 is the first command argument. 
 *@{
 */

/** Returns the number of arguments for the current command. */
uint8_t emberCommandArgumentCount(void);

/** Retrieves unsigned integer arguments. */
uint32_t emberUnsignedCommandArgument(uint8_t argNum);

/** Retrieves signed integer arguments. */
int16_t emberSignedCommandArgument(uint8_t argNum);

/** Retrieve quoted string or hex string arguments.
 * Hex strings have already been converted into binary.  
 * To retrieve the name of the command itself, use an argNum of -1.
 * For example, to retrieve the first character of the command, do:
 * uint8_t firstChar = emberStringCommandArgument(-1, NULL)[0].
 * If the command is nested, an index of -2, -3, etc will work to retrieve
 * the higher level command names.
 */
uint8_t *emberStringCommandArgument(int8_t argNum, uint8_t *length);

/** Copies the string argument to the given destination up to maxLength.
 * If the argument length is nonzero but less than maxLength
 * and leftPad is TRUE, leading zeroes are prepended to bring the
 * total length of the target up to maxLength.  If the argument 
 * is longer than the maxLength, it is truncated to maxLength.  
 * Returns the minimum of the argument length and maxLength.
 *
 * This function is commonly used for reading in hex strings
 * such as EUI64 or key data and left padding them with zeroes.
 * See ::emberCopyKeyArgument and ::emberCopyEui64Argument for 
 * convenience macros for this purpose.
 */
uint8_t emberCopyStringArgument(int8_t argNum,
                              uint8_t *destination, 
                              uint8_t maxLength,
                              _Bool leftPad);

/** A convenience macro for copying security key arguments to an 
 * EmberKeyData pointer.
 */

/** A convenience macro for copying eui64 arguments to an EmberEUI64. */

/** @} // END name group
 */

/** The application may implement this handler.  To override
 * the default handler, define EMBER_APPLICATION_HAS_COMMAND_ACTION_HANDLER
 * in the CONFIGURATION_HEADER.
 */
void emberCommandActionHandler(const CommandAction action);
/** The application may implement this handler.  To override
 * the default handler, define EMBER_APPLICATION_HAS_COMMAND_ERROR_HANDLER
 * in the CONFIGURATION_HEADER.  Defining this will also remove the
 * help functions ::emberPrintCommandUsage(), ::emberPrintCommandUsageNotes(),
 * and ::emberPrintCommandTable().
 */
void emberCommandErrorHandler(EmberCommandStatus status);
void emberPrintCommandUsage(EmberCommandEntry *entry);
void emberPrintCommandUsageNotes(void);
void emberPrintCommandTable(void);

/** @brief Initialize the command interpreter.
 */
void emberCommandReaderInit(void);

/** @brief Process the given string as a command.
 */
_Bool emberProcessCommandString(uint8_t *input, uint8_t size);

/** @brief Process input coming in on the given serial port.
 * @return TRUE if an end of line character was read.
 * If the application uses a command line prompt,
 * this indicates it is time to print the prompt.
 * @code
 * void emberProcessCommandInput();
 * @endcode
 */

/** @brief Turn echo of command line on.
 */
  
/** @brief Turn echo of command line off.
 */

/** @brief Returns true if echo is on, false otherwise. 
 */  
/** @} // END addtogroup 
*/

// Copyright 2014 Silicon Laboratories, Inc.

/**
 * @addtogroup debug_print
 *
 * See debug-print.h for source code.
 * @{
 */

/** @brief Indicates if a printing area is enabled. */
_Bool emberAfPrintEnabled(uint16_t area);

/** @brief Enables a printing area. */
void emberAfPrintOn(uint16_t userArea);

/** @brief Disables a printing area. */
void emberAfPrintOff(uint16_t userArea);

/** @brief Enables all printing areas. */
void emberAfPrintAllOn(void);

/** @brief Disables all printing areas. */
void emberAfPrintAllOff(void);

/** @brief Prints the status of the printing areas. */
void emberAfPrintStatus(void);

/** @brief Prints a formatted message. */
void emberAfPrint(uint16_t area, const char * formatString, ...);

/** @brief Prints a formatted message followed by a newline. */
void emberAfPrintln(uint16_t area, const char * formatString, ...);

/** @brief Prints a buffer as a series of bytes in hexidecimal format. */
void emberAfPrintBuffer(uint16_t area,
                        const uint8_t *buffer,
                        uint16_t bufferLen,
                        _Bool withSpace);

/** @brief Print an EUI64 (IEEE address) in big-endian format. */
void emberAfPrintBigEndianEui64(const EmberEUI64 eui64);

/** @brief Print an EUI64 (IEEE address) in little-endian format. */
void emberAfPrintLittleEndianEui64(const EmberEUI64 eui64);

/** @brief Prints a 16-byte key. */
void emberAfPrintKey(const uint8_t *key);

/** @brief Waits for all data currently queued to be transmitted. */
void emberAfFlush(uint16_t area);

extern uint16_t emberAfPrintActiveArea;

/** @} END addtogroup */

/***************************************************************************//**
 * @file descriptors.h
 * @brief USB descriptor prototypes for composite device example project.
 * @version 4.0.0
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



extern const USB_DeviceDescriptor_TypeDef   USBDESC_deviceDesc;
extern const uint8_t                        USBDESC_configDesc[];
extern const void * const                   USBDESC_strings[4];
extern const uint8_t                        USBDESC_bufferingMultiplier[];


_Pragma( "pack( 1 )" )
typedef struct
{
  uint8_t  len;
  uint8_t  type;
  uint16_t name[17];
} sernum;
_Pragma( "pack()" )

extern sernum iSerialNumber;



/**
  * @file usb-common.h
  * Copyright 2015 Silicon Laboratories, Inc.                              *80*
  */



/**
 * @addtogroup usb
 *
 * See usb-common.h for source code.
 * @{
 */

void usbQueueInit(void);
_Bool usbQueueEmpty(void);
_Bool usbQueueFull(void);
_Bool usbQueueGet(uint8_t **data, int *ByteCount);
_Bool usbQueuePut(uint8_t *data, int byteCount);

_Bool usbTxString(void *data, uint32_t len);

// Returns number of characters written
uint8_t usbPrintf(const char* formatString, ...);
uint8_t usbPrintfln(const char* formatString, ...);

/** @} // END addtogroup
*/

/**
  * @file usb-cdc.h
  * Copyright 2015 Silicon Laboratories, Inc.                              *80*
  */


/**
 * @addtogroup usb
 *
 * See usb-cdc.c for source code.
 * @{
 */

/**************************************************************************//**
 * @brief
 *   Callback function for CDC output reports. I.E. Rx dta
 *   This function will be called by the driver each time an output report is
 *   received by the device.
 *
 * @param[in] data
 *               Address of bytes
 * @param[in] length
 *               Number of bytes
 *****************************************************************************/
void emberUsbCdcRxCallback(char * data, int length);

int UsbCdcDataTransmitted(USB_Status_TypeDef status,
                          uint32_t xferred,
                          uint32_t remaining);

int  UsbCdc_SetupCmd(const USB_Setup_TypeDef *setup);
void UsbCdc_StateChangeEvent(USBD_State_TypeDef oldState,
                             USBD_State_TypeDef newState);

/** @} // END addtogroup
*/

void emberUsbCdcRxCallback(char * data, int length);

static char usbRxLine[200];
static int usbRxLineStart;
static int usbRxLineLen;
static int usbRxCount;

void emUsbCdcCliInit(void)
{
  memset((void *)usbRxLine, 0, sizeof(usbRxLine));
  usbRxLineStart = 0;
  usbRxLineLen = 0;
  usbRxCount = 0;
}

void emberUsbCdcRxCallback(char * data, int length)
{
  int cur = usbRxLineStart + usbRxLineLen;
  int inCur = 0;
  usbRxCount += length;
  while ( length > 0 )
  {
    char cc = data[inCur++];
    if ( cur + 1 >= 200 )
    {
      usbRxLineStart = 0;
      usbRxLineLen = 0;
      cur = 0;
    }
    usbRxLine[cur++] = cc;
    length--;
    usbRxLineLen++;
    if ( (cc == '\n') || (cc == '\r') )
    {
      usbRxLineStart = cur;
      usbRxLineLen = 0;
    }
  }
}

void emberAfPluginUsbCdcIncomingMessage(EmberIncomingMessage *message)
{
  emberAfPrint(0x0001, "Output to USB: ");
  if ( usbTxString(message->payload, message->length) )
    emberAfPrintln(0x0001, "True");
  else
    emberAfPrintln(0x0001, "False");
}

void usbCdcDataCommand(void)
{
  uint8_t length;
  uint8_t *contents = emberStringCommandArgument(0, &length);

  emberAfPrint(0x0001, "usb: Data {");
  emberAfPrintBuffer(0x0001, (contents), (length), (1));
  emberAfPrint(0x0001, "}: ");

  if ( usbTxString(contents, length) )
    emberAfPrintln(0x0001, "True");
  else
    emberAfPrintln(0x0001, "False");
}

void usbCdcPeekCommand(void)
{
  int idx = emberUnsignedCommandArgument(0);
  int len = emberUnsignedCommandArgument(1);

  if ( idx < 0 )
    idx = 0;
  if ( idx >= 200 )
    idx = 200 - 1;
  if ( len < 1 )
    len = 1;
  if ( idx + len >= 200 )
    len = 200 - 1 - idx;
  emberAfPrint(0x0001, "usb: rxData[%d],%d { ", idx, len);
  emberAfPrintBuffer(0x0001, ((unsigned char const *)&usbRxLine[idx]), (len), (1));
  emberAfPrintln(0x0001, "}");
}

void usbCdcInfoCommand(void)
{
  static char curLine[200 + 1];

  emberAfPrintln(0x0001, "      USB state: %p", USBD_GetUsbStateName(USBD_GetUsbState()));
  emberAfPrintln(0x0001, " usbRxLineStart: %d", (uint16_t)usbRxLineStart);
  emberAfPrintln(0x0001, "   usbRxLineLen: %d", (uint16_t)usbRxLineLen);
  emberAfPrintln(0x0001, "     usbRxCount: %d", (uint16_t)usbRxCount);
  /* Display data as a string. */
  memcpy((void *)curLine, (void *)&usbRxLine[usbRxLineStart], usbRxLineLen);
  curLine[usbRxLineLen] = 0;
  emberAfPrintln(0x0001, "        usbData: %s", curLine);
}