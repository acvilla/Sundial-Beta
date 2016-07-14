# This Makefile defines how to build a unix host application connected to an
# Ember NCP EZSP device.  This also works for Windows machines running
# Cygwin.

# Variables

# If using a different compiler than GCC, you can create a makefile
# that overrides the following variables.  
#   COMPILER - Compiler binary path
#   LINKER - Linker binary path
#   ARCHIVE - Optional archive tool, only necessary for building a library.
#     Must also set GENERATE_LIBRARY := 1 in your makefile.
#   COMPILER_INCLUDES - Any additional compiler includes each prefixed with -I
#   COMPILER_DEFINES - Any additional compiler defines each prefixed with -D
#   COMPILER_FLAGS - The set of compiler flags (not including dependencies)
#   LINKER_FLAGS - The set of linker flags
#   ARCHIVE_FLAGS - The set of archive tool flags.
#   DEPENDENCY_FLAGS - The set of dependency generation flags used to generate
#     dependencies at the same time compilation is executed.
#   DEPENDENCY_POST_PROCESS - An optional post processing step for massaging
#     generated depenendencies.  Only necessary when using a compiler on the 
#     non-native platform (e.g. Windows compiler on Linux)
#   PLATFORM_HEADER_FILE - The header file defining the basic int8u, int32u,
#     and other typedefs and platform elements.
#   BOARD_HEADER_FILE - The header file describing any board specific options.
#   ARCHIVE_EXTENSION - The file extension for archives if not using the standard
#     .a file extension.
#
# Then pass the makefile to this one on the command line with:
#   "make -C app/builder/$--projectName--$/Makefile INCLUDE_MAKEFILE=my-custom.mak"
#   or 
#   "cd app/builder/$--projectName--$; make"
#

ifdef INCLUDE_MAKEFILE
  include $(INCLUDE_MAKEFILE)
endif  

COMPILER ?= gcc
LINKER   ?= gcc
ARCHIVE  ?= ar

ARCHIVE_EXTENSION ?= .a

CC = $(COMPILER)
LD = $(LINKER)
SHELL = /bin/sh

ifneq ($(CURDIR),$(shell dirname $(abspath $(lastword $(MAKEFILE_LIST)))))
$(error This makefile should only be invoked under its current directory ($(shell dirname $(abspath $(lastword $(MAKEFILE_LIST))))))
endif

COMPILER_INCLUDES ?= 

INCLUDES= \
  $(COMPILER_INCLUDES) \
  -I./$--stackDirFromProjFs--$ \
  -I./$--stackDirFromProjFs--$/app/builder/$--projectName--$ \
  -I./$--stackDirFromProjFs--$/app/framework/cli \
  -I./$--stackDirFromProjFs--$/app/framework/include \
$--includePathsMak--$ \
  -I./$--stackDirFromProjFs--$/app/framework/security \
  -I./$--stackDirFromProjFs--$/app/framework/util \
  -I./$--stackDirFromProjFs--$/app/util \
  -I./$--stackDirFromProjFs--$/app/util/common \
  -I./$--stackDirFromProjFs--$/app/util/ezsp \
  -I./$--stackDirFromProjFs--$/app/util/serial \
  -I./$--stackDirFromProjFs--$/app/util/zigbee-framework \
  -I./$--halDirFromProjFs--$/.. \
  -I./$--halDirFromProjFs--$ \
  -I./$--halDirFromProjFs--$/micro/generic \
  -I./$--halDirFromProjFs--$/micro/unix/host \
  -I./$--stackDirFromProjFs--$/stack

APP_BUILDER_OUTPUT_DIRECTORY=.
APP_BUILDER_CONFIG_HEADER=$(APP_BUILDER_OUTPUT_DIRECTORY)/$--projectName--$.h
APP_BUILDER_STORAGE_FILE=$(APP_BUILDER_OUTPUT_DIRECTORY)/$--projectName--$_endpoint_config.h

PLATFORM_HEADER_FILE ?= \"$--halDirFromProjFs--$/micro/unix/compiler/gcc.h\"
BOARD_HEADER_FILE    ?= \"$--halDirFromProjFs--$/micro/unix/host/board/host.h\"

