import pygame
from pytmx import load_pygame, TiledObjectGroup

from actor.japanese_shoot_soldier import JapaneseShootSoldier
from actor.japanese_soldier import JapaneseWalkSoldier
from actor.prizes import PrizesSprite
from actor.red_army_shoot_soldier import RedArmyShootSoldier
from scene import BaseScene, ScenePassStatus
from scene.task import TaskStatus
from scene.task.task2_kill_japanene import KillJapaneseTask
from scene.task.task1_take_prizes import TakePrizesTask
from scene.task.task3_transmit_message import TransmitMessageTask


class TunnelWarScene(BaseScene):
    def __init__(self, xiao_tie):
        pygame.mixer.music.load("./resources/sound/十送红军.mp3")
        pygame.mixer.music.play()
        super(TunnelWarScene, self).__init__(xiao_tie, "./resources/tmx/tunnel_map.png")
        self.tiled_map_data = load_pygame("./resources/tmx/tunnel_map.tmx")
        self.obstacle_group = pygame.sprite.Group()
        self.japanese_group = pygame.sprite.Group()
        self.prizes_group = pygame.sprite.Group()
        self.xiao_tie_group = pygame.sprite.Group()
        self.init_actor()
        self.init_task()

    def init_actor(self):
        self.jian_jun = None
        self.tie_tou = None
        for group in self.tiled_map_data.objectgroups:
            if group.name == "日本人":
                for obj in group:
                    japanese = JapaneseShootSoldier(obj.x, obj.y)
                    self.japanese_group.add(japanese)
            elif group.name == "奖品":
                for obj in group:
                    prizes = PrizesSprite(obj.x, obj.y)
                    prizes.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    self.prizes_group.add(prizes)
            elif group.name == "障碍物":
                for obj in group:
                    obstacle = pygame.sprite.Sprite()
                    obstacle.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    self.obstacle_group.add(obstacle)
            elif group.name == "解放军":
                for obj in group:
                    if obj.name == "建军":
                        self.jian_jun = RedArmyShootSoldier(obj.x, obj.y)
                    if obj.name == "铁头":
                        self.tie_tou = RedArmyShootSoldier(obj.x, obj.y)

            elif group.name == "小铁":
                for obj in group:
                    if obj.name == "小铁":
                        self.xiao_tie.set_pos(obj.x, obj.y)

    def init_task(self):
        self.font = pygame.font.Font("./resources/font/迷你简粗宋.TTF", 15)
        self.tasks = []
        self.tasks.append(TakePrizesTask(self.xiao_tie, self.prizes_group, self.font))
        self.tasks.append(KillJapaneseTask(self.xiao_tie, self.japanese_group, self.font))
        self.tasks.append(TransmitMessageTask(self.xiao_tie, self.jian_jun, self.tie_tou, self.font))
        self.task_id = 0

    def draw_actor(self):
        self.xiao_tie.draw(self.current_surface, self.view_x, self.view_y)
        for japanese in self.japanese_group:
            japanese.draw(self.current_surface, self.view_x, self.view_y)
        for prizes in self.prizes_group:
            prizes.draw(self.current_surface, self.view_x, self.view_y)
        self.tasks[self.task_id].draw(self.current_surface, self.view_x, self.view_y)

    def run(self, down_flag, key_list):
        self.xiao_tie.run(down_flag, key_list, self.obstacle_group, self.japanese_group)
        for japanese in self.japanese_group:
            japanese.run(down_flag, key_list, self.obstacle_group, self.xiao_tie_group, self.xiao_tie)

        self.tasks[self.task_id].do_task(down_flag, key_list)
        take_status = self.tasks[self.task_id].get_status()

        # if key_list[pygame.K_1]:
        #     print(self.xiao_tie.pos_x, self.xiao_tie.pos_y, self.xiao_tie.rect)

        # 传送检测
        if abs(self.xiao_tie.pos_x - 3070) <= 5 and abs(self.xiao_tie.pos_y - 950) <= 30:
            self.xiao_tie.pos_x = 5
            self.xiao_tie.pos_y = 925
            self.xiao_tie.rect = pygame.Rect(self.xiao_tie.pos_x + 15, self.xiao_tie.pos_y + 60, 20, 10)

        if abs(self.xiao_tie.pos_x + 5) <= 5 and abs(self.xiao_tie.pos_y - 925) <= 25:
            self.xiao_tie.pos_x = 3060
            self.xiao_tie.pos_y = 950
            self.xiao_tie.rect = pygame.Rect(self.xiao_tie.pos_x + 15, self.xiao_tie.pos_y + 60, 20, 10)

        # 碰到日本人就被抓了
        for japanese in self.japanese_group:
            is_collide = pygame.sprite.collide_rect(self.xiao_tie, japanese)
            if is_collide:
                self.pass_status = ScenePassStatus.final_fail
                pygame.mixer.music.stop()


        if take_status == TaskStatus.win_over:
            self.task_id += 1
            if self.task_id >= len(self.tasks):
                self.pass_status = ScenePassStatus.final_win
                pygame.mixer.music.stop()
        elif take_status == TaskStatus.fail_over:
            self.pass_status = ScenePassStatus.final_fail
            pygame.mixer.music.stop()

    def get_pass_status(self):
        if self.pass_status == ScenePassStatus.final_win:
            return self.pass_status, "WinScene"
        elif self.pass_status == ScenePassStatus.final_fail:
            return self.pass_status, "FailScene"
        return ScenePassStatus.normal, None
