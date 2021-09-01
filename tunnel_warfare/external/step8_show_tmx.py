import pygame
from pygame.constants import QUIT

from pythonProject.utils.tiled_render import TiledRender


def step8_show_tmx():
    """
    第八步：渲染图片
    :return:
    """

    pygame.init()
    icon = pygame.image.load("../resources/images/pygame图标.jpg")#设置图标
    pygame.display.set_icon(icon)

    pygame.display.set_caption("我是一个游戏")
    pygame.display.get_caption()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280,720),0,32)
    tiled_map = TiledRender("../resources/tmx/map.tmx")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        tiled_map.render_map(screen)
        clock.tick(20)
        pygame.display.flip()

if __name__ =="__main__":
    step8_show_tmx()