DEFINES = \
  $(COMPILER_DEFINES) \
  -DUNIX \
  -DUNIX_HOST \
  -DPHY_NULL \
  -DCONFIGURATION_HEADER=\"$--stackDirFromProjFs--$/app/framework/util/config.h\" \
  -DEZSP_HOST \
  -DGATEWAY_APP \
  -DZA_GENERATED_HEADER=\"$(APP_BUILDER_CONFIG_HEADER)\" \
  -DATTRIBUTE_STORAGE_CONFIGURATION=\"$(APP_BUILDER_STORAGE_FILE)\" \
  -DPLATFORM_HEADER=$(PLATFORM_HEADER_FILE) \
  -DBOARD_HEADER=$(BOARD_HEADER_FILE) \
  $--dashDMacros:"\"--$


COMPILER_FLAGS ?= \
  -Wall \
  -ggdb \
  -O0

APPLICATION_FILES= \
  $--stackDirFromProjFs--$/app/builder/$--projectName--$/call-command-handler.c \
  $--stackDirFromProjFs--$/app/builder/$--projectName--$/callback-stub.c \
  $--stackDirFromProjFs--$/app/builder/$--projectName--$/stack-handler-stub.c \
  $--stackDirFromProjFs--$/app/builder/$--projectName--$/cli.c \
  $--stackDirFromProjFs--$/app/builder/$--projectName--$/$--projectName--$_callbacks.c \
  $--stackDirFromProjFs--$/app/framework/cli/core-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/network-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/option-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/plugin-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/security-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/zcl-cli.c \
  $--stackDirFromProjFs--$/app/framework/cli/zdo-cli.c \
  $--stackDirFromProjFs--$/app/framework/security/af-node.c \
  $--stackDirFromProjFs--$/app/framework/security/af-security-common.c \
  $--stackDirFromProjFs--$/app/framework/security/af-trust-center.c \
  $--stackDirFromProjFs--$/app/framework/security/crypto-state.c \
  $--stackDirFromProjFs--$/app/framework/util/af-event.c \
  $--stackDirFromProjFs--$/app/framework/util/af-main-common.c \
  $--stackDirFromProjFs--$/app/framework/util/af-main-host.c \
  $--stackDirFromProjFs--$/app/framework/util/attribute-size.c \
  $--stackDirFromProjFs--$/app/framework/util/attribute-storage.c \
  $--stackDirFromProjFs--$/app/framework/util/attribute-table.c \
  $--stackDirFromProjFs--$/app/framework/util/client-api.c \
  $--stackDirFromProjFs--$/app/framework/util/message.c \
  $--stackDirFromProjFs--$/app/framework/util/multi-network.c \
  $--stackDirFromProjFs--$/app/framework/util/print.c \
  $--stackDirFromProjFs--$/app/framework/util/print-formatter.c \
  $--stackDirFromProjFs--$/app/framework/util/process-cluster-message.c \
  $--stackDirFromProjFs--$/app/framework/util/process-global-message.c \
  $--stackDirFromProjFs--$/app/framework/util/service-discovery-common.c \
  $--stackDirFromProjFs--$/app/framework/util/service-discovery-host.c \
  $--stackDirFromProjFs--$/app/framework/util/time-util.c \
  $--stackDirFromProjFs--$/app/framework/util/util.c \
  $--stackDirFromProjFs--$/app/util/common/library.c \
  $--stackDirFromProjFs--$/app/util/serial/command-interpreter2.c \
  $--stackDirFromProjFs--$/app/util/zigbee-framework/zigbee-device-common.c \
  $--stackDirFromProjFs--$/app/util/zigbee-framework/zigbee-device-host.c \
  $--stackDirFromProjFs--$/stack/framework/event-control.c \
  $--halDirFromProjFs--$/micro/generic/buzzer-stub.c \
  $--halDirFromProjFs--$/micro/generic/crc.c \
  $--halDirFromProjFs--$/micro/generic/led-stub.c \
  $--halDirFromProjFs--$/micro/generic/antenna-stub.c \
  $--halDirFromProjFs--$/micro/generic/mem-util.c \
  $--halDirFromProjFs--$/micro/generic/random.c \
  $--halDirFromProjFs--$/micro/generic/system-timer.c \
  $--halDirFromProjFs--$/micro/unix/host/micro.c \
