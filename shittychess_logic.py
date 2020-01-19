# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyLogic:

    def __init__(self, settings: ShittySettings):
        self.settings = settings
        self.__coords = {}
        self.configure_layout()


    def configure_layout(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = ['8', '7', '6', '5', '4', '3', '2', '1']
        for row, y in zip(rows, range(0, int(self.settings.square_height() * self.settings.rows), self.settings.square_height())):
            for col, x in zip(cols, range(0, int(self.settings.square_width() * self.settings.cols), self.settings.square_width())):
                pos_name = col + row
                tmp_rect = pygame.Rect(x, y, self.settings.square_width(), self.settings.square_height())
                self.__coords.update({pos_name: tmp_rect})


    def coords(self, coords: str) -> pygame.Rect:
        if self.settings.headers:
            tmp_coords = pygame.Rect(self.__coords[coords])
            tmp_coords.left += self.settings.vertical_header_size
            tmp_coords.top += self.settings.horizontal_header_size
            return tmp_coords
        return self.__coords[coords]
