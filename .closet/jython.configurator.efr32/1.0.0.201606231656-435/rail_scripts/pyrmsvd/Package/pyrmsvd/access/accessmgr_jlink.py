
from pyjlinklib import *
from accessmgr import *

__all__ = [ 'JLINK_AccessManager' ]


class JLINK_AccessManager(object):
    def __init__(self, label, connectOpts, threaded):
        assert isinstance(label, basestring)
        assert isinstance(threaded, bool)
        self._connectOpts = connectOpts
        self._isConnected = False
        self._threaded = threaded
        self._label = label
        if self._threaded:
            self._jlink_lib = JLINKARM_LIBRARY_PROC(label)
        else:
            self._jlink_lib = JLINKARM_LIBRARY(label)

    def GetJLinkLibraryHandle(self):
        return self._jlink_lib

    def Connect(self):
        if self._isConnected:
            raise AccessMgrIoException("Invalid call sequence - Already connected!")
        if self._jlink_lib is None:
            if self._threaded:
                self._jlink_lib = JLINKARM_LIBRARY_PROC(self._label)
            else:
                self._jlink_lib = JLINKARM_LIBRARY(self._label)
        self._jlink_lib.Disconnect()
        self._jlink_lib.Connect(self._connectOpts.serialNum,
                      self._connectOpts.interfaceType,
                      self._connectOpts.rate)
        self._isConnected = True

    def Disconnect(self):
        self._isConnected = False
        result = 0
        if self._jlink_lib:
            result = self._jlink_lib.Disconnect()
            self._jlink_lib.Cleanup()
            self._jlink_lib = None
        return result

    def ReadRegister(self, address):
        """
        Read the memory mapped 32-bit register at given address.

        :type  address: `int` or `long`
        :param address: The memory mapped register address
        :rtype: `long`
        :return: The register value
        :raises: AccessMgrIoException
        """
        if not self._isConnected:
            raise AccessMgrIoException("ERROR: Disconnected - Unable to read address")
        return self._jlink_lib.ReadMem32(address)

    def WriteRegister(self, address, data):
        """
        Write the 32-bit data to the memory mapped 32-bit register at given address.

        :type  address: `int` or `long`
        :param address: The memory mapped register address
        :type  data: `int` or `long`
        :param data: The 32-bit data
        :rtype: `long`
        :return: 0 on success
        :raises: AccessMgrIoException
        """
        if not self._isConnected:
            raise AccessMgrIoException("ERROR: Disconnected - Unable to write address")
        return self._jlink_lib.WriteMem32(address, data)
