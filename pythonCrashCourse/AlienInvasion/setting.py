import pygame


class Setting:
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化"""
        # 背景
        self.bg_image = pygame.image.load('image/bg.bmp')  # 1300*700
        self.screen_width = 1300
        self.screen_height = 700
        self.screen_name = '瑞瑞的世界'
        self.bg_color = (230, 230, 230)

        # 狗
        self.dog_image = pygame.image.load('image/dog.bmp')  # 94*100
        self.dog_speed = 0.6
        self.dog_limit = 3

        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_color = (60, 60, 60)
        # # 小子弹
        self.bullet_width1 = 10
        self.bullet_height1 = 20
        # # 炸弹
        self.bullet_width2 = 200
        self.bullet_height2 = 30

        # 外星人
        self.alien_image = pygame.image.load('image/emery.bmp')  # 调整为80*80
        self.alien_interval = 2
        self.alien_speed = 0.3
        self.fleet_drop_speed = 30  # 垂直速度
        self.fleet_direction = 1  # 移动方向 1右 -1左

