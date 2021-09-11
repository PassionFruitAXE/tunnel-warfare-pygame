import pygame

from actor import DirShootByAImage, ShootDir, WalkDir
from actor.walk_soldier import WalkSoldier


class ShootSoldier(WalkSoldier):
    shoot_image_width = 100
    shoot_image_height = 100

    def __init__(self, work_image_path: str, shoot_image_path: str,
                 x: int, y: int, name: str, hp: int):
        super(ShootSoldier, self).__init__(work_image_path, x, y, name, hp)
        self.shoot_action = DirShootByAImage(shoot_image_path,
                                             self.shoot_image_width, self.shoot_image_height, True)

        self.shoot_action.set_dir(ShootDir.not_shoot)

    # 0 下 1 左  2 右 3 上
    def run(self, down_flag, key_list):
        super(ShootSoldier, self).run(down_flag, key_list)
        if down_flag:
            if key_list[pygame.K_q]:
                self.shoot_action.set_dir(ShootDir.left_up)
            elif key_list[pygame.K_a]:
                self.shoot_action.set_dir(ShootDir.left_down)
            elif key_list[pygame.K_e]:
                self.shoot_action.set_dir(ShootDir.right_up)
            elif key_list[pygame.K_d]:
                self.shoot_action.set_dir(ShootDir.right_down)
            elif key_list[pygame.K_w]:
                self.walk_action.set_dir(WalkDir.up)
                self.shoot_action.set_dir(ShootDir.up)
            elif key_list[pygame.K_s]:
                self.walk_action.set_dir(WalkDir.down)
                self.shoot_action.set_dir(ShootDir.down)

    def draw(self, surface, x: int, y: int):
        if self.shoot_action.shoot_dir == ShootDir.not_shoot:
            super(ShootSoldier, self).draw(surface, x, y)
        elif self.shoot_action.shoot_dir == ShootDir.down:
            image = self.shoot_action.get_image()
            surface.blit(image, (self.pos_x - x, self.pos_y - y))
            image = self.walk_action.get_image()
            surface.blit(image, (self.pos_x - x, self.pos_y - y))
        elif self.shoot_action.shoot_dir == ShootDir.up:
            image = self.shoot_action.get_image()
            surface.blit(image, (self.pos_x - x, self.pos_y - y - 60))
            image = self.walk_action.get_image()
            surface.blit(image, (self.pos_x - x, self.pos_y - y))
        else:
            image = self.shoot_action.get_image()
            surface.blit(image, (self.pos_x - x, self.pos_y - y))
