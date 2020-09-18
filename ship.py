import pygame


class Ship:
    # manages ship
    def __init__(self, ai_game):
        # initializes ship and its start point
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # loads ship image and gets its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        # starts each new ship at bottom center of window
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draws ship at current location
        self.screen.blit(self.image, self.rect)
