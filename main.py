import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    dt = 0
    score = Score()
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
        points = score.render(f"{score.points}",True,(100,100,100))
        screen.blit(points,(SCREEN_WIDTH - score.get_height(),0))
        if player.lives == 0:
            print("!GAME OVER!")
            exit()
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for i in range(0,player.lives):
            screen.blit(pygame.font.Font(None,150).render(f"\n",True,(200,200,200)),(i*50,0))
        for asteroid in asteroids:
            if asteroid.CheckCollision(player) and player.iframes <= 0:
                player.get_hit()
            for shot in shots:
                if shot.CheckCollision(asteroid):
                    score.points += 1
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

if __name__ == "__main__":
    main()