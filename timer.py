import pygame
from constants import *

class Timer(pygame.font.Font):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__("fonts/Retro Gaming.ttf",50,self.containers)
        else:
            super().__init__("fonts/Retro Gaming.ttf",50)
        self.seconds = 0
        self.minutes = 0
        self.ready = self.render(f"Time:{round(self.seconds,2) - (self.minutes * 60)}",True,(200,200,200))
        self.sizes = self.ready.get_size()
        self.position = pygame.Vector2(SCREEN_WIDTH/2 - self.sizes[1]*2,40)
        self.pause = 0
        

    def draw(self,screen):
        screen.blit(self.ready,self.position)
    
    def update(self,dt):
        if self.pause == 1:
            return
        self.seconds += float("{:.2f}".format(dt))
        if self.seconds >= (self.minutes+1) * 60:
            self.minutes += 1
        if self.minutes >= 1:
            self.ready = self.render(f"Time:{self.minutes}:{round(self.seconds - (self.minutes * 60),2)}",True,(200,200,200))
        else:
            self.ready = self.render(f"Time:{round(self.seconds - (self.minutes * 60),2 )}",True,(200,200,200))
       
            