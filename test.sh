#!/bin/bash

# If parameter provided, execute that program
if [ $# -lt 1 ]; then
    PROGRAM="./a.out"
else
    PROGRAM=$1
fi

# Test program and store output
tmpoutput=`echo -e freddy '\n' susan | $PROGRAM`

# Number correct
CORRECT=0

# Test 1
f1=`echo $tmpoutput | grep -q 'freddy'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

# Test 2
f1=`echo $tmpoutput | grep -q 'susan'`
if [ $? = 0 ]; then
    let CORRECT=CORRECT+1
fi

# Return number correct
exit $CORRECT
