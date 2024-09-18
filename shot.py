import pygame
from circleshape import CircleShape
from player import Player
from constants import *
from enemies.asteroid import Asteroid

class Shot(CircleShape):
    def __init__(self,x,y,radius = SHOT_RADIUS,color = (255,255,255),mode = 0, velocity = pygame.Vector2(0,0)):
        super().__init__(x,y,radius)
        self.color = color
        self.mode = mode
        self.velocity = velocity
    
    def draw(self,screen):
        pygame.draw.circle(surface=screen,color=self.color,radius=self.radius,width=2,center=self.position)

    def update(self,dt):
        self.position += self.velocity * dt

    def CheckCollision(self, entity):
        lst = []
        if pygame.math.Vector2.distance_to(self.position,entity.position) < self.radius + entity.radius:
            if isinstance(entity,Asteroid) and self.mode == 0:
                lst.append(True)
                entity.get_hit()
                self.kill()
                if entity.lifes <= 0:
                    entity.split()
                    lst.append(True)
                    return lst
            if isinstance(entity,Player) and self.mode == 1:
                lst.append(True)
                entity.get_hit()
                self.kill()
                return lst
        lst.append(False)
        return lst
