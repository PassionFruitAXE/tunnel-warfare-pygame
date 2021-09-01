import enum

import pygame

from dialog.actor_dialog import JianJunDialog, TieTouDialog
from dialog.tunnel_dialog import TunnelTask3BeginDialog, TunnelTask3EndDialog, TunnelTaskFailDialog
from scene.task import BaseTask, TaskStatus


class TransmitMessageTaskStatus(enum.IntEnum):
    finding_jian_jun = 0  # 找建军
    found_jian_jun = 1  # 找到建军，对话中
    finding_tie_tou = 2  # 找铁头
    found_tie_tou = 3  # 到到铁头，对话中
    ok = 5  # 带信成功
    fail = 6  # 带信失败


class TransmitMessageTask(BaseTask):
    def __init__(self, xiao_tie, jian_jun, tie_tou, font):
        self.jian_jun = jian_jun
        self.tie_tou = tie_tou
        self.xiao_tie = xiao_tie
        self.time_count = 100000

        self.state = TransmitMessageTaskStatus.finding_jian_jun
        self.jian_jun_dialog = JianJunDialog(self.jian_jun, font)
        self.tie_tou_dialog = TieTouDialog(self.tie_tou, font)

        self.start_dialog = TunnelTask3BeginDialog(font)
        self.win_dialog = TunnelTask3EndDialog(font)
        self.fail_dialog = TunnelTaskFailDialog(font)

        super(TransmitMessageTask, self).__init__(self.start_dialog, self.win_dialog,
                                                  self.fail_dialog)

    def draw_task(self, surface, view_x, view_y):
        self.jian_jun.draw(surface, view_x, view_y)
        if self.state == TransmitMessageTaskStatus.found_jian_jun:
            self.jian_jun_dialog.draw(surface, view_x, view_y)
        elif self.state == TransmitMessageTaskStatus.found_tie_tou:
            self.tie_tou_dialog.draw(surface, view_x, view_y)
        if self.state >= TransmitMessageTaskStatus.finding_tie_tou:
            self.tie_tou.draw(surface, view_x, view_y)

    def __do_collide_actor(self, actor):
        temp_rect = self.xiao_tie.rect
        self.xiao_tie.rect = pygame.Rect(self.xiao_tie.pos_x + 5,
                                         self.xiao_tie.pos_y + 5,
                                         20, 60)
        is_collide = pygame.sprite.collide_rect(self.xiao_tie, actor)
        self.xiao_tie.rect = temp_rect
        return is_collide

    def do_self_task(self, key_down, key_list):
        if self.state == TransmitMessageTaskStatus.finding_jian_jun:
            if self.__do_collide_actor(self.jian_jun):
                self.state = TransmitMessageTaskStatus.found_jian_jun

        elif self.state == TransmitMessageTaskStatus.found_jian_jun:
            if key_down and key_list[pygame.K_SPACE]:
                self.jian_jun_dialog.next_text()
            if self.jian_jun_dialog.is_finish():
                self.state = TransmitMessageTaskStatus.finding_tie_tou

        elif self.state == TransmitMessageTaskStatus.finding_tie_tou:
            if self.__do_collide_actor(self.tie_tou):
                self.state = TransmitMessageTaskStatus.found_tie_tou

        elif self.state == TransmitMessageTaskStatus.found_tie_tou:
            if key_down and key_list[pygame.K_SPACE]:
                self.tie_tou_dialog.next_text()
            if self.tie_tou_dialog.is_finish():
                self.state = TransmitMessageTaskStatus.ok
                self.task_status = TaskStatus.win_dialog

        self.time_count -= 1
        if self.time_count < 0:
            self.state = TransmitMessageTaskStatus.fail
            self.task_status = TaskStatus.fail_dialog
