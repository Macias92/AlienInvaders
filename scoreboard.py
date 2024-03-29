import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """Class intended to show user score during and after his game"""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (0, 100, 200)
        self.font = pygame.font.SysFont(None, 48, False, True)
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ships()

    def prep_score(self):
        """Put score on game screen"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, None)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Put high score on the screen"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_lvl(self):
        """Put actual game lvl on the screen"""
        lvl_str = str(self.stats.level)
        self.lvl_image = self.font.render(lvl_str, True, self.text_color, None)
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Display number of ships available in current game"""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Display actual score, level and ships left on the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check high score done by far"""
        ath_read = open('ath.txt')
        ath_write = open('ath.txt', 'r+')
        high_score = int(ath_read.readline())
        if self.stats.score > high_score:
            ath_write.write(str(self.stats.score))
            self.prep_high_score()
