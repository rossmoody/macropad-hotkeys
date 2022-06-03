import time

from utils.button import Button
from utils.colors import *


def init(macropad, configs, group):
    last_position = None
    index = 0

    while True:
        if macropad.encoder != last_position:
            index = macropad.encoder % len(configs)
            configs[index].change(group, macropad)
            last_position = macropad.encoder

        event = macropad.keys.events.get()

        if not event or event.key_number >= len(configs[index].macros):
            continue

        button = Button(macropad, event.key_number)
        color = configs[index].macros[event.key_number][0]
        label = configs[index].macros[event.key_number][1]
        action = configs[index].macros[event.key_number][2]

        if event.pressed:
            for item in action:
                if isinstance(item, int):
                    button.press(item)

                elif isinstance(item, float):
                    time.sleep(item)

                elif isinstance(item, str):
                    button.write(item)

                elif isinstance(item, list):
                    for code in item:
                        if isinstance(code, int):
                            macropad.consumer_control.release()
                            macropad.consumer_control.press(code)

                        if isinstance(code, float):
                            time.sleep(code)

                elif isinstance(item, dict):
                    print("Dictionary press")
        else:
            button.reset(color)
            button.release_everything()

    