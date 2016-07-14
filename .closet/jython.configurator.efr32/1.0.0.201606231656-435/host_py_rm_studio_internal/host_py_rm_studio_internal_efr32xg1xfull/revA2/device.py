
"""
Device
^^^^^^
This package provides a top-level device class, ``RM_Device_EFR32XG1XFULL``,
which is instantiated in either an offline mode for stand-alone simulated
register I/O or in a live session with a real part.

  .. autoclass::  RM_Device_EFR32XG1XFULL
     :members:
     :show-inheritance:
     :inherited-members:

The ARM CMSIS System View Description (SVD) XML hierarchy is reflected in
this package module composition. The ``device.py`` imports a number of
peripheral modules, which in turn import register, field, and optional enum
modules.

"""


__all__ = [ 'RM_Device_EFR32XG1XFULL' ]

from static import Base_RM_Device, RM_SVD_Info
from CM3 import *
from MSC import *
from EMU import *
from RMU import *
from CMU import *
from CRYPTO import *
from GPIO import *
from PRS import *
from LDMA import *
from FPUEH import *
from GPCRC import *
from TIMER0 import *
from TIMER1 import *
from PROTIMER import *
from USART0 import *
from USART1 import *
from LEUART0 import *
from LETIMER0 import *
from CRYOTIMER import *
from RFSENSE import *
from PCNT0 import *
from I2C0 import *
from ADC0 import *
from ACMP0 import *
from ACMP1 import *
from IDAC0 import *
from RTCC import *
from WDOG import *
from RAC import *
from FRC import *
from BUFC import *
from CRC import *
from SYNTH import *
from MODEM import *
from AGC import *
from SYSCFG import *
from SEQ import *


