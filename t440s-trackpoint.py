# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    # Thinkpad T440s trackpoint buttons
    Key.BTN_RIGHT: Key.ENTER,
    Key.BTN_MIDDLE: Key.ESC,
})
