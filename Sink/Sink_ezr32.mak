
# IAR 7.xx toolchain
ifndef ARM_IAR7_DIR
$(error ARM_IAR7_DIR is not set. Please define ARM_IAR7_DIR pointing to your IAR 7.xx installation folder.)
endif

ARCH = $(JAMEXE_PREFIX) $(ARM_IAR7_DIR)/arm/bin/iarchive.exe
AS = $(JAMEXE_PREFIX) $(ARM_IAR7_DIR)/arm/bin/iasmarm.exe
CC = $(JAMEXE_PREFIX) $(ARM_IAR7_DIR)/arm/bin/iccarm.exe
ELFTOOL = $(JAMEXE_PREFIX) $(ARM_IAR7_DIR)/arm/bin/ielftool.exe
LD = $(JAMEXE_PREFIX) $(ARM_IAR7_DIR)/arm/bin/ilinkarm.exe

# Stack and submodule directories
GLOBAL_STACK_DIR = ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect
GLOBAL_SUBMODULES_DIR = ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/

# IAR creates dependency file containing Windows path
# Need to add native IAR and project paths here
# Also, need a way to clean up wrong dep files after build.
ifneq ($(OS),Windows_NT)
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Darwin)
		ARM_IAR_NATIVE_PATH ?= "/Users/mananni/.wine/drive_c/Program\ Files/IAR\ Systems/Embedded\ Workbench\ 7.0/"
		C_DRIVE_NATIVE_PATH ?= /Users/mananni/.wine/drive_c
	  Z_DRIVE_NATIVE_PATH ?= 
	endif
	CLEAN_UP_DEP_CMD = if [ $$? -ne 0 ]; then $(RM) $(@:%.o=%.d); exit 1; fi
else
	CLEAN_UP_DEP_CMD =
endif

ARCHITECTURE_DIR = ezr32
BUILD_DIR = build
OUTPUT_DIR = $(BUILD_DIR)/$(ARCHITECTURE_DIR)

GLOBAL_BASE_DIR = $(GLOBAL_SUBMODULES_DIR)/base
GLOBAL_EMLIB_DIR = $(GLOBAL_SUBMODULES_DIR)/emlib
GLOBAL_EMDRV_DIR = $(GLOBAL_SUBMODULES_DIR)/emdrv
GLOBAL_CMSIS_DIR = $(GLOBAL_SUBMODULES_DIR)/CMSIS
GLOBAL_DEVICE_DIR = $(GLOBAL_SUBMODULES_DIR)/Device
GLOBAL_KITS_DIR = $(GLOBAL_SUBMODULES_DIR)/kits

LOCAL_PLUGIN_DIR = $(GLOBAL_STACK_DIR)/connect/plugins
LOCAL_STACK_DIR  = $(GLOBAL_STACK_DIR)/connect/plugins/stack

CDEFS =   -DCONNECT_PHY_OPTION=0 \
  -DPHY_PRO2 \
  -DBOARD_HEADER=\"brd4502c.h\" \
  -DEZR32WG330F256R60 \
  -DEZR32WG330F256 \
  -DCORTEXM3_EZR32WG330F256 \
  -DNULL_BTL \
  -DCORTEXM3 \
  -DCORTEXM3_EFM32_MICRO \
  -DENABLE_EXT_DEVICE \
  -DPRO2_RADIO_BOOT_MODE=1 \
  -DDEBUG_LEVEL=0 \
  -DHAL_MICRO \
  -DBOARD_EZR32 \
  -DEMBER_STACK_CONNECT \
  -DCONFIGURATION_HEADER=\"connect-configuration.h\" \
  -DPLATFORM_HEADER=\"micro/cortexm3/compiler/iar.h\" \
  -DEMBER_ASSERT_SERIAL_PORT=2 \
  -DMAP_MAC_PG0_CHANNELS=0 \
  -DAPPLICATION_TOKEN_HEADER=\"connect-token.h\" \


