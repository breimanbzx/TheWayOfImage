import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """发射一个子弹的类"""
    def __init__(self, ai_game):
        super().__init__()  # 继承sprite是为了将子弹组放一起
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # 创建一个子弹模型
        self.rect = pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        # self.
