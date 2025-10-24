from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

from kmk.extensions.lock_status import LockStatus

import board
import digitalio

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.extensions.append(LockStatus())

keyboard.row_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4]
keyboard.col_pins = [
    board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP17, board.GP18
]

keyboard.keymap = [
    [KC.ESC, KC.ONE, KC.TWO, KC.THREE, KC.FOUR, KC.FIVE, KC.SIX, KC.SEVEN, KC.EIGHT, KC.NINE, KC.ZERO, KC.MINUS, KC.EQUAL, KC.BSPC],
    [KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRACKET, KC.RBRACKET, KC.BSLS],
    [KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT],
    [KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT],
    [KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL]
]

if __name__ == '__main__':
    keyboard.go()
