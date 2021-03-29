import pygame


class Dog:
    """创建小狗类"""

    def __init__(self, ai_game):  # 传入屏幕设置
        """初始化小狗、设置位置"""
        self.setting = ai_game.setting
        # 在原有屏幕类中开辟一个新位置screen_rect给小狗矩形
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()  #

        # 导入小狗图片、设置成矩形 self.rect 才是主角 60*48
        self.image = pygame.image.load('image/dog.bmp')
        self.rect = self.image.get_rect()  # 小狗照片

        # 将主角放到指定初始位置
        self.rect.midbottom = self.screen_rect.midbottom  # 将小狗照片原来的midbottom位置  改为 在当前屏幕中的位置

        # 允许小狗移动小数值的像素
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动管理
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def update(self):
        # self.rect.right是小狗矩形右边缘x轴坐标
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.x += self.setting.dog_speed
        if self.move_left and self.rect.left >= 0:
            self.x -= self.setting.dog_speed
        #
        self.rect.x = self.x

        if self.move_up and self.rect.top >= 0:
            self.y -= self.setting.dog_speed
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.setting.dog_speed
        self.rect.y = self.y

    def blitme(self):
        """绘制狗到屏幕上"""
        self.screen.blit(self.image, self.rect)  # 位块传输
