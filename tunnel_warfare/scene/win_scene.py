from actor.win_sprite import WinSprite
from scene import BaseScene, ScenePassStatus


class WinScene(BaseScene):
    def __init__(self,xiao_tie):
        super(WinScene, self).__init__(xiao_tie,
                                           "./resources/images/win/win.jpg")
        self.actor = WinSprite(50,300)

    def draw_actor(self):
        self.actor.draw(self.current_surface,0,0)

    def run(self,down_flag,key_list):
        self.actor.run(down_flag,key_list)
        if self.actor.pos_x>1000:
            self.pass_status = ScenePassStatus.over


