import pygame

class Score(pygame.font.Font):
    def __init__(self):
        super().__init__("fonts/Retro Gaming.ttf",100)
        self.points = 0
    
    def draw(self):
        return self.render(f"{self.points}",True,(100,100,100))