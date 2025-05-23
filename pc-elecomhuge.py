# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    # ELECOM HUGE
    Key.BTN_BACK: Key.ENTER,
    Key.BTN_SIDE: Key.ENTER,
    Key.BTN_EXTRA: Key.BTN_MOUSE,
})

# Keybindings for Browsers
define_keymap(re.compile("firefox|chromium|Brave|librewolf"), {
    K("C-right"): K("C-TAB"),
    K("C-left"): K("C-Shift-TAB"),
}, "Browsers")

# Affects all apps
define_keymap(lambda wm_class: wm_class not in ("AnAppThatDoesNotExist"), {
    # ELECOM HUGE
    K("BTN_FORWARD"): K("C-w"),
    K("BTN_TASK"): K("C-f7"),
}, "All apps")
