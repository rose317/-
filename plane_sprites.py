import random
import pygame
#定义设置窗口参数
SCREEN_RECT = pygame.Rect(0,0,480,700)
#定义设置帧数参数
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#创建英雄的发射子弹常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):
        #调用父类初始化方法
        super().__init__()
        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        #2.指定敌机的初始随机速度
        self.speed = random.randint(1,3)
        #3.指定敌机的初始随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        #1.调用父类的update的方法
        super().update()
        #2.判断是否飞出屏幕，如果是，精灵组需要删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            #print("敌机飞出屏幕")

            self.kill()

    def __del__(self):
        #print("敌机挂了 %s" % self.rect)
        pass

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        #1.调用父类方法,设置image，speed
        super().__init__("./images/me1.png",0)
        #2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120
        #3.创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        #英雄在水平方向上移动
        self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        #print("发射子弹")
        for i in (0,1,2):
            #1.创建子弹精灵
            bullet = Bullet()
            #2.设置子弹位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            #3.将子弹精灵添加到精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁")





