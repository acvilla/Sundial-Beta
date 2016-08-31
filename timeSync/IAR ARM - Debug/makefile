################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include stack/stack-common/subdir.mk
-include sim-eeprom1/subdir.mk
-include serial/subdir.mk
-include poll/subdir.mk
-include phy-ezradio/subdir.mk
-include main/subdir.mk
-include idle-sleep/subdir.mk
-include hal/hal-ezr32/EZR32_WG330/subdir.mk
-include hal/hal-ezr32/subdir.mk
-include diagnostic/EZR32/subdir.mk
-include debug-print/subdir.mk
-include command-interpreter/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(S79_DEPS)),)
-include $(S79_DEPS)
endif
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(MSA_UPPER_DEPS)),)
-include $(MSA_UPPER_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(MSA_DEPS)),)
-include $(MSA_DEPS)
endif
ifneq ($(strip $(ASM_UPPER_DEPS)),)
-include $(ASM_UPPER_DEPS)
endif
ifneq ($(strip $(S79_UPPER_DEPS)),)
-include $(S79_UPPER_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 

# All Target
all: timeSync.out

# Tool invocations
timeSync.out: $(OBJS) $(USER_OBJS)
	@echo 'Building target: $@'
	@echo 'Invoking: IAR Linker for ARM'
	ilinkarm $(OBJS) $(USER_OBJS) -o "timeSync.out" --config "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base/hal/micro/cortexm3/efm32/ezr32lg330f256/iar-cfg.icf" --config_def BTL_SIZE=0K --config_def NULL_BTL=1 --no_wrap_diagnostics "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/hal-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/parent-support-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/form-and-join-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/packet-queue-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/sim-eeprom1-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/stack-common-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/stack-counters-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/aes-security-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/phy-pro2-brd4502c-library.a" "C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/libraries/xxtea-security-library.a" --entry halEntryPoint --map "C:/Users/Alex/SimplicityStudio/v3_workspace/timeSync/IAR ARM - Debug/timeSync.map" --log_file "C:/Users/Alex/SimplicityStudio/v3_workspace/timeSync/IAR ARM - Debug/timeSync.log" --log initialization,modules,sections,veneers --remarks --diag_suppress=Lp012 --redirect _Printf=_PrintfFull --redirect _Scanf=_ScanfFull  
	ielftool --ihex --verbose "timeSync.out" "timeSync.hex"  
	ielftool --ihex "timeSync.out" "timeSync.hex" 
	ielftool --bin "timeSync.out" "timeSync.bin" 
	ielftool --srec "timeSync.out" "timeSync.s37"
	@echo 'Finished building target: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) $(OBJS)$(C_DEPS)$(S79_DEPS)$(S_DEPS)$(CXX_DEPS)$(MSA_UPPER_DEPS)$(S_UPPER_DEPS)$(ASM_DEPS)$(CC_DEPS)$(MSA_DEPS)$(ASM_UPPER_DEPS)$(S79_UPPER_DEPS)$(CPP_DEPS)$(EXECUTABLES)$(C_UPPER_DEPS) timeSync.out
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
