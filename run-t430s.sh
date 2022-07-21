#!/bin/sh

# xkeysnail ~/.xkeysnail-config/t430s-kinesis-elecomhuge.py --devices /dev/input/event8 /dev/input/event12 --quiet </dev/null &>/dev/null &

# With mouse+keyboard
# xkeysnail ~/.xkeysnail-config/t430s-kinesis-elecomhuge.py --devices /dev/input/event8 /dev/input/event11 --quiet </dev/null &>/dev/null &
# xkeysnail ~/.xkeysnail-config/t430s-kinesis-elecomhuge.py --devices /dev/input/event8 /dev/input/event12 --quiet </dev/null &>/dev/null &

# Laptop only without mouse+keyboard
xkeysnail ~/.xkeysnail-config/t430s-default.py --quiet </dev/null &>/dev/null &
