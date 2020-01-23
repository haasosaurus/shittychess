# coding=utf-8

from os import PathLike
from typing import NoReturn

import pathlib


class ShittySettings:
    """class to store the game settings in"""

    def __init__(self) -> NoReturn:
        """constructor"""

        # general declarations/initializations
        app_icon = pathlib.Path('shitty_art/shitty_knight_black.png')
        self.app_icon_path = str(app_icon)
        self.debug = True
        self.cols = 8
        self.rows = 8
        self.__space_width = 60
        self.__space_height = 60

        # board theme image paths
        self.space_path_solid_black = 'shitty_art/space_solid_black.png'
        self.space_path_solid_white = 'shitty_art/space_solid_white.png'

        self.space_path_wood_black = 'shitty_art/space_wood_black.png'
        self.space_path_wood_white = 'shitty_art/space_wood_white.png'

        # game piece image paths
        self.shitty_pawn_black_path = 'shitty_art/shitty_pawn_black.png'
        self.shitty_pawn_white_path = 'shitty_art/shitty_pawn_white.png'
        self.shitty_rook_black_path = 'shitty_art/shitty_rook_black.png'
        self.shitty_rook_white_path = 'shitty_art/shitty_rook_white.png'
        self.shitty_bishop_black_path = 'shitty_art/shitty_bishop_black.png'
        self.shitty_bishop_white_path = 'shitty_art/shitty_bishop_white.png'
        self.shitty_knight_black_path = 'shitty_art/shitty_knight_black.png'
        self.shitty_knight_white_path = 'shitty_art/shitty_knight_white.png'
        self.shitty_queen_black_path = 'shitty_art/shitty_queen_black.png'
        self.shitty_queen_white_path = 'shitty_art/shitty_queen_white.png'
        self.shitty_king_black_path = 'shitty_art/shitty_king_black.png'
        self.shitty_king_white_path = 'shitty_art/shitty_king_white.png'

        self.trad_pawn_black_path = 'shitty_art/trad_pawn_black.png'
        self.trad_pawn_white_path = 'shitty_art/trad_pawn_white.png'
        self.trad_rook_black_path = 'shitty_art/trad_rook_black.png'
        self.trad_rook_white_path = 'shitty_art/trad_rook_white.png'
        self.trad_bishop_black_path = 'shitty_art/trad_bishop_black.png'
        self.trad_bishop_white_path = 'shitty_art/trad_bishop_white.png'
        self.trad_knight_black_path = 'shitty_art/trad_knight_black.png'
        self.trad_knight_white_path = 'shitty_art/trad_knight_white.png'
        self.trad_queen_black_path = 'shitty_art/trad_queen_black.png'
        self.trad_queen_white_path = 'shitty_art/trad_queen_white.png'
        self.trad_king_black_path = 'shitty_art/trad_king_black.png'
        self.trad_king_white_path = 'shitty_art/trad_king_white.png'

        # header variables declarations/initializations
        self.headers_enabled = True
        self.__row_header_width = 30
        self.__col_header_height = 30
        self.col_headers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.row_headers = ['8', '7', '6', '5', '4', '3', '2', '1']
        self.header_background_color = (30, 30, 30)
        self.header_font_color = (221, 221, 221)
        self.header_font_sz = 15
        self.header_font_width = self.header_font_sz
        self.header_font_height = self.header_font_sz
        header_font = pathlib.Path('fonts/LiberationMono-Regular.ttf')
        self.header_font_path = str(header_font)
        header_font_bold = pathlib.Path('fonts/LiberationMono-Bold.ttf')
        self.header_font_bold_path = str(header_font_bold)

        # assorted colors
        self.color_white = (255, 255, 255)
        self.color_light_blue = (140, 240, 255)
        self.color_blue = (0, 0, 255)

        # game state variables
        self.shitty_mode = False
        self.board_theme_wood = False
        self.exiting = False
        self.turn_black = False

    def pawn_path(self, black: bool) -> PathLike:
        """returns pawn image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_pawn_black_path)
            return pathlib.Path(self.trad_pawn_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_pawn_white_path)
        return pathlib.Path(self.trad_pawn_white_path)

    def rook_path(self, black: bool) -> PathLike:
        """returns rook image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_rook_black_path)
            return pathlib.Path(self.trad_rook_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_rook_white_path)
        return pathlib.Path(self.trad_rook_white_path)

    def bishop_path(self, black: bool) -> PathLike:
        """returns bishop image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_bishop_black_path)
            return pathlib.Path(self.trad_bishop_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_bishop_white_path)
        return pathlib.Path(self.trad_bishop_white_path)

    def knight_path(self, black: bool) -> PathLike:
        """returns knight image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_knight_black_path)
            return pathlib.Path(self.trad_knight_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_knight_white_path)
        return pathlib.Path(self.trad_knight_white_path)

    def queen_path(self, black: bool) -> PathLike:
        """returns queen image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_queen_black_path)
            return pathlib.Path(self.trad_queen_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_queen_white_path)
        return pathlib.Path(self.trad_queen_white_path)

    def king_path(self, black: bool) -> PathLike:
        """returns king image path"""

        if black:
            if self.shitty_mode:
                return pathlib.Path(self.shitty_king_black_path)
            return pathlib.Path(self.trad_king_black_path)
        if self.shitty_mode:
            return pathlib.Path(self.shitty_king_white_path)
        return pathlib.Path(self.trad_king_white_path)

    def space_path(self, black: bool) -> PathLike:
        """returns board space image path"""

        if black:
            if self.board_theme_wood:
                return pathlib.Path(self.space_path_wood_black)
            return pathlib.Path(self.space_path_solid_black)
        if self.board_theme_wood:
            return pathlib.Path(self.space_path_wood_white)
        return pathlib.Path(self.space_path_solid_white)

    def row_header_width(self) -> int:
        """returns row header width in pixels"""

        return self.__row_header_width

    def row_header_height(self) -> int:
        """returns row header height in pixels"""

        return self.board_height() + self.col_header_height() * 2

    def col_header_width(self) -> int:
        """returns column header width in pixels"""

        return self.board_width() + self.row_header_width() * 2

    def col_header_height(self) -> int:
        """returns column header height in pixels"""

        return self.__col_header_height

    def row_header_y_start(self) -> int:
        """
        returns the y coordinate to start iterating the row header labels at,
        increment it by self.space_height()
        """

        return int(
            self.col_header_height() \
            + (self.space_height() / 2) \
            - (self.header_font_height / 2)
        )

    def row_header_x_left(self) -> int:
        """returns the x coordinate for all left row header labels"""

        return int((self.row_header_width() - self.header_font_width) / 2)

    def row_header_x_right(self) -> int:
        """returns the x coordinate for all right row header labels"""

        return int(
            self.board_width() \
            + self.row_header_width() \
            + ((self.row_header_width() - self.header_font_width) / 2)
        )

    def col_header_x_start(self) -> int:
        """
        returns the x coordinate to start iterating the column header labels
        at, increment it by self.space_width()
        """

        return int(
            self.row_header_width() \
            + (self.space_width() / 2) \
            - (self.header_font_width / 2)
        )

    def col_header_y_top(self) -> int:
        """returns the y coordinate for all top column header labels"""

        return int((self.col_header_height() - self.header_font_height) / 2)

    def col_header_y_bottom(self) -> int:
        """returns the y coordinate for all bottom column header labels"""

        return int(
            self.board_height() \
            + self.col_header_height() \
            + ((self.col_header_height() - self.header_font_height) / 2)
        )

    def space_width(self) -> int:
        """returns the width of a board space in pixels"""

        return self.__space_width

    def space_height(self) -> int:
        """returns the height of a board space in pixels"""

        return self.__space_height

    def board_start_x(self) -> int:
        """
        returns the x coordinate for the left of the game board
        for use iterating the board space sprites, etc
        """

        if self.headers_enabled:
            return self.row_header_width()
        return 0

    def board_start_y(self) -> int:
        """
        returns the y coordinate for the top of the game board
        for use iterating board space sprites, etc
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
