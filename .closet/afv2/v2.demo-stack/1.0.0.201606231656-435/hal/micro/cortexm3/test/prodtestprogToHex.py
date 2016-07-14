#!/usr/bin/env python
#
# This python script is used for converting a production test programming
# S37 file into a hex file suitable for the tester.  It also parses the
# corresponding map file for printing out the shared memory addresses.
#
# Author: Brooks Barrett
#
# * Copyright 2009 by Ember Corporation.  All rights reserved.              *80*
################################################################################

import sys
import re
import os


FLETCHER_TEST_VECTOR = [0x0000,0x0001,0x0002,0x0003,0x0004,
                        0x0005,0x0006,0x0007,0x0008,0x0009,
                        0x000A,0x000B,0x000C,0x000D,0x000E,
                        0x000F,0x0010,0x0011]
FLETCHER_TEST_VECTOR_RESULT = 0x03C90099

#The input data must be an array with each item in the array a 16bit number.
#If no length parameter is specified, the method will operate on the entire
#data list.  Length parameter let's the caller decided to restrict calculation..
def calculateFletcher32Checksum(data, length=None):
  if length is None:
    length = len(data)
  
  dataIndex = 0
  
  sum1 = 0xFFFF
  sum2 = 0xFFFF
  
  while(length):
    if(length > 360):
      tLength = 360
    else:
      tLength = length
    
    length -= tLength
    
    for i in xrange(tLength):
      sum1 = sum1 + data[dataIndex]
      sum2 = sum2 + sum1
      dataIndex = dataIndex + 1
    
    sum1 = (sum1 & 0xFFFF) + (sum1 >> 16)
    sum2 = (sum2 & 0xFFFF) + (sum2 >> 16)
  
  #This reduction step is for reducing the sums to 16 bits
  sum1 = (sum1 & 0xFFFF) + (sum1 >> 16)
  sum2 = (sum2 & 0xFFFF) + (sum2 >> 16)
  
  result = (sum2 << 16) | sum1
  return result


def processMemoryAddresses(file, outFile):
  file = open(file).read()
  
  match = re.search("ENTRYPOINT\s+ro code\s+(?P<address>\S+)", file)
  address = long(match.group('address'), 16)
  outFile.write("#ENTRYPOINT=0x%08X\n"%(address))
  
  match = re.search("CSTACK\s+0x(?P<address>\S+)\s+0x(?P<size8>\S+)", file)
  address = long(match.group('address'), 16)
  size8 = long(match.group('size8'), 16)
  address += size8
  outFile.write("#CSTACK=0x%08X\n"%(address))
  
  match = re.search("sharedMemoryCommand\s+(?P<address>\S+)", file)
  address = long(match.group('address'), 16)
  outFile.write("#sharedMemoryCommand=0x%08X\n"%(address))
  
  match = re.search("sharedMemoryStatus\s+(?P<address>\S+)", file)
  address = long(match.group('address'), 16)
  outFile.write("#sharedMemoryStatus=0x%08X\n"%(address))
  
  match = re.search("sharedMemoryDataIn\s+(?P<address>\S+)", file)
  address = long(match.group('address'), 16)
  outFile.write("#sharedMemoryDataIn=0x%08X\n"%(address))
  
  match = re.search("sharedMemoryDataOut\s+(?P<address>\S+)", file)
  address = long(match.group('address'), 16)
  outFile.write("#sharedMemoryDataOut=0x%08X\n"%(address))
  
  #The address at which we need to install the RAM Code checksum
  match = re.search("ramCodePresetChecksum\s+(?P<address>\S+)", file)
  ramCodePresetChecksumAddress = long(match.group('address'), 16)
  #outFile.write("#ramCodePresetChecksum=0x%08X\n"%(address))
  
  #The address at which we need to install the address of the end of RAM Code
  match = re.search("ramCodeEndAddress\s+(?P<address>\S+)", file)
  ramCodeEndAddressAddress = long(match.group('address'), 16)
  #outFile.write("#ramCodeEndAddress=0x%08X\n"%(address))
  
  return (ramCodePresetChecksumAddress, ramCodeEndAddressAddress)
  
  
