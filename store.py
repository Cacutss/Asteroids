import pygame
from constants import *
import sys
sys.path.insert(0,"items")

class Store(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.position = pygame.Vector2(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.screen = pygame.surface.Surface(self.position)
        self.items = []
    
    def draw(self,screen):
        self.screen.blit(screen,(200,200,200,200))
    
    def add_items(self):
        pass