$--includeFilesMak--$$--pluginFiles--$$--pluginOptionFiles--$

OUTPUT_DIR=$(APP_BUILDER_OUTPUT_DIRECTORY)/build
OUTPUT_DIR_CREATED= $(OUTPUT_DIR)/created
EXE_DIR=$(OUTPUT_DIR)/exe
# Build a list of object files from the source file list, but all objects
# live in the $(OUTPUT_DIR) above.  The list of object files
# created assumes that the file part of the filepath is unique
# (i.e. the bar.c of foo/bar.c is unique across all sub-directories included).
APPLICATION_OBJECTS= $(shell echo $(APPLICATION_FILES) | xargs -n1 echo | sed -e 's^.*/\(.*\)\.c^$(OUTPUT_DIR)/\1\.o^')

ifdef GENERATE_LIBRARY
TARGET_FILE= $(EXE_DIR)/$--projectName--$$(ARCHIVE_EXTENSION)
else
TARGET_FILE= $(EXE_DIR)/$--projectName--$
endif

# -MMD and -MF generates Makefile dependencies while at the same time compiling.
# -MP notes to add a dummy 'build' rule for each header file.  This 
# prevent a problem where a removed header file will generate an error because a
# dependency references it but it can't be found anymore.
DEPENDENCY_FLAGS ?= -MMD -MP -MF $(@D)/$*.d 

# Dependency post process is a way to massage generated dependencies.
# This is necessary for example when using Make under Cygwin but compiling
# using a native Windows compiler that generates native Windows paths
# that Cygwin will choke on.  Or if compiling on Linux using Wine to run a 
# Windows compiler, a similar problem can occur.  
DEPENDENCY_POST_PROCESS ?=

CPPFLAGS= $(INCLUDES) $(DEFINES) $(COMPILER_FLAGS) $(DEPENDENCY_FLAGS)
LINKER_FLAGS ?=

ifdef NO_READLINE
  CPPFLAGS += -DNO_READLINE
else
  LINKER_FLAGS +=  \
    -lreadline \
    -lncurses 
endif

ARCHIVE_FLAGS ?= rus

# Rules

all: $(TARGET_FILE)

ifneq ($(MAKECMDGOALS),clean)
-include $(APPLICATION_OBJECTS:.o=.d)
endif

ifdef GENERATE_LIBRARY
$(TARGET_FILE): $(APPLICATION_OBJECTS)
	$(ARCHIVE) $(ARCHIVE_FLAGS) $(TARGET_FILE) $^
	@echo -e '\n$@ build success'
else
$(TARGET_FILE): $(APPLICATION_OBJECTS)
	$(LD) $^ $(LINKER_FLAGS) -o $(TARGET_FILE)
	@echo -e '\n$@ build success'
endif

clean:
	rm -rf $(OUTPUT_DIR)

$(OUTPUT_DIR_CREATED):
	mkdir -p $(OUTPUT_DIR)
	mkdir -p $(EXE_DIR)
	touch $(OUTPUT_DIR_CREATED)

# To facilitate generating all output files in a single output directory, we
# must create separate .o and .d rules for all the different sub-directories
# used by the source files.
# If additional directories are added that are not already in the
# $(APPLICATION_FILES) above, new rules will have to be created below.

# Object File rules

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/builder/$--projectName--$/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/ezsp-host/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/ezsp-host/ash/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/ezsp-host/spi/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/ezsp-host/usb/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/framework/cli/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$--outputDirRulesMak--$

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/framework/security/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/framework/util/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/common/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/ezsp/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/gateway/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/serial/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/app/util/zigbee-framework/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/stack/framework/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--stackDirFromProjFs--$/stack/gp/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--halDirFromProjFs--$/micro/generic/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)

$(OUTPUT_DIR)/%.o: $--halDirFromProjFs--$/micro/unix/host/%.c $(OUTPUT_DIR_CREATED)
	$(CC) $(CPPFLAGS) -c $< -o $(OUTPUT_DIR)/$(@F)
	$(DEPENDENCY_POST_PROCESS)


# Dependency rules
# No explicit rules.  Dependencies are generated as part of the compile step.
