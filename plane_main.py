import pygame
from plane_sprites import *

class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")

        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock = pygame.time.Clock()
        #3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        #4.设置定时器事件-创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)


    def __create_sprites(self):

        #创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_ground = pygame.sprite.Group(bg1,bg2)

        #创建敌机的精灵组
        self.enemy_ground = pygame.sprite.Group()
        #创建英雄精灵
        self.hero = Hero()
        self.hero_ground = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")

        while True:
            #1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #2.事件监听
            self.__event_handle()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            pygame.display.update()

    def __event_handle(self):
        #判断是否退出游戏
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #print("敌机出场")
                #创建敌机精灵
                enemy = Enemy()
                self.enemy_ground.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()


             #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
              #    print("向右移动")

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        #1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_ground,True,True)
        #2.敌机摧毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_ground,True)
        if len(enemies) > 0:
            #让英雄牺牲
            self.hero.kill()
            #调用退出游戏方法
            PlaneGame.__game_over()



    def __update_sprites(self):
        #更新背景精灵组
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        #更新敌机精灵组
        self.enemy_ground.update()
        self.enemy_ground.draw(self.screen)
        #更新英雄精灵组
        self.hero_ground.update()
        self.hero_ground.draw(self.screen)
        #更新子弹精灵组
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    #创建游戏对象
    game = PlaneGame()
    #调用开始游戏
    game.start_game()