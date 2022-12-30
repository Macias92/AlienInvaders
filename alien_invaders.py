import sys
from settings import Settings
import pygame
from ship import Ship


class AlienInvaders:
    """General class intended for manage the resources and the way the game works"""

    def __init__(self):
        """Initialize the game and it's resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invaders")

        self.ship = Ship(self)

        # Define the backscreen color
        self.bg_color = (10, 10, 60)

    def run_game(self):
        """Run the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Refreshing the screen during every game loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Display the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvaders()
    ai.run_game()
