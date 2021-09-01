import enum

import pygame.image


class ActionByMulti:
    def __init__(self,path_expression:str, image_count:int, is_loop:bool):
        """
        初始化构造函数
        :param path_expression:路径表达式
        :param image_count:图片数量
        :param is_loop:是否循环
        """
        self.image_index = 0
        self.action_images = []
        self.image_count = image_count
        self.is_loop = is_loop

        for i in range(0,image_count):
            image_path = str.format(path_expression % (i + 1 ))
            self.action_images.append(pygame.image.load(image_path))

    def get_image(self) -> pygame.image:
        """
        获取当前图片
        :return:
        """
        current_image = self.action_images[self.image_index]

        self.image_index +=1
        if self.image_index >= self.image_count:
            if self.is_loop:
                self.image_index=0
            else:
                self.image_index=self.image_count-1;
        return current_image

    def is_end(self)->bool:
        """
        播放完毕否
        :return:
        """
        if self.is_loop:
            return False
        else:
            if self.image_index >= self.image_count-1:
                return True
            else:
                return False


class WalkDir(enum.IntEnum):
    """
    行走方向的枚举
    """
    down = 0
    left = 1
    right = 2
    up = 3

class DirWalkByAImage:
    """
    四个方向的行走 下，左，右，上
    """
    image_count =16
    image_col = 4
    image_width = 49
    image_height = 74
    walk_dir = WalkDir.down

    def __init__(self,path_name:str,image_width:int,image_height:int,is_loop:bool):
        """
        初始化
        :param path_name:
        :param image_width:
        :param image_height:
        :param is_loop:
        """
        self.path_name = path_name
        self.image_index = 0
        self.action_images = []#四个方向的数组
        self.image_width=image_width
        self.image_height=image_height
        self.is_loop = is_loop
        self.image = pygame.image.load(path_name)
        for i in range(0, self.image_count):
           row = int(i/self.image_col)
           col = i % self.image_col
           if col == 0:
               dir = []
               self.action_images.append(dir)
           rect = (col * self.image_width,
                   row * self.image_height,
                   self.image_width,self.image_height)

           sub_image = self.image.subsurface(rect)
           dir.append(sub_image)

    def get_image(self)->pygame.image:
        current_image = self.action_images[self.walk_dir][self.image_index]
        self.image_index += 1;
        if self.image_index >= self.image_col:
            if self.is_loop:
                self.image_index=0
            else:
                self.image_index = self.col-1
        return current_image

    def set_dir(self,dir):
        self.walk_dir = dir

    def is_end(self)->bool:
        if self.is_loop:
            return False
        else:
            if self.image_index == self.image_col - 1:
                return True
            else:
                return False

class ShootDir(enum.IntEnum):
    not_shoot = 0
    left_down = 1
    right_down = 2
    left_up = 3
    right_up = 4
    up = 5
    down = 6


class DirShootByAImage(DirWalkByAImage):
    shoot_dir = ShootDir.not_shoot

    @staticmethod
    def __init_load_shoot_image():
        """
        初始化射击图片
        :param up_image_path:
        :param down_image_path:
        :return:
        """

        DirShootByAImage.up_shoot_image = pygame.image.load("./resources/images/shoot/up_shoot.png")\
            .convert_alpha()
        DirShootByAImage.down_shoot_image = pygame.image.load("./resources/images/shoot/down_shoot.png")\
            .convert_alpha()

    def __init__(self, shoot_image_path: str, image_width: int
                 , image_height: int, is_loop):
        super(DirShootByAImage, self).__init__(shoot_image_path, image_width, image_height, is_loop)
        self.__init_load_shoot_image()

    def get_image(self) -> pygame.surface:
        """
        获取射击图片
        :return:
        """
        if self.shoot_dir == ShootDir.not_shoot:
            return None
        if self.shoot_dir  < ShootDir.up:
            current_image = self.action_images[self.shoot_dir - 1][self.image_index]
            self.image_index += 1
            if self.image_index >= self.image_col:
                if self.is_loop:
                    self.image_index = 0
                else:
                    self.image_index = self.image_col - 1
        elif self.shoot_dir  == ShootDir.up:
            current_image = DirShootByAImage.up_shoot_image
        else:
            current_image = DirShootByAImage.down_shoot_image
        return current_image

    def set_dir(self, dir: ShootDir):
        """
        获取射击方向
        :param dir:
        :return:
        """
        self.shoot_dir = dir


