import pygame
from pygame.constants import QUIT

from pythonProject.actor.japanese_shoot_soldier import JapaneseShootSoldier
from pythonProject.actor.japanese_soldier import JapaneseWalkSoldier
from pythonProject.actor.welcome_sprite import WelcomeSprite


def step5_show_shoot_chinese():
    """
    steps:射击
    :return:
    """

    pygame.init()

    icon = pygame.image.load("../resources/images/pygame图标.jpg")#设置图标
    pygame.display.set_icon(icon)

    pygame.display.set_caption("我是一个游戏")
    pygame.display.get_caption()

    clock = pygame.time.Clock()

    #screen = pygame.display.set_mode((640, 426), 0, 32)#显示屏幕的大小
    screen = pygame.display.set_mode((1280,720),0,32)

    background = pygame.image.load("../resources/images/welcome/welcome.jpg").convert()
    #actor_images = lode_actor_image()

    xiao_tie = WelcomeSprite(50,200)
    japanese = JapaneseWalkSoldier(400,300)
    japanese_shoot = JapaneseShootSoldier(600,300)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                japanese_shoot.run(event.key)


        screen.blit(background, (0, 0))#粘贴图片
        xiao_tie.draw(screen)
        japanese.draw(screen)
        japanese_shoot.draw(screen)

        clock.tick(20)
        pygame.display.flip()

        xiao_tie.run()
        japanese.run()

if __name__ =="__main__":
    step5_show_shoot_chinese()