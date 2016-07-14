# Makefile for $$--target--$$
# 
# THIS IS A GENERATED FILE. DO NOT EDIT.
#
# Copyright 2015 by Silicon Laboratories. All rights reserved.
#

# Set the GCC directory to a known default
ARM_GCC_DIR ?= 'C:\Program Files (x86)\GNU Tools ARM Embedded\4.9 2015q1'

# Configure the GCC tool prefix by default to use the ARM none EABI
TOOL_PREFIX ?= arm-none-eabi-

AS        = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)gcc
AR        = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)ar
CC        = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)gcc
LINK      = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)gcc
OBJDUMP   = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)objdump
OBJCOPY   = $(ARM_GCC_DIR)/bin/$(TOOL_PREFIX)objcopy

CCFLAGS = $$--ccflags--$$
ASFLAGS = $$--asflags--$$
ARFLAGS = $$--arflags--$$

FILE_LIST = $$--filelist--$$
OBJECT_FILES = $$--objfilelist--$$
TARGET = $$--target--$$
TARGET_DIR = $(dir $(TARGET))

DEPENDENCY_FILES = $(OBJECT_FILES:.o=.d)

# Configure the directories to search for C files
VPATH = $(dir $(FILE_LIST))

.PHONY: all
.DEFAULT: all
all: $(TARGET)

$(TARGET_DIR)%.o: %.s
$(TARGET_DIR)%.o: %.s79
	$(AS) $(ASFLAGS) -Wa,-a=$(@:.o=.lst) -o $@ $<

$(TARGET_DIR)%.o: %.c
	$(CC) $(CCFLAGS) -Wa,-a=$(@:.o=.lst) -D__SOURCEFILE__=\"$(notdir $(basename $<))\" -o $@ $<

$(TARGET): $(OBJECT_FILES)
	$(AR) $(ARFLAGS) $@ $(OBJECT_FILES)

.PHONY: $(notdir $(basename $(TARGET)))
$(notdir $(basename $(TARGET))): $(TARGET)

.PHONY: clean
clean:
	rm -f $(OBJECT_FILES)
	rm -f $(TARGET)

# Include dependency files if they exist
#  Do this at the end to leave 'all' as the default target
ifneq ($(MAKECMDGOALS),clean)
  -include $(DEPENDENCY_FILES)
endif
