# coding=utf-8


from typing import NoReturn

import pathlib


class ShittySettings:
    """class to store the game settings in"""

    def __init__(self) -> NoReturn:
        # general declarations/initializations
        self.debug = True
        self.cols = 8
        self.rows = 8
        self.tile_image_path_obj = pathlib.Path('shitty_art/shittychess_tile.png')
        self.tile_image_path = str(self.tile_image_path_obj)
        self.tile_w = 120
        self.tile_h = 120
        self.cols_per_tile = 2
        self.rows_per_tile = 2
        self.coords_list = []

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

        # assorted colors
        self.color_white = (255, 255, 255)
        self.color_light_blue = (140, 240, 255)
        self.color_blue = (0, 0, 255)

        # game state variables
        self.exiting = False
        self.turn_black = False

    def horizontal_tile_count(self) -> int:
        """returns the amount of tiles needed to the draw board - horizontally"""

        return int(self.cols / self.cols_per_tile)

    def vertical_tile_count(self) -> int:
        """returns the amount of tiles needed to draw the board - vertically"""

        return int(self.rows / self.rows_per_tile)

    def row_header_width(self) -> int:
        """returns row header width in pixels"""

        return self.__row_header_w

    def row_header_height(self) -> int:
        """returns row header height in pixels"""

        return self.board_height() + self.col_header_height() * 2

    def col_header_width(self) -> int:
        """returns column header width in pixels"""

        return self.board_width() + self.row_header_width() * 2

    def col_header_height(self) -> int:
        """returns column header height in pixels"""

        return self.__col_header_h

    def row_header_y_start(self) -> int:
        """
        returns the y coordinate to start iterating the row header labels at
        increment it by self.space_height()
        """

        return int(self.col_header_height() + (self.space_height() / 2) - (self.header_font_height / 2))

    def row_header_x_left(self) -> int:
        """returns the x coordinate for all left row header labels"""

        return int((self.row_header_width() - self.header_font_width) / 2)

    def row_header_x_right(self) -> int:
        """returns the x coordinate for all right row header labels"""

        return int(self.board_width() + self.row_header_width() + ((self.row_header_width() - self.header_font_width) / 2))

    def col_header_x_start(self) -> int:
        """
        returns the x coordinate to start iterating the column header labels at
        increment it by self.space_width()
        """

        return int(self.row_header_width() + (self.space_width() / 2) - (self.header_font_width / 2))

    def col_header_y_top(self) -> int:
        """returns the y coordinate for all top column header labels"""

        return int((self.col_header_height() - self.header_font_height) / 2)

    def col_header_y_bottom(self) -> int:
        """returns the y coordinate for all bottom column header labels"""

        return int(self.board_height() + self.col_header_height() + ((self.col_header_height() - self.header_font_height) / 2))

    def space_width(self) -> int:
        """returns the width of a board space in pixels"""

        return int(self.tile_w / self.cols_per_tile)

    def space_height(self) -> int:
        """returns the height of a board space in pixels"""

        return int(self.tile_h / self.rows_per_tile)

    def board_start_x(self) -> int:
        """
        returns the x coordinate for the left of the game board
        for use iterating the board tiles, etc
        """

        if self.headers_enabled:
            return self.row_header_width()
        return 0

    def board_start_y(self) -> int:
        """
        returns the y coordinate for the top of the game board
        for use iterating board tiles, etc
        """

        if self.headers_enabled:
            return self.col_header_height()
        return 0

    def board_width(self) -> int:
        """returns the width of the board in pixels"""

        return self.space_width() * self.cols

    def board_height(self) -> int:
        """returns the height of the board in pixels"""

        return self.space_height() * self.rows

    def screen_width(self) -> int:
        """returns the width of the screen in pixels"""

        if self.headers_enabled:
            return self.board_width() + self.row_header_width() * 2
        return self.board_width()

    def screen_height(self) -> int:
        """returns the height of the screen in pixels"""

        if self.headers_enabled:
            return self.board_height() + self.col_header_height() * 2
        return self.board_height()
