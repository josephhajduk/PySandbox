import simplegui
from z_init import *
from Missile import *

def key_down_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel += -1
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel += 1
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    elif key == simplegui.KEY_MAP["space"]:
        shoot()

    print my_ship.angle_vel, my_ship.thrust


def key_up_handler(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel -= -1
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel -= 1
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False

    print my_ship.angle_vel, my_ship.thrust