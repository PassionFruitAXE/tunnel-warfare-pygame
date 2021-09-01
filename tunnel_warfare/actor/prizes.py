import random

import pygame.sprite


class PrizesSprite(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(PrizesSprite, self).__init__()
        id = random.randint(1,4)
        self.image = pygame.image.load("./resources/images/prizes/prizes"+str(id)+".png")
        self.pos_x = x
        self.pos_y = y

    def draw(self,surface,x,y):
        surface.blit(self.image,(self.pos_x - x,self.pos_y - y))

    def run(self, down_flag,key_list):
        pass