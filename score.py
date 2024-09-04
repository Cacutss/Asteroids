import pygame
from constants import *
from asteroid import Asteroid

class Score(pygame.font.Font):
    def __init__(self):
        super().__init__("fonts/Retro Gaming.ttf",100)
        self.points = 0
        self.cache = 0
    
    def draw(self):
        return self.render(f"{self.points}",True,(100,100,100))
    
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