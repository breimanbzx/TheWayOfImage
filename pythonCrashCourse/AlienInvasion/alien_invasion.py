import sys
import pygame
from pythonCrashCourse.AlienInvasion import setting, dog


# 1. 创建空白屏幕:set_mode访问屏幕模式（fill/get_rect访问位置/）设置尺寸 、 事件循环
# 2. 创建飞船的类


class AlienInvasion:
    """管理游戏资源（屏幕设置）、行为（事件）"""

    def __init__(self):
        """初始化游戏并创建资源"""
        # 初始化游戏
        pygame.init()
        # 创建资源：屏幕设置
        self.setting = setting.Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption(self.setting.screen_name)
        # 创建小狗的类
        self.dog = dog.Dog(self)  # self指AlienInvasion类自身，由于狗类中会用到屏幕中的参数，因此需要传入self

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            # 一直循环，后续用键盘改变变量
            self.dog.update()
            self._update_screen()

    def _check_events(self):
        # 事件循环
        for event in pygame.event.get():
            # 如果点击退出
            if event.type == pygame.QUIT:
                sys.exit()
            # 如果按下键盘 type键盘是按下还是弹出
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 按下键盘后松开了再停止移动(event.key)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # key按得是哪个键
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.dog.move_right = True
        elif event.key == pygame.K_LEFT:
            self.dog.move_left = True
        elif event.key == pygame.K_UP:
            self.dog.move_up = True
        elif event.key == pygame.K_DOWN:
            self.dog.move_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.dog.move_right = False
        elif event.key == pygame.K_LEFT:
            self.dog.move_left = False
        elif event.key == pygame.K_UP:
            self.dog.move_up = False
        elif event.key == pygame.K_DOWN:
            self.dog.move_down = False

    def _update_screen(self):
        # 游戏中进行屏幕设置：填充颜色
        self.screen.fill(self.setting.bg_color)
        # 绘制狗到屏幕上
        self.dog.blitme()
        # 显示屏幕
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
