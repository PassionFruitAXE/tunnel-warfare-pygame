import pygame
from pytmx import *
from pytmx.util_pygame import load_pygame


class TiledRender(object):
    """
    Super simple way to render a tiled map
    """
    def __init__(self, filename):
        tm = load_pygame(filename)

        # self.size will be the pixel size of the map
        # this value is used later to render the entire map to a pygame surface
        self.pixel_size = tm.width * tm.tilewidth, tm.height * tm.tileheight
        self.tmx_data = tm

        # for layer in self.tmx_data.visible_tile_layers:
        #     layer = self.tmx_data.layers[layer]
        #     for i in layer.tiles():
        #         # print(i)
        #         continue

    def render_map(self, surface):
        """ Render our map to a pygame surface
        Feel free to use this as a starting point for your pygame app.
        This method expects that the surface passed is the same pixel
        size as the map.
        Scrolling is a often requested feature, but pytmx is a map
        loader, not a renderer!  If you'd like to have a scrolling map
        renderer, please see my pyscroll project.
        """

        # fill the background color of our render surface
        if self.tmx_data.background_color:
            surface.fill(pygame.Color(self.tmx_data.background_color))

        # iterate over all the visible layers, then draw them

        for layer in self.tmx_data.visible_layers:
            # each layer can be handled differently by checking their type
            if isinstance(layer, TiledTileLayer):
                self.render_tile_layer(surface, layer)

            elif isinstance(layer, TiledObjectGroup):
                self.render_object_layer(surface, layer)

            elif isinstance(layer, TiledImageLayer):
                self.render_image_layer(surface, layer)
            elif isinstance(layer, TiledObjectGroup):
                self.render_object_layer(surface, layer)


    def render_tile_layer(self, surface, layer):
        """ Render all TiledTiles in this layer
        """
        # deref these heavily used references for speed
        tw = self.tmx_data.tilewidth
        th = self.tmx_data.tileheight
        surface_blit = surface.blit

        # iterate over the tiles in the layer, and blit them
        for x, y, image in layer.tiles():
            surface_blit(image, (x * tw, y * th))

    def render_object_layer(self, surface, layer):
        """ Render all TiledObjects contained in this layer
        """
        # deref these heavily used references for speed
        draw_rect = pygame.draw.rect
        draw_lines = pygame.draw.lines
        surface_blit = surface.blit

        # these colors are used to draw vector shapes,
        # like polygon and box shapes
        rect_color = (255, 0, 0)
        poly_color = (0, 255, 0)

        # iterate over all the objects in the layer
        # These may be Tiled shapes like circles or polygons, GID objects, or Tiled Objects
        for obj in layer:
            # objects with points are polygons or lines
            if hasattr(obj, 'points'):
                draw_lines(surface, poly_color, obj.closed, obj.points, 3)

            # some objects have an image
            # Tiled calls them "GID Objects"
            elif obj.image:
                surface_blit(obj.image, (obj.x, obj.y))

            # draw a rect for everything else
            # Mostly, I am lazy, but you could check if it is circle/oval
            # and use pygame to draw an oval here...I just do a rect.
            else:
                draw_rect(surface, rect_color,
                          (obj.x, obj.y, obj.width, obj.height), 3)

    def render_image_layer(self, surface, layer):
        if layer.image:
            surface.blit(layer.image, (0, 0))

    def blit_text(surface, text, pos, font, color=pygame.Color('red')):
        words = text.split(";")
        x, y = pos
        for line in words:
            word_surface = font.render(line, None, color)
            surface.blit(word_surface, (x, y))
            word_width, word_height = word_surface.get_size()
            y += word_height