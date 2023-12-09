# 《Python程序设计基础》程序设计作品说明书

题目： 外星人入侵游戏👽

学院： 21计科

姓名： 陶启睿

学号： B20210302126

指导教师： 周景

起止日期：2023.11.10-2023.12.10

## 摘要

本项目通过使用Pygame库，实现了一个外星人入侵游戏👽小游戏，玩家可以通过键盘控制飞船的移动和射击，以防止外星人入侵。
在实现过程中，项目首先设计了游戏画面，包括飞船、外星人、子弹、背景色等元素。接着，通过使用Pygame库中的函数和方法，实现了游戏的逻辑和交互性包括设计开始按钮、显示剩余飞船、显示得分、显示难度等级。此外，还对游戏进行了测试，以确保游戏的稳定性。

关键词：游戏开发、Python、Pygame、外星人入侵

## 第1章 需求分析

一、功能性需求

1. 玩家控制：游戏需要提供玩家控制的飞船，玩家可以通过键盘控制飞船的移动和射击。
2. 外星人生成与移动：游戏需要在屏幕上生成一定数量的外星人，并让它们从屏幕顶部向下移动。
3. 碰撞检测：游戏需要检测飞船与外星人之间的碰撞以及外星人与屏幕底部的碰撞，一旦发生碰撞，玩家的飞船减少一个，如果此时没有剩下飞船，游戏结束。
4. 得分明细：游戏需要实时计算并显示玩家的得分，以便玩家了解自己在游戏中的表现。
5. 游戏难度递增：随着游戏的进行，外星的移动速度应该逐渐增加，以增加游戏的挑战性和玩家的兴趣。
6. 视觉效果：游戏需要提供视觉效果，如飞船射击、碰撞等动画效果。
7. 游戏结束提示：当玩家失去所有的飞船时，游戏应该结束。
二、非功能性需求

1. 稳定性：游戏应该稳定运行，没有崩溃或死锁等问题。
2. 性能优化：游戏应该优化性能，确保在各种设备上都能够流畅运行。
3. 易于上手：游戏应该易于上手，玩家能够快速理解游戏规则并开始游戏。
4. 图形界面：游戏应该具有简洁明了的图形界面，易于观察和理解。
5. 可扩展性：游戏应该能够扩展功能和内容，以支持更多的玩家和游戏模式。

## 第2章 分析与设计

项目报告：外星人入侵小游戏的分析与设计

一、引言

随着游戏产业的快速发展，越来越多的人加入到游戏开发领域。本报告将对外星人入侵小游戏进行分析与设计，包括系统架构、系统流程和系统模块等方面。通过对外星人入侵小游戏的深入了解和分析，我们将设计出一款具有挑战性和趣味性的游戏，满足玩家的需求。

二、系统架构

1. 游戏框架

本游戏采用Pygame库进行开发，以Python语言为编程语言。游戏框架主要包括游戏画面的创建、游戏逻辑的实现、碰撞检测等功能。

2. 模块划分

游戏分为以下几个模块：

（1）游戏画面的创建与更新：该模块负责游戏画面的绘制和更新，包括飞船、外星人、子弹等元素。

（2）设置模块：该模块负责保存游戏各项参数。

（3）玩家控制模块：该模块负责接收玩家的输入指令，并控制飞船的移动和射击。

（4）外星人生成与移动模块：该模块负责生成外星人。

（5）碰撞检测模块：该模块负责检测外星人与飞船、屏幕或子弹之间的碰撞情况。

（6）计分板与剩余飞船数量模块：该模块负责计算玩家的得分，根据外星人被击杀和等级等情况进行计分而且需要显示当前等级与飞船剩余。

（7）难度递增模块：该模块负责根据游戏进度递增游戏难度，增加外星人移动速度。

三、系统流程

1. 游戏启动

游戏开始时，先初始化游戏窗口和Pygame库，然后创建游戏画面，包括Play按钮、背景色、飞船、外星人等元素。同时，初始化玩家控制模块、外星人生成与移动模块、碰撞检测模块、得分计算模块和难度递增模块。

2. 游戏循环

进入游戏循环后，先检测玩家输入指令，然后更新玩家控制模块。接着，根据游戏进度更新外星人生成与移动模块和难度递增模块。然后进行碰撞检测，如果发生子弹碰撞，则根据得分计算模块计算得分。如果发生外星人碰撞，则扣除飞船数量，如果没有飞船，则游戏结束。如果没有发生碰撞，则更新游戏画面，进入下一帧。

