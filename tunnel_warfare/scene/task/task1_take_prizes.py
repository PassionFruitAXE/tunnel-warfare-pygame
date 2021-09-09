import pygame

from dialog.tunnel_dialog import TunnelTask1BeginDialog, TunnelTask1EndDialog, TunnelTaskFailDialog
from scene.task import BaseTask, TaskStatus


class TakePrizesTask(BaseTask):
    def __init__(self, xiao_tie, prizes_group, font):

        self.score = 0
        self.xiao_tie = xiao_tie
        self.prizes_group = prizes_group
        self.font = font

        self.start_dialog = TunnelTask1BeginDialog(font)
        self.win_dialog = TunnelTask1EndDialog(font)
        self.fail_dialog = TunnelTaskFailDialog(font)

        self.sound = pygame.mixer.Sound("./resources/sound/prizes.mp3")

        super(TakePrizesTask, self).__init__(self.start_dialog,
                                             self.win_dialog, self.fail_dialog)

    def do_self_task(self, key_down, key_list):
        temp_rect = self.xiao_tie.rect
        self.xiao_tie.rect = pygame.Rect(self.xiao_tie.pos_x + 5,
                                         self.xiao_tie.pos_y + 6, 20, 60)
        collide_list = pygame.sprite.spritecollide(self.xiao_tie, self.prizes_group, True)
        self.xiao_tie.rect = temp_rect

        if len(collide_list) > 0:
            self.score += 1
            self.sound.play()
        if self.score > 4:
            self.task_status = TaskStatus.win_dialog
