import random

import pygame

from actor import WalkDir
from actor.walk_soldier import WalkSoldier


class JapaneseWalkSoldier(WalkSoldier):
    def __init__(self,x,y):
        soldier_id = random.randint(1,4)
        walk_image_path = "./resources/images/japanese/soldier{0}.png".format(soldier_id)
        super(JapaneseWalkSoldier, self).__init__(walk_image_path,x,y,"小日本"+str(soldier_id),
                                                 100)
        self.count = 10

    def run(self, down_flag, key_list, obstacle_group,xiao_tie_group):

        if self.count == 0:
            key = random.randint(0,3)
            self.count = 5
            if key == 0:
                self.walk_action.set_dir(WalkDir.down)
            elif key == 1:
                self.walk_action.set_dir(WalkDir.up)
            elif key == 2:
                self.walk_action.set_dir(WalkDir.left)
            elif key == 3:
                self.walk_action.set_dir(WalkDir.right)
        else:
            self.count = 0

        off_x = 0
        off_y = 0

        if self.walk_action.walk_dir == WalkDir.down:
            off_y += 10
        elif self.walk_action.walk_dir == WalkDir.up:
            off_y += -10
        elif self.walk_action.walk_dir == WalkDir.left:
            off_x += -10
        elif self.walk_action.walk_dir == WalkDir.right:
            off_x += 10

        temp_rect = self.rect
        self.rect = self.rect.move(off_x, off_y)
        collide_list = pygame.sprite.spritecollide(self, obstacle_group, False) or pygame.sprite.spritecollide(self,xiao_tie_group,False)
        if len(collide_list) > 0:
            self.rect = temp_rect
        else:
            self.pos_x += off_x
            self.pos_y += off_y



