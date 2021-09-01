import pygame
from pygame.constants import QUIT


def step2_show_image():
    """
    第二步：pygame基本结构
    :return:
    """

    pygame.init()
    icon = pygame.image.load("../resources/images/pygame图标.jpg")#设置图标
    pygame.display.set_icon(icon)

    pygame.display.set_caption("我是一个游戏")
    pygame.display.get_caption()

    clock = pygame.time.Clock()
    #screen = pygame.display.set_mode((640, 426), 0, 32)#显示屏幕的大小
    screen = pygame.display.set_mode((600,400),pygame.RESIZABLE)
    background = pygame.image.load("../resources/images/地道战图片.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))#粘贴图片
        clock.tick(20)
        pygame.display.flip()

if __name__ =="__main__":
    step2_show_image()