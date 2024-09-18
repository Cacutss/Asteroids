import pygame

from enemies.asteroid import Asteroid

from constants import *

from particles import Particles

import random

class Fast_Asteroid(Asteroid):
    def __init__(self,x,y,radius,lifes = 0,kind = 1):
        super().__init__(x,y,radius)
        self.timer = 1
        self.type = kind
        self.color = (255,255,255)
        self.width = 2
        self.lifes = lifes
        self.dead = 0
        self.hit = -1
        self.explosion = Particles(self.position[0],self.position[1],self.radius,pygame.image.load("images/explosion.png"))

    def draw(self,screen):
        pygame.draw.circle(surface=screen,color=self.color,radius=self.radius,center=self.position,width=self.width)
        if self.dead == 1:
            self.explosion.draw(screen)

    def update(self,dt):
        if self.dead == 1:
            self.kill()
            self.explosion.kill()
        self.color = (255,255,0)
        if self.hit >= 0:
            self.color = (100,100,100)
        self.position += self.velocity * dt
        self.timer -= dt
        self.hit -= dt


    def split(self):
        self.dead = 1
        sfx = pygame.mixer.Sound("sounds/explosion.mp3")
        sfx.set_volume(float(self.radius / 500))
        sfx.play()
        sfx.fadeout(1000)
        if random.randint(0,200) <= 2:
            shield = sh(self.position[0],self.position[1])
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            velocity1 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(20,50))
            velocity2 = pygame.math.Vector2(self.velocity[0],self.velocity[1]).rotate(random.uniform(-20,-50))
            new_radius = self.radius / 2 
            new1 = Fast_Asteroid(self.position[0],self.position[1],new_radius,kind=self.type)
            new2 = Fast_Asteroid(self.position[0],self.position[1],new_radius,kind=self.type)
            if self.type == 1:
                new1.velocity = velocity1 * 1.1
                new2.velocity = velocity2 * 1.1
            else:
                new1.velocity = velocity1 * 2
                new2.velocity = velocity2 * 2

from items.shield import Shield as sh