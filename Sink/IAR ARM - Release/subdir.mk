################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../connect-bookkeeping.c \
../connect-callback-stubs.c \
../connect-callbacks.c \
../connect-cli.c \
../connect-events.c 

OBJS += \
./connect-bookkeeping.o \
./connect-callback-stubs.o \
./connect-callbacks.o \
./connect-cli.o \
./connect-events.o 

C_DEPS += \
./connect-bookkeeping.d \
./connect-callback-stubs.d \
./connect-callbacks.d \
./connect-cli.d \
./connect-events.d 


# Each subdirectory must supply rules for building sources it contributes
connect-bookkeeping.o: ../connect-bookkeeping.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_wrap_diagnostics -I"C:\Users\Alex\SimplicityStudio\v3_workspace\Sink\main_inc" -e --cpu Cortex-M4 --fpu VFPv4_sp --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Om --no_unroll --no_inline --no_tbaa --no_scheduling --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '

connect-callback-stubs.o: ../connect-callback-stubs.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_wrap_diagnostics -I"C:\Users\Alex\SimplicityStudio\v3_workspace\Sink\main_inc" -e --cpu Cortex-M4 --fpu VFPv4_sp --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Om --no_unroll --no_inline --no_tbaa --no_scheduling --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '

connect-callbacks.o: ../connect-callbacks.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_wrap_diagnostics -I"C:\Users\Alex\SimplicityStudio\v3_workspace\Sink\main_inc" -e --cpu Cortex-M4 --fpu VFPv4_sp --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Om --no_unroll --no_inline --no_tbaa --no_scheduling --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '

connect-cli.o: ../connect-cli.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_wrap_diagnostics -I"C:\Users\Alex\SimplicityStudio\v3_workspace\Sink\main_inc" -e --cpu Cortex-M4 --fpu VFPv4_sp --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Om --no_unroll --no_inline --no_tbaa --no_scheduling --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '

connect-events.o: ../connect-events.c
	@echo 'Building file: $<'
	@echo 'Invoking: IAR C/C++ Compiler for ARM'
	iccarm "$<" -o "$@" --no_wrap_diagnostics -I"C:\Users\Alex\SimplicityStudio\v3_workspace\Sink\main_inc" -e --cpu Cortex-M4 --fpu VFPv4_sp --dlib_config "C:\Program Files (x86)\IAR Systems\Embedded Workbench 7.5\arm\inc\c\DLib_Config_Normal.h" --endian little --cpu_mode thumb -Om --no_unroll --no_inline --no_tbaa --no_scheduling --dependencies=m "$(basename $(notdir $<)).d"
	@echo 'Finished building: $<'
	@echo ' '


