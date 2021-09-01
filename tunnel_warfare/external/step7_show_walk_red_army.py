import pygame
from pygame.constants import QUIT

from pythonProject.actor.red_army_soldier import RedArmyWalkSoldier
from pythonProject.actor.welcome_sprite import WelcomeSprite


def step7_show_walk_red_army():
    """
    step3:显示角色
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
    red_army = RedArmyWalkSoldier(400,300)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                red_army.run(event.key)


        screen.blit(background, (0, 0))#粘贴图片
        xiao_tie.draw(screen)
        red_army.draw(screen)

        clock.tick(20)
        pygame.display.flip()

        xiao_tie.run()


if __name__ =="__main__":
    step7_show_walk_red_army()