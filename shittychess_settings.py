#!/usr/bin/env python
# coding=utf-8


class ShittySettings:

    def __init__(self):
        self.headers = True
        self.vertical_header_size = 30
        self.horizontal_header_size = 30

        self.__screen_width = 480
        self.__screen_height = 480

        # Settings for the board
        self.tile_w = 120
        self.tile_h = 120

        self.cols = 8
        self.rows = 8

        self.cols_per_tile = 2
        self.rows_per_tile = 2


    def board_start_x(self) -> int:
        if self.headers:
            return self.vertical_header_size
        return 0


    def board_start_y(self) -> int:
        if self.headers:
            return self.horizontal_header_size
        return 0


    def screen_width(self) -> int:
        if self.headers:
            return self.__screen_width + self.vertical_header_size * 2
        else:
            return self.__screen_width


    def screen_height(self) -> int:
        if self.headers:
            return self.__screen_height + self.horizontal_header_size * 2
        else:
            return self.__screen_height


    def square_width(self) -> int:
        return int(self.tile_w / self.cols_per_tile)


    def square_height(self) -> int:
        return int(self.tile_h / self.rows_per_tile)
