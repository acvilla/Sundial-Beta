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

if [[ -n "$1" && cygwin == $1 ]]
then
  echo "Compiling with cygwin"
  cgywin=""
else
  echo "Compiling without cygwin"
  cgywin="-mno-cygwin"
fi

files="demo.c tester-emulate.c unlock-utils.c ../../loader/jtag-util.c"
libs="../../loader/JLinkARM.lib"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o em3xx_prodtest

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="flashdemo.c tester-emulate.c utils.c ../../loader/jtag-util.c"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
#gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o flashdemo

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="unlock.c tester-emulate.c ../../loader/jtag-util.c"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o unlock

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi

files="xtal-test.c tester-emulate.c ../../loader/jtag-util.c"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o xtal-test

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi


files="flash_unlock.c tester-emulate.c ../../loader/jtag-util.c"

# Load extra GDB flags with second script parameter $2 (e.g. -ggdb)
gcc $2 -Wall $cgywin $files $libs -lws2_32 -lpsapi -o flash_unlock

if [ $? == 0 ]; then
  echo "Done"
else
  echo "Build Failed."
fi
