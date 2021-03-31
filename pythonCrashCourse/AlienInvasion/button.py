import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()  # 获取屏幕
        # 按钮参数
        self.width = 200
        self.height = 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('SimHei', 24)  # 创建文本对象
        # 构造按钮方块
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        # 创建按钮标签
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """构造按钮文字，将msg渲染为图像，并使其在按钮上居中。"""
        # 将文字转成图像 render
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        # 将创建好的 文字图形对象 的 位置对象 改为居中
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 填充颜色用 fill(颜色，形状对象)
        self.screen.fill(self.button_color, self.rect)
        # 把图片放屏幕上用 blit(图片，位置)
        self.screen.blit(self.msg_image, self.msg_image_rect)
