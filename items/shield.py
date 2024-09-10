import pygame
from circleshape import CircleShape
from asteroid import Asteroid
from constants import *

class Shield(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,66)
        self.timer = 5
        self.image = pygame.image.load("images/shield.png")
        self.size = 100
        self.acquired = 0
        self.timer = 5
        self.color = (50,50,50)
        self.copies = 0
    
    def draw(self,screen):
        if self.acquired < 1:
            image = pygame.transform.scale(self.image,(self.size,self.size)) 
            screen.blit(image,(self.position[0] - int(image.get_width()) / 2, self.position[1] - int(image.get_height()) / 2))
        else:
            if self.timer >= 0.5:
                pygame.draw.circle(screen,self.color,center=self.position,radius=self.radius,width=3)
    
    def CheckCollision(self,entity:Asteroid,screen):
        if super().CheckCollision(entity):
            if entity.lifes > 0:
                entity.get_hit()
            else:
                entity.split(screen)
                return True
            
    def acquire(self):
        self.radius = SHIELD_RADIUS
        self.timer = 5

    def update(self,dt):
        if self.acquired == 1:
            self.timer -= dt
            self.color = (int(50*self.timer),int(50*self.timer),int(50*self.timer))
            if self.timer <= 0:
                self.kill()
        