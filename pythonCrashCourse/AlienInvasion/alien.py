import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """创建单个外星人"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.setting

        # 将图片处理成正方形 get_rect()
        self.image = self.setting.alien_image
        self.rect = self.image.get_rect()
        # 设置外星人初始坐标x,y,在48,60附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 精确位置
        self.x = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self, *args, **kwargs) -> None:
        self.x += (self.setting.alien_speed*self.setting.fleet_direction)
        self.rect.x = self.x



