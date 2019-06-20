import pygame
from plane_sprites import *

#pygame初始化
pygame.init()

#创建主窗口
screen = pygame.display.set_mode((480,700))

#绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))

#绘制英雄战机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))

pygame.display.update()

#创建时钟对象
clock = pygame.time.Clock()

hero_rect = pygame.Rect(150,300,102,126)

#创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
#创建敌机精灵组
enemy_ground = pygame.sprite.Group(enemy,enemy1)

while True:
    clock.tick(60)

    #事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            #quit卸载所有模块
            pygame.quit()
            #退出游戏
            exit()

    #修改飞机的位置
    hero_rect.y -= 1
    #判断飞机的位置
    bottom = hero_rect.y + hero_rect.height
    if bottom <= 0 :
        hero_rect.y = 700
    #调用bilt方法绘制敌机
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #让精灵组调用两个方法
    #1.update-让组中所有精灵更新位置
    enemy_ground.update()
    #2.draw-在screen上绘制所有精灵
    enemy_ground.draw(screen)

    #调用update方法更新显示
    pygame.display.update()

pygame.quit()

