# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({

    # Default keyboard
    Key.LEFT_ALT: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_ALT,
    Key.CAPSLOCK: Key.BACKSPACE,

})

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

    # Gnome for Fedora Workstation
    K("RShift-T"): [launch(["gnome-terminal"])],
    K("RShift-V"): [launch(["nvim-qt"])],
    # K("RShift-X"): [launch(["xkill"])],
    K("RShift-F"): [launch(["nautilus"])],
    K("RShift-W"): [launch(["firefox","-new-tab","about:newtab"])],

}, "All apps")
