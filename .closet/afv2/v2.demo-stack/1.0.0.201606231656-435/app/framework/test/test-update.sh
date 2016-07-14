#!/usr/bin/sh

$ROB/find-replace.pl \
--find-pattern '*.bsh' \
--path app/framework/test \
\
--find-text "build/full-th-afv2-unix-simulation-af_spi_host/full-th-afv2" \
--replacement-text "build/FullTh-simulation-ezsp/FullTh" \
\
--find-text "build/full-th-afv2-unix-simulation/full-th-afv2" \
--replacement-text "build/FullTh-simulation/FullTh" \
\
\
--find-text "build/ha-combined-interface-afv2-unix-simulation/ha-combined-interface-afv2" \
--replacement-text "build/HaCombinedInterface-simulation/HaCombinedInterface" \
\
--find-text "build/ha-combined-interface-afv2-unix-simulation-af_spi_host/ha-combined-interface-afv2" \
--replacement-text "build/HaCombinedInterface-simulation-ezsp/HaCombinedInterface" \
\
--find-text "build/ha-door-lock-afv2-unix-simulation/ha-door-lock-afv2" \
--replacement-text "build/HaDoorLock-simulation/HaDoorLock" \
\
--find-text "build/ha-door-lock-afv2-unix-simulation-af_spi_host/ha-door-lock-afv2" \
--replacement-text "build/HaDoorLock-simulation-ezsp/HaDoorLock" \
\
--find-text "build/ha-home-gateway-afv2-unix-simulation/ha-home-gateway-afv2" \
--replacement-text "build/HaHomeGateway-simulation/HaHomeGateway" \
\
--find-text "build/ha-home-gateway-afv2-unix-simulation-af_spi_host/ha-home-gateway-afv2" \
--replacement-text "build/HaHomeGateway-simulation-ezsp/HaHomeGateway" \
\
--find-text "build/ha-light-afv2-unix-simulation/ha-light-afv2" \
--replacement-text "build/HaLight-simulation/HaLight" \
\
--find-text "build/ha-light-afv2-unix-simulation-af_spi_host/ha-light-afv2" \
--replacement-text "build/HaLight-simulation-ezsp/HaLight" \
\
--find-text "build/ha-range-extender-afv2-unix-simulation/ha-range-extender-afv2" \
--replacement-text "build/HaRangeExtender-simulation/HaRangeExtender" \
\
--find-text "build/ha-range-extender-afv2-unix-simulation-af_spi_host/ha-range-extender-afv2" \
--replacement-text "build/HaRangeExtender-simulation-ezsp/HaRangeExtender" \
\
--find-text "build/ha-switch-afv2-unix-simulation/ha-switch-afv2" \
--replacement-text "build/HaSwitch-simulation/HaSwitch" \
\
--find-text "build/ha-switch-afv2-unix-simulation-af_spi_host/ha-switch-afv2" \
--replacement-text "build/HaSwitch-simulation-ezsp/HaSwitch" \
\
--find-text "build/hc-weight-scale-afv2-unix-simulation/hc-weight-scale-afv2" \
--replacement-text "build/HcWeightScale-simulation/HcWeightScale" \
\
--find-text "build/hc-weight-scale-afv2-unix-simulation-af_spi_host/hc-weight-scale-afv2" \
--replacement-text "build/HcWeightScale-simulation-ezsp/HcWeightScale" \
\
\
--find-text "build/mn-esi-ipd-afv2-unix-simulation/mn-esi-ipd-afv2" \
--replacement-text "build/MnEsiIpd-simulation/MnEsiIpd" \
\
--find-text "build/mn-esi-ipd-afv2-unix-simulation-af_spi_host/mn-esi-ipd-afv2" \
--replacement-text "build/MnEsiIpd-simulation-ezsp/MnEsiIpd" \
\
--find-text "build/mn-esi-ipd-afv2-unix-simulation-real_ecc/mn-esi-ipd-afv2" \
--replacement-text "build/MnEsiIpd-simulation-REAL_ECC/MnEsiIpd" \
\
\
--find-text "build/rf4ce-controller-afv2-unix-simulation/rf4ce-controller-afv2" \
--replacement-text "build/Rf4ceController-simulation/Rf4ceController" \
\
--find-text "build/rf4ce-controller-afv2-unix-simulation-af_spi_host/rf4ce-controller-afv2" \
--replacement-text "build/Rf4ceController-simulation-ezsp/Rf4ceController" \
\
--find-text "build/rf4ce-target-afv2-unix-simulation/rf4ce-target-afv2" \
--replacement-text "build/Rf4ceTarget-simulation/Rf4ceTarget" \
\
--find-text "build/rf4ce-target-afv2-unix-simulation-af_spi_host/rf4ce-target-afv2" \
--replacement-text "build/Rf4ceTarget-simulation-ezsp/Rf4ceTarget" \
\
\
--find-text "build/se-esp-afv2-unix-simulation-af_spi_host/se-esp-afv2" \
--replacement-text "build/SeEsp-simulation-ezsp/SeEsp" \
\
--find-text "build/se-esp-afv2-unix-simulation/se-esp-afv2" \
--replacement-text "build/SeEsp-simulation/SeEsp" \
\
--find-text "build/se-esp-afv2-unix-simulation-af_spi_host-real_ecc/se-esp-afv2" \
--replacement-text "build/SeEsp-simulation-ezsp-REAL_ECC/SeEsp" \
\
--find-text "build/se-esp-afv2-unix-simulation-real_ecc/se-esp-afv2" \
--replacement-text "build/SeEsp-simulation-REAL_ECC/SeEsp" \
\
--find-text "build/se-full-th-afv2-unix-simulation-af_spi_host/se-full-th-afv2" \
--replacement-text "build/SeFullTh-simulation-ezsp/SeFullTh" \
\
--find-text "build/se-full-th-afv2-unix-simulation/se-full-th-afv2" \
--replacement-text "build/SeFullTh-simulation/SeFullTh" \
\
--find-text "build/se-full-th-afv2-unix-simulation-af_spi_host-ember_af_tc_swap_out_test-real_ecc/se-full-th-afv2" \
--replacement-text "build/SeFullTh-simulation-ezsp-EMBER_AF_TC_SWAP_OUT_TEST-REAL_ECC/SeFullTh" \
\
--find-text "build/se-full-th-afv2-unix-simulation-ember_af_tc_swap_out_test-real_ecc/se-full-th-afv2" \
--replacement-text "build/SeFullTh-simulation-EMBER_AF_TC_SWAP_OUT_TEST-REAL_ECC/SeFullTh" \
\
--find-text "build/se-ipd-afv2-unix-simulation-af_spi_host/se-ipd-afv2" \
--replacement-text "build/SeIpd-simulation-ezsp/SeIpd" \
\
--find-text "build/se-ipd-afv2-unix-simulation/se-ipd-afv2" \
--replacement-text "build/SeIpd-simulation/SeIpd" \
\
--find-text "build/se-ipd-afv2-unix-simulation-af_spi_host-real_ecc/se-ipd-afv2" \
--replacement-text "build/SeIpd-simulation-ezsp-REAL_ECC/SeIpd" \
\
--find-text "build/se-ipd-afv2-unix-simulation-real_ecc/se-ipd-afv2" \
--replacement-text "build/SeIpd-simulation-REAL_ECC/SeIpd" \
\
--find-text "build/se-meter-gas-afv2-unix-simulation-af_spi_host/se-meter-gas-afv2" \
--replacement-text "build/SeMeterGas-simulation-ezsp/SeMeterGas" \
\
--find-text "build/se-meter-gas-afv2-unix-simulation/se-meter-gas-afv2" \
--replacement-text "build/SeMeterGas-simulation/SeMeterGas" \
\
--find-text "build/se-meter-gas-sleepy-afv2-unix-simulation-af_spi_host/se-meter-gas-sleepy-afv2" \
--replacement-text "build/SeMeterGasSleepy-simulation-ezsp/SeMeterGasSleepy" \
\
--find-text "build/se-meter-gas-sleepy-afv2-unix-simulation/se-meter-gas-sleepy-afv2" \
--replacement-text "build/SeMeterGasSleepy-simulation/SeMeterGasSleepy" \
\
--find-text "build/se-meter-mirror-afv2-unix-simulation-af_spi_host/se-meter-mirror-afv2" \
--replacement-text "build/SeMeterMirror-simulation-ezsp/SeMeterMirror" \
\
--find-text "build/se-meter-mirror-afv2-unix-simulation/se-meter-mirror-afv2" \
--replacement-text "build/SeMeterMirror-simulation/SeMeterMirror" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-af_spi_host/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-ezsp/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-real_ecc/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-REAL_ECC/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-ember_test_ota_eeprom_soc_bootload-real_ecc/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-EMBER_TEST_OTA_EEPROM_SOC_BOOTLOAD-REAL_ECC/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-ember_test_ota_eeprom_page_erase-real_ecc/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-EMBER_TEST_OTA_EEPROM_PAGE_ERASE-REAL_ECC/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-ember_test_ota_eeprom_page_erase-ember_test_ota_eeprom_soc_bootload-real_ecc/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-EMBER_TEST_OTA_EEPROM_PAGE_ERASE-EMBER_TEST_OTA_EEPROM_SOC_BOOTLOAD-REAL_ECC/SeOtaEepromTest" \
\
--find-text "build/se-ota-eeprom-test-afv2-unix-simulation-af_spi_host-ember_test_ota_eeprom_page_erase-real_ecc/se-ota-eeprom-test-afv2" \
--replacement-text "build/SeOtaEepromTest-simulation-ezsp-EMBER_TEST_OTA_EEPROM_PAGE_ERASE-REAL_ECC/SeOtaEepromTest" \
\
--find-text "build/se-pct-afv2-unix-simulation-af_spi_host/se-pct-afv2" \
--replacement-text "build/SePct-simulation-ezsp/SePct" \
\
--find-text "build/se-pct-afv2-unix-simulation/se-pct-afv2" \
--replacement-text "build/SePct-simulation/SePct" \
\
--find-text "build/se-tunneling-afv2-unix-simulation-af_spi_host/se-tunneling-afv2" \
--replacement-text "build/SeTunneling-simulation-ezsp/SeTunneling" \
\
--find-text "build/se-tunneling-afv2-unix-simulation/se-tunneling-afv2" \
--replacement-text "build/SeTunneling-simulation/SeTunneling" \
\
--find-text "build/se-range-extender-afv2-unix-simulation/se-range-extender-afv2" \
--replacement-text "build/SeRangeExtender-simulation/SeRangeExtender" \
\
--find-text "build/se-range-extender-afv2-unix-simulation-af_spi_host/se-range-extender-afv2" \
--replacement-text "build/SeRangeExtender-simulation-ezsp/SeRangeExtender" \
\
--find-text "build/sleepy-generic-afv2-unix-simulation/sleepy-generic-afv2" \
--replacement-text "build/SleepyGeneric-simulation/SleepyGeneric" \
\
--find-text "build/sleepy-generic-afv2-unix-simulation-af_spi_host/sleepy-generic-afv2" \
--replacement-text "build/SleepyGeneric-simulation-ezsp/SleepyGeneric" \
\
\
--find-text "build/xncp-host-afv2-unix-simulation-af_spi_host/xncp-host-afv2" \
--replacement-text "build/XncpHost-simulation-ezsp/XncpHost" \
\
\
--find-text "build/zll-color-light-afv2-unix-simulation/zll-color-light-afv2" \
--replacement-text "build/ZllColorLight-simulation/ZllColorLight" \
\
--find-text "build/zll-color-light-afv2-unix-simulation-af_spi_host/zll-color-light-afv2" \
--replacement-text "build/ZllColorLight-simulation-ezsp/ZllColorLight" \
\
--find-text "build/zll-color-scene-remote-afv2-unix-simulation/zll-color-scene-remote-afv2" \
--replacement-text "build/ZllColorSceneRemote-simulation/ZllColorSceneRemote" \
\
--find-text "build/zll-color-scene-remote-afv2-unix-simulation-af_spi_host/zll-color-scene-remote-afv2" \
--replacement-text "build/ZllColorSceneRemote-simulation-ezsp/ZllColorSceneRemote" \
\
--find-text "build/zll-color-scene-remote-sleepy-afv2-unix-simulation/zll-color-scene-remote-sleepy-afv2" \
--replacement-text "build/ZllColorSceneRemoteSleepy-simulation/ZllColorSceneRemoteSleepy" \
\
--find-text "build/zll-color-scene-remote-sleepy-afv2-unix-simulation-af_spi_host/zll-color-scene-remote-sleepy-afv2" \
--replacement-text "build/ZllColorSceneRemoteSleepy-simulation-ezsp/ZllColorSceneRemoteSleepy" \
\
--find-text "build/zll-control-bridge-afv2-unix-simulation/zll-control-bridge-afv2" \
--replacement-text "build/ZllControlBridge-simulation/ZllControlBridge" \
\
--find-text "build/zll-control-bridge-afv2-unix-simulation-af_spi_host/zll-control-bridge-afv2" \
--replacement-text "build/ZllControlBridge-simulation-ezsp/ZllControlBridge" \
\
--find-text "build/zll-on-off-light-afv2-unix-simulation/zll-on-off-light-afv2" \
--replacement-text "build/ZllOnOffLight-simulation/ZllOnOffLight" \
\
--find-text "build/zll-on-off-light-afv2-unix-simulation-af_spi_host/zll-on-off-light-afv2" \
--replacement-text "build/ZllOnOffLight-simulation-ezsp/ZllOnOffLight" \
\
