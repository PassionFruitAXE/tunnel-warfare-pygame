import pygame.sprite

from actor import DirWalkByAImage, WalkDir


class WalkSoldier(pygame.sprite.Sprite):
    hp = 100
    name = '某军'
    pos_x = 100
    pos_y = 300
    image_width = 50
    image_height = 100

    walk_action = None
    rect = ()

    def __init__(self, walk_path: str, x, y, name, hp):
        super(WalkSoldier, self).__init__()
        self.walk_action = DirWalkByAImage(walk_path, self.image_width,
                                           self.image_height, True)
        self.walk_action.set_dir(WalkDir.down)
        self.pos_x = x
        self.pos_y = y
        self.name = name
        self.hp = hp
        self.rect = pygame.Rect(x, y, self.image_width, self.image_height)

    def run(self, down_flag, key_list):
        if key_list[pygame.K_DOWN]:
            self.walk_action.set_dir(WalkDir.down)
            self.pos_y += 5
        elif key_list[pygame.K_UP]:
            self.walk_action.set_dir(WalkDir.up)
            self.pos_y -= 5
        elif key_list[pygame.K_LEFT]:
            self.walk_action.set_dir(WalkDir.left)
            self.pos_x -= 5
        elif key_list[pygame.K_RIGHT]:
            self.walk_action.set_dir(WalkDir.right)
            self.pos_x += 5

    def draw(self, surface: pygame.Surface, x: int, y: int):
        current_image = self.walk_action.get_image()
        surface.blit(current_image, (self.pos_x - x, self.pos_y - y))
        rect_x, rect_y, w, h = self.rect
        pygame.draw.rect(surface, pygame.Color(255, 255, 0), (rect_x - x, rect_y - y, w, h), 1)