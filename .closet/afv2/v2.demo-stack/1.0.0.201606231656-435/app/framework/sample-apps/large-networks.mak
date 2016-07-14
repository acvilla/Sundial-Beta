# This file lists all the targets used by the large network test. This eventually needs to be generated.


.PHONY: all
all: run-large-network-tests

.PHONY: run-large-network-tests
run-large-network-tests: \
    build/af-test-apps/largeNetworkCoordinator-simulation/largeNetworkCoordinator \
    build/af-test-apps/largeNetworkRouter-simulation/largeNetworkRouter \
    scope
		java -classpath build com.ember.peek.app.zigbee.LargeNetworkTest -tests all -seed 75 -encryption-type real

scope:
		make -f Makefile scope

build/af-test-apps/largeNetworkCoordinator-simulation/largeNetworkCoordinator:
		make -f app/framework/sample-apps/large-network-coordinator/gen/simulation/Makefile


build/af-test-apps/largeNetworkRouter-simulation/largeNetworkRouter:
		make -f app/framework/sample-apps/large-network-router/gen/simulation/Makefile