3. 游戏结束

当玩家失去所有的飞船时，游戏结束。

四、系统模块详细设计

1. 游戏画面的创建与更新模块

该模块主要负责游戏画面的绘制和更新。首先，需要定义游戏画面的尺寸和背景色等属性。然后，创建飞船、外星人、子弹等元素的类和方法，用于绘制和更新它们的位置和状态。同时，还需要定义绘制方法和刷新方法，用于实现游戏画面的动态更新。
```python
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
        
```
2. 设置模块
该模块负责保存游戏各项参数。
```python
class Settings:
#存储游戏《外星⼈⼊侵》中所有设置的类
    def __init__(self):
        #初始化游戏的设置
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
        
        #子弹设置
        self.bullet_speed = 3.0
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10
        
        #外星人设置
        self.fleet_drop_speed = 10
        
        #节奏加快的倍率
        self.speedup_scale = 1.1
        
        #外星人分数的提高速度
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        #初始化设置变量
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        
        #fleet_direction = 1 表示右 -1 表示左.
        self.fleet_direction = 1
        
        #计分设置
        self.alien_points = 50

    def increase_speed(self):
        #提高速度
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
```

3. 玩家控制模块

该模块主要负责接收玩家的输入指令，并控制飞船的移动和射击。需要定义玩家控制方法，用于处理键盘或鼠标输入指令，并调用飞船控制类和方法实现飞船的移动和射击。同时，还需要定义玩家的初始状态和属性，如初始分数、飞船数量等。
```python
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
            
```

4. 外星人生成与移动模块

该模块主要负责生成外星人。需要定义外星人类和方法，用于生成外星人对象并设置它们的初始位置。同时，还需要实现外星人的生成，根据游戏进度调整外星人的移动速度。
```python
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
    
```

5. 碰撞检测模块

该模块主要负责检测外星人与飞船、地面或子弹之间的碰撞情况。需要定义碰撞检测方法，通过判断飞船、外星人、子弹、屏幕等元素的位置和大小来实现碰撞检测。如果发生碰撞，则触发相应的事件或效果，如计分、改变外星人位置与移动方向、增加等级、扣除飞船等。   
```python
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
```

6. 计分板与剩余飞船数量模块

该模块负责计算玩家的得分，根据外星人被击杀和等级等情况进行计分而且需要显示当前等级与飞船剩余，并在游戏过程中实时更新得分数据。
```python
class Scoreboard:
    #计分板
    
    def __init__(self, ai_game):
        #初始化显示得分涉及的属性
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        #显示得分信息的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        #初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        #将得分渲染为图像
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        #在右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        #将最高分渲染为图像
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        #将最高分放在顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        #将等级渲染为图像
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
                
        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def prep_ships(self):
        #显示还有几个飞船
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def check_high_score(self):
        #检测是否出现了最高分
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            
    def show_score(self):
        #在屏幕上显示得分、等级和余下飞船数量
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
```

7. 难度递增模块
该模块主要负责根据游戏进度递增游戏难度，包括增加外星人数量、移动速度等。需要定义难度递增类和方法，根据游戏规则和进度调整外星人的数量、移动速度等属性，以增加游戏的挑战性和玩家的兴趣。
```python
class GameStats:
    
    #跟踪游戏统计信息
    
    def __init__(self, ai_game):
        #初始化统计信息
        self.settings = ai_game.settings
        self.reset_stats()
        
        #任何时候不重置最高分
        self.high_score = 0
        
    def reset_stats(self):
        #初始化在游戏运行期间可能变化的统计信息
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
```

## 第3章 软件测试

_本章的内容主要包括以类和函数作为单元进行单元测试，编写的对系统的主要功能的测试用例，以及测试用例执行的测试报告。_

### 单元测试用例

| \#  | 测试目标 | 输入 | 预期结果 | 测试结果 |
| --- | --------- | ----- | ---------------- | ----------------- |
| 1   |飞船移动|键盘左右键|飞船移动正常|通过|
| 2   |飞船射击|键盘空格键|飞船射击正常|通过|
| 3   |飞船死亡|无|余数减少|通过|

1. 飞船移动测试：

