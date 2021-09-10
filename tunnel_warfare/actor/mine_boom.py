import pygame.sprite


class Mine(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Mine, self).__init__()
        self.pos_x = x
        self.pos_y = y
        self.image = image
        x, y, w, h = self.image.get_rect()
        self.rect = pygame.Rect(self.pos_x, self.pos_y, w, h)

    def draw(self, surface, view_x, view_y):
        surface.blit(self.image, (self.pos_x - view_x, self.pos_y - view_y))


class Boom(pygame.sprite.Sprite):
    def __init__(self, x, y, image, row, col):
        super(Boom, self).__init__()
        self.row = row
        self.col = col
        self.pos_x = x
        self.pos_y = y
        self.image = image
        x, y, w, h = self.image.get_rect()

        w = int(w / col)
        h = int(h / row)
        self.no = 0
        self.count = row * col
        self.boom_image = []
        for i in range(0, self.count):
            temp_row = int(i / self.col)
            temp_col = i % self.col
            rect = (temp_col * w, temp_row * h, w, h)
            image = self.image.subsurface(rect)
            self.boom_image.append(image)

        self.show_count = 0

    def draw(self, surface, view_x, view_y):
        if self.no >= self.count - 1:
            return
        self.show_count += 1
        if self.show_count > 5:
            self.no += 1
            self.show_count = 0
            if self.no >= self.count:
                return
        surface.blit(self.boom_image[self.no],
                     (self.pos_x - view_x, self.pos_y - view_y))

    def kill_flag(self):
        if self.no >= self.count:
            return True
        else:
            return False
