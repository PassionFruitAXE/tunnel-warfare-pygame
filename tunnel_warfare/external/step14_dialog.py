import pygame
from pygame.constants import QUIT

from pythonProject.actor.xiao_tie import XiaoTie
from pythonProject.dialog.actor_dialog import JianJunDialog
from pythonProject.dialog.tunnel_dialog import TunnelTask1BeginDialog


def step14_dialog():
    """
    step14_dialog
    :return:
    """

    pygame.init()
    icon = pygame.image.load("./resources/images/pygame图标.jpg")#设置图标
    pygame.display.set_icon(icon)

    pygame.display.set_caption("我是一个游戏")
    pygame.display.get_caption()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720), 0, 32)#显示屏幕的大小
    #screen = pygame.display.set_mode((600,400),pygame.RESIZABLE)
    background = pygame.image.load("./resources/images/welcome/welcome.jpg").convert()
    font = pygame.font.Font("./resources/font/迷你简粗宋.TTF",15)
    actor = XiaoTie(50,200)
    sys_dialog = TunnelTask1BeginDialog(font)
    actor_dialog = JianJunDialog(actor,font)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                sys_dialog.next_text()
                actor_dialog.next_text()
        screen.blit(background, (0, 0))#粘贴图片
        actor.draw(screen,0,0)
        sys_dialog.draw(screen)
        actor_dialog.draw(screen,0,0)
        clock.tick(20)
        pygame.display.flip()

if __name__ =="__main__":
    step14_dialog()