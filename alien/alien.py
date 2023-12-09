import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类
    
    def __init__(self, ai_game):
        #初始化外星人并设置其起始位置
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #加载图像并设置rect属性
        self.image = pygame.image.load('D:\git_practice\python_class\\alien\images\\alien.bmp')
        self.rect = self.image.get_rect()
        
        #每个外星人最初在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #存储外星人准确水平位置
        self.x = float(self.rect.x)
        
    def update(self):
        #左右移动外星人
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
        
    def check_edges(self):
        #如果外星人位于边缘返回true
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
