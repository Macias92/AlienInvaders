import pygame


class Settings:
    """Class which stores all game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1680
        self.screen_height = 1000
        self.ship_speed = 3.5
        self.bg = pygame.image.load('images/space_background.png')

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 1

