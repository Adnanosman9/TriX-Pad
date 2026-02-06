import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.pegasus_oled import PegasusOLED

pad = KMKKeyboard()
pad.row_pins = (board.D2, board.D4, board.D3)
pad.col_pins = (board.D10, board.D8, board.D9)

pad.diode_orientation = DiodeOrientation.ROW2COL
oled_ext = PegasusOLED(
    i2c_device=board.I2C(),
    width=128,
    height=32,
)
pad.extensions.append(oled_ext)

pad.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
    ]
]

if __name__ == '__main__':
    pad.go()