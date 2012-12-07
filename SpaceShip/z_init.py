import simplegui
from y_main import *
from Entity import *
from Ship import *
from Control import *

# initialize frame
frame = simplegui.create_frame("Asteroids", width, height)

# initialize ship and two sprites
my_ship = Ship([width / 2, height / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Entity([width / 3, height / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Entity([2 * width / 3, 2 * height / 3], [-1, 1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()