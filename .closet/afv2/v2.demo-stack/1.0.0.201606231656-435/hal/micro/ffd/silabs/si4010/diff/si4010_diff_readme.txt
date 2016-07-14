#-------------------------------------------------------------------------------
#                           Silicon Laboratories, Inc.
#                                Copyright 2010
#                          CONFIDENTIAL & PROPRIETARY
#-------------------------------------------------------------------------------
#
#     AUTHOR:   Martin Pechanec
#     DATE:     April 30, 2010, Friday
#     FILE:     si4010_diff_readme.txt
#
#     File:     $URL: svn+ssh://svn.silabs.com/si6110/trunk/firmware/cust/si4010/common/diff/si4010_diff_readme.txt $
#     Id:       $Id: si4010_diff_readme.txt 4705 2010-05-01 01:53:05Z mapechan $
#     Author:   $Author: mapechan $
#     Version:  $Revision: 4705 $
#     Date:     $Date: 2010-04-30 18:53:05 -0700 (Fri, 30 Apr 2010) $
#
#-------------------------------------------------------------------------------

1. Important note
-----------------

The directory

  .../firmware/cust/si4010/common/diff/

is NOT FOR CUSTOMER RELEASE! The files in this directory MUST not be
revealed outside of SiLabs.

+------------------------------------------------------------------+
|  This is a CONFIDENTIAL directory for SiLabs internal use only!  |
+------------------------------------------------------------------+


2. Description
--------------

This file is a readme explaining the use of Si4010 headers
and build data files required to build firmware and applications.

The root for all the directories mentioned is

  revA/ (or rev<N>/ directory)

or in SVN the trunk:

  http://svnaus001/svn/si6110/trunk/


2.1 Customer user of the chip and ROM API (Si4010)
--------------------------------------------------

Customer is presented with a subset of the Si6110 headers and ROM API
functions. All the customer headers start with si4010 prefix, so they
are easily distinguishable from the full development si6110 headers.
The exception is that the files in the diff directory has si4010
prefix, but must not be revealed to customers.

Files are located in the customer files development directory:

  firmware/cust/si4010/common/src/


2.2 Development of differece headers for internal testing (Si4010 as Si6110)
----------------------------------------------------------------------------

To be able to use the Si4010 customer headers and the chip to behave
with full Si6110 behavior, one has to add the differential headers
and A51/C files to the build. This setup does not include
access to the si6110_sw_data.c, used for building the firmware
and possible firmware debug function replacements.

The Si4010 customer headers along with the Si4010 difference headers
describe here provide a user view of the full Si6110 functionality
of the chip. They are not intended for ROM API firmware development.

All the difference files must be added on top of the original files.
The difference file names end with '_diff' string:

  Original: <file>.<ext>  -->  Difference: <file>_diff.<ext>

Difference files are located in the customer files development directory:

  firmware/cust/si4010/common/diff/

Files:

  si4010_diff.inc         .. A51 HW reg description

  si4010_diff.h           .. C HW reg description
  si4010_api_rom_diff.h   .. C API ROM functions header

  si4010_data_diff.c      .. C data def's of globals

  si4010_rom_all_diff.a51  .. A51 ROM API map file for all
  si4010_rom_keil_diff.a51 .. A51 ROM API for Keil only

To develop software in C the user must include the following headers:

  #include "si4010.h"
  #include "si4010_diff.h"
  #include "si4010_api_rom.h"
  #include "si4010_api_rom_diff.h"

To develop assembly one must include:

  $INCLUDE (si4010.inc)
  $INCLUDE (si4010_diff.inc)

The following files must be included in the main() build:

  startup.a51
  si4010_rom_{all|keil}.a51
  si4010_rom_{all|keil}_diff.a51
  si4010_link.c
  si4010_data.c
  si4010_data_diff.c

Add the following two path to the compiler/assemble source file/include
path:

   ../../common/src/
   ../../common/diff/

Then add the headers as desribed above. This is the method to be used
on Si401x development.

#
#-------------------------------------------------------------------------------
#

