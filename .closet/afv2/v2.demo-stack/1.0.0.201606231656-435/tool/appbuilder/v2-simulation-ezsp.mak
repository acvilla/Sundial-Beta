# This Makefile defines how to build a simulated host application connected to a
# simulated Ember NCP EZSP SPI device.  

# Remove all built-in rules.
# All we need is contained within this file.
.SUFFIXES:

# Variables
ifdef E_CC
  CC := $(E_CC)
else
  CC := gcc
endif

# LD is set to CC so that we can properly pull in the necessary object
# files that contain the code that runs prior to main() and is a standard part of
# a GNU C executable.
LD := $(CC)
SHELL := /bin/sh

# matchStackBase.mak finds the right base and sets GLOBAL_BASE_DIR.
include matchStackBase.mak
ifeq ($(origin GLOBAL_BASE_DIR), undefined)
  $(error ERROR: GLOBAL_BASE_DIR is not defined, I can not build, sorry.)
endif

APP_BUILDER_OUTPUT_DIRECTORY=app/builder/_replace_projectName_
APP_CALLBACK_FILE_DIRECTORY=$(APP_BUILDER_OUTPUT_DIRECTORY)
APP_BUILDER_CONFIG_HEADER=$(APP_BUILDER_OUTPUT_DIRECTORY)/_replace_projectName_.h
APP_BUILDER_STORAGE_FILE=$(APP_BUILDER_OUTPUT_DIRECTORY)/_replace_projectName__endpoint_config.h

# Global defines allows the user to add #defines across all files
# All files will be compiled this way and the output directory
# will reflect these additional parameters as well.
# They can be specified on the command-line as follows:
#   make -f Foo.mak GLOBAL_DEFINES=EMBER_TEST
#   make -f Foo.mak GLOBAL_DEFINES="EMBER_TEST SOME_OTHER_DEFINE"
ifdef GLOBAL_DEFINES
  OUTPUT_DIR_GLOBAL_DEFINES_PATH=-$(shell echo $(GLOBAL_DEFINES) | sed -e 's/ /\-/g')
  COMPILER_GLOBAL_DEFINES=-D$(shell echo $(GLOBAL_DEFINES) | sed -e 's/ / \-D/g')
endif

INCLUDES= \
  -I. \
  -I$(APP_BUILDER_OUTPUT_DIRECTORY) \
  -I./app/framework/cli \
  -I./app/framework/include \
