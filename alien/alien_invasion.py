import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """管理游戏资源的类"""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        #创建存储游戏统计信息的实例
        self.stats = GameStats(self)
        #创建计分板
        self.sb = Scoreboard(self)
        
        # 设置背景⾊
        self.bg_color = (230, 230, 230)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        #初始化完成后游戏还不能开始
        self.game_active = False
        
        #创建Play按钮
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        #游戏主循环
        while True:
            self._check_events()
            
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
    #相应键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        #点击play按钮开始新游戏
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialize_dynamic_settings()
            
            #重置统计信息
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True
            
            #清空外星人和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            
            #创建新的外星人舰队并将飞船放在屏幕底部正中
            self._create_fleet()
            self.ship.center_ship()
            
            #隐藏光标
            pygame.mouse.set_visible(False)
            
            #重置游戏设置
            self.settings.initialize_dynamic_settings()
            
    def _check_keydown_events(self, event):
        #按下
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        #释放
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    def _fire_bullet(self):
        #创建一颗子弹并且将其加入bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        #更新子弹位置并且删除应该消失的子弹
        #更新子弹位置
        self.bullets.update()
        #删除应该消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
            self._check_bullet_alien_collisions()
        
        
    def _check_bullet_alien_collisions(self):
        #响应子弹与外星人的碰撞
        #删除被子弹打中的外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            #删除所有子弹并创建新舰队并加速
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            #升级
            self.stats.level += 1
            self.sb.prep_level()
            
    def _update_screen(self):
        #更新屏幕上的图像并切换到新屏幕
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        #如果游戏没开始就绘制play按钮，死了也是一样
        if not self.game_active:
            self.play_button.draw_button()
        
        #显示分数
        self.sb.show_score()

        pygame.display.flip()
        
    def _create_fleet(self):
        #创建一个舰队
        #不断添加外星人,直到没有水平空间
        #外星人之间的间距为外星人宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
                
            #添加完一行后，重置x并递增y
            current_x = alien_width
            current_y += 2 * alien_height
            
    def _create_alien(self, x_position, y_position):
        #创建外星人并加入舰队
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _update_aliens(self):
        #检查是否有外星人位于屏幕边缘，更新外星舰队中所有外星人的位置
        self._check_fleet_edges()
        self.aliens.update()
        
        #检查外星人与飞船的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        #检查外星人与屏幕底部的碰撞
        self._check_aliens_bottom()
        
    def _check_aliens_bottom(self):
        #检查是否有外星人撞到了底部
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #和飞船被外星人撞到一样
                self._ship_hit()
                break
            
    def _check_fleet_edges(self):
        #在有外星人到达边缘时采取相应措施
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        #将整个外星舰队向下移动并改变方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _ship_hit(self):
        #响应飞船与外星人的碰撞
        if self.stats.ships_left > 0:
            #ships_left-1
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            #清空外星人列表和子弹列表
            self.bullets.empty()
            self.aliens.empty()
            
            #创建新外星人舰队并将飞船放在屏幕正中央
            self._create_fleet()
            self.ship.center_ship()
            
            #暂停
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
if __name__ == '__main__':
    # 创建游戏实例并运⾏游戏
    ai = AlienInvasion()
    ai.run_game()
    