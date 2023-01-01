import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class showing alien spaceship"""

    """Initialize new alien obcject"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Put new alien on top left cornet of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

