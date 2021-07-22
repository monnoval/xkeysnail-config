# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    # Kinesis Advantage
    Key.RIGHT_META: Key.RIGHT_CTRL,
    Key.LEFT_CTRL: Key.RIGHT_META,

    # ELECOM 'EX-G WIRED TRACKBALL
    Key.BTN_SIDE: Key.ENTER,
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile('Gvim|nvim-qt'), {
    Key.RIGHT_META: Key.RIGHT_CTRL,
})

# Keybindings for Browsers
define_keymap(re.compile("Gvim|nvim-qt"), {
    # ELECOM 'EX-G WIRED TRACKBALL
    K("BTN_EXTRA"): K("C-q"),
}, "Gvim")

# Keybindings for Browsers
define_keymap(re.compile("Firefox|firefox|Google-chrome|Chromium|LibreWolf"), {
    K("C-right"): K("C-TAB"),
    K("C-left"): K("C-Shift-TAB"),
}, "Browsers")

# Affects all apps
define_keymap(lambda wm_class: wm_class not in ("AnAppThatDoesNotExist"), {

    # KDE neon launch apps
    K("RShift-T"): [launch(["konsole"])],
    K("RShift-V"): [launch(["nvim-qt"])],
    K("RShift-X"): [launch(["xkill"])],
    K("RShift-F"): [launch(["dolphin"])],
    K("RShift-W"): [launch(["firefox","-new-tab","about:newtab"])],
    K("RShift-KEY_1"): [launch(["/opt/1Password/1password","%U"])],

    # ELECOM 'EX-G WIRED TRACKBALL
    K("BTN_EXTRA"): K("C-w"),
    K("BTN_FORWARD"): K("C-f7"),

    # Kinesis Advantage
    K("HOME"): K("C-f9"),

}, "All apps")
