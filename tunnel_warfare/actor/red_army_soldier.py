import random

from actor.walk_soldier import WalkSoldier


class RedArmyWalkSoldier(WalkSoldier):
    def __init__(self, x, y):
        soldier_id = random.randint(1, 2)
        walk_image_path = "./resources/images/chinese/red_army/red_army{0}.png".format(soldier_id)
        super(RedArmyWalkSoldier, self).__init__(walk_image_path, x, y, "红军" + str(soldier_id),
                                                 100)
