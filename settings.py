import pygame


class Settings:
    """Class which stores all game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1680
        self.screen_height = 1000
        # self.bg_color = (10, 10, 60)
        self.ship_speed = 5.5
        self.bg = pygame.image.load('images/space_background.png')

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 0)
        self.bullets_allowed = 10

