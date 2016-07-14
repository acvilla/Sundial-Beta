This readme describes how to setup the 3xx tools to work on Mac and Linux.

Mac:

You shouldn't have to do anything to just run em3xx_load on the Mac.

To udpate the JLink DLL you must follow the instuctions below or the JLink DLL
will not search in the right locations for the USB library.
  1. Rename libjlinkarm.4.xx.xx.dylib to libjlinkarm.4.dylib
  2. install_name_tool -change /Developer/SDKs/MacOSX10.5.sdk/usr/local/lib/libusb-1.0.0.dylib @loader_path/libusb-1.0.0.dylib libjlinkarm.4.dylib
  3. install_name_tool -change /usr/local/lib/libusb-1.0.0.dylib @loader_path/libusb-1.0.0.dylib libjlinkarm.4.dylib
  4. install_name_tool -id @loader_path/libjlinkarm.4.dylib libjlinkarm.4.dylib
  5. Copy the modified libjlinkarm.4.dylib to hal/micro/cortexm3/loader/libjlinkarm.4.dylib


Linux:

Use your package manager to install libusb. Once you have this installed you should
be able to access the ISA3 over Ethernet, but will likely have permissions issues
when using USB. To fix these, follow the instructions below from Segger.

- Place the rule file "45-jlink.rules" provided with this J-Link software package
  at /etc/udev/rules.d/

- Make sure that you are member of the group "plugdev"

- If the group "plugdev" does not exist, you have to create it:
  Command line:
  groupadd plugdev                      // Creates new group "plugdev"
	usermod -a -G plugdev <Username>      // Appends user <Username> to the group "plugdev"

- Restart your system

