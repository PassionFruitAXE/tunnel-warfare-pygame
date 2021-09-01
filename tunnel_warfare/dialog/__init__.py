import pygame

from game import SCREEN_WIDTH
from utils.text_render import blit_text


class SysBaseDialog:
    def __init__(self,text_list:list,font):
        self.text_list = text_list
        self.current_id = 0
        self.dialog_image = pygame.image.load("./resources/images/dialog/sys_dialog.png")
        x,y,w,h = self.dialog_image.get_rect()
        self.pos_x = int((SCREEN_WIDTH-w)/2)+35
        self.pos_y = 35
        self.finish = False
        self.font = font

    def draw(self,surface):
        if self.current_id >= len(self.text_list):
            return
        else:
            surface.blit(self.dialog_image,(self.pos_x,self.pos_y))
            blit_text(surface,self.text_list[self.current_id],
                      (self.pos_x + 30,self.pos_y + 30),self.font)

    def is_finish(self):
        return self.finish

    def next_text(self):
        self.current_id += 1
        if self.current_id >= len(self.text_list):
            self.finish = True
            self.current_id >= len(self.text_list)


class ActorBaseDialog(SysBaseDialog):
    def __init__(self, actor, text_list: list,font):
        self.text_list = text_list
        self.actor = actor
        self.current_id = 0
        self.dialog_image = pygame.image.load("./resources/images/dialog/actor_dialog.png")
        self.finished = False
        self.font = font
        super(ActorBaseDialog, self).__init__(text_list, font)

    def draw(self, surface, view_x, view_y):
        if self.current_id >= len(self.text_list):
            return
        temp_x = self.actor.pos_x - view_x + 5
        temp_y = self.actor.pos_y - view_y - 55
        surface.blit(self.dialog_image, (temp_x, temp_y))
        blit_text(surface, self.text_list[self.current_id],
                  (temp_x + 10, temp_y + 10), self.font)




