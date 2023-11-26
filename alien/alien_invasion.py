import sys
import pygame
from settings import Settings

class AlienInvasion:
    """管理游戏资源的类"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景⾊
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """游戏主循环"""
        while True:
            pygame.display.flip()
            self.clock.tick(60)
            #监听键盘鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys:exit()
                # 每次循环时都重绘屏幕
                self.screen.fill(self.settings.bg_color)
                # 让最近绘制的屏幕可⻅
                pygame.display.flip()
                self.clock.tick(60)
                
if __name__ == '__main__':
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()