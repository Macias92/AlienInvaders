import pygame


class Settings:
    """Class which stores all game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1680
        self.screen_height = 1000
        self.bg = pygame.image.load('images/space_background.png')
        self.ship_speed = 3.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 0.75
        self.fleet_drop_speed = 10.0
        self.fleet_direction = 0.75

        # Change game speed (difficulty level):
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which are changing during the game"""
        self.ship_speed = 3.5
        self.bullet_speed = 2.0
        self.alien_speed = 0.75
        self.fleet_direction = 0.75

    def increase_speed(self):
        """Change game speed settings"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale


