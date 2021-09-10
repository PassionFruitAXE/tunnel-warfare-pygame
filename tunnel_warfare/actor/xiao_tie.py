import pygame.sprite

from actor import DirWalkByAImage, WalkDir


class XiaoTie(pygame.sprite.Sprite):
    hp = 100
    name = "小铁"
    pos_x = 1000
    pos_y = 200
    image_width = 50
    image_height = 74
    current_status = "boy"
    boy_base_action = None
    army_base_action = None
    dir = WalkDir.down

    def __init__(self, x, y):
        super(XiaoTie, self).__init__()
        self.boy_base_action = DirWalkByAImage("./resources/images/chinese/militia/boy1.png",
                                               self.image_width, self.image_height, True)
        self.army_base_action = DirWalkByAImage("./resources/images/chinese/red_army/boy1.png",
                                                self.image_width, self.image_height, True)
        self.boy_base_action.set_dir(self.dir)
        self.army_base_action.set_dir(self.dir)
        self.current_action = self.boy_base_action

        self.pos_x = x
        self.pos_y = y
        self.rect = pygame.Rect(self.pos_x + 15, self.pos_y + 60, 20, 10)

    def set_status(self, status: str):
        if status == "boy":
            self.current_action = self.boy_base_action
        else:
            self.current_action = self.army_base_action

    def run(self, down_flag, key_list, obstacle_group: pygame.sprite.Group, japanese_group):
        off_x = 0
        off_y = 0

        if key_list[pygame.K_DOWN]:
            self.dir = WalkDir.down
            off_y += 10
        elif key_list[pygame.K_UP]:
            self.dir = WalkDir.up
            off_y -= 10
        elif key_list[pygame.K_LEFT]:
            self.dir = WalkDir.left
            off_x -= 10
        elif key_list[pygame.K_RIGHT]:
            self.dir = WalkDir.right
            off_x += 10
        self.boy_base_action.set_dir(self.dir)
        self.army_base_action.set_dir(self.dir)

        temp_rect = self.rect
        self.rect = self.rect.move(off_x, off_y)
        collide_list = pygame.sprite.spritecollide(self, obstacle_group, False) or pygame.sprite.spritecollide(self,
                                                                                                               japanese_group,
                                                                                                               False)
        if len(collide_list) > 0:
            self.rect = temp_rect
            pass
        else:
            self.pos_x += off_x
            self.pos_y += off_y

    def draw(self, surface: pygame.surface, x: int, y: int):
        """
        任务绘制
        :param surface:视窗图像
        :param x: 视窗左上角x
        :param y:视窗左上角y
        :return:
        """
        current_image = self.current_action.get_image()
        surface.blit(current_image, (self.pos_x - x, self.pos_y - y))
        pygame.draw.rect(surface, pygame.Color(255, 255, 0),
                         (self.pos_x - x + 15, self.pos_y - y + 60, 20, 10), 1)

    def set_pos(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.rect = pygame.Rect(self.pos_x + 15, self.pos_y + 60, 20, 10)
