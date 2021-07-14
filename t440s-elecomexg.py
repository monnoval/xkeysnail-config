# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({

    # Thinkpad T440s default keyboard
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_ALT,
    Key.CAPSLOCK: Key.BACKSPACE,

    # ELECOM 'EX-G WIRED TRACKBALL
    Key.BTN_SIDE: Key.ENTER,

    # Thinkpad T440s trackpad buttons
    Key.BTN_MIDDLE: Key.ESC,
})

# Keybindings for Editor
define_keymap(re.compile("nvim-qt"), {
    # ELECOM 'EX-G WIRED TRACKBALL
    K("BTN_EXTRA"): K("C-q"),
}, "Editor")

# Keybindings for Browsers
define_keymap(re.compile("Firefox|firefox|Chromium|LibreWolf"), {

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

    # Thinkpad T440s default keyboard
    K("RShift-T"): [launch(["xfce4-terminal"])],
    K("RShift-V"): [launch(["nvim-qt"])],
    K("RShift-X"): [launch(["xkill"])],
    K("RShift-F"): [launch(["thunar"])],
    K("RShift-W"): [launch(["firefox","-new-tab","about:newtab"])],

    # ELECOM 'EX-G WIRED TRACKBALL
    K("BTN_EXTRA"): K("C-w"),
    K("BTN_FORWARD"): K("C-f7"),

}, "All apps")
