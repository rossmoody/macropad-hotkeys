import os

import displayio
from adafruit_macropad import MacroPad

from config import Config
from init import init
from setup_display import setup_display

# INITIALIZATION -----------------------

macropad = MacroPad()
group = displayio.Group()

# SETUP THE DISPLAY -----------------------

setup_display(macropad, group)

# LOAD MACROS ----------------------------

configs = []

for filename in os.listdir("/macros/"):
    module = __import__("/macros/" + filename[:-3])
    configs.append(Config(module.config))

configs[0].change(group, macropad)

# MAIN LOOP ----------------------------

init(macropad, configs, group)
