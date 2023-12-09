import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #管理子弹的类

    def __init__(self, ai_game):
        #在飞船所在位置创建子弹
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #先在（0，0）处创建子弹的矩形再设置正确位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储子弹位置
        self.y = float(self.rect.y)

    def update(self):
        #子弹向上移动
        #更新子弹准确位置
        self.y -= self.settings.bullet_speed
        #更新表示子弹的RECT位置
        self.rect.y = self.y

    def draw_bullet(self):
        #绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)