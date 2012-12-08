class Sprite:
    def __init__(self, pos, ang, image, info, sprite_index = 0):
        self.pos = [pos[0], pos[1]]
        self.angle = ang

        self.sprite_index = 0

        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_sprite_coord(self):
        return [
            self.image_center[0]+self.image_size[0]*self.sprite_index,
            self.image_center[1]
            ]


    def draw(self, canvas):
            #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
        canvas.draw_image(self.image,self.get_sprite_coord(),self.image_size,self.pos,self.image_size, self.angle)