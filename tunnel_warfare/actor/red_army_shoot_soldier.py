import pygame

from actor.shoot_soldier import ShootSoldier


class RedArmyShootSoldier(ShootSoldier):
    def __init__(self, x, y):
        super(RedArmyShootSoldier, self).__init__("./resources/images/chinese/red_army/red_army1.png",
                                                  "./resources/images/chinese/red_army/red_army1-1.png",
                                                  x, y, "红军", 100)
