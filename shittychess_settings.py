#!/usr/bin/env python
# coding=utf-8


class ShittySettings:

    def __init__(self):
        self.headers = True
        self.vertical_header_size = 30
        self.horizontal_header_size = 30
        self.horizontal_headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.vertical_headers = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.header_background_color = (30, 30, 30)
        self.header_font_color = (221, 221, 221)
        self.header_font_size = 16
        self.header_font_path = 'fonts/LiberationMono-Regular.ttf'
        self.header_font_bold_path = 'fonts/LiberationMono-Bold.ttf'

        self.__screen_width = 480
        self.__screen_height = 480
        self.cols = 8
        self.rows = 8

        self.tile_image_path = 'shitty_art/shittychess_tile.png'
        self.tile_w = 120
        self.tile_h = 120
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


    # terrible name, needs to be changed
    def square_width(self) -> int:
        return int(self.tile_w / self.cols_per_tile)


    # not so terrible but still needs to be changed to match square_width's new name
    def square_height(self) -> int:
        return int(self.tile_h / self.rows_per_tile)