ASMDEFS =   -DCONNECT_PHY_OPTION=0 \
  -DPHY_PRO2 \
  -DBOARD_HEADER=\"brd4502c.h\" \
  -DEZR32WG330F256R60 \
  -DEZR32WG330F256 \
  -DCORTEXM3_EZR32WG330F256 \
  -DNULL_BTL \
  -DCORTEXM3 \
  -DCORTEXM3_EFM32_MICRO \
  -DENABLE_EXT_DEVICE \
  -DPRO2_RADIO_BOOT_MODE=1 \
  -DDEBUG_LEVEL=0 \
  -DHAL_MICRO \
  -DBOARD_EZR32 \
  -DEMBER_STACK_CONNECT \
  -DCONFIGURATION_HEADER=\"connect-configuration.h\" \
  -DPLATFORM_HEADER=\"micro/cortexm3/compiler/iar.h\" \
  -DEMBER_ASSERT_SERIAL_PORT=2 \
  -DMAP_MAC_PG0_CHANNELS=0 \
  -DAPPLICATION_TOKEN_HEADER=\"connect-token.h\" \


CINC = -I. \
  -I$(GLOBAL_CMSIS_DIR)/Include  \
  -I$(GLOBAL_BASE_DIR) \
  -I$(GLOBAL_BASE_DIR)/hal \
  -I$(GLOBAL_BASE_DIR)/hal/micro/cortexm3/efm32/board \
  -I$(GLOBAL_BASE_DIR)/phy \
  -I$(GLOBAL_BASE_DIR)/hal/micro/cortexm3/efm32 \
  -I$(GLOBAL_EMLIB_DIR)/inc \
  -I$(GLOBAL_EMDRV_DIR)/common/inc \
  -I$(GLOBAL_EMDRV_DIR)/rtcdrv/inc \
  -I$(GLOBAL_EMDRV_DIR)/rtcdrv/test \
  -I$(GLOBAL_EMDRV_DIR)/sleep/inc \
  -I$(GLOBAL_EMDRV_DIR)/dmadrv/inc \
  -I$(GLOBAL_EMDRV_DIR)/radio/test/src \
  -I$(GLOBAL_EMDRV_DIR)/gpiointerrupt/inc \
  -I$(GLOBAL_EMDRV_DIR)/config \
  -I$(GLOBAL_EMDRV_DIR)/uartdrv/inc \
  -I$(GLOBAL_EMDRV_DIR)/ustimer/inc \
  -I$(GLOBAL_EMDRV_DIR)/spidrv/inc \
  -I$(GLOBAL_EMDRV_DIR)/rtcdrv/inc \
  -I$(GLOBAL_KITS_DIR)/common/bsp  \
  -I$(GLOBAL_KITS_DIR)/common/drivers \
  -I$(GLOBAL_KITS_DIR)/SLWSTK6200A_EZR32LG/config \
  -I$(GLOBAL_KITS_DIR)/common/bsp \
  -I$(GLOBAL_DEVICE_DIR)/SiliconLabs/ \
  -I$(LOCAL_STACK_DIR) \
  -I$(LOCAL_PLUGIN_DIR) \
  -I$(ARM_IAR7_DIR)/ARM/INC \
  -I../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/usb/inc \
  -I../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/stack/include \
  -I../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/usb \


CCFLAGS = --cpu=cortex-m3 \
          --cpu_mode=thumb \
          --diag_suppress=Pa050 \
          -e \
          --endian=little \
          --fpu=none \
          --no_path_in_file_macros \
          --separate_cluster_for_initialized_variables \
          --dlib_config=$(ARM_IAR7_DIR)/ARM/inc/c/DLib_Config_Normal.h \
          --debug \
          --dependencies=m $*.d \
          -Ohz \
          $(CDEFS) \
          $(CINC)

ASMFLAGS = --cpu cortex-M3 \
           --fpu None \
           -s+ \
           "-M<>" \
           -w+ \
           -t2 \
           -r \
           $(CINC) \
           $(ASMDEFS)

