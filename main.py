import pygame
from constants import *
from player import Player
from enemies.asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score
from particles import Particles
from enemies.boss import Boss
from timer import Timer
from store import Store
from items.shield import Shield
from wrapper import wrap
import sys
import random

class Game:
    def __init__(self):
        self.gameStateManager = GameStateManager('level')
        self.statebefore = self.gameStateManager.get_state()
        self.loop = True
        self.timer = Timer()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.dt = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN,pygame.SCALED)
        Game.drawable = pygame.sprite.Group()
        Game.updatable = pygame.sprite.Group()
        Game.asteroids = pygame.sprite.Group()
        Game.wrappable = pygame.sprite.Group()
        Game.bosses = pygame.sprite.Group()
        Game.shots = pygame.sprite.Group()
        Game.items = pygame.sprite.Group()
        Shield.containers = (Game.drawable,Game.updatable,Game.items)
        AsteroidField.containers = (Game.updatable)
        Player.containers = (Game.drawable,Game.updatable,Game.wrappable)
        Asteroid.containers = (Game.drawable,Game.updatable,Game.asteroids,Game.wrappable)
        Particles.containers = (Game.drawable,Game.updatable)
        Boss.containers = (Game.drawable,Game.updatable,Game.bosses,Game.asteroids)
        Timer.containers = (Game.drawable,Game.updatable)
        Shot.containers = (Game.updatable,Game.drawable,Game.shots)
        self.level = Level(self.screen,self.gameStateManager)
        self.menu = Menu(self.screen,self.gameStateManager)
        self.states = {'level':self.level, "menu":self.menu}
    
    def run(self):
        while(self.loop):
            self.dt = self.clock.tick(self.fps)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if self.gameStateManager.get_state() == "menu":
                            self.gameStateManager.currentState = self.statebefore
                        else:
                            self.statebefore = self.gameStateManager.get_state()
                            self.gameStateManager.currentState = "menu"
            pygame.Surface.fill(self.screen,(15, 15, 15))
            self.states[self.gameStateManager.get_state()].run()
            if not self.gameStateManager.get_state() == "menu":
                for thing in self.wrappable:
                    wrap(thing)
                self.update()
                self.draw()
                self.timer.update(self.dt)
                self.timer.draw(self.screen)
            pygame.display.flip()
    def draw(self):
        for thing in self.drawable:
            thing.draw(self.screen)

    def update(self):
        for thing in self.updatable:
            if isinstance(thing,AsteroidField):
                thing.update(self.dt,self.timer.seconds)
            else:
                thing.update(self.dt)

class Level:
    def __init__(self,screen,gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.score = Score()
        self.hearth = pygame.transform.scale(pygame.image.load("images/hearth.png"),(100,100))
        self.spawner = AsteroidField()
        self.player = Player(x = SCREEN_WIDTH/2,y = SCREEN_HEIGHT/2)

    def run(self):
        if self.player.lives <= 0:
            print("!GAME OVER!")
            quit()
            sys.exit()
        self.score.draw(self.screen)
        for i in range(0,self.player.lives):
            self.screen.blit(self.hearth,(i*100,0,0,0))
        for item in Game.items:
            if not self.player.CheckCollision(item) and item.acquired == 0:
                self.player.acquire(item)
        for asteroid in Game.asteroids:
            if not self.player.CheckCollision(asteroid) and self.player.iframes <= 0:
                self.player.get_hit()
                self.player.tackle()
            for item in self.player.items:
                if not isinstance(item,Shield) or len(item.groups()) == 0:
                    continue
                if item.CheckCollision(asteroid):
                    self.score.update(asteroid)
            for shot in Game.shots:
                if all(shot.CheckCollision(asteroid)):
                    self.score.update(asteroid)
                shot.CheckCollision(self.player)
class Menu:
    def __init__(self,screen,gameStateManager):
        self.screen = screen
        self.gameStateManager = gameStateManager
        self.font = pygame.font.Font("fonts/Retro Gaming.ttf",60)
        self.title = "Asteroids"
    
    def run(self):
        self.draw_text(screen=self.screen,text=self.title,x=(SCREEN_WIDTH/2),y=(SCREEN_HEIGHT/5))

    def draw_text(self,screen,text,x,y):
        button = self.font.render(text,True,(255,255,255))
        screen.blit(button,(x - button.get_width()/2,y - button.get_height()))

class GameStateManager:
    def __init__(self,currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    
def main():
    pygame.mixer.pre_init()
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(64)
    game = Game()
    game.run()

if __name__ == "__main__":
    main()