# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyLogic:

    def __init__(self, settings: ShittySettings) -> None:
        self.settings = settings
        self.__coords = {}
        self.board_grid = []  # i don't know if this is needed
        self.configure_layout()
        self.initialize_board_grid()


    def initialize_board_grid(self) -> None:
        for row_number in self.settings.row_headers:
            row_list = []
            for col_letter in self.settings.col_headers:
                row_list.append(f'{col_letter}{row_number}')
            self.board_grid.append(row_list)

        if self.settings.debug:
            self.print_board_grid()


    def print_board_grid(self) -> None:
        for row in self.board_grid:
            print(' '.join(row))


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
