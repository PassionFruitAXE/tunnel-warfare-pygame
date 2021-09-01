import pygame
from pygame.constants import QUIT
from pytmx import load_pygame, TiledObjectGroup

from pythonProject.actor.red_army_shoot_soldier import RedArmyShootSoldier


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

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    background = pygame.image.load("../resources/tmx/map02.png")
    tiled_map_data = load_pygame("../resources/tmx/map_1.tmx")
    for layer in tiled_map_data.visible_layers:
        if isinstance(layer, TiledObjectGroup):
            if layer.name == "日本人":
                print("发现日本人")
                for obj in layer:
                    print(obj.x, obj.y)
            if layer.name == "奖品":
                print("发现奖品")
                for obj in layer:
                    print(obj.x, obj.y)
            if layer.name == "xiao_tie":
                print("发现小铁")
                for obj in layer:
                    print(obj.x, obj.y)
            if layer.name == "解放军":
                print("发现解放军")
                for obj in layer:
                    print(obj.x, obj.y)
            if layer.name == "障碍物":
                print("遇到障碍物")
                for obj in layer:
                    print(obj.x, obj.y)

    chinese = RedArmyShootSoldier(600,300)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                chinese.run(event.key)


        screen.blit(background, (0, 0))#粘贴图片
        chinese.draw(screen)

        clock.tick(20)
        pygame.display.flip()

if __name__ =="__main__":
    step5_show_shoot_chinese()