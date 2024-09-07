import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from particles import Particles
from boss import Boss
from timer import Timer
from store import Store
from wrapper import wrap
import sys
import random

def main():
    global loop
    loop = True
    global store_state
    store_state = False
    pygame.mixer.pre_init()
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(64)
    game_timer = Timer()
    clock = pygame.time.Clock()
    dt = 0
    score = Score()
    hearth = pygame.transform.scale(pygame.image.load("images/hearth.png"),(100,100))
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    wrappable = pygame.sprite.Group()
    bosses = pygame.sprite.Group()
    Player.containers = (drawable,updatable,wrappable)
    Asteroid.containers = (drawable,updatable,asteroids,wrappable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)
    Particles.containers = (drawable,updatable)
    Boss.containers = (drawable,updatable,bosses,asteroids)
    Timer.containers = (drawable,updatable)
    Score.containers = (drawable)
    field = AsteroidField()
    player = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN)
    while(loop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if store_state:
            game_timer.pause = 1
        else:
            game_timer.pause = 0
        pygame.Surface.fill(screen,(15,15,15))
        if player.lives == 0:
            print("!GAME OVER!")
            quit()
            sys.exit()
        game_timer.update(dt)
        game_timer.draw(screen)
        update(updatable,dt,game_timer)
        score.draw(screen)
        draw(drawable,screen)
        for thing in wrappable:
            wrap(thing)
        for i in range(0,player.lives):
            screen.blit(hearth,(i*100,0,0,0))
        for asteroid in asteroids:
            if store_state:
                asteroid.kill()
            if not player.CheckCollision(asteroid) and player.iframes <= 0:
                player.get_hit()
                player.tackle()
            for shot in shots:
                if shot.CheckCollision(asteroid):
                    if asteroid.lifes >= 1:
                        asteroid.get_hit()
                        shot.kill()
                    else:
                        score.update(asteroid)
                        shot.kill()
                        asteroid.split(screen)
        pygame.display.flip()
        dt = (clock.tick(60)) / 1000

def draw(drawable,screen):
    for thing in drawable:
        thing.draw(screen)

def update(updatable,dt,timer):
     for thing in updatable:
        if isinstance(thing,AsteroidField):
            if store_state:
                continue
            thing.update(dt,timer.seconds)
        else:
            thing.update(dt)

if __name__ == "__main__":
    main()