import os

import displayio
from adafruit_macropad import MacroPad

from init import init
from macro import Macro
from setup_display import setup_display

# INITIALIZATION -----------------------

macropad = MacroPad()
group = displayio.Group()

# SETUP THE DISPLAY -----------------------

setup_display(macropad, group)

# LOAD MACROS ----------------------------

macros = []
for filename in os.listdir("/macros/"):
    module = __import__("/macros/" + filename[:-3])
    macros.append(Macro(module.config))

# MAIN LOOP ----------------------------

init(macropad, macros, group)
