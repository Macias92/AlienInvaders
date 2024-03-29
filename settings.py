import pygame


class Settings:
    """Class which stores all game settings"""

    def __init__(self):
        """Initialize game settings"""
        self.screen_width = 1680
        self.screen_height = 1000
        self.bg = pygame.image.load('images/space_background.png')
        self.ship_limit = 3
        self.ship_speed = 3.5

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 60, 0)
        self.bullets_allowed = 10
        self.alien_bullet_color = (255, 255, 0)

        # Alien settings
        self.fleet_drop_speed = 10.0
        self.last_alien_shot = pygame.time.get_ticks()

        # Change game speed (difficulty level):
        self.speedup_scale = 1.2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which are changing during the game"""
        self.bullet_speed = 2.0
        self.alien_speed = 0.5
        self.fleet_direction = 0.5
        self.alien_points = 50
        self.alien_bullet_speed = 1.0
        self.alien_bullet_cd = 2500  # alien bullet cooldown in miliseconds

    def increase_speed(self):
        """Change game speed settings"""
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale
        self.alien_bullet_cd /= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
