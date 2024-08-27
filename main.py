import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable,updatable)
    Asteroid.containers = (drawable,updatable,asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if asteroid.CheckCollision(player):
                print("!GAME OVER!")
                exit()
            for shot in shots:
                if shot.CheckCollision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()