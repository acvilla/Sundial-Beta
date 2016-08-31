################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/main/main.c 

OBJS += \
./main/main.o 

C_DEPS += \
./main/main.d 


# Each subdirectory must supply rules for building sources it contributes
main/main.o: C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect/connect/plugins/main/main.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_path_in_file_macros --separate_cluster_for_initialized_variables --no_wrap_diagnostics -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/usb/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/stack/include" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/usb" -IC:/Users/Alex/SimplicityStudio/v3_workspace/microSD -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//connect/plugins/stack" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base/hal" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base/hal/micro/cortexm3/efm32/board" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base/phy" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/CMSIS/Include" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/common/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/dmadrv/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/gpiointerrupt/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/radio/test/src" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/rtcdrv/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/rtcdrv/test" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/config" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/sleep/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/spidrv/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/uartdrv/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emdrv/ustimer/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/emlib/inc" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/kits/common/bsp" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/kits/common/drivers" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/base/hal/micro/cortexm3/efm32" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/Device/SiliconLabs" -I"C:/SiliconLabs/SiliconLabsConnect/SiliconLabsConnect//submodules/kits/SLWSTK6200A_EZR32LG/config" -I"C:\Users\Alex\Downloads\microsd-fix\Includes" -e --use_c++_inline --cpu Cortex-M3 --fpu None --debug --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Ohz '-DEZR32WG330F256R60=1' '-DCONNECT_PHY_OPTION=0' '-DPHY_PRO2=1' '-DBOARD_HEADER="brd4502c.h"' '-DEZR32WG330F256=1' '-DCORTEXM3_EZR32WG330F256=1' '-DNULL_BTL=1' '-DCORTEXM3=1' '-DCORTEXM3_EFM32_MICRO=1' '-DENABLE_EXT_DEVICE=1' '-DPRO2_RADIO_BOOT_MODE=1' '-DDEBUG_LEVEL=0' '-DHAL_MICRO=1' '-DBOARD_EZR32=1' '-DEMBER_STACK_CONNECT=1' '-DPLATFORM_HEADER="micro/cortexm3/compiler/iar.h"' '-DEMBER_ASSERT_SERIAL_PORT=2' '-DMAP_MAC_PG0_CHANNELS=0' '-DAPPLICATION_TOKEN_HEADER="connect-token.h"' '-DCONFIGURATION_HEADER="connect-configuration.h"' --preprocess=c . --diag_suppress Pa050 --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '


