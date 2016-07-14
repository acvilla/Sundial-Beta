(bitmap apsOptions int16u "APS Options."
  (encryption             0x0020 "Enable APS encryption")
  (enableRetry            0x0040 "Enable APS retry")
  (enableRouteDiscovery   0x0100 "Enable route discovery")
  (forceRouteDiscovery    0x0200 "Force route discovery")
  (sourceEUI64            0x0400 "Include source EUI64")
  (destinationEUI64       0x0800 "Include destination EUI64")
  (enableAddressDiscovery 0x1000 "Enable address discovery")
  (pollResponse           0x2000 "Poll response message")
  (fragment               0x8000 "Part of fragmented message")
)

(enum stackStatus int8u "Stack status."
  (NETWORK_UP 0x90 "Network up.")
  (NETWORK_DOWN 0x91 "Network down.")
  (JOIN_FAILED 0x94 "Join failed.")
  (MOVE_FAILED 0x96 "Move failed.")
  (CANNOT_JOIN_AS_ROUTER 0x98 "Can not join as router.")
  (NODE_ID_CHANGED 0x99 "Node Id changed.")
  (PAN_ID_CHANGED 0x9A "Pan Id changed.")
  (CHANNEL_CHANGED 0x9B "Channel changed.")
  (NO_BEACONS 0xAB "No beacons.")
  (RECEIVED_KEY_IN_THE_CLEAR 0xAC "Received key in the clear.")
  (NO_NETWORK_KEY_RECEIVED 0xAD "No network key received.")
  (NO_LINK_KEY_RECEIVED 0xAE "No link key received.")
  (PRECONFIGURED_KEY_REQUIRED 0xAF "Preconfigured key required.")
)

(enum messageType int8u "Incoming message type."
  (UNICAST            0x00 "Unicast")
  (UNICAST_REPLY      0x01 "Unicast reply")
  (MULTICAST          0x02 "Multicast")
  (MULTICAST_LOOPBACK 0x03 "Multicast loopback")
  (BROADCAST          0x04 "Broadcast")
  (BROADCAST_LOOPBACK 0x05 "Broadcast loopback")
)

