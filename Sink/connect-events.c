// This file is generated by Ember Desktop.  Please do not edit manually.
//
//

// Enclosing macro to prevent multiple inclusion
#ifndef __CONNECT_EVENTS__
#define __CONNECT_EVENTS__


// Generated events.
#include PLATFORM_HEADER
#include "stack/include/ember-types.h"
#include "hal/hal.h"


void emAfPluginMailboxClientEventHandler(void);
extern EmberEventControl emAfPluginMailboxClientEventControl;

void emAfPluginMailboxServerEventHandler(void);
extern EmberEventControl emAfPluginMailboxServerEventControl;

void emberAfPluginPollEventHandler(void);
extern EmberEventControl emberAfPluginPollEventControl;

void adcHandler(void);
extern EmberEventControl adcEventControl;

void advertiseHandler(void);
extern EmberEventControl advertiseControl;

const EmberEventData emAppEvents[] = {
		{&adcEventControl, adcHandler},
		{&advertiseControl, advertiseHandler},
  {&emAfPluginMailboxClientEventControl, emAfPluginMailboxClientEventHandler},
  {&emAfPluginMailboxServerEventControl, emAfPluginMailboxServerEventHandler},
  {&emberAfPluginPollEventControl, emberAfPluginPollEventHandler},
  {NULL, NULL}
};
#endif // __CONNECT_EVENTS__
