import time


def init(macropad, apps, group):
  last_position = None
  app_index = 0
  apps[app_index].switch(group, macropad)

  while True:
      encoder_position = macropad.encoder

      if encoder_position != last_position:
          app_index = encoder_position % len(apps)
          apps[app_index].switch(group, macropad)
          last_position = encoder_position

      event = macropad.keys.events.get()
      if not event or event.key_number >= len(apps[app_index].macros):
          continue
      key_number = event.key_number
      pressed = event.pressed
      sequence = apps[app_index].macros[key_number][2]

      if pressed:
          if key_number < 12:
              macropad.pixels[key_number] = 0xFFFFFF
              macropad.pixels.show()
          for item in sequence:
              if isinstance(item, int):
                  if item >= 0:
                      macropad.keyboard.press(item)
                  else:
                      macropad.keyboard.release(-item)
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
                  if "buttons" in item:
                      if item["buttons"] >= 0:
                          macropad.mouse.press(item["buttons"])
                      else:
                          macropad.mouse.release(-item["buttons"])
                  macropad.mouse.move(
                      item["x"] if "x" in item else 0,
                      item["y"] if "y" in item else 0,
                      item["wheel"] if "wheel" in item else 0,
                  )
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
                  if item >= 0:
                      macropad.keyboard.release(item)
              elif isinstance(item, dict):
                  if "buttons" in item:
                      if item["buttons"] >= 0:
                          macropad.mouse.release(item["buttons"])
                  elif "tone" in item:
                      macropad.stop_tone()
          macropad.consumer_control.release()
          if key_number < 12:  # No pixel for encoder button
              macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
              macropad.pixels.show()
