class Setting:
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化"""
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_name = '瑞瑞的世界'
        self.bg_color = (230, 230, 230)
        self.dog_speed = 0.2
        # 子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 50
        self.bullet_height = 60
        self.bullet_color = (60, 60, 60)
        # 外星人
        self.alien_interval = 2
        self.alien_speed = 1
        self.fleet_drop_speed = 10  # 垂直速度
        self.fleet_direction = 1 # 移动方向 1右 -1左

