import time

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

        key_number = event.key_number
        sequence = configs[index].macros[key_number][2]

        if event.pressed:
            macropad.pixels[key_number] = WHITE
                
            for item in sequence:
                if isinstance(item, int):
                    macropad.keyboard.press(item)

                elif isinstance(item, float):
                    time.sleep(item)

                elif isinstance(item, str):
                    macropad.keyboard_layout.write(item)

                elif isinstance(item, list):
                    for code in item:
                        if isinstance(code, int):
                            macropad.consumer_control.release()
                            macropad.consumer_control.press(code)

                        if isinstance(code, float):
                            time.sleep(code)

                elif isinstance(item, dict):
                    if "tone" in item:
                        if item["tone"] > 0:
                            macropad.stop_tone()
                            macropad.start_tone(item["tone"])
                        else:
                            macropad.stop_tone()
                    
                    elif "play" in item:
                        macropad.play_file(item["play"])
        else:
            for item in sequence:
                if isinstance(item, int):
                    macropad.keyboard.release(item)
                
                elif isinstance(item, dict):
                    if "buttons" in item:
                        if item["buttons"] >= 0:
                            macropad.mouse.release(item["buttons"])
                    
                    elif "tone" in item:
                        macropad.stop_tone()

            macropad.consumer_control.release()

            # Reset the key color
            if key_number < 12: 
                macropad.pixels[key_number] = configs[index].macros[key_number][0]
                macropad.pixels.show()

    