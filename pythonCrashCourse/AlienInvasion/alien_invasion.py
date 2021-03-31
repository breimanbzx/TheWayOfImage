import sys
import pygame
from pythonCrashCourse.AlienInvasion import \
    setting, dog, bullet, alien, game_stats, button
import time


# 1. 创建空白屏幕:set_mode访问屏幕模式（fill/get_rect访问位置/）设置尺寸 、 事件循环
# 2. 创建飞船的类
# **项目规划
# 玩家控制一艘最初出现在屏幕底部中央 的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键射 击。
# 在屏幕左上角添加一个外星人，并指定合适的边距。
# 根据第一个外星人的边距和屏幕尺寸计算屏幕上可容纳多少个外星 人。
# 编写一个循环来创建一系列外星人，使其填满屏幕的上半部 分。
# 让外星人群向两边和下方移动，直到外星人被全部击落、有外星人 撞到飞船或有外星人抵达屏幕底端。
# 如果整群外星人都被击落，将 再创建一群外星人。
# 如果有外星人撞到了飞船或抵达屏幕底端，将 销毁飞船并再创建一群外星人。
# 限制玩家可用的飞船数量。
# 当配给的飞船用完之后，游戏将结束。

# 关卡设计：每关之间停顿5秒，显示击杀数据
# 子弹：连续、频率可变
# 背景：缓慢向下移动
# 第一关：完虐翘脚狗： 子弹：小/频率低        敌人速度：慢   图片：全换
# 第二关：狗队也不怕： 子弹：小/频率高        敌人速度：中
# 第三关：狂揍村霸狗： 子弹：大/频率高        敌人速度：快
# 第四关：决战采石场： 子弹：大/频率高/穿透   敌人速度：超级快、多

