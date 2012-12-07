from _Newtonian import *
from _Sprite import *
from _Helpers import *
import math
from _Globals import *

# Ship class
class Ship(Newtonian,Sprite):
    def __init__(self, pos, vel, angle, image, info):
        Sprite.__init__(self,pos,angle,image,info)
        Newtonian.__init__(self,pos,vel,angle,0)

        self.thrust = 0
        self.angle_thrust = 0

        #controls how fast the ship will spin
        self.angle_velocity_factor = 5* math.pi / 180

        #acceleration in pixels per frame per frame
        self.thrust_factor = 3

        #we want the ship to slow down eventually
        self.friction_factor = 0.99

    def draw(self, canvas):
        if self.thrust:
            self.sprite_index = 1
        else:
            self.sprite_index = 0

        #need this to be a copy not just reference
        origpos = [self.pos[0],self.pos[1]]

        #draw center sprite
        Sprite.draw(self,canvas)

        #draw right sprite
        self.pos[0] = origpos[0]+width
        Sprite.draw(self,canvas)

        #draw left sprite
        self.pos[0] = origpos[0]-width
        Sprite.draw(self,canvas)

        #reset x position
        self.pos[0] = origpos[0]

        #draw upper sprite
        self.pos[1] = origpos[1]+height
        Sprite.draw(self,canvas)

        #draw lower sprite
        self.pos[1] = origpos[1]-height
        Sprite.draw(self,canvas)

        #reset y position
        self.pos[1] = origpos[1]

    def update(self,time):
        if self.lastUpdate != -1:
            deltaT = time - self.lastUpdate

            #bound position to mod width/height
            self.pos = [
                self.pos[0] % width,
                self.pos[1] % height
            ]

            #update angular velocity
            self.angle_vel = self.angle_thrust * self.angle_velocity_factor

            #direction vector of the ship
            dir_vec = angle_to_vector(self.angle)

            #scale acceleration by the inverse of the velocity so that we have an effective maximum speed
            absolute_vel = dist(self.vel, [0,0])
            e = 2.71828182846
            scale_factor = e**(-absolute_vel)

            #update velocity
            self.vel = [
                self.vel[0] + scale_factor*self.thrust*dir_vec[0]*self.thrust_factor*deltaT,
                self.vel[1] + scale_factor*self.thrust*dir_vec[1]*self.thrust_factor*deltaT
            ]

            Newtonian.update(self,time)
        self.lastUpdate = time
