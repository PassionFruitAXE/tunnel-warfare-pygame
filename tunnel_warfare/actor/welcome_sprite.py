import pygame.sprite

from actor import ActionByMulti


class WelcomeSprite(pygame.sprite.Sprite):
    def __init__(self,x:int,y:int):
        """
        初始化欢迎精灵
        :param x:x坐标
        :param y:y坐标
        """

        super(WelcomeSprite,self).__init__()
        self.action = ActionByMulti("./resources/images/welcome/%d-1.png",8,True)
        self.pos_x = x
        self.pos_y = y

    def draw(self,surface:pygame.surface,x:int, y:int):
        """
        绘制
        :param surface:背景
        :return:
        """

        current_image = self.action.get_image()
        surface.blit(current_image,(self.pos_x-x,self.pos_y-y))

    def run(self,down_flag,key_list):
        """
        运动
        :return:
        """

        if self.pos_x <1050 :
            self.pos_x += 10
