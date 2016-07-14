ZigBee 3.0 Sample Applications

ZigBee 3.0 provides a foundation of commissioning and network management
mechanisms to be used in all ZigBee applications. The sample scenario
presented here demonstrates the flexibility that the ZigBee 3.0 specification
provides to applications. They also act as an excellent starting point for users
wishing to build their own ZigBee 3.0 applications.

These applications can take on three possible roles.
  1. The gateway can form a centralized network, and the light and the switch
     can join the centralized network by performing network steering.
  2. The light, acting as a router, can form a distributed network, and the
     switch, acting as an end device, can join the distributed network.
  3. The light, acting as a touchlink target, can touchlink with the
     switch, acting as a touchlink initiator.

The gateway provides a robust application interface to the user. Pressing
button 0 or 1 on the application when the gateway is not on a network will
form a centralized network. The gateway application can then be triggered to
allow other devices onto the network using button 0. Devices can then join the
network using the ZigBeeAlliance09 link key, or by manaully entering the install
code of the joining device onto the gateway using the CLI. Pressing button 1
will no longer allow devices onto the gateway's network. When the gateway has
formed a network, it will set its COMMISSIONING_STATUS_LED. When the network is
open for joining, the LED will blink.

The light application provides almost no interface to the user. Therefore, the
light performs network steering automatically once it is powered. If the light
does not find a suitable network to join, it forms its own distributed network.
The light will open its network as soon as the network comes up.
Once a distributed network is formed, the switch may join its network by
performing network steering itself or through touchlink commissioning. Once the
light is on a network, it will set its COMMISSIONING_STATUS_LED. When the light
starts identifying as a find and bind target, it will blink its
COMMISSIONING_STATUS_LED.

The switch provides a simple application interface to the user. When the switch
is not on a network, it can initiate network steering to join a network using
button 0. The switch can also initiate touchlink commissioning using button 1.
After the switch has successfully joining a network, it will perform the finding
and binding procedure for an initiator. After this takes place, the switch
should have at least two bindings to the light in its binding table: one for the
On/Off cluster and one for the Level Control cluster. While the switch is
performing its network commissioning, it will blink its
COMMISSIONING_STATUS_LED. When the switch is active on the network, it will
set its COMMISSIONING_STATUS_LED. Once the switch has finished finding and binding,
users can use buttons 0 and 1 to send On/Off Toggle and Level Control Move
to Level commands to the light, respectively.

The current debug printing settings in these applications are only for the
purpose of aiding users in understanding and debugging this sample scenario.
Debug printing should be turned off in order to save code size on a final
product.
