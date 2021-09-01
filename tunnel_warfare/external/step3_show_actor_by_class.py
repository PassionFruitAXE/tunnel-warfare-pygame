import pygame
from pygame.constants import QUIT

from pythonProject.actor.welcome_sprite import WelcomeSprite


def lode_actor_image():
    """
    加载角色图片
    :return:
    """
    actor_images = []
    for i in range(1,10):#取值1~9
        image_path = "../resources/images/welcome/" +str(i)+ "-1.png"
        print(image_path)
        image = pygame.image.load(image_path)
        actor_images.append(image)
    return  actor_images

def step3_show_actor_by_class():
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

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(background, (0, 0))#粘贴图片
        #screen.blit(actor_images[num],(x,300))
        xiao_tie.draw(screen)

        clock.tick(20)
        pygame.display.flip()

        xiao_tie.run()


if __name__ =="__main__":
    step3_show_actor_by_class()