#  记录游戏中可能变化的统计信息


class GameStats:
    """跟踪游戏的统计信息"""
    dog_life: int
    score: int

    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """记录游戏中可能变化的统计信息，并且需要在重启后清零的"""
        self.dog_life = self.setting.dog_limit
        self.score = 0
