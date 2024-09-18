import pygame
from constants import *
from enemies.asteroid import Asteroid

class Score(pygame.font.Font):
    def __init__(self):
        if hasattr(self,"containers"):
            super().__init__("fonts/Retro Gaming.ttf",50,self.containers)
        else:
            super().__init__("fonts/Retro Gaming.ttf",50)
        self.points = 0
        self.cache = 0
    
    def draw(self,screen):
        points = self.render(f"${self.points}",True,(100,100,100))
        psize = points.get_size()
        screen.blit(points,(SCREEN_WIDTH - psize[0],0))
    
    def update(self,asteroid:Asteroid):
        if asteroid.radius <= ASTEROID_MIN_RADIUS:
            self.cache = 1
        elif asteroid.radius >= ASTEROID_MIN_RADIUS and asteroid.radius <= ASTEROID_MIN_RADIUS * 2:
            self.cache = 3
        elif asteroid.radius >= ASTEROID_MIN_RADIUS * 2 and asteroid.radius <= ASTEROID_MAX_RADIUS:
            self.cache = 5
        elif asteroid.radius == ASTEROID_GIANT_RADIUS:
            self.cache = 25
        elif asteroid.radius >= ASTEROID_GIANT_RADIUS:
            self.cache == 100
        if asteroid.type == 0:
            self.points += self.cache
            self.cache = 0
            return
        elif asteroid.type == 1:
            self.points += self.cache * 2
            self.cache = 0
            return
        elif asteroid.type == 2:
            self.points += self.cache * 3
            self.cache = 0
            return