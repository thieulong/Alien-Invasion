import pygame
from pygame.sprite import Sprite
import game_stats

class Alien(Sprite):

    def __init__(self, ai_game):

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        level = int(self.stats.level)

        if level % 10 == 1:
            self.image = pygame.image.load('images/ufo1.bmp')
        elif level % 10 == 2:
            self.image = pygame.image.load('images/ufo2.bmp')
        elif level % 10 == 3:
            self.image = pygame.image.load('images/ufo3.bmp')
        elif level % 10 == 4:
            self.image = pygame.image.load('images/ufo4.bmp')
        elif level % 10 == 5:
            self.image = pygame.image.load('images/ufo5.bmp')
        elif level % 10 == 6:
            self.image = pygame.image.load('images/ufo6.bmp')
        elif level % 10 == 7:
            self.image = pygame.image.load('images/ufo7.bmp')
        elif level % 10 == 8:
            self.image = pygame.image.load('images/ufo8.bmp')
        elif level % 10 == 9:
            self.image = pygame.image.load('images/ufo9.bmp')
        elif level % 10 == 0:
            self.image = pygame.image.load('images/ufo10.bmp')

        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self):

        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
