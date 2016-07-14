#!/bin/bash
# Building em3xx_load depends on the flashloader-em3xx.h files existing.  These
# files are normally checked into perforce and already available.  This script
# will always attempt to create new flashloader headers, though.  If the Perl
# script below fails because the em35x-flashloader.[s37|map] are not found,
# the existing flashloader-em3xx.h files will be used.
#
# This script can take one parameter:
#   cygwin - this will cause em3xx_load to be built with cygwin dependency
#

SPEED=3000

if [[ -n "$1" && cygwin == $1 ]]
then
  echo "Compiling with cygwin"
  cgywin=""
else
  echo "Compiling without cygwin"
  cgywin="-mno-cygwin"
fi

libs="../../loader/em3xx_isa.lib"
libs="./JLinkARM.lib"
files="flash_unlock.c tester-emulate.c ../../loader/jtag-util.c"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o flash_unlock

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="pattern-emulator.c pattern-emulator-utils.c tester-emulate.c"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=$SPEED -D DEBUG -o jtagreplay

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi


if [[ -n "$1" && cygwin == $1 ]]
then
  echo "Compiling with cygwin"
  cgywin=""
else
  echo "Compiling without cygwin"
  cgywin="-mno-cygwin"
fi

files="tester.c pattern-emulator-utils.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"
libs="./JLinkARM.lib"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=$SPEED -D DEBUG -o jtagtester

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="em3xx_prodtest_flash.c em3xx_prodtest_flash_utils.c pattern-emulator-utils.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=$SPEED -D SITES=4 -o em3xx_prodtest_flash

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="em3xx_prodtest_reflash.c em3xx_prodtest_flash_utils.c pattern-emulator-utils.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=$SPEED -D SITES=4 -o em3xx_prodtest_reflash

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="em3xx_prodtest_unlock.c em3xx_prodtest_flash_utils.c pattern-emulator-utils.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=$SPEED -D DEBUG -D SITES=4 -o em3xx_prodtest_unlock

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="em3xx_prodtest_read.c em3xx_prodtest_flash_utils.c pattern-emulator-utils.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=3000 -D DEBUG -D SITES=4 -o em3xx_prodtest_read

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="blankness.c tester-emulate.c"
libs="../../loader/em3xx_isa.lib"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -D SWJCLK_SPEED=500 -o blankness

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="ramtest.c ../../loader/jtag-util.c"
libs="../../loader/em3xx_isa.lib"
#libs="./JLinkARM.lib"

echo $files

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -mno-cygwin -lws2_32 -lpsapi -D JTAG_SPEED=100 -D DEBUG -o ramtest-debug
gcc $2 -Wall $cgywin $files $libs -mno-cygwin -lws2_32 -lpsapi -D JTAG_SPEED=500 -o ramtest

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

