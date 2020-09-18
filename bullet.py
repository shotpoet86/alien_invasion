import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """controls bullets fired from ship"""


def __init__(self, ai_game):
    """creates bullet object at the ships current position"""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color
    # creates bullet rect at 0,0 then sets correct position
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                            self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop
    self.y = float(self.rect.y)


def update(self):
    """moves bullets up screen"""
    # updates decimal position of bullet
    self.y -= self.settings.bullet_speed
    # updates rect position
    self.rect.y = self.y


def draw_bullet(self):
    """draws bullet to screen"""
    pygame.draw.rect(self.screen, self.color, self.rect)
