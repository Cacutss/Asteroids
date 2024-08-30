import pygame
from constants import *

class Particles(pygame.sprite.Sprite):
    def __init__(self,x,y,radius,image):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x,y)
        self.size = radius * 2
        self.timer = 0.5
        self.image = image

    def draw(self,screen:pygame.surface.Surface):
        image = pygame.transform.scale(self.image,((self.size * 2) * self.timer,(self.size * 2) * self.timer)) 
        screen.blit(image,(self.position[0] - int(image.get_width()) / 2, self.position[1] - int(image.get_height()) / 2))

    def update(self,dt):
        if self.timer <= 0.1:
            self.kill()
            return
        self.timer -= dt
