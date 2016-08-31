/**************************************************************************//**
 * @file main_eeprom_emulation.c
 * @brief EEPROM Emulation Demo Application
 * @author Silicon Labs
 * @version 1.10
 ******************************************************************************
 * @section License
 * <b>(C) Copyright 2014 Silicon Labs, http://www.silabs.com</b>
 *******************************************************************************
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 *
 * DISCLAIMER OF WARRANTY/LIMITATION OF REMEDIES: Silicon Labs has no
 * obligation to support this Software. Silicon Labs is providing the
 * Software "AS IS", with no express or implied warranties of any kind,
 * including, but not limited to, any implied warranties of merchantability
 * or fitness for any particular purpose or warranties against infringement
 * of any proprietary rights of a third party.
 *
 * Silicon Labs will not be liable for any consequential, incidental, or
 * special damages, or any other relief, or for any claim by any third party,
 * arising from your use of this Software.
 *
 ******************************************************************************/

#include "em_chip.h"
#include "em_device.h"
#include "em_cmu.h"
#include "em_emu.h"
#include "em_lcd.h"
#include "eeprom_emulation.h"
#include "segmentlcd.h"


void moveInterruptVectorToRam(void);

/*******************************************************************************
 ***************************   GLOBAL VARIABLES   ******************************
 ******************************************************************************/

/* Define the non-volatile variables. */
EE_Variable_TypeDef var1, var2, var3, boolVar;

uint16_t             readValue;


/*******************************************************************************
 **************************   GLOBAL FUNCTIONS   *******************************
 ******************************************************************************/

/**************************************************************************//**
 * @brief  Main function
 *   The main function demonstrates the main functionality of the supplied
 *   EEPROM Emulator example API: The abilities to read and write single
 *   variables to/from the non-volatile flash memory. It also features a
 *   for loop, writing 10k times and checking the validity of the data
 *   afterwards.
 *****************************************************************************/
int main(void)  
{

  /* Configure HFRCO Band */
  CMU_HFRCOBandSet(cmuHFRCOBand_28MHz);
  
  /* Move the interrupt vector table to RAM to safely handle interrupts
   * while performing write/erase operations on flash */
  moveInterruptVectorToRam();

  /* Enables the flash controller for writing. */
  MSC_Init();

  /* Initialize the eeprom emulator using 3 pages. */
  if ( !EE_Init(3) ) {
    
    /* If the initialization fails we have to take some measure
     * to obtain a valid set of pages. In this example we simply 
     * format the pages */
    EE_Format(3);
  }
  
  
  /* All variables should be declared prior to any writes. */
  EE_DeclareVariable(&var1);
  EE_DeclareVariable(&var2);
  EE_DeclareVariable(&var3);
  EE_DeclareVariable(&boolVar);

  /* Write to var2. */
  EE_Write(&var2, 0x2222);

  /* Write to boolVar. */  
  EE_Write(&boolVar, true);

  /* Write to var3. */
  EE_Write(&var3, 0x3333);

  /* Write to var1. */
  EE_Write(&var1, 0x7777);

  EE_Write(&var1, 0x1111);



  /* Read the value of var2. */
  EE_Read(&var2, &readValue);


  /* Mark all previously written values of var2, var3 and boolVar as garbage. */
  EE_DeleteVariable(&var2);
  EE_DeleteVariable(&var3);
  EE_DeleteVariable(&boolVar);

  
  /* Stay in this loop forever. */
  while (1) {
    EMU_EnterEM2(true);
  }
}
