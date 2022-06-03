from utils.colors import *


class Button:

  def __init__(self, macropad, key_number):
    self.macropad = macropad
    self.key_number = key_number
  
  def highlight(self):
    self.macropad.start_tone(262)
    self.macropad.pixels[self.key_number] = WHITE
  
  def reset(self, color):
    self.macropad.stop_tone()
    self.macropad.pixels[self.key_number] = color or WHITE
    self.macropad.pixels.show()

  def press(self, item):
    self.highlight()
    self.macropad.keyboard.press(item)
  
  def write(self, item):
    self.highlight()
    self.macropad.keyboard_layout.write(item)
  
  def release(self, item):
    self.macropad.keyboard.release(item)

  def release_everything(self):
    self.macropad.keyboard.release_all()
    self.macropad.consumer_control.release()
    self.macropad.mouse.release_all()
    self.macropad.stop_tone()
    self.macropad.pixels.show()
    self.macropad.display.refresh()
