import simplegui
from z_init import *
from Missile import *

def key_down_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_thrust += -1
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_thrust += 1
    elif key == simplegui.KEY_MAP["up"]:
        ship_thrust_sound.rewind()
        ship_thrust_sound.play()
        my_ship.thrust += 1
    elif key == simplegui.KEY_MAP["space"]:
        shoot()


def key_up_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_thrust -= -1
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_thrust -= 1
    elif key == simplegui.KEY_MAP["up"]:
        ship_thrust_sound.pause()
        my_ship.thrust -= 1