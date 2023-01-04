class GameStats:
    """Monitoring statistic data in game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        ath = open("ath.txt", 'r')
        self.high_score = int(ath.readline())

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
