from x_Assets import *
from _Globals import *
from z_init import *
import random

def draw(canvas):
    global time

    # animate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [width / 2, height / 2],
        [width, height])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]],
        [width / 2 + 1.25 * wtime, height / 2], [width - 2.5 * wtime, height])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]],
        [1.25 * wtime, height / 2], [2.5 * wtime, height])

    #draw lives
    canvas.draw_text("Lives: 03", (10, 20), 12, "Red")

    #draw score
    canvas.draw_text("Score: 9000", [width - 85, 20], 12, "Red")

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)

    # update ship and sprites
    my_ship.update(time)
    a_rock.update(time)
    a_missile.update(time)

# timer handler that spawns a rock    
def rock_spawner():
    a_rock.pos = [random.randint(0,width),random.randint(0,height)]
    a_rock.angle = random.randint(0,2*math.pi//1)
    a_rock.angle_vel = random.randint(-10,10) * math.pi / 180
    a_rock.vel = scale(angle_to_vector(a_rock.angle),random.randint(1,5))
