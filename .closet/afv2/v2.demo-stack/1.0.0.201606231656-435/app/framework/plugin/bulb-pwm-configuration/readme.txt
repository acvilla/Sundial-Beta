Bulb Config Plugin

Plugin to control the behavior of the bulb.  By writing the top area of the CIB
Token area, you can change behavior of the bulb.  Here is the memory map:

Memory Map:
To configure the bulb, tokens can be written into the Customer Information
Block of the EM3xx chip (see hal/micro/cortexm3/token-manufacturing.h for more
details on Customer Information Block).  Token locations below are defined with
a base address and a specific offset from that base address for each token.  

Base Address:  0x08040000 // EM351/7
               0x08080000 // EM358x/9x

Token List:
CFG_MASK              0xffe  // 2 bytes
CFG_TX_POWER          0xffc  // 2 bytes
CFG_PWM_FREQ          0xffa  // 2 bytes
CFG_PWM_MIN_ON        0xff8  // 2 bytes
CFG_PWM_MAX_ON        0xff6  // 2 bytes
CFG_PWM_WHITE         0xff4  // 2 bytes
CFG_PWM_RED           0xff2  // 2 bytes
CFG_PWM_GREEN         0xff0  // 2 bytes
CFG_PWM_BLUE          0xfee  // 2 bytes
CFG_HARDWARE_VERSION  0xfec // 1 byte
       
Token Definition

CFG_MASK:
16 bit mask to define which tokens have been written.  Note:  because this is
being written into a flash area, writing a bit converts it from a 1 to a 0.
Therefore, any bit that is a 0 indicates that the token is present and will
override the default value.  

Bit 0:  CFG_TX_POWER
Bit 1:  CFG_PWM_FREQ
Bit 2:  CFG_PWM_MIN_ON
Bit 3:  CFG_PWM_MAX_ON
Bit 4:  PWM_WHITE
Bit 5:  PWM_RED
Bit 6:  PWM_GREEN
Bit 7:  PWM_BLUE
Bit 8:  Hardware Version
Bit 9-15:  reserved for future use

CFG_TX_POWER:
This token sets the TX power for the module.  The lower byte of the 16-bit word
is a two's complement signed integer denoting the TX power of our chip.  Valid
values range from 8 to -31 dBm, where an 8 dbm is defined with 0x08 and -31 dBm 
is defined with 0xE1

CFG_PWM_FREQ:
This value, in Hz, defines the frequency at which the PWMs will be driven.  The
default value is 1000, or 1 kHz.  Valid values are from 100 to 3000 Hz.

em3xx_load --patch @8080ffe=0xfd --ip <ISA3 IP> // TX token is enabled, all others disabled
em3xx_load --patch @8080ffa=0x00 --patch @8080ffb=0x02 --ip <ISA3 IP> // 0x0200 or 512 Hz
em3xx_load --patch @8080ffa=0x84 --patch @8080ffb=0x03 --ip <ISA3 IP> // 0x0384 or 900 Hz

CFG_PWM_MIN_ON_TIME
LED bulb hardware can not support PWM on times below a certain threshold.  This
value determines that minimum threshold in microseconds.  Valid range is 0 to
65536 microseconds.

em3xx_load --patch @8080ffe=0xfb --ip <ISA3 IP> // min on uS token is enabled, all others disabled
em3xx_load --patch @8080ff8=0x10 --patch @8080ff9=0x00 --ip <ISA3 IP> // 0x0010 or 16 uS

CFG_PWM_MAX_ON_TIME
LED bulb hardware can not support PWM on to off transitions above a certain
threshold.  This value determines that minimum threshold in microseconds.
Valid range is 0 to 65536 microseconds.

em3xx_load --patch @8080ffe=0xf7 --ip <ISA3 IP> // max on uS token is enabled, all others disabled
em3xx_load --patch @8080ff6=0x00 --patch @8080ff7=0x04 --ip <ISA3 IP> // 0x0400 or 1024 uS

PWM_WHITE, PWN_RED, PWM_GREEN, PWM_BLUE

The lower byte of these tokens defines the port and pin number for the specific
LED drive output value.  This is defined in our bit-mapped port/pin
configuration.  The lowest 3 bits defines the specific pin number (1-7), and
bit 3 defines the port number, where A is 0 and B is 1.  For example, port B
pin 2 would be 0b00001002 or 0x0A.  Note:  for this initial release, the port
is limited to port B, and the pins are limited to pins 1 through 4.  Therefore,
the only valid values are 0x09, 0x0a, 0x0b, and 0x0c for port B pin 1 through 4
respectively.  

Writing individual tokens:
Writing individual tokens is a two step process.  First, the bitmask must be
written to configure which tokens are now valid.  Next, the actual token must
be written.  This can be done with the em3xx_load program.

For example, if I want to change the transmit power to -3 on an EM3585, I would
write the following two tokens:

em3xx_load --patch @8080ffe=0xfe --ip <ISA3 IP> // TX token is enabled
em3xx_load --patch @8080ffc=0xfd --ip <ISA3 IP> // -3 in the lower byte

Note: if I am re-writing the configuration mask, I need to take care to include
previously writen bits so I am not attempting to write a 1 where a 0 currently
exists.  This could invalidate other tokens I have attempted to configure in
previous write attempts.

CFG_HARDWARE_VERSION

This token allows the user to set the version of the hardware that is
shipping with this image.  It is important to track this.  The bulb-config
plugin will copy this into the basic cluster attribute, if it is set, and 
use a default value of 0 if it is not set.  

em3xx_load --patch @8080fff=0xfe --ip <ISA3 IP> // HW version token is enabled
em3xx_load --patch @8080fec=0x01 --ip <ISA3 IP> // version 1

MANUFACTURER NAME and MODEL NUMBER

The manufacturing token TOKEN_MFG_STRING is used by the bulb-config plugin to
configure the manufacturer name.  Similarly, the token TOKEN_MFG_BOARD_NAME is
used by the bulb-config plugin to identifiy the model number.  If you create a
text file token.txt with the following lines:

TOKEN_MFG_STRING:  "Silicon Labs"
TOKEN_MFG_BOARD_NAME: "IST-A21"

and run the command:

em3xx_load --cibtokenspatch token.txt --ip <ISA3 IP>

the bulb-cfg will be able to copy "Silicon Labs" into the basic cluster
manufacturer name token and "IST-A21" into the basic cluster model identifier
token.
