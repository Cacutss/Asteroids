import pygame

from circleshape import CircleShape

from constants import *

from particles import Particles

import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius,lifes = 0,kind = 0):
        super().__init__(x,y,radius)
        self.timer = 1
        self.type = kind
        self.color = (255,255,255)
        self.width = 2
        self.lifes = lifes
        self.hit = -1

    def draw(self,screen):
        pygame.draw.circle(surface=screen,color=self.color,radius=self.radius,width=self.width,center=self.position)
    
    def update(self,dt):
        match(self.type):
            case 0: 
                self.color = (0,255,0)
            case 1:
                self.color = (255,255,0)
            case 2:
                self.color = (255,0,0)
        if self.hit >= 0:
            self.color = (100,100,100)
        self.position += self.velocity * dt
        self.timer -= dt
        self.hit -= dt

    def get_hit(self):
        self.hit = 0.4
        self.lifes -= 1

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(20,50))
            velocity2 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(-20,-50))
            new_radius = self.radius / 2 
            new1 = Asteroid(self.position[0],self.position[1],new_radius,kind=self.type)
            new2 = Asteroid(self.position[0],self.position[1],new_radius,kind=self.type)
            if self.type == 1:
                new1.velocity = velocity1 * 1.1
                new2.velocity = velocity2 * 1.1
            else:
                new1.velocity = velocity1 * 2
                new2.velocity = velocity2 * 2
        