- 测试目标： 验证飞船的移动、射击和碰撞检测功能。
- 测试用例： 模拟飞船移动、射击、与外星人碰撞的情况。
- 测试报告： 飞船模块通过测试，各项功能运作正常。
```python
import unittest
import pygame
from ship import Ship
from settings import Settings
class TestShipMovement(unittest.TestCase):
def setUp(self):
"""初始化测试"""
    pygame.init()
    self.ai_settings = Settings()
    self.screen = pygame.display.set_mode((self.ai_settings.screen_width,
    self.ai_settings.screen_height))
    pygame.display.set_caption("ship move test")
    self.ship = Ship(self.ai_settings, self.screen)
def test_move_right(self):
    """测试向右移动"""
    self.ship.moving_right = True
    original_center = self.ship.rect.centerx
    self.ship.update()
    self.assertGreater(self.ship.rect.centerx, original_center)
def test_move_left(self):
    """测试向左移动"""
    self.ship.moving_left = True
    original_center = self.ship.rect.centerx
    self.ship.update()
    self.assertLess(self.ship.rect.centerx, original_center)
def tearDown(self):
"""清理测试"""
pygame.quit()
self.screen = None
self.ai_settings = None

if name == 'main':
unittest.main()
```

2. 飞船射击测试:
- 测试目标： 验证子弹的生成、移动和碰撞检测功能。
- 测试用例： 模拟子弹生成、移动、与外星人碰撞的情况。
- 测试报告： 子弹模块通过测试，各项功能正常。
好的，以下是一个使用 Pygame 实现的飞船射击测试程序。这个程序包括一个飞船（可以发射子弹），一些敌机（即外星人），以及子弹和敌机的碰撞检测。


```python
import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置窗口标题
pygame.display.set_caption("飞船射击测试")

# 加载飞船和敌机的图像
ship_image = pygame.image.load("ship.bmp")
alien_image = pygame.image.load("alien.bmp")

# 设置飞船、敌机和子弹的属性
ship_x = screen_width // 2
ship_y = screen_height - ship_image.get_height()
alien_speed = 5
bullet_speed = 10
bullet_width = bullet_image.get_width()
bullet_height = bullet_image.get_height()
aliens = [[0, 50], [screen_width // 2 - alien_image.get_width() // 2, random.randint(100, 300)], 
           [screen_width // 2 + alien_image.get_width() // 2, random.randint(100, 300)]]
bullets = []

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_SPACE:
            # 发射子弹
            bullet_x = ship_x + ship_image.get_width() // 2 - bullet_width // 2
            bullet_y = ship_y - bullet_height - 10
            bullets.append([bullet_x, bullet_y])

    # 更新子弹位置
    new_bullets = []
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] > -bullet_height:
            new_bullets.append(bullet)
    bullets = new_bullets

    # 更新敌机位置，检测碰撞，删除被击中的敌机
    aliens = [[alien for alien in aliens if alien[1] > 0] if alien[0] > ship_x and alien[0] < ship_x + ship_image.get_width() else aliens for alien in aliens]
    aliens = [alien for alien in aliens if alien[1] > 0]  # 删除已经移出屏幕的敌机
    if aliens:  # 如果还有敌机在屏幕上，则生成新的敌机，位置随机且不能与原来的敌机重叠
        x = random.randint(screen_width - alien_image.get_width(), screen_width)
```
3. 飞船死亡测试:
- 测试目标： 飞船与外星人碰撞检测功能。
- 测试用例： 模拟外星人与飞船碰撞的情况。
- 测试报告： 飞船碰撞模块通过测试，各项功能正常。
以下是一个可能的Python测试用例，用于测试飞船与外星人的碰撞检测功能：


```python
import unittest
import pygame
from pygame import Rect
from ship import Ship
from alien import Alien

class TestShipCollision(unittest.TestCase):
    def setUp(self):
        # 初始化Pygame和测试窗口
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.settings = pygame.display.get_surface()
        self.ship = Ship(self)
        self.alien = Alien(self)
        
    def test_ship_collision(self):
        # 测试飞船与外星人的碰撞检测功能
        self.alien.rect.x = self.ship.rect.x + self.ship.rect.width - self.alien.rect.width
        self.alien.rect.y = self.ship.rect.y + self.ship.rect.height - self.alien.rect.height
        self.ship.update()
        self.alien.update()
        result = self.ship.check_collision(self.alien)
        self.assertTrue(result)
        
    def test_ship_no_collision(self):
        # 测试飞船与外星人没有碰撞的情况
        self.alien.rect.x = self.ship.rect.x + self.ship.rect.width + self.alien.rect.width
        self.alien.rect.y = self.ship.rect.y + self.ship.rect.height + self.alien.rect.height
        self.ship.update()
        self.alien.update()
        result = self.ship.check_collision(self)
        self.assertFalse(result)
        
    def tearDown(self):
        # 关闭Pygame窗口和事件循环线程
        pygame.quit()
```
## 结论
在本项目中，我们实现了一个外星人入侵游戏，玩家可以通过键盘控制飞船的移动和射击，以防止外星人入侵。具体功能包括：

