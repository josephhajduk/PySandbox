class Newtonian:
    def __init__(self, pos, vel, ang, ang_vel):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel

        # this should be < 1,  every frame we will do vel * friction_factor
        self.friction_factor = 1

        self.lastUpdate = -1

    def update(self,time):
        if self.lastUpdate != -1:

            deltaT = time - self.lastUpdate

            #friction
            self.vel = [
                self.vel[0] * self.friction_factor**deltaT,
                self.vel[1] * self.friction_factor**deltaT,
            ]

            #velocity is in pixels per frame
            self.pos = [
                self.pos[0] + self.vel[0] * deltaT,
                self.pos[1] + self.vel[1] * deltaT
            ]

            #angel_vel is in unit angle per frame
            self.angle += self.angle_vel * deltaT

        self.lastUpdate = time