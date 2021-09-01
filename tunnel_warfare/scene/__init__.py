import enum

import pygame

from actor.xiao_tie import XiaoTie
from game import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT, FULL_WIDTH, \
    FULL_HEIGHT


class ScenePassStatus(enum.IntEnum):
    final_win = 0
    final_fail = 1
    over = 3
    level_pass = 4
    level_fail = 5
    normal = 6


class BaseScene:
    def __init__(self, xiao_tie: XiaoTie, background_path):
        self.xiao_tie = xiao_tie
        self.path = background_path
        self.background_image = pygame.image.load(background_path)
        self.current_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT)).convert()

        if (self.background_image.get_width() <= SCREEN_WIDTH) and \
                (self.background_image.get_height() <= SCREEN_HEIGHT):
            self.sub_scene_flag = False
            pass
        else:
            self.sub_scene_flag = True
            pass
        self.pass_status = ScenePassStatus.normal

    def __boundary(self):
        view_x = self.xiao_tie.pos_x - SCREEN_HALF_WIDTH
        view_y = self.xiao_tie.pos_y - SCREEN_HALF_HEIGHT
        if view_x < 0:
            view_x = 0
        if view_y < 0:
            view_y = 0
        if view_x > FULL_WIDTH - SCREEN_WIDTH:
            view_x = FULL_WIDTH - SCREEN_WIDTH - 1
        if view_y > FULL_HEIGHT - SCREEN_HEIGHT:
            view_y = FULL_HEIGHT - SCREEN_HEIGHT - 1
        return view_x, view_y

    def get_current_surface(self):
        if not self.sub_scene_flag:
            self.current_surface.blit(self.background_image, self.current_surface.get_rect())
        else:
            self.view_x, self.view_y = self.__boundary()

            image = self.background_image.subsurface((self.view_x, self.view_y, SCREEN_WIDTH, SCREEN_HEIGHT))
            self.current_surface.blit(image, self.current_surface.get_rect())
        self.draw_actor()
        return self.current_surface

    def draw_actor(self):
        pass

    def run(self, down_flag, key_list):
        pass

    def get_pass_status(self):
        """
        获取通关状态
        :return:
        """
        return self.pass_status, None