class RM_Device_EFR32XG1XFULL(Base_RM_Device):
    """
    The top level register map class. This class can be used in an offline
    mode for stand-alone simulated register I/O. In this case the class will
    use a dictionary initialized with reset values from the CMSIS SVD XML.

    .. code-block:: py

       # Example: Use register map package in offline mode
       import sys
       sys.path.append("path/to/this/package")

       from EFR32XG1XFULL import *

       rm = RM_Device_EFR32XG1XFULL(label='offline_rm')

    The class is used by the base application classes in the Python Debug Bench
    to control the part. This requires an RPC interface provided by the
    pyvsrpc package. If you want to use live outside the PDB, you can use the
    JLINK_AccessManager class from the pyjlinklib package.

    .. code-block:: py

        # Example: Use register map with live J-Link connection
        import sys
        sys.path.append("path/to/the/packages")

        from pyrmsvd import *
        from pyjlinklib import *
        from EFR32XG1XFULL import *

        dut_label = 'dut_1'
        accessMgr = JLINK_AccessManager(dut_label, JLINK_ARM_OPTIONS(), False)
        accessMgr.Connect()

        rmIO = RegisterMap_IO(accessMgr.ReadRegister, accessMgr.WriteRegister)
        rm = RM_Device_EFR32XG1XFULL(rmIO, dut_label)

    The ``svdInfo`` property is an instance of :class:`pyrmsvd.static.common.svdinfo.RM_SVD_Info`.

    """

    def __init__(self, rmio=None, label='offline_rm'):
        """
        Register the ``RegisterMapInterface`` instance and the logging label.

        :type  rmio: :class:`pyrmsvd.static.common.regmapio.RegisterMapInterface` or ``NoneType``
        :param rmio: The register map I/O instance, which contains the \
                     read/write functions for the registers. If ``None``, then \
                     the class will automatically create an internal ``RegisterMapInterface`` \
                     with an :class:`pyrmsvd.static.common.accessmgr.Offline_AccessManager` \
                     instance for operation in offline mode.
        :type  label: ``str``
        :param label: The register map DUT label to use in the system logger.
        """
        self.__dict__['zz_frozen'] = False
        super(RM_Device_EFR32XG1XFULL, self).__init__(rmio, label,
            'EFR32XG1XFULL',
            RM_SVD_Info('EFR32XG1XFULL_SEQ.svd', '40a59925d8f03169ddaf16855088a77a'))

        self.CM3 = RM_Peripheral_CM3(self.zz_rmio, self.zz_label)
        self.zz_pdict['CM3'] = self.CM3
        self.MSC = RM_Peripheral_MSC(self.zz_rmio, self.zz_label)
        self.zz_pdict['MSC'] = self.MSC
        self.EMU = RM_Peripheral_EMU(self.zz_rmio, self.zz_label)
        self.zz_pdict['EMU'] = self.EMU
        self.RMU = RM_Peripheral_RMU(self.zz_rmio, self.zz_label)
        self.zz_pdict['RMU'] = self.RMU
        self.CMU = RM_Peripheral_CMU(self.zz_rmio, self.zz_label)
        self.zz_pdict['CMU'] = self.CMU
        self.CRYPTO = RM_Peripheral_CRYPTO(self.zz_rmio, self.zz_label)
        self.zz_pdict['CRYPTO'] = self.CRYPTO
        self.GPIO = RM_Peripheral_GPIO(self.zz_rmio, self.zz_label)
        self.zz_pdict['GPIO'] = self.GPIO
        self.PRS = RM_Peripheral_PRS(self.zz_rmio, self.zz_label)
        self.zz_pdict['PRS'] = self.PRS
        self.LDMA = RM_Peripheral_LDMA(self.zz_rmio, self.zz_label)
        self.zz_pdict['LDMA'] = self.LDMA
        self.FPUEH = RM_Peripheral_FPUEH(self.zz_rmio, self.zz_label)
        self.zz_pdict['FPUEH'] = self.FPUEH
        self.GPCRC = RM_Peripheral_GPCRC(self.zz_rmio, self.zz_label)
        self.zz_pdict['GPCRC'] = self.GPCRC
        self.TIMER0 = RM_Peripheral_TIMER0(self.zz_rmio, self.zz_label)
        self.zz_pdict['TIMER0'] = self.TIMER0
        self.TIMER1 = RM_Peripheral_TIMER1(self.zz_rmio, self.zz_label)
        self.zz_pdict['TIMER1'] = self.TIMER1
        self.PROTIMER = RM_Peripheral_PROTIMER(self.zz_rmio, self.zz_label)
        self.zz_pdict['PROTIMER'] = self.PROTIMER
        self.USART0 = RM_Peripheral_USART0(self.zz_rmio, self.zz_label)
        self.zz_pdict['USART0'] = self.USART0
        self.USART1 = RM_Peripheral_USART1(self.zz_rmio, self.zz_label)
        self.zz_pdict['USART1'] = self.USART1
        self.LEUART0 = RM_Peripheral_LEUART0(self.zz_rmio, self.zz_label)
        self.zz_pdict['LEUART0'] = self.LEUART0
        self.LETIMER0 = RM_Peripheral_LETIMER0(self.zz_rmio, self.zz_label)
        self.zz_pdict['LETIMER0'] = self.LETIMER0
        self.CRYOTIMER = RM_Peripheral_CRYOTIMER(self.zz_rmio, self.zz_label)
        self.zz_pdict['CRYOTIMER'] = self.CRYOTIMER
        self.RFSENSE = RM_Peripheral_RFSENSE(self.zz_rmio, self.zz_label)
        self.zz_pdict['RFSENSE'] = self.RFSENSE
        self.PCNT0 = RM_Peripheral_PCNT0(self.zz_rmio, self.zz_label)
        self.zz_pdict['PCNT0'] = self.PCNT0
        self.I2C0 = RM_Peripheral_I2C0(self.zz_rmio, self.zz_label)
        self.zz_pdict['I2C0'] = self.I2C0
        self.ADC0 = RM_Peripheral_ADC0(self.zz_rmio, self.zz_label)
        self.zz_pdict['ADC0'] = self.ADC0
        self.ACMP0 = RM_Peripheral_ACMP0(self.zz_rmio, self.zz_label)
        self.zz_pdict['ACMP0'] = self.ACMP0
        self.ACMP1 = RM_Peripheral_ACMP1(self.zz_rmio, self.zz_label)
        self.zz_pdict['ACMP1'] = self.ACMP1
        self.IDAC0 = RM_Peripheral_IDAC0(self.zz_rmio, self.zz_label)
        self.zz_pdict['IDAC0'] = self.IDAC0
        self.RTCC = RM_Peripheral_RTCC(self.zz_rmio, self.zz_label)
        self.zz_pdict['RTCC'] = self.RTCC
        self.WDOG = RM_Peripheral_WDOG(self.zz_rmio, self.zz_label)
        self.zz_pdict['WDOG'] = self.WDOG
        self.RAC = RM_Peripheral_RAC(self.zz_rmio, self.zz_label)
        self.zz_pdict['RAC'] = self.RAC
        self.FRC = RM_Peripheral_FRC(self.zz_rmio, self.zz_label)
        self.zz_pdict['FRC'] = self.FRC
        self.BUFC = RM_Peripheral_BUFC(self.zz_rmio, self.zz_label)
        self.zz_pdict['BUFC'] = self.BUFC
        self.CRC = RM_Peripheral_CRC(self.zz_rmio, self.zz_label)
        self.zz_pdict['CRC'] = self.CRC
        self.SYNTH = RM_Peripheral_SYNTH(self.zz_rmio, self.zz_label)
        self.zz_pdict['SYNTH'] = self.SYNTH
        self.MODEM = RM_Peripheral_MODEM(self.zz_rmio, self.zz_label)
        self.zz_pdict['MODEM'] = self.MODEM
        self.AGC = RM_Peripheral_AGC(self.zz_rmio, self.zz_label)
        self.zz_pdict['AGC'] = self.AGC
        self.SYSCFG = RM_Peripheral_SYSCFG(self.zz_rmio, self.zz_label)
        self.zz_pdict['SYSCFG'] = self.SYSCFG
        self.SEQ = RM_Peripheral_SEQ(self.zz_rmio, self.zz_label)
        self.zz_pdict['SEQ'] = self.SEQ

        if self.offline:
            # assign the default reset values to the simulated register dictionary
            for key in self.zz_pdict:
                self.zz_pdict[key].assignRegDefault()
        # build the register address-to-name mapping
        for pkey in self.zz_pdict:
            self.zz_pdict[pkey].getAddressNameMap(self.zz_reg_addr_to_name)

        self.__dict__['zz_frozen'] = True