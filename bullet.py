import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class intended to manage bullet shot by ship"""

    def __init__(self, ai_game):
        """Create bullet in current ship's location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rectangle in (0,0) and define its appropriate location
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet on the screen"""
        self.y -= self.settings.bullet_speed

        # Update the bullet's location
        self.rect.y = self.y

    def draw_bullet(self):
        """Show bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class AlienBullet(Sprite):
    """Class intended to manage bullet fired by random alien"""

    def __init__(self, ai_game, shooting_alien):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color
        self.shooting_alien = shooting_alien
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = ai_game.shooting_alien.rect.midbottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw_alien_bullet(self):
        """Show alien bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
