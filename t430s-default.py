# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({

    # Thinkpad T440s default keyboard
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_ALT,
    Key.CAPSLOCK: Key.BACKSPACE,

    # Thinkpad T440s trackpad buttons
    Key.BTN_MIDDLE: Key.ESC,
})

# Keybindings for Browsers
define_keymap(re.compile("Firefox|firefox|Google-chrome|Chromium|Brave"), {

    # Next and previous tab
    K("C-left"): K("C-Shift-TAB"),
    K("C-right"): K("C-TAB"),
    K("LC-LShift-H"): K("C-Shift-TAB"),
    K("LC-LShift-L"): K("C-TAB"),

    # Browser back and forward
    K("LSuper-H"): K("LM-LEFT"),
    K("LSuper-L"): K("LM-RIGHT"),

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

}, "All apps")
