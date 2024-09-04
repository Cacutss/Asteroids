import pygame
from constants import *
from asteroid import Asteroid

class Boss(Asteroid):
    def __init__(self,x = SCREEN_WIDTH/2, y = -SCREEN_WIDTH/2, radius = SCREEN_WIDTH/2, lifes = 100,color = (240,0,0),type=2):
        super().__init__(x,y,radius,lifes,kind=2)
        self.speed = 20
        self.width = 2

    def draw(self,screen):
        super().draw(screen)

    def update(self,dt):
        self.position[1] += self.speed *dt
        super().update(dt)
     