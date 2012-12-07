from _Newtonian import *
from _Sprite import *

# Sprite class
class Entity(Newtonian,Sprite):
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.sound = sound
        self.age = 0

        Sprite.__init__(self, pos, ang, image, info)
        Newtonian.__init__(self,pos,vel,ang,ang_vel)

    def doSound(self):
        if self.sound:
            self.sound.rewind()
            self.sound.play()

    def draw(self,canvas):
        if not self.age > self.lifespan:
            Sprite.draw(self,canvas)


    def update(self,time):
        self.age += time - self.lastUpdate
        Newtonian.update(self,time)
