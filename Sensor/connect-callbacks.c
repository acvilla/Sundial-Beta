// This file is generated by Ember Desktop.  Please do not edit manually.
//
//

// This callback file is created for your convenience. You may add application
// code to this file. If you regenerate this file over a previous version, the
// previous version will be overwritten and any code you have added will be
// lost.
#include PLATFORM_HEADER
#include CONFIGURATION_HEADER
#include "stack/include/ember.h"
#include "command-interpreter/command-interpreter.h"
#include "heartbeat/heartbeat.h"
#include "hal/hal.h"
#include "serial/serial.h"
#include "connect-debug-print.h"
#include "ustimer.h"




#define SENSOR_SINK_TX_POWER                 10
#define SENSOR_SINK_CHANNEL                  1
#define SENSOR_SINK_PROTOCOL_ID              0xC00F

#define SENSOR_SINK_PROTOCOL_ID_OFFSET       0
#define SENSOR_SINK_COMMAND_ID_OFFSET        2
#define SENSOR_SINK_EUI64_OFFSET             3
#define SENSOR_SINK_NODE_ID_OFFSET           11
#define SENSOR_SINK_DATA_OFFSET              13
#define SENSOR_SINK_MAXIMUM_DATA_LENGTH      10
#define SENSOR_SINK_MINIMUM_LENGTH           SENSOR_SINK_DATA_OFFSET
#define SENSOR_SINK_MAXIMUM_LENGTH           (SENSOR_SINK_MINIMUM_LENGTH \
                                             + SENSOR_SINK_MAXIMUM_DATA_LENGTH)

#define SENSOR_SINK_SECURITY_KEY    {0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA,       \
                                     0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAA,       \
                                     0xAA, 0xAA, 0xAA, 0xAA}

static EmberKeyData securityKey = SENSOR_SINK_SECURITY_KEY;
uint8_t application_channel =   1;
uint8_t ScanSuccess =   1;
static uint8_t message[SENSOR_SINK_MAXIMUM_LENGTH];
static EmberMessageLength messageLength;
static EmberMessageOptions txOptions = EMBER_OPTIONS_NONE;
EmberNetworkParameters parameters;
enum {
  SENSOR_SINK_COMMAND_ID_ADVERTISE_REQUEST = 0,
  SENSOR_SINK_COMMAND_ID_ADVERTISE         = 1,
  SENSOR_SINK_COMMAND_ID_DATA              = 2,
};
typedef uint8_t SensorSinkCommandId;

// The Simulated EEPROM callback function, implemented by the
// application.
void halSimEepromCallback(EmberStatus status) {
 // your code here
}

// Handler called whenever the radio is powered on.
void halRadioPowerUpHandler(void) {
 // your code here
}

// Handler called whenever the radio is powered off.
void halRadioPowerDownHandler(void) {
 // your code here
}

/** @brief Ok To Sleep
 *
 * This function is called by the Idle/Sleep plugin before sleeping.  It is
 * called with interrupts disabled.  The application should return TRUE if the
 * device may sleep or FALSE otherwise.
 *
 * @param durationMs The maximum duration in milliseconds that the device will
 * sleep.  Ver.: always
 */
bool emberAfPluginIdleSleepOkToSleepCallback(uint32_t durationMs) {
 // your code here
}

/** @brief Wake Up
 *
 * This function is called by the Idle/Sleep plugin after sleeping.
 *
 * @param durationMs The duration in milliseconds that the device slept.  Ver.:
 * always
 */
void emberAfPluginIdleSleepWakeUpCallback(uint32_t durationMs) {
 // your code here
}

/** @brief Ok To Idle
 *
 * This function is called by the Idle/Sleep plugin before idling.  It is called
 * with interrupts disabled.  The application should return TRUE if the device
 * may idle or FALSE otherwise.
 *
 */
bool emberAfPluginIdleSleepOkToIdleCallback(void) {
 return FALSE;// your code here
}

/** @brief Active
 *
 * This function is called by the Idle/Sleep plugin after idling.
 *
 */
void emberAfPluginIdleSleepActiveCallback(void) {
 // your code here
}

/** @brief Main Init
 *
 * This function is called when the application starts and can be used to
 * perform any additional initialization required at system startup.
 */
void emberAfMainInitCallback(void) {
	    CMU_ClockEnable(cmuClock_HFPER, true);
		USTIMER_Init();                                         //calibrate delay timer
		//initSundialADC();
		//initSundialGPIO();

		MEMSET(&parameters, 0, sizeof(EmberNetworkParameters));
		parameters.radioTxPower = SENSOR_SINK_TX_POWER;
		parameters.radioChannel = SENSOR_SINK_CHANNEL; 			//   PANID will be set when beacon is received

		EmberStatus status = emberNetworkInit();				//try to rejoin old network

		if (status == EMBER_SUCCESS) {
		// Successfully rejoined previous network
		} else {
			emberSetSecurityKey(securityKey);
			status = emberStartActiveScan(application_channel);
			emberAfCorePrintln("Scan Result: %x", status);
		}

}

