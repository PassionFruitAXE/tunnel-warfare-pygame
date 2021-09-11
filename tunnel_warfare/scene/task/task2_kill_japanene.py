import pygame.sprite

from actor.mine_boom import Mine, Boom
from dialog.tunnel_dialog import TunnelTask2BeginDialog, TunnelTask2EndDialog, TunnelTaskFailDialog
from scene.task import BaseTask, TaskStatus


class KillJapaneseTask(BaseTask):
    def __init__(self, xiao_tie, japanese_group, font):
        self.japanese_group = japanese_group
        self.xiao_tie = xiao_tie
        self.mines_group = pygame.sprite.Group()
        self.booms_group = pygame.sprite.Group()

        self.score = 0
        mine = pygame.image.load("./resources/images/mine/mine.png")
        self.mine_image = pygame.transform.scale(mine, (40, 40))
        self.boom_image = pygame.image.load("./resources/images/mine/boom.png")

        self.start_dialog = TunnelTask2BeginDialog(font)
        self.win_dialog = TunnelTask2EndDialog(font)
        self.fail_dialog = TunnelTaskFailDialog(font)

        super(KillJapaneseTask, self).__init__(self.start_dialog, self.win_dialog, self.fail_dialog)

    def draw_task(self, surface, view_x, view_y):
        for mine in self.mines_group:
            mine.draw(surface, view_x, view_y)

        for boom in self.booms_group:
            boom.draw(surface, view_x, view_y)

    def do_self_task(self, key_down, key_list):
        collide_list = pygame.sprite.groupcollide(self.mines_group, self.japanese_group, True, True)
        for item in collide_list:
            self.__create_boom(item.rect.x - item.rect.width + 20,
                               item.rect.y - item.rect.height + 20)
            self.score += 1

        if self.score > 4:
            self.task_status = TaskStatus.win_dialog
            self.xiao_tie.set_status("army")

        if key_down and key_list[pygame.K_SPACE]:
            self.__create_mine(self.xiao_tie.pos_x, self.xiao_tie.pos_y)

        for boom in self.booms_group:
            if boom.kill_flag():
                self.booms_group.remove(boom)
                # boom.kill()

    def __create_mine(self, x, y):
        mine = Mine(x, y, self.mine_image)
        self.mines_group.add(mine)

    def __create_boom(self, x, y):
        boom = Boom(x, y, self.boom_image, 4, 3)
        self.booms_group.add(boom)
