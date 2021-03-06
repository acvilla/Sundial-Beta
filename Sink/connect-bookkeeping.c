// This file is generated by Ember Desktop.  Please do not edit manually.
//
//

#include PLATFORM_HEADER
#include CONFIGURATION_HEADER
#include "stack/include/ember.h"

// Init function declarations.
void emberCommandReaderInit(void);
void emAfPluginMailboxClientInitCallback(void);
void emAfPluginMailboxServerInitCallback(void);

void emberAfInit(void)
{
  emberCommandReaderInit();
  emAfPluginMailboxClientInitCallback();
  emAfPluginMailboxServerInitCallback();
}

// Tick function declarations.
void emberAfPluginCommandInterpreterTickCallback(void);
void emberAfPluginIdleSleepTickCallback(void);

void emberAfTick(void)
{
  emberAfPluginCommandInterpreterTickCallback();
  emberAfPluginIdleSleepTickCallback();
}

// StackStatus function declarations.
void emAfPluginMailboxServerStackStatusCallback(EmberStatus status);
void emberAfPluginPollStackStatusCallback(EmberStatus status);

void emberAfStackStatus(EmberStatus status)
{
  emAfPluginMailboxServerStackStatusCallback(status);
  emberAfPluginPollStackStatusCallback(status);
}

void emberAfStackIsr(void)
{
}

// IncomingMessage function declarations.
void emAfPluginMailboxClientIncomingMessageCallback(EmberIncomingMessage* message);
void emAfPluginMailboxServerIncomingMessageCallback(EmberIncomingMessage* message);

void emberAfIncomingMessage(EmberIncomingMessage* message)
{
  emAfPluginMailboxClientIncomingMessageCallback(message);
  emAfPluginMailboxServerIncomingMessageCallback(message);
}

// MessageSent function declarations.
void emAfPluginMailboxClientMessageSentCallback(EmberStatus status, EmberOutgoingMessage* message);
void emAfPluginMailboxServerMessageSentCallback(EmberStatus status, EmberOutgoingMessage* message);

void emberAfMessageSent(EmberStatus status, EmberOutgoingMessage* message)
{
  emAfPluginMailboxClientMessageSentCallback(status, message);
  emAfPluginMailboxServerMessageSentCallback(status, message);
}

void emberAfChildJoin(EmberNodeType nodeType, EmberNodeId nodeId)
{
}

void emberAfIncomingBeacon(EmberPanId panId, EmberNodeId nodeId, uint8_t payloadLength, uint8_t* payload)
{
}

void emberAfActiveScanComplete(void)
{
}

void emberAfEnergyScanComplete(int8_t mean, int8_t min, int8_t max, uint16_t variance)
{
}

// MarkApplicationBuffers function declarations.
void emberAfMarkApplicationBuffersCallback(void);
void emAfPluginMailboxServerMarkBuffersCallback(void);

void emberMarkApplicationBuffersHandler(void)
{
  emberAfMarkApplicationBuffersCallback();
  emAfPluginMailboxServerMarkBuffersCallback();
}
