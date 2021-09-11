import random

import pygame

from actor import WalkDir, ShootDir
from actor.shoot_soldier import ShootSoldier


class JapaneseShootSoldier(ShootSoldier):
    def __init__(self, x, y):
        super(JapaneseShootSoldier, self).__init__("./resources/images/japanese/soldier2.png",
                                                   "./resources/images/japanese/soldier2-1.png",
                                                   x, y, "日军", 100)
        self.count = 10

    def run(self, down_flag, key_list, obstacle_group, xiao_tie_group, xiao_tie):
        # super(ShootSoldier, self).run(down_flag, key_list)
        if self.count == 0:
            key = random.randint(0, 3)
            self.count = 5
            if key == 0:
                self.walk_action.set_dir(WalkDir.left)
                self.shoot_action.set_dir(ShootDir.left_down)
            elif key == 1:
                self.walk_action.set_dir(WalkDir.right)
                self.shoot_action.set_dir(ShootDir.right_down)
            elif key == 2:
                self.walk_action.set_dir(WalkDir.up)
                self.shoot_action.set_dir(ShootDir.up)
            elif key == 3:
                self.walk_action.set_dir(WalkDir.down)
                self.shoot_action.set_dir(ShootDir.down)
        else:
            self.count = 0
        off_x = 0
        off_y = 0

        if self.walk_action.walk_dir == WalkDir.down:
            off_y += 5
        elif self.walk_action.walk_dir == WalkDir.up:
            off_y += -5
        elif self.walk_action.walk_dir == WalkDir.left:
            off_x += -5
        elif self.walk_action.walk_dir == WalkDir.right:
            off_x += 5

        temp_rect = self.rect
        self.rect = self.rect.move(off_x, off_y)
        collide_list = pygame.sprite.spritecollide(self, obstacle_group, False) or pygame.sprite.spritecollide(self,
                                                                                                               xiao_tie_group,
                                                                                                               False)
        if len(collide_list) > 0:
            self.rect = temp_rect
        else:
            self.pos_x += off_x
            self.pos_y += off_y
