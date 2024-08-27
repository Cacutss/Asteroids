import pygame

class Score(pygame.font.Font):
    def __init__(self):
        super().__init__(None,200)
        self.points = 0
    
    def draw(self):
        self.render(text=self.points,color=(100,100,100))