import pygame
from constants import *
from player import Player

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()