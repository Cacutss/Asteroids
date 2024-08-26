import pygame

from circleshape import CircleShape

from constants import *

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(surface=screen,color=(255,255,255),points=self.triangle(),width=2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.move(-abs(dt))
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_a]:
            self.rotate(-abs(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)    
    
    def move(self,dt):
        vector = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += vector * PLAYER_SPEED * dt