import os

import displayio
from adafruit_macropad import MacroPad

from app import App
from display import setup
from main_loop import init

MACRO_FOLDER = "/macros/"


# INITIALIZATION -----------------------

macropad = MacroPad()
group = displayio.Group()
apps = []

# SETUP THE DISPLAY -----------------------

setup(macropad, group)

# LOAD MACROS ----------------------------

for filename in os.listdir(MACRO_FOLDER):
    module = __import__(MACRO_FOLDER + filename[:-3])
    app = App(module.app)
    apps.append(app)

# MAIN LOOP ----------------------------

init(macropad, apps, group)
