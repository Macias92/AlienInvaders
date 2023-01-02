import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class intended for manage a ship"""

    def __init__(self, ai_game):
        """Initialize ship and its location on the screen"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rectangle:
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Every new ship appears at the bottom of the screen:
        self.rect.midbottom = self.screen_rect.midbottom

        # Horizontal placing of the ship is stored in float type
        self.x = float(self.rect.x)

        # option related to moving a ship, default is False
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's location based on his move option"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object based on self.x
        self.rect.x = self.x

    def blitme(self):
        """Displaying ship in its actual location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
