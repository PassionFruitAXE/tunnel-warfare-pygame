import pygame
from pytmx import load_pygame

from pythonProject.actor.japanese_soldier import JapaneseWalkSoldier
from pythonProject.actor.red_army_shoot_soldier import RedArmyShootSoldier
from pythonProject.actor.xiao_tie import XiaoTie
from pythonProject.game import SCREEN_HALF_WIDTH, SCREEN_HALF_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH


def boundary(x,y):
    view_x = x - SCREEN_HALF_WIDTH
    view_y = y - SCREEN_HALF_HEIGHT
    if view_x<0:
        view_x = 0
    if view_y<0:
        view_y = 0
    if view_y > 1200 - SCREEN_HEIGHT:
        view_y = 1200 - SCREEN_HEIGHT - 1
    if view_x >2800 - SCREEN_WIDTH:
        view_x = 2800 -SCREEN_WIDTH - 1
    return view_x,view_y

def create_sprite(tiled_map_data,obstacle_group,japanese_group,prizes_group):
    xiao_tie = None
    jian_jun = None
    tie_tou = None
    for group in tiled_map_data.objectgroups:
        if group.name == "日本人":
            for obj in group:
                japanese = JapaneseWalkSoldier(obj.x, obj.y)
                japanese_group.add(japanese)
        elif group.name == "奖品":
            for obj in group:
                prizes = pygame.sprite.Sprite()
                prizes.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                prizes_group.add(prizes)
        elif group.name == "障碍物":
            for obj in group:
                obstacle = pygame.sprite.Sprite()
                obstacle.rect = pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                obstacle_group.add(obstacle)
        elif group.name == "解放军":
            for obj in group:
                if obj.name == "建军":
                    jian_jun = RedArmyShootSoldier(obj.x, obj.y)
                if obj.name == "铁头":
                    tie_tou = RedArmyShootSoldier(obj.x, obj.y)

        elif group.name == "小铁":
            for obj in group:
                if obj.name == "小铁":
                    xiao_tie = XiaoTie(obj.x, obj.y)
    return xiao_tie, jian_jun, tie_tou

def step10_screen_view():
    """
    step10: 创建视图移动。
    :return:
    """
    # 初始化pygame
    pygame.init()
    #游戏图标
    icon = pygame.image.load("../resources/images/pygame图标.jpg")  # 设置图标
    pygame.display.set_icon(icon)
    #游戏标题
    pygame.display.set_caption("我是一个游戏")
    pygame.display.get_caption()
    # 获取游戏时钟
    clock = pygame.time.Clock()
    # 创建游戏的窗口 640 * 236 根据要显示图片的大小设置
    screen = pygame.display.set_mode((1280, 720), 0, 32)
    # 加载图片文件
    background = pygame.image.load("../resources/tmx/map02.png")
    tiled_map_data = load_pygame("../resources/tmx/map_1.tmx")

    obstacle_group = pygame.sprite.Group()
    japanese_group = pygame.sprite.Group()
    prizes_group = pygame.sprite.Group()
    xiao_tie, jian_jun, tie_tou = create_sprite(tiled_map_data,obstacle_group,japanese_group,prizes_group)

    while True:
        # 游戏循环
        for event in pygame.event.get():
            # 关闭事件，进行退出处理
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                xiao_tie.run(event.key)

        # 绘制图片到显示窗口
        view_x, view_y = boundary(xiao_tie.pos_x,xiao_tie.pos_y)
        sub_view = background.subsurface((view_x,view_y,SCREEN_WIDTH,SCREEN_HEIGHT))
        screen.blit(sub_view, (0, 0))
        xiao_tie.draw(screen,view_x,view_y)

        # 通过时钟对象指定循环频
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()


if __name__=="__main__":
    step10_screen_view()