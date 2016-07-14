#!/bin/bash

OUTPUT_DIR=$1

if [ -z "$OUTPUT_DIR" ]; then
  echo "Error: Must specify OUTPUT_DIR as first argument."
  exit 1
fi

# Set the compiler to use
CC="${E_CC:-gcc}"

FILES="token-util.c token-util-test.c endianness.c"

TARGET="$OUTPUT_DIR/token-util-test"
INCLUDES="-I../../../../"
OPTIONS="-DEMBER_TEST -DPLATFORM_HEADER=\"../../unix/compiler/gcc.h\""
COMMAND="$CC -Wall -Werror -ggdb $INCLUDES $OPTIONS $FILES -o $TARGET"

echo $COMMAND
$COMMAND

STATUS=$?
if [ $STATUS != 0 ]; then
  exit 1
fi

cd $OUTPUT_DIR
./token-util-test
STATUS=$?
exit $STATUS
