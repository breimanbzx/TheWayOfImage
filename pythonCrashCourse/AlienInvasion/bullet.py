import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """发射一个子弹的类"""
    def __init__(self, ai_game, bullet_shape):
        super().__init__()  # 继承sprite是为了将子弹组放一起
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        # 创建一个子弹模型
        if bullet_shape == 1:
            self.rect = pygame.Rect(0,0,self.setting.bullet_width1,self.setting.bullet_height1)
        else:
            self.rect = pygame.Rect(0, 0, self.setting.bullet_width2, self.setting.bullet_height2)
        self.rect.midtop = ai_game.dog.rect.midtop

        self.y = float(self.rect.y)

    def update(self, *args, **kwargs) -> None:
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """显示子弹"""
        # 画pygame子弹形状用pygame.draw
        pygame.draw.rect(self.screen, self.color, self.rect)