/** @brief Main Tick
 *
 * This function is called in each iteration of the main application loop and
 * can be used to perform periodic functions.  The frequency with which this
 * function is called depends on how quickly the main loop runs.  If the
 * application blocks at any time during the main loop, this function will not
 * be called until execution resumes. Sleeping and idling will block.
 */
void emberAfMainTickCallback(void) {
	EmberStatus status = emberJoinNetwork(EMBER_STAR_END_DEVICE,&parameters);
}

/** @brief Stack Status
 *
 * This function is called when the stack status changes.  This callbacks
 * provides applications an opportunity to be notified of changes to the stack
 * status and take appropriate action.
 *
 * @param status   Ver.: always
 */
void emberAfStackStatusCallback(EmberStatus status) {
 // your code here
}

/** @brief Incoming Message
 *
 * This function is called when a message is received.
 *
 * @param message   Ver.: always
 */
void emberAfIncomingMessageCallback(EmberIncomingMessage *message) {
	switch (message->payload[SENSOR_SINK_COMMAND_ID_OFFSET]) {
		case SENSOR_SINK_COMMAND_ID_ADVERTISE:
			emberAfCorePrintln("Advertise Message Received");
	        break;
		case SENSOR_SINK_COMMAND_ID_DATA:
			emberAfCorePrintln("Data Received");
	}
}

static void storeLowHighInt16u(uint8_t *contents, uint16_t value)
{
  contents[0] = LOW_BYTE(value);
  contents[1] = HIGH_BYTE(value);
}
static EmberStatus send(EmberNodeId nodeId,
                        SensorSinkCommandId commandId,
                        uint8_t *buffer,
                        uint8_t bufferLength)
{
  messageLength = 0;
  storeLowHighInt16u(message + messageLength, SENSOR_SINK_PROTOCOL_ID);
  messageLength += 2;
  message[messageLength++] = commandId;
  MEMCOPY(message + messageLength, emberGetEui64(), EUI64_SIZE);
  messageLength += EUI64_SIZE;
  storeLowHighInt16u(message + messageLength, emberGetNodeId());
  messageLength += 2;
  if (bufferLength != 0) {
    MEMCOPY(message + messageLength, buffer, bufferLength);
    messageLength += bufferLength;
  }
  return emberMessageSend(nodeId,
                          0, // endpoint
                          0, // messageTag
                          messageLength,
                          message,
                          txOptions);
}

/** @brief Message Sent
 *
 * This function is called to indicate whether an outgoing message was 
 * successfully transmitted or to indicate the reason of failure.
 *
 * @param status    Ver.: always
 * @param message   Ver.: always
 */
void emberAfMessageSentCallback(EmberStatus status, EmberOutgoingMessage *message){
 // your code here
}

/** @brief Child Join
 *
 * This function is called when a node has joined the network.
 *
 * @param nodeType   Ver.: always
 * @param nodeId     Ver.: always
 */
void emberAfChildJoinCallback(EmberNodeType nodeType,
                              EmberNodeId nodeId) {
 // your code here
}

/** @brief Active Scan Complete
 *
 * This function is called when a node has completed an active scan.
 */
void emberAfActiveScanCompleteCallback(void) {

}

/** @brief Child Join
 *
 * This function is called when a node has joined the network.
 *
 * @param mean       Ver.: always
 * @param min        Ver.: always
 * @param max        Ver.: always
 * @param variance   Ver.: always
 */
void emberAfEnergyScanCompleteCallback(int8_t mean,
                                       int8_t min,
                                       int8_t max,
                                       uint16_t variance) {
 // your code here
}

/** @brief Incoming Beacon
 *
 * This function is called when a node is performing an active scan and a beacon
 * is received.
 *
 * @param panId          Ver.: always
 * @param nodeId         Ver.: always
 * @param payloadLength  Ver.: always
 * @param payload        Ver.: always
 */
void emberAfIncomingBeaconCallback(EmberPanId panId,
                                   EmberNodeId nodeId,
                                   uint8_t payloadLength,
                                   uint8_t *payload) {
 parameters.panId = panId;
 emberAfCorePrintln("Incoming Beacon Received: %d", panId);
 EmberStatus status = emberJoinNetwork(EMBER_STAR_END_DEVICE,&parameters);

}
