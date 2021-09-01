import pygame
from pytmx import load_pygame

from pythonProject.actor.japanese_soldier import JapaneseWalkSoldier
from pythonProject.actor.red_army_shoot_soldier import RedArmyShootSoldier
from pythonProject.actor.welcome_sprite import WelcomeSprite


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
                    xiao_tie = WelcomeSprite(obj.x, obj.y)
    return xiao_tie, jian_jun, tie_tou

def step9_create_sprite():
    """
    step9: 创建人物精灵
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
                xiao_tie.run()
        # 绘制图片到显示窗口
        screen.blit(background, (0, 0))
        xiao_tie.draw(screen)
        jian_jun.draw(screen)
        tie_tou.draw(screen)
        for japanese in japanese_group:
            japanese.draw(screen)
            japanese.run()
        # 通过时钟对象指定循环频
        clock.tick(20)
        # 调用flip方法更新显示,也可以使用update方法
        pygame.display.flip()


if __name__=="__main__":
    step9_create_sprite()