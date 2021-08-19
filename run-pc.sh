#!/bin/sh

xkeysnail .xkeysnail-config/pc-kinesis-elecomexg.py --devices /dev/input/event3 /dev/input/event8 --quiet </dev/null &>/dev/null &
xkeysnail .xkeysnail-config/pc-elecomhuge.py --devices /dev/input/event9 --quiet </dev/null &>/dev/null &
