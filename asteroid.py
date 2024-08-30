import pygame

from circleshape import CircleShape

from constants import *

from particles import Particles

import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(surface=screen,color=(255,255,255),radius=self.radius,width=2,center=self.position)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(20,50))
            velocity2 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(-20,-50))
            new_radius = self.radius / 2 
            new1 = Asteroid(self.position[0],self.position[1],new_radius)
            new2 = Asteroid(self.position[0],self.position[1],new_radius)
            new1.velocity = velocity1 * 2
            new2.velocity = velocity2 * 2
        