#Get architecture descriptor and make it consumable
ARCH_DESCR = EZR32~WG330~256K~SI4460-REVC2A+BRD4502C
ARCH_DIR := ezr32

ARCH_DIR := $(ARCH_DIR)$(if $(findstring LG230,$(ARCH_DESCR)),lg230)
ARCH_DIR := $(ARCH_DIR)$(if $(findstring LG330,$(ARCH_DESCR)),lg330)
ARCH_DIR := $(ARCH_DIR)$(if $(findstring WG230,$(ARCH_DESCR)),wg230)
ARCH_DIR := $(ARCH_DIR)$(if $(findstring WG330,$(ARCH_DESCR)),wg330)
ARCH_DIR := $(ARCH_DIR)$(if $(findstring HG230,$(ARCH_DESCR)),hg230)
ARCH_DIR := $(ARCH_DIR)$(if $(findstring HG330,$(ARCH_DESCR)),hg330)

ARCH_DIR := $(ARCH_DIR)f256

LDFLAGS = --entry halEntryPoint \
          --log initialization,modules,sections,veneers \
          --diag_suppress=Lp012 \
          --config $(GLOBAL_BASE_DIR)/hal/micro/cortexm3/efm32/$(ARCH_DIR)/iar-cfg.icf \
          --config_def BTL_SIZE=0K \
          --config_def NULL_BTL=1

SOURCE_FILES = \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/command-interpreter/command-interpreter.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/debug-print/debug-print.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/idle-sleep/idle-sleep.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/mailbox/mailbox-client/mailbox-client.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/mailbox/mailbox-server/mailbox-server.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/main/main.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/poll/poll.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/serial/com.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/serial/ember-printf.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/serial/serial.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/stack/config/ember-configuration.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/assert-crash-handlers.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/button.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/buzzer.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/cstartup-common.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/diagnostic.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/ext-device.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/faults.s79 \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/isr-stubs.s79 \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/led.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/mfg-token.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/micro-common.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/micro.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/mpu.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/sleep-efm32.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/symbol-timer.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/token-def.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/cortexm3/efm32/token.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/generic/crc.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/generic/endian.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/generic/mem-util.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/generic/random.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/hal/micro/generic/sim-eeprom.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/base/phy/pro2class/phy-config-connect.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/Device/SiliconLabs/EZR32WG/Source/system_ezr32wg.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/dmadrv/src/dmadrv.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/gpiointerrupt/src/gpiointerrupt.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/rtcdrv/src/rtcdriver.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/sleep/src/sleep.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/spidrv/src/spidrv.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/uartdrv/src/uartdrv.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emdrv/ustimer/src/ustimer.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_acmp.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_adc.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_aes.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_assert.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_burtc.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_cmu.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_dac.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_dbg.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_dma.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_ebi.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_emu.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_gpio.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_i2c.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_idac.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_int.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_lesense.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_letimer.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_leuart.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_mpu.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_msc.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_opamp.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_pcnt.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_prs.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_rmu.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_rtc.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_system.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_timer.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_usart.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_vcmp.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/emlib/src/em_wdog.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/kits/common/bsp/bsp_stk_leds.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/kits/common/drivers/dmactrl.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/kits/common/drivers/i2cspm.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/kits/common/drivers/si7013.c \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/submodules/kits/common/drivers/udelay.c \
  connect-bookkeeping.c \
  connect-callback-stubs.c \
  connect-callbacks.c \
  connect-cli.c \
  connect-events.c \


LIB_FILES = \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/aes-security-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/form-and-join-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/hal-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/packet-queue-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/parent-support-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/phy-pro2-brd4502c-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/sim-eeprom1-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/stack-common-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/stack-counters-library.a \
  ../../../../../SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/libraries/xxtea-security-library.a \


DEP_FILES = $(addprefix $(OUTPUT_DIR)/,$(subst ../,,$(CSOURCES:.c=.d)))

TARGET = Sink

