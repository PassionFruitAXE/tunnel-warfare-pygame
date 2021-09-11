import pygame

from actor.welcome_sprite import WelcomeSprite
from scene import BaseScene, ScenePassStatus


class WelcomeScene(BaseScene):
    def __init__(self, xiao_tie):
        super(WelcomeScene, self).__init__(xiao_tie,
                                           "./resources/images/welcome/welcome.jpg")
        self.actor = WelcomeSprite(50, 300)
        pygame.mixer.music.load("./resources/sound/地道战.mp3")
        pygame.mixer.music.play(start=20)

    def draw_actor(self):
        self.actor.draw(self.current_surface, 0, 0)

    def run(self, down_flag, key_list):
        self.actor.run(down_flag, key_list)
        if self.actor.pos_x > 1000:
            self.actor.pos_x = 0
        if key_list[pygame.K_SPACE]:
            self.pass_status = ScenePassStatus.over
            pygame.mixer.music.stop()

    def get_pass_status(self):
        if self.pass_status != ScenePassStatus.over:
            return self.pass_status, None
        else:
            return self.pass_status, "TunnelWarScene"