class AlienInvasion:
    """管理游戏资源（屏幕设置）、行为（事件）"""

    # 静态图片组合
    def __init__(self):
        """初始化游戏并创建资源"""
        # 初始化游戏
        pygame.init()
        # 创建资源：屏幕设置
        self.setting = setting.Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption(self.setting.screen_name)
        # 统计信息
        self.stats = game_stats.GameStats(self)
        # 游戏剧情

        # 创建小狗的类
        # self指AlienInvasion类自身，由于狗类中会用到屏幕中的参数，因此需要传入self
        # 也可以简单点，逐个传入AlienInvasion类中的变量
        self.dog = dog.Dog(self)
        # 创建子弹编组Group, 由于bullet类的操作直接保存到sprite里了，所以不用调用bullet类：子弹是可以同时出现的
        self.bullet = pygame.sprite.Group()
        # 外星人
        self.alien = pygame.sprite.Group()
        self._create_fleet()
        # 创建play按钮
        self.play_button = button.Button(self, '点击开始游戏')

    def _create_fleet(self):
        """创建一群外星人"""
        ali = alien.Alien(self)
        ali_width = ali.rect.width
        ali_height = ali.rect.height
        # 外星人横向纵向个数
        num_alien_x = self.setting.screen_width // (self.setting.alien_interval * ali_width) - 2
        num_alien_y = 3  # (self.setting.screen_height // (self.setting.alien_interval * ali_height))
        for alien_y_NO in range(num_alien_y):
            for alien_x_NO in range(num_alien_x):
                # 循环创建多个新外星人，并修改每个外星人的x，使其平铺开来
                self._create_alien(alien_x_NO, alien_y_NO)

    def _create_alien(self, alien_x_NO, alien_y_NO):
        ali = alien.Alien(self)
        ali_width = ali.rect.width
        ali_height = ali.rect.height
        ali.x = ali_width + self.setting.alien_interval * ali_width * alien_x_NO
        ali.rect.x = ali.x
        # 让外星人刚开始在屏幕外 ali_height调试完后删除
        ali.rect.y = ali_height - self.setting.alien_interval * ali_height * alien_y_NO
        self.alien.add(ali)

    # 动起来吧图片
    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            # 游戏结束后不运行
            if self.stats.game_active:
                self.dog.update()
                self._update_bullet()
                self._update_alien()
            self._update_screen()

    # 1. 按键控制
    def _check_events(self):
        """响应按键和鼠标的事件"""
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
            # 按下鼠标后...
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 获取鼠标点击的位置
                mouse_pos = pygame.mouse.get_pos()
                # 如果在按钮 碰撞点上
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        # 如果在按钮 碰撞点 上, 且当前游戏未开始
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            # 如果不重置生命，那么生命一直小于0，游戏就重新开始不了
            self.stats.reset_stats()
            # 重置速度
            self.setting.init_dynamic_setting()
            self.stats.game_active = True
            # 游戏重新开始后，清空子弹和外星人、创建新外星人并居中
            self.bullet.empty()
            self.alien.empty()
            self._create_fleet()
            self.dog.center_dog()
            # 隐藏鼠标光标
            pygame.mouse.set_visible(False)

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
        # Z小炮
        elif event.key == pygame.K_z:
            self._fire_bullet(1)
        # X大炮
        elif event.key == pygame.K_x:
            if len(self.bullet) == 0:
                self._fire_bullet(2)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.dog.move_right = False
        elif event.key == pygame.K_LEFT:
            self.dog.move_left = False
        elif event.key == pygame.K_UP:
            self.dog.move_up = False
        elif event.key == pygame.K_DOWN:
            self.dog.move_down = False

    # 2.子弹移动控制
    def _fire_bullet(self, bullet_shape):
        new_bullet = bullet.Bullet(self, bullet_shape)
        # 一个子弹类表示一个子弹，按一下空格就添加一个子弹类到精灵编组中去
        self.bullet.add(new_bullet)

    def _update_bullet(self):
        self.bullet.update()
        # 删除消失的子弹
        for bu in self.bullet.copy():
            if bu.rect.bottom <= 0:
                self.bullet.remove(bu)
        self._check_bullet_alien_collisions()

    # 3. 子弹、外星人交互
    def _check_bullet_alien_collisions(self):
        """判断是否碰撞，碰撞后删除"""
        collisions = pygame.sprite.groupcollide(self.bullet, self.alien, True, True)
        # 如果外星人打完了，进入下一关，换敌人、背景图片
        if not self.alien:
            self.bullet.empty()
            # 添加 第几关 参数
            self._create_fleet()

            self.setting.increase_speed()
        # print(len(self.bullet))

    # 4. 外星人移动控制、外星人与狗交互
    def _update_alien(self):
        """检查是否有外星人触碰边缘、撞到狗"""
        self._check_fleet_edge()
        self.alien.update()
        if pygame.sprite.spritecollideany(self.dog, self.alien):
            self._dog_die()
        self._check_alien_bottom()

    def _check_alien_bottom(self):
        """删除向下消失的外星人"""
        for ali in self.alien.copy():
            if ali.rect.bottom >= self.screen.get_rect().bottom:
                self.alien.remove(ali)
        # print(len(self.alien))

    def _dog_die(self):
        if self.stats.dog_life > 0:
            self.stats.dog_life -= 1
            # 清空余下的动图、小狗归位、外星人重现
            self.alien.empty()
            self.bullet.empty()
            self.dog.center_dog()
            self._create_fleet()
            # 等待一秒，重新开始
            time.sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
            print('game over')

    def _check_fleet_edge(self):
        """有外星人碰到边缘时，所有外星人都下移，且改变方向 """
        for ali in self.alien.sprites():
            if ali.check_edge():
                self._change_fleet_direction()
                break  # 跳出循环：因为只要有一个外星人碰到边界就下移一次，然后进入下面的水平移动

    def _change_fleet_direction(self):
        """如果有触碰，循环所有外星人，全部下移，之后改变x轴方向"""
        for ali2 in self.alien.sprites():
            ali2.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1

    # 5. 屏幕刷新
    def _update_screen(self):
        # 游戏中进行屏幕设置：填充颜色
        # self.screen.fill(self.setting.bg_color)
        # 显示背景图片
        self.screen.blit(self.setting.bg_image, (0, 0))  # 对齐的坐标
        # 绘制狗到屏幕上
        self.dog.blitme()
        for bu in self.bullet.sprites():
            bu.draw_bullet()
        self.alien.draw(self.screen)
        # 如果游戏结束，画上按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        # 显示屏幕
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