(frame 0x00 SET_BINDING "Set binding" "Set binding function call. "
  (command
    (int8u index "Index" "Index.")
  )
)
(frame 0x01 DELETE_BINDING "Delete binding" "Delete binding function call. "
  (command
    (int8u index "Index" "Index.")
  )
)
(frame 0x02 CLEAR_BINDING_TABLE "Clear binding table" "Clear binding table function call. "
  (command)
)
(frame 0x06 SEND_LIMITED_MULTICAST "Send limited multicast" "Send limited multicast function call. "
  (command
    (int16u groupId "Group Id" "Group Id of APS structure.")
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int8u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
    (int8u radius "Radius" "Radius.")
    (int8u nonmemberRadius "Non-member radius" "Non-member radius.")
  )
)
(frame 0x08 SEND_UNICAST "Send unicast" "Send unicast function call. "
  (command
    (int16u indexOrDestination "Index or destination" "Index or destination.")
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int16u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
  )
)
(frame 0x09 SEND_BROADCAST "Send broadcast" "Send broadcast function call. "
  (command
    (int16u destination "Destination" "Destination.")
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int16u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
    (int8u radius "Radius" "Radius.")
  )
)
(frame 0x0A PROXY_BROADCAST "Proxy broadcast" "Proxy broadcast function call. "
  (command
    (int16u source "Source" "Source.")
    (int16u destination "Destination" "Destination.")
    (int8u sequence "Sequence" "Sequence number of NWK frame.")
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int16u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
    (int8u radius "Radius" "Radius.")
  )
)
(frame 0x0B CANCEL_MESSAGE "Cancel message" "Cancel message function call. "
  (command
    (int8u message "Message" "Message.")
  )
)
(frame 0x0C SEND_REPLY "Send reply" "Send reply function call. "
  (command
    (int16u clusterId "Cluster Id" "Cluster Id.")
    (int8u reply "Reply" "Reply.")
  )
)
(frame 0x0D SET_REPLY_BINDING "Set reply binding" "Set reply binding function call. "
  (command
    (int8u index "Index" "Index.")
  )
)
(frame 0x0E MESSAGE_SENT "Message sent" "Message sent function call. "
  (command
    (int8u mode "Mode" "Mode.")
    (int16u destination "Destination" "Destination.")
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int16u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
    (int8u status "Status" "Status.")
  )
)
(frame 0x11 INCOMING_MESSAGE_HANDLER "Incoming message handler" "Incoming message handler function call. "
  (command
    (int8u type "Type" "Type." messageType)
    (int16u profileId "Profile Id" "Profile Id of APS structure.")
    (int16u clusterId "Cluster Id" "Cluster Id of APS structure.")
    (int8u sourceEndpoint "Source Endpoint" "Source endpoint of APS structure.")
    (int8u destinationEndpoint "Destination Endpoint" "Destination endpoint of APS structure.")
    (int16u options "Options" "Options of APS structure." apsOptions)
  )
)
(frame 0x13 STACK_STATUS_HANDLER "Stack status handler" "Stack status handler function call. "
  (command
    (int8u stackStatus "Status" "Status." stackStatus)
  )
)
(frame 0x14 NETWORK_INIT "Network init" "Network init function call. "
  (command
    (int8u nodeType "Node Type" "Nodetype.")
  )
)
(frame 0x15 FORM_NETWORK "Form network" "Form network function call. "
  (command
    (ptr8 extendedPanId "Extended PAN ID" "The network's extended PAN identifier.")
    (int16u panId "PAN ID" "The network's PAN identifier.")
    (int8u radioTxPower "TX Power" "The radio TX power setting, in dBm.")
    (int8u radioChannel "Channel" "The radio channel.")
  )
)
(frame 0x16 JOIN_NETWORK "Join network" "Join network function call. "
  (command
    (int8u nodeType "Node Type" "Role that this node will have in the network.")
    (ptr8 extendedPanId "Extended PAN ID" "The network's extended PAN identifier.")
    (int16u panId "PAN ID" "The network's PAN identifier.")
    (int8u radioTxPower "TX Power" "The radio TX power setting, in dBm.")
    (int8u radioChannel "Channel" "The radio channel.")
    (int8u joinMethod "Join Method" "Method used to establish an initial parent.")
    (int16u nwkManagerId "Network Manager ID" "The commissioned ID of the network manager.")
    (int8u nwkUpdateId "Network Update ID" "The commissioned network update ID.")
    (int32u channels "Network Channel Mask" "The commissioned list of preferred channels.")
  )
)
(frame 0x17 LEAVE_NETWORK "Leave network" "Leave network function call. "
  (command
  )
)
(frame 0x18 PERMIT_JOINING "Permit joining" "Permit joining function call. "
  (command
    (int8u duration "Duration" "Duration.")
  )
)
(frame 0x19 POLL_FOR_DATA "Poll for data" "Poll for data function call. "
  (command)
)
(frame 0x1A POLL_HANDLER "Poll handler" "Poll handler function call. "
  (command
    (int16u id "Id" "Id.")
    (int8u sendAppJitMessage "Jit message" "Jit message.")
  )
)
(frame 0x1E TRUST_CENTER_JOIN_HANDLER "Trust center join handler" "Trust center join handler function call. "
  (command
    (int8u status "Status" "Status.")
    (int8u decision "Decision" "Decision.")
  )
)
(frame 0x20 SET_MESSAGE_FLAG "Set message flag" "Set message flag function call. "
  (command
    (int16u childId "Child Id" "Child Id.")
  )
)
(frame 0x21 CLEAR_MESSAGE_FLAG "Clear message flag" "Clear message flag function call. "
  (command
    (int16u childId "Child Id" "Child Id.")
  )
)
(frame 0x22 POLL_COMPLETE_HANDLER "Poll complete handler" "Poll complete handler function call. "
  (command
    (int8u status "Status" "Status.")
  )
)
(frame 0x23 CHILD_JOIN_HANDLER "Child join handler" "Child join handler function call. "
  (command
    (int8u childIndex "Child Index" "Child Index.")
    (int8u joining "Joining" "Joining.")
  )
)
(frame 0x24 START_SCAN "Start scan" "Start scan function call. "
  (command
    (int8u scanType "Scan Type" "Scan Type.")
    (int32u channelMask "Channel Mask" "Channel Mask.")
    (int8u duration "Duration" "Duration.")
  )
)
(frame 0x25 STOP_SCAN "Stop scan" "Stop scan function call. "
  (command
  )
)
(frame 0x26 SCAN_COMPLETE_HANDLER "Scan complete handler" "Scan complete handler function call. "
  (command
    (int8u data "Data" "Data.")
    (int8u status "Status" "Status.")
  )
)
(frame 0x27 NETWORK_FOUND_HANDLER "Network found handler" "Network found handler function call. "
  (command
    (int16u panId "Pan Id" "Pan Id.")
    (int8u permitJoin "Permit Join" "Permit Join.")
    (int8u stackProfile "Stack Profile" "Stack Profile.")
  )
)
(frame 0x28 ENERGY_SCAN_RESULT_HANDLER "Energy scan result handler" "Energy scan result handler function call. "
  (command
    (int8u channel "Channel" "Channel.")
    (int8u rssi "Rssi" "Rssi.")
  )
)
(frame 0x2B SET_INITIAL_SECURITY_STATE "Set initial security state" "Set initial security state function call. "
  (command
    (int16u mask "Mask" "Mask.")
    (ptr16 preconfiguredKey "Preconfigured Key" "Preconfigured key.")
    (ptr16 networkKey "Network Key" "Network Key.")
    (int8u keySequence "Key Sequence" "Network key sequence number.")
  )
)
(frame 0x2C REJOIN_NETWORK "Rejoin network" "Rejoin network function call. "
  (command
    (int8u haveKey "Have Key" "Have curren tnetwork key.")
    (int32u channelMask "Channel Mask" "Channel Mask.")
    (int8u status "Status" "Status.")
  )
)
(frame 0x2D STACK_POWER_DOWN "Stack power down" "Stack power down function call."
  (command
  )
)
(frame 0x2E STACK_POWER_UP "Stack power up" "Stack power up function call."
  (command
  )
)
(frame 0x2F SET_EXTENDED_SECURITY_BITMASK "Set extended security bitmask" "Set extended security bitmask function call. "
  (command
    (int16u mask "Bitmask" "Extended Security Bitmask.")
  )
)
(frame 0x30 RF4CE_SET_PAIRING_TABLE_ENTRY "RF4CE set pairing table entry" "RF4CE set pairing table entry function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (ptr16 securityLinkKey "Security Link Key" "The link key of the pairing link.")
    (ptr8 destLongId "Destination long ID" "The IEEE address of the peer node.")
    (int32u frameCounter "Frame counter" "The outgoing frame counter of the pairing link.")
    (int16u sourceNodeId "Source node ID" "The node ID of the local node for the pairing link.")
    (int16u destPanId "Destination PAN ID" "The PAN ID of the pairing link.")
    (int16u destNodeId "Destination node ID" "The node ID of the peer node.")
    (int16u destVendorId "Destination vendor ID" "The vendor ID of the peer node.")
    (int8u destProfileIdListLength "Destination profile ID list length" "The length of the list of profiles supported by the peer node.")
    (int8u info "Info" "The info byte of the pairing entry.")
    (int8u channel "Channel" "The channel of the pairing link.")
    (int8u capabilities "Capabilities" "The node capabilities of the peer node.")
    (int8u lastSeqn "Last Sequence Number" "Last MAC sequence number seen on this pairing link.")
  )
)
(frame 0x31 RF4CE_GET_PAIRING_TABLE_ENTRY "RF4CE get pairing table entry" "RF4CE get pairing table entry function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
  )
)
(frame 0x32 RF4CE_DELETE_PAIRING_TABLE_ENTRY "RF4CE get pairing table entry" "RF4CE get pairing table entry function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
  )
)
(frame 0x33 RF4CE_SET_APPLICATION_INFO "RF4CE set application info" "RF4CE set application info function call. "
  (command
    (int8u capabilities "Capabilities" "The application capabilities.")
  )
)
(frame 0x34 RF4CE_GET_APPLICATION_INFO "RF4CE get application info" "RF4CE get application info function call. "
  (command
  )
)
(frame 0x35 RF4CE_KEY_UPDATE "RF4CE key update" "RF4CE key update function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (ptr16 key "Key" "The new key.")
  )
)
(frame 0x36 RF4CE_SEND "RF4CE send" "RF4CE send function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (int8u profileId "Profile ID" "The profile ID.")
    (int16u vendorId "Vendor ID" "The vendor ID.")
    (int8u txOptions "TX options" "The TX options.")
    (int8u messageTag "Message TAG" "The message TAG.")
  )
)
(frame 0x37 RF4CE_MESSAGE_SENT_HANDLER "RF4CE message sent handler" "RF4CE message sent handler function call. "
  (command
    (int8u status "Status" "The status of the transmission.")
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (int8u txOptions "TX options" "The TX options.")
    (int8u profileId "Profile ID" "The profile ID.")
    (int16u vendorId "Vendor ID" "The vendor ID.")
    (int8u messageTag "Message TAG" "The message TAG originally set by the application.")
  )
)
(frame 0x38 RF4CE_INCOMING_MESSAGE_HANDLER "RF4CE incoming message handler" "RF4CE incoming message handler function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (int8u profileId "Profile ID" "The profile ID.")
    (int16u vendorId "Vendor ID" "The vendor ID.")
    (int8u txOptions "TX Options" "The TX options.")
  )
)
(frame 0x39 RF4CE_START "RF4CE start" "RF4CE start function call. "
  (command
    (int8u nodeCapabilities "Node capabilities" "The node capabilities.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u power "power" "The radio power.")
  )
)
(frame 0x3A RF4CE_STOP "RF4CE stop" "RF4CE stop function call. "
  (command
  )
)
(frame 0x3B RF4CE_DISCOVERY "RF4CE discovery" "RF4CE discovery function call. "
  (command
    (int16u panId "PAN ID" "The PAN ID.")
    (int16u nodeId "Node ID" "The node ID.")
    (int8u searchDevType "Search device type" "The device type to search for.")
    (int16u discDuration "Discovery duration" "The discovery duration.")
    (int8u maxDiscRepetitions "Maximum discovery repetitions" "The maximum number of discovery repetitions.")
  )
)
(frame 0x3C RF4CE_DISCOVERY_COMPLETE_HANDLER "RF4CE discovery complete handler" "RF4CE discovery complete handler function call. "
  (command
    (int8u status "Status" "The discovery status.")
  )
)
(frame 0x3D RF4CE_DISCOVERY_REQUEST_HANDLER "RF4CE discovery request handler" "RF4CE discovery request handler function call. "
  (command
    (ptr8 srcIeeeAddr "Source IEEE address" "The IEEE address of the source node.")
    (int8u nodeCapabilities "Node Capabilities" "The node capabilities.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u appCapabilities "Application capabilities" "The application capabilities field of the application info.")
    (int8u searchDevType "Search device type" "The device type to search for.")
    (int8u rxLinkQuality "RX link quality" "The RX link quality index.")
  )
)
(frame 0x3E RF4CE_DISCOVERY_RESPONSE_HANDLER "RF4CE discovery response handler" "RF4CE discovery response handler function call. "
  (command
    (int8u atCapacity "At capacity" "Flag indicating whether the node has room i nthe pairing table for a new pairing link.")
    (int8u channel "channel" "The channel.")
    (int16u panId "PAN ID" "The PAN ID.")
    (ptr8 srcIeeeAddr "Source IEEE address" "The IEEE address of the source node.")
    (int8u nodeCapabilities "Node Capabilities" "The node capabilities.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u appCapabilities "Application capabilities" "The application capabilities field of the application info.")
    (int8u rxLinkQuality "RX link quality" "The RX link quality index.")
    (int8u discRequestLqi "Discovery request LQI" "The discovery request link quality index.")
  )
)
(frame 0x3F RF4CE_ENABLE_AUTO_DISCOVERY_RESPONSE "RF4CE enable auto discovery response" "RF4CE enable auto discovery response function call. "
  (command
    (int16u duration "Duration" "The discovery duration.")
  )
)
(frame 0x40 RF4CE_AUTO_DISCOVERY_RESPONSE_COMPLETE_HANDLER "RF4CE auto discovery response complete handler" "RF4CE auto discovery response complete handler function call. "
  (command
    (int8u status "Status" "The discovery status.")
    (ptr8 srcIeeeAddr "Source IEEE address" "The IEEE address of the source node.")
    (int8u nodeCapabilities "Node Capabilities" "The node capabilities.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u appCapabilities "Application capabilities" "The application capabilities field of the application info.")
    (int8u searchDevType "Search device type" "The device type to search for.")
  )
)
(frame 0x41 RF4CE_PAIR "RF4CE pair" "RF4CE pair function call. "
  (command
    (int8u channel "channel" "The channel.")
    (int16u panId "PAN ID" "The PAN ID.")
    (ptr8 ieeeAddr "IEEE address" "The IEEE address of the destination node.")
    (int8u keyExchangeTransferCount "Key exchange transfer count" "The key exchange transfer count parameter.")
  )
)
(frame 0x42 RF4CE_PAIR_COMPLETE_HANDLER "RF4CE pair complete handler" "RF4CE pair complete handler function call. "
  (command
    (int8u status "Status" "The pairing status.")
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u appCapabilities "Application capabilities" "The application capabilities field of the application info.")
  )
)
(frame 0x43 RF4CE_PAIR_REQUEST_HANDLER "RF4CE pair request handler" "RF4CE pair request handler function call. "
  (command
    (int8u status "Status" "The pairing status.")
    (int8u pairingIndex "Pairing Index" "The pairing index.")
    (ptr8 srcIeeeAddr "Source IEEE address" "The IEEE address of the source node.")
    (int8u nodeCapabilities "Node Capabilities" "The node capabilities.")
    (int16u vendorId "Vendor ID" "The vendor ID field of the vendor info.")
    (int8u appCapabilities "Application capabilities" "The application capabilities field of the application info.")
    (int8u keyExchangeTransferCount "Key exchange transfer count" "The key exchange transfer count parameter.")
  )
)
(frame 0x44 RF4CE_UNPAIR "RF4CE unpair" "RF4CE unpair function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
  )
)
(frame 0x45 RF4CE_UNPAIR_HANDLER "RF4CE unpair handler" "RF4CE unpair handler function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
  )
)
(frame 0x46 RF4CE_UNPAIR_COMPLETE_HANDLER "RF4CE unpair complete handler" "RF4CE unpair complete handler function call. "
  (command
    (int8u pairingIndex "Pairing Index" "The pairing index.")
  )
)
(frame 0x47 RF4CE_SET_POWER_SAVING_PARAMETERS "RF4CE set power saving parameters" "RF4CE set power saving parameters function call. "
  (command
    (int32u dutyCycle "Duty cycle" "The duty cycle parameter.")
    (int32u activePeriod "Active period" "The active period parameter.")
  )
)
(frame 0x48 RF4CE_SET_FREQUENCY_AGILITY_PARAMETERS "RF4CE set frequency agility parameters" "RF4CE set frequency agility parameters function call. "
  (command
    (int8u rssiWindowSize "RSSI window size" "The RSSI window size.")
    (int8u channelChangeReads "Channel change reads" "The channel change reads.")
    (int8u rssiThreshold "RSSI threshold" "The RSSI threshold.")
    (int16u readInterval "Read interval" "The read interval.")
    (int8u readDuration "Read duration" "The read duration.")
  )
)
(frame 0x49 RF4CE_SET_DISCOVERY_LQI_THRESHOLD "RF4CE set discovery LQI threshold" "RF4CE set discovery LQI threshold function call. "
  (command
    (int8u threshold "Threshold" "The LQI threshold.")
  )
)