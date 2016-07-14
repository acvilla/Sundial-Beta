#!/usr/bin/env python
#
# This python script is used for converting a production test
# S37 file into a hex file suitable for the tester.  It also parses the
# corresponding map file for printing out the shared memory addresses.
#
# * Copyright 2009 by Ember Corporation.  All rights reserved.              *80*
################################################################################

import sys
import re
import os

def processMemoryAddresses(mapFile, outFile):
  mapFile = open(mapFile).read()

  match = re.search("ENTRYPOINT\s+ro code\s+(?P<address>\S+)", mapFile)
  address = long(match.group('address'), 16)
  outFile.write("#ENTRYPOINT=0x%08X\n"%(address))

  match = re.search("CSTACK\s+0x(?P<address>\S+)\s+0x(?P<size8>\S+)", mapFile)
  address = long(match.group('address'), 16)
  size8 = long(match.group('size8'), 16)
  address += size8
  outFile.write("#CSTACK=0x%08X\n"%(address))

  match = re.search("SHAREDRAM\s+\S+\s+0x(?P<address>\S+)", mapFile)
  address = long(match.group('address'), 16)
  outFile.write("#SHAREDRAM=0x%08X\n"%(address))

def processS37File(file, outFile):
  #parse the S37 file into address-8bit pairing
  address8bit = {}
  for line in open(file):
    if(line[0:2] == 'S3'):
      recordLength = int(line[2:4],16)
      dataLength = recordLength-5
      address = long(line[4:12],16)
      
      for i in xrange(dataLength):
        data8 = int(line[(12+(i*2))+0:(12+(i*2))+2],16)
        address8bit[address+i] = data8
  
  return address8bit

#-------------------------------------------------------------------------------
if __name__ == '__main__':
  print ""
  
  try:
    #if we're running standalone, automatically load the files and generate a hex
    buildPathRoot = sys.argv[1].rsplit('/',1)[0]+'/'
  except:
    print "This program requires a path to the application to be converted."
    raise SystemExit
  
  s37File = buildPathRoot + "production-test-ram.s37"
  mapFile = buildPathRoot + "production-test-ram.map"
  if(not os.path.isfile(s37File)):
    raise Exception("S37 file " + s37File + " not found.")
  else:
    print "Parsing %s"%(s37File)
  if(not os.path.isfile(mapFile)):
    raise Exception("Map file " + mapFile + " not found.")
  else:
    print "Parsing %s"%(mapFile)
  
  outputFileName = "production-test.hex"
  outFile = open(outputFileName, 'w')
  outFile.write("#%s\n"%(buildPathRoot.rsplit('/',2)[1]))
  processMemoryAddresses(mapFile, outFile)
  address8bit = processS37File(s37File, outFile)
  
  #Put the keys into an array and sort them for min and max address values
  addresses = address8bit.keys()
  addresses.sort()
  minAddress = addresses[0]
  maxAddress = addresses[-1]+1
  
  #Convert the address-8bit pairing into an optimized address-32bit pairing,
  #injecting 0x00 where necessary to pad out to full 32bit values.
  for address in xrange(minAddress, maxAddress, 4):
    #If an address does not exist, the get method will return 0x00
    data32bit = ((address8bit.get(address+0,0x00)<< 0)|
                 (address8bit.get(address+1,0x00)<< 8)|
                 (address8bit.get(address+2,0x00)<<16)|
                 (address8bit.get(address+3,0x00)<<24))
    outFile.write("0x%08X:0x%08X\n"%(address, data32bit))
