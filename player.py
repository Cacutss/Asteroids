import pygame

from circleshape import CircleShape

from shot import Shot

from constants import *

import random

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.position = pygame.Vector2(x,y)
        self.acceleration = PLAYER_ACCELERATION
        self.rotation = 0
        self.timer = 0
        self.iframes = 0
        self.lives = 3
        self.hit = 0
        self.hitbox = self.triangle()
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        if self.hit == 1 and random.randint(0,10) > 5:
            pygame.draw.polygon(surface=screen,color=(10,10,10),points=self.triangle(),width=2)
        else:
            pygame.draw.polygon(surface=screen,color=(255,255,255),points=self.triangle(),width=2)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def CheckCollision(self, entity):
        lista = []
        for i in range(0,len(self.hitbox)):
            if pygame.math.Vector2.distance_to(self.hitbox[i],entity.position) < entity.radius - 2:
                lista.append(True)
            else:
                lista.append(False)
        if not any(lista):
            return True
        return False

    def update(self, dt):
        self.hitbox = self.triangle()
        self.timer -= dt
        self.iframes -= dt
        if self.iframes > 0:
            self.hit = 1
        else:
            self.hit = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.move(-abs(dt))
        if keys[pygame.K_w]:
            self.move(dt)
        else:
            self.acceleration = PLAYER_ACCELERATION
        if keys[pygame.K_a]:
            self.rotate(-abs(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
    
    def move(self,dt):
        movement = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += (movement * PLAYER_SPEED * dt) * self.acceleration
        if self.acceleration > PLAYER_MAX_ACCELERATION:
            return
        else:  
            self.acceleration += 0.001 

    def shoot(self):
        shot = Shot(self.position[0],self.position[1])
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def get_hit(self):
        self.lives -= 1
        self.acceleration = 0.5
        self.iframes = PLAYER_FRAMES