_replace_includePathsMak_ \
  -I./app/framework/security \
  -I./app/framework/util \
  -I./app/util \
  -I./app/util/common \
  -I./app/util/serial \
  -I./app/util/zigbee-framework \
  -I$(GLOBAL_BASE_DIR_HAL) \
  -I$(GLOBAL_BASE_DIR_HAL)/hal \
  -I$(GLOBAL_BASE_DIR_HAL)/hal/micro/generic \
  -I$(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/host/generic \
  -I$(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation \
  -I./stack \
  -I./tool/simulator/child

DEFINES= \
  $(COMPILER_GLOBAL_DEFINES) \
  -DUNIX \
  -DPHY_NULL \
  -DCONFIGURATION_HEADER=\"app/framework/util/config.h\" \
  -DEZSP_HOST \
  -DEMBER_TEST \
  -DZA_GENERATED_HEADER=\"$(APP_BUILDER_CONFIG_HEADER)\" \
  -DATTRIBUTE_STORAGE_CONFIGURATION=\"$(APP_BUILDER_STORAGE_FILE)\" \
  -DPLATFORM_HEADER=\"$(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/compiler/gcc.h\" \
  -DBOARD_HEADER=\"$(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/board/simulation.h\" \
  $--dashDMacros:"\"--$


# Clang warns about many more things than GCC.  The most warnings, by far, are
# about potential cast alignment problems.  To reduce the flood of warnings a
# little, -Wcast-align and -Wno-missing-braces is not used with Clang.
CLANG = $(shell $(CC) 2>&1 | grep -iqs clang ; echo $$?)
ifeq "$(CLANG)" "0"
  WNO_CLANG_WARNINGS= -Wno-cast-align -Wno-missing-braces
else
  WNO_CLANG_WARNINGS=
endif

SIMULATION_FILES= \
  tool/simulator/child/adc.c    \
  tool/simulator/child/child-main.c  \
  tool/simulator/child/spawn.c  \
  tool/simulator/child/timer.c  \
  tool/simulator/child/uart.c

HOST_SIMULATION_FILES= \
  tool/simulator/child/ezsp-host-stubs.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/ezsp-host-sim.c

SPI_HOST_FILES= \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/spi-protocol-ncp-sim.c

APPLICATION_FILES= \
  $(APP_BUILDER_OUTPUT_DIRECTORY)/call-command-handler.c \
  $(APP_BUILDER_OUTPUT_DIRECTORY)/callback-stub.c \
  $(APP_BUILDER_OUTPUT_DIRECTORY)/cli.c \
  $(APP_BUILDER_OUTPUT_DIRECTORY)/stack-handler-stub.c \
  $(APP_CALLBACK_FILE_DIRECTORY)/_replace_projectName__callbacks.c \
  app/framework/cli/core-cli.c \
  app/framework/cli/network-cli.c \
  app/framework/cli/option-cli.c \
  app/framework/cli/plugin-cli.c \
  app/framework/cli/security-cli.c \
  app/framework/cli/zcl-cli.c \
  app/framework/cli/zdo-cli.c \
  app/framework/security/af-node.c \
  app/framework/security/af-security-common.c \
  app/framework/security/af-trust-center.c \
  app/framework/security/crypto-state.c \
  app/framework/util/af-event.c \
  app/framework/util/af-main-common.c \
  app/framework/util/af-main-host.c \
  app/framework/util/attribute-size.c \
  app/framework/util/attribute-storage.c \
  app/framework/util/attribute-table.c \
  app/framework/util/client-api.c \
  app/framework/util/message.c \
  app/framework/util/multi-network.c \
  app/framework/util/print.c \
  app/framework/util/print-formatter.c \
  app/framework/util/process-cluster-message.c \
  app/framework/util/process-global-message.c \
  app/framework/util/service-discovery-common.c \
  app/framework/util/service-discovery-host.c \
  app/framework/util/time-util.c \
  app/framework/util/util.c \
  app/util/common/library.c \
  app/util/serial/command-interpreter2.c \
  app/util/serial/serial.c \
  app/util/security/security-address-cache.c \
  app/util/zigbee-framework/zigbee-device-common.c \
  app/util/zigbee-framework/zigbee-device-host.c \
  stack/framework/event-control.c \
  $(SIMULATION_FILES) \
  $(HOST_SIMULATION_FILES) \
  $(SPI_HOST_FILES) \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/buzzer-stub.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/crc.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/led-stub.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/mem-util.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/symbol-timer-sim.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/generic/system-timer-sim.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/button.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/micro.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/fake-eeprom.c \
  $(GLOBAL_BASE_DIR_HAL)/hal/micro/unix/simulation/random-sim.c \
_replace_includeFiles__replace_pluginFiles__replace_pluginOptionFiles_

OUTPUT_DIR= build/_replace_projectName_
# A subtetly exists here.  We use the := variable syntax so we don't do recursive variable
# substitution.  The assumption being that both of these variables don't contain additional
# variables that must be resolved.  I tried using += without any success, and
# so := was the best alternative.
OUTPUT_DIR := $(OUTPUT_DIR)$(OUTPUT_DIR_GLOBAL_DEFINES_PATH)

# Build a list of object files from the source file list, but all objects
# live in the $(OUTPUT_DIR) above.  The list of object files
# created assumes that the file part of the filepath is unique
# (i.e. the bar.c of foo/bar.c is unique across all sub-directories included).
APPLICATION_OBJECTS= $(addprefix $(OUTPUT_DIR)/, $(notdir $(APPLICATION_FILES:.c=.o)))

VPATH = $(dir $(APPLICATION_FILES))

APP_FILE= $(OUTPUT_DIR)/_replace_projectName_

CFLAGS= -ggdb -O0 -Wall $(WNO_CLANG_WARNINGS)
CPPFLAGS= $(DEFINES) $(INCLUDES) -MF $(OUTPUT_DIR)/$(@F:.o=.d) -MMD -MP

# Note:  Order matters.  This will insure linking will match up all the references since
# we only perform a single link pass.
LIBRARIES=

LINK_FLAGS=

# Rules

all: $(APP_FILE)

ifneq ($(MAKECMDGOALS),clean)
-include $(APPLICATION_OBJECTS:.o=.d)
endif

$(APP_FILE): $(APPLICATION_OBJECTS) $(LIBRARIES) | $(OUTPUT_DIR)
	$(LD) $^ $(LINK_FLAGS) -o $(APP_FILE)
	@echo -e '\n$@ build success'

$(OUTPUT_DIR)/%.o: %.c | $(OUTPUT_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -c -o $@ $<

$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)

clean:
	rm -rf $(OUTPUT_DIR)

include stack-libs.mak
