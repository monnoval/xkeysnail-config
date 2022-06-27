# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    # Kinesis Advantage
    Key.RIGHT_META: Key.RIGHT_CTRL,
    Key.LEFT_CTRL: Key.RIGHT_META,

    # ELECOM HUGE
    Key.BTN_BACK: Key.ENTER,
    Key.BTN_SIDE: Key.ENTER,
    Key.BTN_EXTRA: Key.BTN_MOUSE,
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile('nvim-qt'), {
    # Kinesis Advantage
    Key.RIGHT_META: Key.RIGHT_CTRL,
})

# Keybindings for Browsers
define_keymap(re.compile("nvim-qt"), {
    # ELECOM HUGE
    K("BTN_FORWARD"): K("C-q"),
}, "Gvim")

# Keybindings for Browsers
define_keymap(re.compile("Firefox|firefox|Google-chrome|Chromium|Brave"), {
    K("C-right"): K("C-TAB"),
    K("C-left"): K("C-Shift-TAB"),
}, "Browsers")

# Affects all apps
define_keymap(lambda wm_class: wm_class not in ("AnAppThatDoesNotExist"), {

    # Linux apps
    K("RShift-V"): [launch(["nvim-qt"])],
    K("RShift-X"): [launch(["xkill"])],
    K("RShift-W"): [launch(["brave-browser-beta","about:newtab"])],

    # Plasma launch apps
    K("RShift-T"): [launch(["konsole","--profile","work"])],
    K("RShift-F"): [launch(["dolphin"])],

    # ELECOM HUGE
    K("BTN_FORWARD"): K("C-w"),
    K("BTN_TASK"): K("C-f7"),

    # Kinesis Advantage
    K("HOME"): K("C-f9"),

}, "All apps")
