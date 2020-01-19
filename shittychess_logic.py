# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyLogic:

    def __init__(self, settings: ShittySettings) -> None:
        self.settings = settings
        self.__coords = {}
        self.configure_layout()


    def configure_layout(self) -> None:
        for row, y in zip(self.settings.row_headers, range(0, int(self.settings.space_height() * self.settings.rows), self.settings.space_height())):
            for col, x in zip(self.settings.col_headers, range(0, int(self.settings.space_width() * self.settings.cols), self.settings.space_width())):
                pos_name = col + row
                tmp_rect = pygame.Rect(x, y, self.settings.space_width(), self.settings.space_height())
                self.__coords.update({pos_name: tmp_rect})


    def coords(self, coords: str) -> pygame.Rect:
        if self.settings.headers_enabled:
            tmp_coords = pygame.Rect(self.__coords[coords])
            tmp_coords.left += self.settings.row_header_width()
            tmp_coords.top += self.settings.col_header_height()
            return tmp_coords
        return self.__coords[coords]