def processMemorySizes(file, outFile):
  file = open(file).read()
  
  error = 0
  
  match = re.search("sharedMemoryCommand +(?P<size8>\d+)", file)
  if(long(match.group('size8'), 10) != 4):
    error += 1
  
  match = re.search("sharedMemoryStatus +(?P<size8>\d+)", file)
  if(match):
    error += 1
  
  match = re.search("sharedMemoryDataIn +(?P<size8>\d+)", file)
  if(long(match.group('size8'), 10) != 4096):
    error += 1
  
  match = re.search("sharedMemoryDataOut +(?P<size8>\d+)", file)
  if(match):
    error += 1
  
  if(error):
    print "ERROR! Due to the complexities of IAR map and list files, this"
    print "script is not designed to automatically parse for shared memory"
    print "sizes.  Therefore, it expects to find exactly the following:"
    print "  sharedMemoryCommand               4"
    print "  sharedMemoryStatus                 "
    print "  sharedMemoryDataIn             4096"
    print "  sharedMemoryDataOut                "
    print "so that it can simply write out the proper sizes.  The script"
    print "failed to find the above pattern of shared memory sizes!"
    raise SystemExit
  
  outFile.write("#sharedMemoryCommandSize16bits=0x1\n")
  outFile.write("#sharedMemoryStatusSize16bits=0x1\n")
  outFile.write("#sharedMemoryDataInSize16bits=0x3FD\n")
  outFile.write("#sharedMemoryDataOutSize16bits=0x3FD\n")
  
  
def processTimingParameters(file, outFile):
  file = open(file).read()
  
  match = re.search("ramCodeWorstCaseTimingNormalUs=\d+", file)
  outFile.write("#%s\n"%(match.group()))
  
  match = re.search("ramCodeWorstCaseTimingRmwUs=\d+", file)
  outFile.write("#%s\n"%(match.group()))
  
  
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
  
  s37File = buildPathRoot + "prodtestprog-ram-em3xx.s37"
  mapFile = buildPathRoot + "prodtestprog-ram-em3xx.map"
  lstFile = buildPathRoot + "prodtestprog.lst"
  if(not os.path.isfile(s37File)):
    raise Exception("S37 file " + s37File + " not found.")
  else:
    print "Parsing %s"%(s37File)
  if(not os.path.isfile(mapFile)):
    raise Exception("Map file " + mapFile + " not found.")
  else:
    print "Parsing %s"%(mapFile)
  if(not os.path.isfile(lstFile)):
    raise Exception("Map file " + lstFile + " not found.")
  else:
    print "Parsing %s"%(lstFile)
  
  outputFileName = "prodtestprog.hex"
  outFile = open(outputFileName, 'w')
  
  print ""
  print "REMINDER: If you changed the code, don't forget to update the timing"
  print "parameters.  Refer to the top of prodtestprog.c for more information."
  
  #implant the build string (folder name) into the file so we know where
  #the hex file came from
  outFile.write("#%s\n"%(buildPathRoot.rsplit('/',2)[1]))
  
  #Add the shared memory addresses to the top of the file
  (checksumAddr, codeEndAddr) = processMemoryAddresses(mapFile, outFile)
  
  #Add the shared memory sizes to the top of the file
  processMemorySizes(lstFile, outFile)
  
  #Add the timing parameters to the top of the file
  processTimingParameters(lstFile, outFile)
  
  address8bit = processS37File(s37File, outFile)
  
  #Put the keys into an array and sort them for min and max address values
  addresses = address8bit.keys()
  addresses.sort()
  minAddress = addresses[0]
  maxAddress = addresses[-1]+1
  
  #inject the maxAddress into the location pointed to by codeEndAddr
  address8bit[codeEndAddr+0] = (maxAddress>> 0)&0xFF
  address8bit[codeEndAddr+1] = (maxAddress>> 8)&0xFF
  address8bit[codeEndAddr+2] = (maxAddress>>16)&0xFF
  address8bit[codeEndAddr+3] = (maxAddress>>24)&0xFF
  
  #Convert the address-8bit pairing into an optimized address-16bit pairing,
  #injecting 0x00 where necessary to pad out to full 16bit values.
  data16bit = []
  for address in xrange(minAddress, maxAddress, 2):
    #If an address does not exist, the get method will return 0x00
    data16bit.append((address8bit.get(address+0,0x00)<<0)|
                     (address8bit.get(address+1,0x00)<<8))
  checksum = calculateFletcher32Checksum(data16bit)
  #inject the checksum into the location pointed to by checksumAddr
  address8bit[checksumAddr+0] = (checksum>>16)&0xFF
  address8bit[checksumAddr+1] = (checksum>>24)&0xFF
  address8bit[checksumAddr+2] = (checksum>> 0)&0xFF
  address8bit[checksumAddr+3] = (checksum>> 8)&0xFF
  
  #Convert the address-8bit pairing into an optimized address-32bit pairing,
  #injecting 0x00 where necessary to pad out to full 32bit values.
  for address in xrange(minAddress, maxAddress, 4):
    #If an address does not exist, the get method will return 0x00
    data32bit = ((address8bit.get(address+0,0x00)<< 0)|
                 (address8bit.get(address+1,0x00)<< 8)|
                 (address8bit.get(address+2,0x00)<<16)|
                 (address8bit.get(address+3,0x00)<<24))
    outFile.write("0x%08X:0x%08X\n"%(address, data32bit))
  
  
