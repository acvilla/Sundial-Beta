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
# NOTE: The em351 build is used to create the flashloader for all em35x and
#   em358x variants.
#
# To make new flashloader-em3xx.h files, before executing this script, build:
#   ./build.pl em35x-flashloader PLAT=cortexm3 COMP=iar MICRO=em351 PHY=null BOARD=dev0680 RAMEXE
################################################################################

# Run the new Makefile
make all

# For now, copy the executables to the main directory after a Windows build.
# Eventually all tools will be updated to use the new build/windows directory,
# but this should help ease that transition.
if [[ `uname -s` =~ .*CYGWIN.* ]]
then
  cp build/windows/em3xx_load.exe ./em3xx_load.exe
  cp build/windows/internal_em3xx_load.exe ./internal_em3xx_load.exe
  cp build/windows/em3xx_convert.exe ./em3xx_convert.exe
  cp build/windows/em3xx_buildimage.exe ./em3xx_buildimage.exe
fi