CSOURCES = $(filter %.c, $(SOURCE_FILES))
ASMSOURCES = $(filter %.s79, $(SOURCE_FILES))
ASMSOURCES2 = $(filter %.s, $(SOURCE_FILES))

COBJS = $(addprefix $(OUTPUT_DIR)/,$(subst ../,,$(CSOURCES:.c=.o)))
ASMOBJS = $(addprefix $(OUTPUT_DIR)/,$(subst ../,,$(ASMSOURCES:.s79=.o)))
ASMOBJS2 = $(addprefix $(OUTPUT_DIR)/,$(subst ../,,$(ASMSOURCES2:.s=.o)))

OUTPUT_DIRS = $(sort $(dir $(COBJS)) $(dir $(ASMOBJS)) $(dir $(ASMOBJS2)))

.PHONY: all clean PROLOGUE

all: PROLOGUE $(OUTPUT_DIRS) $(COBJS) $(ASMOBJS) $(ASMOBJS2) $(LIB_FILES)
	@echo 'Linking...'
	@$(LD) $(LIB_FILES) $(COBJS) $(ASMOBJS) $(ASMOBJS2) -o $(OUTPUT_DIR)/$(TARGET).out $(LDFLAGS) --map $(OUTPUT_DIR)/$(TARGET).map --log_file $(OUTPUT_DIR)/$(TARGET).log
	@$(ELFTOOL) $(OUTPUT_DIR)/$(TARGET).out --bin $(OUTPUT_DIR)/$(TARGET).bin
	@$(ELFTOOL) $(OUTPUT_DIR)/$(TARGET).out --ihex $(OUTPUT_DIR)/$(TARGET).hex
	@echo 'Done.'

PROLOGUE:
#	@echo $(COBJS)
#	@echo $(ASMOBJS)
#	@echo $(ASMOBJS2)

$(OUTPUT_DIRS):
	@mkdir -p $@

$(COBJS): %.o:
	@echo 'Building $(notdir $(@:%.o=%.c))...'
	@$(CC) $(CCFLAGS) -o $@ $(filter %$(@:$(OUTPUT_DIR)/%.o=%.c),$(CSOURCES)) > /dev/null; \
	$(CLEAN_UP_DEP_CMD)
ifeq ($(UNAME_S),Darwin)
	@cat $(@:%.o=%.d) | sed -e 's^\\^\/^g'| sed -e 's^/ ^\\\ ^g' | \
	sed -e "s^$(ARM_IAR7_DIR)^$(ARM_IAR_NATIVE_PATH)^" | \
	sed -e 's^\ ^\\\ ^g' | sed -e 's^:\\\ ^:\ ^g' | \
	sed -e "s^C:^$(C_DRIVE_NATIVE_PATH)^" | \
	sed -e "s^Z:^$(Z_DRIVE_NATIVE_PATH)^" \
	> $(@:%.o=%.d_tmp)
	@mv $(@:%.o=%.d_tmp) $(@:%.o=%.d)
endif

$(ASMOBJS): %.o:
	@echo 'Building $(notdir $(@:%.o=%.s79))...'
	@$(AS) $(ASMFLAGS) -o $@ $(filter %$(@:$(OUTPUT_DIR)/%.o=%.s79),$(ASMSOURCES)) > /dev/null

$(ASMOBJS2): %.o:
	@echo 'Building $(notdir $(@:%.o=%.s))...'
	@$(AS) $(ASMFLAGS) -o $@ $(filter %$(@:$(OUTPUT_DIR)/%.o=%.s),$(ASMSOURCES2)) > /dev/null
  
clean:
	$(RM) -r $(OUTPUT_DIR)

# include auto-generated dependency files (explicit rules)
# only Windows and OS-X is supported for now
ifneq (clean,$(findstring clean, $(MAKECMDGOALS)))
ifeq ($(OS),Windows_NT)
-include $(DEP_FILES)
else ifeq ($(UNAME_S),Darwin)
-include $(DEP_FILES)
endif
endif
