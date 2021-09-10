import pygame

from scene.fail_scene import FailScene
from scene.tunnel_war_scene import TunnelWarScene
from scene.win_scene import WinScene
from actor.xiao_tie import XiaoTie
from game import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
from scene import ScenePassStatus
from scene.welcome_scene import WelcomeScene


class TunnelWarGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(GAME_TITLE)
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.xiao_tie = XiaoTie(3070, 1460)
        self.current_scene = WelcomeScene(self.xiao_tie)

    def run(self):
        while True:
            # 游戏循环
            down_flag = False
            for event in pygame.event.get():
                # 关闭事件，进行退出处理
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    down_flag = True
            key_list = pygame.key.get_pressed()

            # 1.获取场景的视窗图像
            current_surface = self.current_scene.get_current_surface()
            # 2.绘制窗口
            self.surface.blit(current_surface, (0, 0))
            # 3.场景的运动
            self.current_scene.run(down_flag, key_list)
            # 4.切换场景
            pass_status, next_scene_name = self.current_scene.get_pass_status()
            if pass_status != ScenePassStatus.normal:
                if next_scene_name:
                    next_scene = globals()[next_scene_name](self.xiao_tie)
                    self.current_scene = next_scene
                else:
                    break

            # 通过时钟对象指定循环频
            self.clock.tick(40)
            # 调用flip方法更新显示,也可以使用update方法
            pygame.display.flip()
