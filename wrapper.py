from asteroid import Asteroid
from constants import *
import random
random.seed()
def wrap(thing):
    lucky = 2
    if isinstance(thing,Asteroid):
        if thing.timer <= 0:
            lucky = random.randint(0,20)
        else:
            return
    if thing.position[0]-(thing.radius*2) >= SCREEN_WIDTH:
        if lucky <= 3:
            thing.position[0] = 0 - thing.radius
        else:
            thing.kill()
        return
    if thing.position[0]+(thing.radius*2) <= 0:
        if lucky <= 3:
            thing.position[0] = SCREEN_WIDTH + thing.radius
        else:
            thing.kill()
        return
    if thing.position[1]-(thing.radius*2) >= SCREEN_HEIGHT:
        if lucky <= 3:
            thing.position[1] = 0 - thing.radius
        else:
            thing.kill()
        return
    if thing.position[1]+(thing.radius*2) <= 0:
        if lucky <= 3:
            thing.position[1] = SCREEN_HEIGHT + thing.radius
        else:
            thing.kill()
        return
