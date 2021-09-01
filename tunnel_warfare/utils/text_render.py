import pygame


def blit_text(surface,text,pos,font,color=pygame.Color('red')):
    words = text.split(";")
    x,y = pos
    for line in words:
        word_surface = font.render(line,None,color)
        surface.blit(word_surface,(x,y))
        word_width, word_height = word_surface.get_size()
        y+=word_height