import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label

from utils.colors import *


def setup_display(macropad, group):
    for key_index in range(12):
        x = key_index % 3
        y = key_index // 3

        group.append(
            label.Label(
                terminalio.FONT,
                text = "",
                color = WHITE,
                anchored_position = (
                    (macropad.display.width - 1) * x / 2,
                    macropad.display.height - 1 - (3 - y) * 12,
                ),
                anchor_point=(x / 2, 1.0),
            )
        )

    group.append(Rect(BLACK, BLACK, macropad.display.width, 12, fill=WHITE))

    group.append(
        label.Label(
            terminalio.FONT,
            text="",
            color=BLACK,
            anchored_position=(macropad.display.width // 2, -2),
            anchor_point=(0.5, 0.0),
        )
    )

    macropad.display.show(group)
