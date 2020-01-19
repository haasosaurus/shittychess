# coding=utf-8


import pathlib


class ShittySettings:

    def __init__(self) -> None:
        # general declarations/initializations
        self.cols = 8
        self.rows = 8
        self.tile_image_path_obj = pathlib.Path('shitty_art/shittychess_tile.png')
        self.tile_image_path = str(self.tile_image_path_obj)
        self.tile_w = 120
        self.tile_h = 120
        self.cols_per_tile = 2
        self.rows_per_tile = 2

        # header variables declarations/initializations
        self.headers_enabled = True
        self.__row_header_w = 30
        self.__col_header_h = 30
        self.col_headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.row_headers = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.header_background_color = (30, 30, 30)
        self.header_font_color = (221, 221, 221)
        self.header_font_sz = 16
        self.header_font_width = self.header_font_sz
        self.header_font_height = self.header_font_sz
        self.header_font_path_obj = pathlib.Path('fonts/LiberationMono-Regular.ttf')
        self.header_font_path = str(self.header_font_path_obj)
        self.header_font_bold_path_obj = pathlib.Path('fonts/LiberationMono-Bold.ttf')
        self.header_font_bold_path = str(self.header_font_bold_path_obj)


    def horizontal_tile_count(self) -> int:
        return int(self.cols / self.cols_per_tile)


    def vertical_tile_count(self) -> int:
        return int(self.rows / self.rows_per_tile)


    def row_header_width(self) -> int:
        return self.__row_header_w


    def row_header_height(self) -> int:
        return self.board_height() + self.col_header_height() * 2


    def col_header_width(self) -> int:
        return self.board_width() + self.row_header_width() * 2


    def col_header_height(self) -> int:
        return self.__col_header_h


    def row_header_y_start(self) -> int:
        return int(self.col_header_height() + (self.space_height() / 2) - (self.header_font_height / 2))


    def row_header_x_left(self) -> int:
        return int((self.row_header_width() - self.header_font_width) / 2)


    def row_header_x_right(self) -> int:
        return int(self.board_width() + self.row_header_width() + ((self.row_header_width() - self.header_font_width) / 2))


    def col_header_x_start(self) -> int:
        return int(self.row_header_width() + (self.space_width() / 2) - (self.header_font_width / 2))


    def col_header_y_top(self) -> int:
        return int((self.col_header_height() - self.header_font_height) / 2)


    def col_header_y_bottom(self) -> int:
        return int(self.board_height() + self.col_header_height() + ((self.col_header_height() - self.header_font_height) / 2))


    def space_width(self) -> int:
        return int(self.tile_w / self.cols_per_tile)


    def space_height(self) -> int:
        return int(self.tile_h / self.rows_per_tile)


    def board_start_x(self) -> int:
        if self.headers_enabled:
            return self.row_header_width()
        return 0


    def board_start_y(self) -> int:
        if self.headers_enabled:
            return self.col_header_height()
        return 0


    def board_width(self) -> int:
        return self.space_width() * self.cols


    def board_height(self) -> int:
        return self.space_height() * self.rows


    def screen_width(self) -> int:
        if self.headers_enabled:
            return self.board_width() + self.row_header_width() * 2
        return self.board_width()


    def screen_height(self) -> int:
        if self.headers_enabled:
            return self.board_height() + self.col_header_height() * 2
        return self.board_height()
