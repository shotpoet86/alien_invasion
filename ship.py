import pygame


class Ship:
    # manages ship
    def __init__(self, ai_game):
        # initializes ship and its start point
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # loads ship image and gets its rect
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()

        # starts each new ship at bottom center of window
        self.rect.midbottom = self.screen_rect.midbottom

        # stores ships horizontal decimal value position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ship position based on movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        # draws ship at current location
        self.screen.blit(self.image, self.rect)
