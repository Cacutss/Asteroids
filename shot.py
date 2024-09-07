import pygame
from circleshape import CircleShape
from constants import *
from asteroid import Asteroid

class Shot(CircleShape):
    def __init__(self,x,y,radius = SHOT_RADIUS):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(surface=screen,color=(255,255,255),radius=self.radius,width=2,center=self.position)

    def update(self,dt):
        self.position += self.velocity * dt
    