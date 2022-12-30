import sys
import pygame


class AlienInvaders:
    """General class intended for manage the resources and the way the game works"""

    def __init__(self):
        """Initialize the game and it's resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1680, 1050))
        pygame.display.set_caption("Alien Invaders")

    def run_game(self):
        """Run the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Display the last modified screen"""
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvaders()
    ai.run_game()