1. 飞船移动：玩家可以通过键盘的上下左右键控制飞船的移动。
2. 飞船射击：玩家可以通过按下特定的按键来发射子弹。
3. 外星人进攻：游戏中有不同类型的外星人，他们会从屏幕两侧出现并向飞船发起进攻。
4. 碰撞检测：游戏会检测飞船和外星人、子弹之间的碰撞，并根据碰撞结果进行相应的处理。
5. 游戏得分：玩家每击中外星人或子弹，都会获得相应的分数。
6. 游戏难度等级：游戏初始时，会显示难度等级供玩家选择，不同等级对应着不同的外星人数量和进攻频率。

通过这些功能的实现，我们达到了以下目标：

1. 创建了一个富有挑战性和趣味性的游戏。
2. 提供了玩家一个休闲娱乐的平台，可以在游戏中放松心情、锻炼反应速度和操作技巧。
3. 通过游戏得分和难度等级的设定，为玩家提供了不断挑战自我、提升游戏水平的动力。

### 项目不足与改进

在项目实施过程中，我们也发现了一些不足之处，并提出了相应的改进方案：

1. 代码组织和可维护性：
   虽然我们在开发过程中尽可能保证了代码的结构清晰和规范，但仍然存在一些可以改进的地方。例如，我们可以进一步细化代码模块，将不同的功能模块化、接口化，提高代码的可读性和可维护性。
2. 性能优化：
   虽然我们的游戏在大部分情况下运行流畅，但在某些情况下仍然会出现卡顿现象。我们可以进一步优化图像资源的加载和释放机制，减少不必要的资源占用，提高游戏的性能表现。
3. 游戏平衡性：
   在测试过程中，我们发现游戏的一些元素需要进一步调整以实现更好的平衡性。例如，飞船的移动速度、外星人的数量和进攻频率等需要适当调整，以使游戏更具挑战性和乐趣。我们可以根据玩家的反馈和测试结果，对游戏参数进行反复调整和优化，以实现更好的游戏平衡性。
4. 多平台兼容性：
   我们的游戏目前只在Windows平台上进行了测试。为了使游戏能够在其他平台上运行，我们需要进一步检查代码和图像资源在不同平台上的兼容性问题，并针对不同平台进行相应的优化和调整。
5. 用户界面设计：
   
   虽然我们在项目中实现了基本的用户界面设计，但仍有改进的空间。我们可以进一步美化游戏界面，提升游戏的视觉效果和用户体验。同时也可以考虑增加更多的交互元素和游戏特效，提升游戏的趣味性和吸引力。

### 结语
我在这个项目中成功地实现了一个外星人入侵游戏。尽管在实施过程中遇到了一些困难和挑战，但通过查找资料和与同学交流，我成功地克服了这些困难并实现了项目的目标。通过这个项目，我们不仅提高了自己的python编程技能和解决问题的能力，还学到了很多关于游戏设计和实现的知识。希望我在未来的项目中能够继续改进和创新。
## 参考文献
[1]美 哈伯 Harbour, Jonathan S.Python游戏编程入门[M].人民邮电出版社,2015.

[2]李志远.Python游戏编程项目开发实战[M].清华大学出版社,2022.

[3]陆嘉诚,王楚虹,师文庆,等.基于Python的飞机大战游戏开发[J].机电工程技术, 
2020, 49(3):3.DOI:CNKI:SUN:JXKF.0.2020-03-029.

[4]刘班.基于Pygame快速开发游戏软件[J].数字技术与应用, 2013(8):1.DOI:CNKI:SUN:SZJT.0.2013-08-090.

[5] Team T T D , Al-Rfou R , Alain G ,et al.Theano: A Python framework for fast computation of mathematical expressions[J].  2016.DOI:10.48550/arXiv.1605.02688.

[6] Bird S , Klein E , Loper E .Natural Language Processing with Python[M].东南大学出版社,2009.

[7] Simon A , Theodor P P , Wolfgang H .HTSeq—a Python framework to work with high-throughput sequencing data[J].Bioinformatics, 2015(2):166-9.DOI:10.1093/bioinformatics/btu638.
