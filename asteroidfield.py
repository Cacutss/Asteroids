import pygame
import random
from asteroid import Asteroid
from constants import *
random.seed()

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity,timer):
        if random.randint(0,100) < 3:
            x,y = self.set_good_spawn(position.x,position.y,ASTEROID_GIANT_RADIUS)
            asteroid = Asteroid(x,y, ASTEROID_GIANT_RADIUS,5)
            asteroid.velocity = velocity / 2
        x,y = self.set_good_spawn(position.x,position.y,radius)
        asteroid = Asteroid(x,y,radius)
        if random.randint(0,100) + (timer * 0.01) > 90:
            asteroid.velocity = velocity * 5
            asteroid.type = 1
        else:
            asteroid.velocity = velocity 
    
    def set_good_spawn(self,x,y,radius):
        if x >= SCREEN_WIDTH:
            return x + radius,y
        elif x <= SCREEN_WIDTH:
            return x - radius,y
        elif y >= SCREEN_HEIGHT:
            return x,0
        elif y <= SCREEN_HEIGHT:
            return x,y-radius

    def update(self, dt,timer):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity,timer)
