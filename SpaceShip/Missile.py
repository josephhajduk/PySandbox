from z_init import *

def shoot():
    a_missile.pos = add_vec(my_ship.pos,scale(angle_to_vector(my_ship.angle),my_ship.radius+5))
    a_missile.angle = my_ship.angle
    a_missile.vel = add_vec(my_ship.vel,scale(angle_to_vector(a_missile.angle),15))
    a_missile.age = 0
    a_missile.doSound()
