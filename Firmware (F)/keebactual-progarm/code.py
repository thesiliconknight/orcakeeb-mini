print("Waking up the keeb...")

import board
import busio
import sys

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

orcakeeb_hw = KMKKeyboard()

# rp2040 gpio matrix pins
orcakeeb_hw.col_pins = (board.GP28, board.GP27, board.GP26, board.GP1)
orcakeeb_hw.row_pins = (board.GP5, board.GP6, board.GP7, board.GP8)
orcakeeb_hw.diode_orientation = DiodeOrientation.COL2ROW

# encoder logic
media_encoder_sys = EncoderHandler()
media_encoder_sys.pins = ((board.GP3, board.GP2, board.GP4, False),)
media_encoder_sys.map = [ ((KC.VOLD, KC.VOLU, KC.MUTE),) ]
orcakeeb_hw.modules.append(media_encoder_sys)

# rgb logic (all 16 of em)
sk6812_matrix_leds = RGB(pixel_pin=board.GP14, num_pixels=16, val_limit=100, val_default=20)
orcakeeb_hw.extensions.append(sk6812_matrix_leds)

try:
    i2c0_bus = busio.I2C(board.GP9, board.GP10)
    oled_driver_ic = SSD1306(i2c=i2c0_bus, device_address=0x3C)
    
    status_display_ui = Display(
        display=oled_driver_ic,
        entries=[
            TextEntry(text="ORCAKEEB", x=0, y=0, y_anchor="T"),
            TextEntry(text="NUMPAD", x=0, y=10, y_anchor="T"),
        ],
        width=128, height=32
    )
    orcakeeb_hw.extensions.append(status_display_ui)
    
except ValueError as pin_err:
    print("Hardware Error: I2C pins in use or missing pull-ups ->", pin_err)
except RuntimeError as i2c_err:
    print("Hardware Error: SSD1306 not detected at address 0x3C ->", i2c_err)
except Exception as e:
    print("bro i think you forogot the oled")
    print("oopse woopsie smthin wrong", e)
    if hasattr(sys, 'print_exception'):
        sys.print_exception(e)

# numpad mapping?
orcakeeb_hw.keymap = [
    [
        KC.KP_7, KC.KP_8,   KC.KP_9,     KC.KP_SLASH,
        KC.KP_4, KC.KP_5,   KC.KP_6,     KC.KP_ASTERISK,
        KC.KP_1, KC.KP_2,   KC.KP_3,     KC.KP_MINUS,
        KC.KP_0, KC.KP_DOT, KC.KP_ENTER, KC.KP_PLUS,
    ]
]

if __name__ == '__main__':
    orcakeeb_hw.go()
