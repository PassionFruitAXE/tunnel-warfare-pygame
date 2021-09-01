import pygame, sys

from pygame.locals import *

pygame.init()
# 在导入了pygame之后并且在调用任何其他的Pygame函数之前，总是需要调用该函数。
# 现在不需要知道这个函数到底做些什么，只需要知道，要让众多的Pygame函数能够工作，我们需要先调用这个函数。
# 如果你看到诸如pygame.error:font not initialized的一个错误，检查看看是否在程序的开始处忘记调用pygame.init()了。
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
