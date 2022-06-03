class Config:
    def __init__(self, config):
        self.name = config["name"]
        self.macros = config["macros"]

    def change(self, group, macropad):
        group[13].text = self.name

        for i in range(12):
            if i < len(self.macros):
                macropad.pixels[i] = self.macros[i][0]
                group[i].text = self.macros[i][1]
            else:
                macropad.pixels[i] = 0
                group[i].text = ""

        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.stop_tone()
        macropad.pixels.show()
        macropad.display.refresh()
