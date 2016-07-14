from pyradioconfig.calculator_model_framework.interfaces.iphy import IPhy
from pyradioconfig.pycalcmodel import ModelInput, ModelOutput
from pyradioconfig.parts.dumbo.phys.phy_common import PHY_COMMON_FRAME_INTERNAL


class PHYS_ASK(IPhy):

    def PHY_Enocean_868MHz_org(self, model):
        phy = self._makePhy(model, model.profiles.Base, 'PHY_Enocean_868MHz')

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_outputs.MODEM_CF_CFOSR.override = 1
        phy.profile_outputs.MODEM_CF_DEC0.override = 2
        phy.profile_outputs.MODEM_CF_DEC1.override = 3
        phy.profile_outputs.MODEM_CF_DEC2.override = 3
        phy.profile_outputs.MODEM_CTRL0_CODING.override = 0
        phy.profile_outputs.MODEM_CTRL0_DIFFENCMODE.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSDOUBLE.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSLEN.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSSHIFTS.override = 0
        phy.profile_outputs.MODEM_CTRL0_FDM0DIFFDIS.override = 1
        phy.profile_outputs.MODEM_CTRL0_MAPFSK.override = 1
        phy.profile_outputs.MODEM_CTRL0_MODFORMAT.override = 6
        phy.profile_outputs.MODEM_CTRL0_SHAPING.override = 0
        phy.profile_outputs.MODEM_CTRL1_COMPMODE.override = 3
        phy.profile_outputs.MODEM_CTRL1_FREQOFFESTLIM.override = 30
        phy.profile_outputs.MODEM_CTRL1_FREQOFFESTPER.override = 0
        phy.profile_outputs.MODEM_CTRL1_PHASEDEMOD.override = 0
        phy.profile_outputs.MODEM_CTRL1_RESYNCPER.override = 4
        phy.profile_outputs.MODEM_CTRL1_SYNCBITS.override = 3
        phy.profile_outputs.MODEM_CTRL2_DATAFILTER.override = 2
        phy.profile_outputs.MODEM_CTRL2_DEVWEIGHTDIS.override = 0
        phy.profile_outputs.MODEM_CTRL2_SQITHRESH.override = 0
        phy.profile_outputs.MODEM_CTRL3_TSAMPDEL.override = 0
        phy.profile_outputs.MODEM_CTRL3_TSAMPLIM.override = 8
        phy.profile_outputs.MODEM_CTRL3_TSAMPMODE.override = 1
        phy.profile_outputs.MODEM_CTRL4_ADCSATLEVEL.override = 1
        phy.profile_outputs.MODEM_CTRL4_DEVOFFCOMP.override = 0
        phy.profile_outputs.MODEM_CTRL4_ISICOMP.override = 0
        phy.profile_outputs.MODEM_CTRL4_OFFSETPHASEMASKING.override = 0
        phy.profile_outputs.MODEM_CTRL5_BRCALAVG.override = 0
        phy.profile_outputs.MODEM_CTRL5_BRCALEN.override = 0
        phy.profile_outputs.MODEM_CTRL5_TDEDGE.override = 0
        phy.profile_outputs.MODEM_CTRL5_TREDGE.override = 0
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINE.override = 0
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINM.override = 0
        phy.profile_outputs.MODEM_MODINDEX_MODINDEXE.override = 23
        phy.profile_outputs.MODEM_MODINDEX_MODINDEXM.override = 24
        phy.profile_outputs.MODEM_PRE_BASE.override = 1
        phy.profile_outputs.MODEM_PRE_BASEBITS.override = 1
        phy.profile_outputs.MODEM_PRE_TXBASES.override = 4
        phy.profile_outputs.MODEM_RXBR_RXBRDEN.override = 5
        phy.profile_outputs.MODEM_RXBR_RXBRINT.override = 2
        phy.profile_outputs.MODEM_RXBR_RXBRNUM.override = 2
        phy.profile_outputs.MODEM_SHAPING0_COEFF0.override = 4
        phy.profile_outputs.MODEM_SHAPING0_COEFF1.override = 10
        phy.profile_outputs.MODEM_SHAPING0_COEFF2.override = 19
        phy.profile_outputs.MODEM_SHAPING0_COEFF3.override = 34
        phy.profile_outputs.MODEM_SHAPING1_COEFF4.override = 50
        phy.profile_outputs.MODEM_SHAPING1_COEFF5.override = 65
        phy.profile_outputs.MODEM_SHAPING1_COEFF6.override = 74
        phy.profile_outputs.MODEM_SHAPING1_COEFF7.override = 79
        phy.profile_outputs.MODEM_SHAPING2_COEFF8.override = 0
        phy.profile_outputs.MODEM_SYNC0_SYNC0.override = 9L
        phy.profile_outputs.MODEM_SYNC1_SYNC1.override = 0L
        phy.profile_outputs.MODEM_TIMING_ADDTIMSEQ.override = 0
        phy.profile_outputs.MODEM_TIMING_FDM0THRESH.override = 0
        phy.profile_outputs.MODEM_TIMING_OFFSUBDEN.override = 0
        phy.profile_outputs.MODEM_TIMING_OFFSUBNUM.override = 0
        phy.profile_outputs.MODEM_TIMING_TIMINGBASES.override = 1
        phy.profile_outputs.MODEM_TIMING_TIMSEQSYNC.override = 1
        phy.profile_outputs.MODEM_TIMING_TIMTHRESH.override = 0
        phy.profile_outputs.MODEM_TXBR_TXBRDEN.override = 5
        phy.profile_outputs.MODEM_TXBR_TXBRNUM.override = 192
        phy.profile_outputs.MODEM_DSSS0_DSSS0.override = 0L
        phy.profile_outputs.MODEM_AFCADJLIM_AFCADJLIM.override = 0
        phy.profile_outputs.MODEM_AFC_AFCAVGPER.override = 0
        phy.profile_outputs.MODEM_AFC_AFCDEL.override = 0
        phy.profile_outputs.MODEM_AFC_AFCRXCLR.override = 0
        phy.profile_outputs.MODEM_AFC_AFCRXMODE.override = 0
        phy.profile_outputs.MODEM_AFC_AFCSCALEE.override = 0
        phy.profile_outputs.MODEM_AFC_AFCSCALEM.override = 0
        phy.profile_outputs.RAC_IFADCCTRL_REALMODE.override = 0
        phy.profile_outputs.RAC_IFADCCTRL_VLDOCLKGEN.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_REGENCLKDELAY.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_INPUTSCALE.override = 1
        phy.profile_outputs.RAC_IFADCCTRL_VCM.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_VLDOSERIES.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_VLDOSERIESCURR.override = 2
        phy.profile_outputs.SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX.override = 245771
        phy.profile_outputs.RAC_IFPGACTRL_VLDO.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_CASCBIAS.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVCASLDO.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVCM.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVREGMIN.override = 0
        phy.profile_outputs.SYNTH_CHSP_CHSP.override = 13653
        phy.profile_outputs.SYNTH_DIVCTRL_LODIVFREQCTRL.override = 1
        phy.profile_outputs.SYNTH_FREQ_FREQ.override = 32836266L
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 251
        phy.profile_outputs.AGC_CTRL0_MODE.override = 2
        phy.profile_outputs.AGC_CTRL2_ADCRSTSTARTUP.override = 0
        phy.profile_outputs.AGC_CTRL2_HYST.override = 0
        phy.profile_outputs.AGC_CTRL2_CFLOOPDEL.override = 25
        phy.profile_outputs.AGC_GAINRANGE_MAXGAIN.override = 60
        phy.profile_outputs.AGC_GAINRANGE_MINGAIN.override = 122
        phy.profile_outputs.AGC_GAININDEX_MININDEXDEGEN.override = 0
        phy.profile_outputs.AGC_GAININDEX_MININDEXPGA.override = 0
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXATTEN.override = 12
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXSLICES.override = 6
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXDEGEN.override = 3
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXPGA.override = 12
        phy.profile_outputs.AGC_MININDEX_INDEXMINPGA.override = 21
        phy.profile_outputs.AGC_MININDEX_INDEXMINDEGEN.override = 18
        phy.profile_outputs.AGC_MININDEX_INDEXMINSLICES.override = 12
        phy.profile_outputs.AGC_MININDEX_INDEXMINATTEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNAATTEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNASLICES.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNASLICESREG.override = 0
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMTRSWGATEV.override = 3
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMVCASLDO.override = 0
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMVREGMIN.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCODETAMPLITUDE.override = 10
        phy.profile_outputs.RAC_VCOCTRL_VCOAREGCURR.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCOCREGCURR.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCODIVCURR.override = 10
        phy.profile_outputs.SYNTH_CTRL_DITHERDSMOUTPUT.override = 1
        phy.profile_outputs.SYNTH_CTRL_DITHERDAC.override = 1



    def PHY_Enocean_868MHz(self, model):
        phy = self._makePhy(model, model.profiles.Base, 'PHY_Enocean_868MHz')

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.base_frequency_hz.value = 2405000000L
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.ASK
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.bitrate.value = 125000
        phy.profile_inputs.preamble_pattern.value = 2
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 8
        phy.profile_inputs.syncword_0.value = 9L
        phy.profile_inputs.syncword_1.value = 0x0L
        phy.profile_inputs.syncword_length.value = 4
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.None
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP1
        phy.profile_inputs.baudrate_tol_ppm.value = 0
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0L
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        phy.profile_inputs.if_frequency_hz.value = 1200000
        phy.profile_inputs.bandwidth_hz.value = 631200
        phy.profile_inputs.timing_resync_period.value = 4
        phy.profile_inputs.agc_speed.value = model.vars.agc_speed.var_enum.NORMAL
        phy.profile_inputs.agc_power_target.value = -5
        phy.profile_inputs.agc_hysteresis.value = 0

        PHY_COMMON_FRAME_INTERNAL(phy, model)


    def PHY_ASK_100kbps(self, model):
        phy = self._makePhy(model, model.profiles.Base, 'ASK')

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_inputs.base_frequency_hz.value = 2405000000L
        phy.profile_inputs.modulation_type.value = model.vars.modulation_type.var_enum.ASK
        phy.profile_inputs.deviation.value = 0
        phy.profile_inputs.bitrate.value = 100000
        phy.profile_inputs.preamble_pattern.value = 1
        phy.profile_inputs.preamble_pattern_len.value = 2
        phy.profile_inputs.preamble_length.value = 128
        phy.profile_inputs.syncword_0.value = 0x6B7DL
        phy.profile_inputs.syncword_1.value = 0x0L
        phy.profile_inputs.syncword_length.value = 16
        phy.profile_inputs.shaping_filter.value = model.vars.shaping_filter.var_enum.Raised_Cosine
        phy.profile_inputs.shaping_filter_param.value = 1.0
        phy.profile_inputs.rx_xtal_error_ppm.value = 0
        phy.profile_inputs.tx_xtal_error_ppm.value = 0
        phy.profile_inputs.fsk_symbol_map.value = model.vars.fsk_symbol_map.var_enum.MAP0
        phy.profile_inputs.baudrate_tol_ppm.value = 938
        phy.profile_inputs.channel_spacing_hz.value = 1000000
        phy.profile_inputs.diff_encoding_mode.value = model.vars.diff_encoding_mode.var_enum.DISABLED
        phy.profile_inputs.dsss_chipping_code.value = 0L
        phy.profile_inputs.dsss_len.value = 0
        phy.profile_inputs.dsss_spreading_factor.value = 0
        #phy.profile_inputs.modulation_depth.value = 100.0
        #phy.profile_inputs.frequency_comp_mode.value = model.vars.frequency_comp_mode.var_enum.INTERNAL_ALWAYS_ON
        #phy.profile_inputs.if_frequency_hz.value = 1200000
        phy.profile_inputs.bandwidth_hz.value = 126240
        #phy.profile_inputs.timing_resync_period.value = 4
        #phy.profile_inputs.agc_speed.value = model.vars.agc_speed.var_enum.NORMAL
        #phy.profile_inputs.agc_power_target.value = -5
        #phy.profile_inputs.agc_hysteresis.value = 0

        PHY_COMMON_FRAME_INTERNAL(phy, model)

    def PHY_ASK_100kbps_org(self, model):
        phy = self._makePhy(model, model.profiles.Base, 'PHY_ASK_100kbps')

        phy.profile_inputs.xtal_frequency_hz.value = 38400000
        phy.profile_outputs.MODEM_CF_CFOSR.override = 3
        phy.profile_outputs.MODEM_CF_DEC0.override = 3
        phy.profile_outputs.MODEM_CF_DEC1.override = 9
        phy.profile_outputs.MODEM_CF_DEC2.override = 0
        phy.profile_outputs.MODEM_CTRL0_CODING.override = 0
        phy.profile_outputs.MODEM_CTRL0_DIFFENCMODE.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSDOUBLE.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSLEN.override = 0
        phy.profile_outputs.MODEM_CTRL0_DSSSSHIFTS.override = 0
        phy.profile_outputs.MODEM_CTRL0_MAPFSK.override = 0
        phy.profile_outputs.MODEM_CTRL0_MODFORMAT.override = 6
        phy.profile_outputs.MODEM_CTRL0_SHAPING.override = 1
        phy.profile_outputs.MODEM_CTRL1_COMPMODE.override = 2
        phy.profile_outputs.MODEM_CTRL1_FREQOFFESTLIM.override = 3
        phy.profile_outputs.MODEM_CTRL1_FREQOFFESTPER.override = 0
        phy.profile_outputs.MODEM_CTRL1_PHASEDEMOD.override = 0
        phy.profile_outputs.MODEM_CTRL1_RESYNCPER.override = 2
        phy.profile_outputs.MODEM_CTRL1_SYNCBITS.override = 15
        phy.profile_outputs.MODEM_CTRL2_DATAFILTER.override = 0
        phy.profile_outputs.MODEM_CTRL2_DEVWEIGHTDIS.override = 0
        phy.profile_outputs.MODEM_CTRL2_SQITHRESH.override = 0
        phy.profile_outputs.MODEM_CTRL3_TSAMPDEL.override = 2
        phy.profile_outputs.MODEM_CTRL3_TSAMPLIM.override = 0
        phy.profile_outputs.MODEM_CTRL3_TSAMPMODE.override = 0
        phy.profile_outputs.MODEM_CTRL4_ADCSATLEVEL.override = 1
        phy.profile_outputs.MODEM_CTRL4_DEVOFFCOMP.override = 0
        phy.profile_outputs.MODEM_CTRL4_ISICOMP.override = 0
        phy.profile_outputs.MODEM_CTRL4_OFFSETPHASEMASKING.override = 0
        phy.profile_outputs.MODEM_CTRL5_BRCALAVG.override = 0
        phy.profile_outputs.MODEM_CTRL5_BRCALEN.override = 0
        phy.profile_outputs.MODEM_CTRL5_TDEDGE.override = 0
        phy.profile_outputs.MODEM_CTRL5_TREDGE.override = 0
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINE.override = 0
        phy.profile_outputs.MODEM_MODINDEX_FREQGAINM.override = 0
        phy.profile_outputs.MODEM_MODINDEX_MODINDEXE.override = 26
        phy.profile_outputs.MODEM_MODINDEX_MODINDEXM.override = 17
        phy.profile_outputs.MODEM_PRE_BASE.override = 2
        phy.profile_outputs.MODEM_PRE_BASEBITS.override = 1
        phy.profile_outputs.MODEM_PRE_TXBASES.override = 64
        phy.profile_outputs.MODEM_RXBR_RXBRDEN.override = 5
        phy.profile_outputs.MODEM_RXBR_RXBRINT.override = 2
        phy.profile_outputs.MODEM_RXBR_RXBRNUM.override = 2
        phy.profile_outputs.MODEM_SHAPING0_COEFF0.override = 0
        phy.profile_outputs.MODEM_SHAPING0_COEFF1.override = 6
        phy.profile_outputs.MODEM_SHAPING0_COEFF2.override = 20
        phy.profile_outputs.MODEM_SHAPING0_COEFF3.override = 40
        phy.profile_outputs.MODEM_SHAPING1_COEFF4.override = 64
        phy.profile_outputs.MODEM_SHAPING1_COEFF5.override = 88
        phy.profile_outputs.MODEM_SHAPING1_COEFF6.override = 108
        phy.profile_outputs.MODEM_SHAPING1_COEFF7.override = 122
        phy.profile_outputs.MODEM_SHAPING2_COEFF8.override = 127
        phy.profile_outputs.MODEM_SYNC0_SYNC0.override = 2391391958L
        phy.profile_outputs.MODEM_SYNC1_SYNC1.override = 0L
        phy.profile_outputs.MODEM_TIMING_ADDTIMSEQ.override = 2
        phy.profile_outputs.MODEM_TIMING_FDM0THRESH.override = 0
        phy.profile_outputs.MODEM_TIMING_OFFSUBDEN.override = 0
        phy.profile_outputs.MODEM_TIMING_OFFSUBNUM.override = 0
        phy.profile_outputs.MODEM_TIMING_TIMINGBASES.override = 8
        phy.profile_outputs.MODEM_TIMING_TIMTHRESH.override = 0
        phy.profile_outputs.MODEM_TXBR_TXBRDEN.override = 1
        phy.profile_outputs.MODEM_TXBR_TXBRNUM.override = 48
        phy.profile_outputs.MODEM_DSSS0_DSSS0.override = 0L
        phy.profile_outputs.MODEM_AFCADJLIM_AFCADJLIM.override = 0
        phy.profile_outputs.MODEM_AFC_AFCAVGPER.override = 0
        phy.profile_outputs.MODEM_AFC_AFCDEL.override = 0
        phy.profile_outputs.MODEM_AFC_AFCRXCLR.override = 0
        phy.profile_outputs.MODEM_AFC_AFCRXMODE.override = 0
        phy.profile_outputs.MODEM_AFC_AFCSCALEE.override = 0
        phy.profile_outputs.MODEM_AFC_AFCSCALEM.override = 0
        phy.profile_outputs.RAC_IFADCCTRL_REALMODE.override = 0
        phy.profile_outputs.RAC_IFADCCTRL_VLDOCLKGEN.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_REGENCLKDELAY.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_INPUTSCALE.override = 1
        phy.profile_outputs.RAC_IFADCCTRL_VCM.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_VLDOSERIES.override = 2
        phy.profile_outputs.RAC_IFADCCTRL_VLDOSERIESCURR.override = 2
        phy.profile_outputs.SEQ_SYNTHLPFCTRLTX_SYNTHLPFCTRLTX.override = 245771
        phy.profile_outputs.RAC_IFPGACTRL_VLDO.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_CASCBIAS.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVCASLDO.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVCM.override = 0
        phy.profile_outputs.RAC_IFPGACTRL_TRIMVREGMIN.override = 0
        phy.profile_outputs.SYNTH_CHSP_CHSP.override = 13653
        phy.profile_outputs.SYNTH_DIVCTRL_LODIVFREQCTRL.override = 1
        phy.profile_outputs.SYNTH_FREQ_FREQ.override = 32836266L
        phy.profile_outputs.AGC_CTRL0_PWRTARGET.override = 0
        phy.profile_outputs.AGC_CTRL0_MODE.override = 1
        phy.profile_outputs.AGC_CTRL2_ADCRSTSTARTUP.override = 0
        phy.profile_outputs.AGC_CTRL2_HYST.override = 0
        phy.profile_outputs.AGC_CTRL2_CFLOOPDEL.override = 40
        phy.profile_outputs.AGC_GAINSTEPLIM_CFLOOPSTEPMAX.override = 5
        phy.profile_outputs.AGC_GAINSTEPLIM_FASTSTEPUP.override = 0
        phy.profile_outputs.AGC_GAINSTEPLIM_FASTSTEPDOWN.override = 5
        phy.profile_outputs.AGC_GAINRANGE_MAXGAIN.override = 60
        phy.profile_outputs.AGC_GAINRANGE_MINGAIN.override = 122
        phy.profile_outputs.AGC_GAININDEX_MININDEXDEGEN.override = 0
        phy.profile_outputs.AGC_GAININDEX_MININDEXPGA.override = 0
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXATTEN.override = 12
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXSLICES.override = 6
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXDEGEN.override = 3
        phy.profile_outputs.AGC_GAININDEX_NUMINDEXPGA.override = 12
        phy.profile_outputs.AGC_MININDEX_INDEXMINPGA.override = 21
        phy.profile_outputs.AGC_MININDEX_INDEXMINDEGEN.override = 18
        phy.profile_outputs.AGC_MININDEX_INDEXMINSLICES.override = 12
        phy.profile_outputs.AGC_MININDEX_INDEXMINATTEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNAATTEN.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNASLICES.override = 0
        phy.profile_outputs.AGC_MANGAIN_MANGAINLNASLICESREG.override = 0
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMTRSWGATEV.override = 3
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMVCASLDO.override = 0
        phy.profile_outputs.RAC_LNAMIXCTRL1_TRIMVREGMIN.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCODETAMPLITUDE.override = 10
        phy.profile_outputs.RAC_VCOCTRL_VCOAREGCURR.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCOCREGCURR.override = 0
        phy.profile_outputs.RAC_VCOCTRL_VCODIVCURR.override = 10
        phy.profile_outputs.SYNTH_CTRL_DITHERDSMOUTPUT.override = 1
        phy.profile_outputs.SYNTH_CTRL_DITHERDAC.override = 1


