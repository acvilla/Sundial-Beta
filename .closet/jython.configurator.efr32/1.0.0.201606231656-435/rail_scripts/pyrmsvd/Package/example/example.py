
import sys

sys.path[0:0] = ['.', '..']

from pyrmsvd import *


SVD_FN = 'EFM32GG990F1024.svd'

# Here we have a direct JLINK ARM connection
accessMgr = JLINK_AccessManager(JLINK_ARM_OPTIONS())
accessMgr.Connect()

# register the SVD reader/writer functions
rmIO = RegisterMap_IO(accessMgr.ReadRegister,
                      accessMgr.WriteRegister)

# create the register map object
rm = RM_Device(SVD_FN, rmIO)

def main():
    
    print("========================")
    print("  Data Review Examples")
    print("========================")
    print("\nList all the peripherals:\n")
    print(rm)
    print("\nList all the registers in DMA peripheral:\n")
    print(rm.DMA)
    print("\nList all the fields in the DMA.STATUS register:\n")
    print(rm.DMA.STATUS)
    print("\nList details for DMA.STATUS.STATE field:\n")
    print(rm.DMA.STATUS.STATE)
    print("\nList enum details for DMA.STATUS.STATE field:\n")
    print(rm.DMA.STATUS.STATE.enum)
    print("\nList value for DMA.STATUS.STATE.enum.IDLE enumeration:\n")
    print(rm.DMA.STATUS.STATE.enum.IDLE)
    print("\n\n")
    print("=====================")
    print("  Data I/O Examples")
    print("=====================")
    print("rm.DMA.STATUS.io reads {:#010x}".format(rm.DMA.STATUS.io))
    print("rm.DMA.STATUS.STATE.io reads {}".format(rm.DMA.STATUS.STATE.io))
    print("Writing rm.DMA.CONFIG.io = 0")
    rm.DMA.CONFIG.io = 0
    print("Writing rm.DMA.CONFIG.EN.io = 0")
    rm.DMA.CONFIG.EN.io = 0
    print("Writing rm.DMA.CH0_CTRL.SOURCESEL.io = rm.DMA.CH0_CTRL.SOURCESEL.enum.NONE")
    rm.DMA.CH0_CTRL.SOURCESEL.io = rm.DMA.CH0_CTRL.SOURCESEL.enum.NONE

if __name__ == '__main__':
    main()

