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
        self.__space_width = 60
        self.__space_height = 60
        self.space_path_wood_black = str(pathlib.Path('shitty_art/space_wood_black.png'))
        self.space_path_wood_white = str(pathlib.Path('shitty_art/space_wood_white.png'))

        # game piece paths
        self.shitty_pawn_black_path = str(pathlib.Path('shitty_art/shittypawnblack.png'))
        self.shitty_pawn_white_path = str(pathlib.Path('shitty_art/shittypawnwhite.png'))
        self.shitty_rook_black_path = str(pathlib.Path('shitty_art/shittyrookblack.png'))
        self.shitty_rook_white_path = str(pathlib.Path('shitty_art/shittyrookwhite.png'))
        self.shitty_bishop_black_path = str(pathlib.Path('shitty_art/shittybishopblack.png'))
        self.shitty_bishop_white_path = str(pathlib.Path('shitty_art/shittybishopwhite.png'))
        self.shitty_knight_black_path = str(pathlib.Path('shitty_art/shittyknightblack.png'))
        self.shitty_knight_white_path = str(pathlib.Path('shitty_art/shittyknightwhite.png'))
        self.shitty_queen_black_path = str(pathlib.Path('shitty_art/shittyqueenblack.png'))
        self.shitty_queen_white_path = str(pathlib.Path('shitty_art/shittyqueenwhite.png'))
        self.shitty_king_black_path = str(pathlib.Path('shitty_art/shittykingblack.png'))
        self.shitty_king_white_path = str(pathlib.Path('shitty_art/shittykingwhite.png'))

        self.trad_pawn_black_path = str(pathlib.Path('shitty_art/trad_pawn_black.png'))
        self.trad_pawn_white_path = str(pathlib.Path('shitty_art/trad_pawn_white.png'))
        self.trad_rook_black_path = str(pathlib.Path('shitty_art/trad_rook_black.png'))
        self.trad_rook_white_path = str(pathlib.Path('shitty_art/trad_rook_white.png'))
        self.trad_bishop_black_path = str(pathlib.Path('shitty_art/trad_bishop_black.png'))
        self.trad_bishop_white_path = str(pathlib.Path('shitty_art/trad_bishop_white.png'))
        self.trad_knight_black_path = str(pathlib.Path('shitty_art/trad_knight_black.png'))
        self.trad_knight_white_path = str(pathlib.Path('shitty_art/trad_knight_white.png'))
        self.trad_queen_black_path = str(pathlib.Path('shitty_art/trad_queen_black.png'))
        self.trad_queen_white_path = str(pathlib.Path('shitty_art/trad_queen_white.png'))
        self.trad_king_black_path = str(pathlib.Path('shitty_art/trad_king_black.png'))
        self.trad_king_white_path = str(pathlib.Path('shitty_art/trad_king_white.png'))

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
        self.header_font_path = str(pathlib.Path('fonts/LiberationMono-Regular.ttf'))
        # self.header_font_bold_path = str(pathlib.Path('fonts/LiberationMono-Bold.ttf'))

        # assorted colors
        self.color_white = (255, 255, 255)
        self.color_light_blue = (140, 240, 255)
        self.color_blue = (0, 0, 255)

        # game state variables
        self.shitty_mode = False
        self.exiting = False
        self.turn_black = False

    def pawn_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_pawn_black_path
        return self.trad_pawn_black_path

    def pawn_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_pawn_white_path
        return self.trad_pawn_white_path

    def rook_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_rook_black_path
        return self.trad_rook_black_path

    def rook_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_rook_white_path
        return self.trad_rook_white_path

    def bishop_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_bishop_black_path
        return self.trad_bishop_black_path

    def bishop_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_bishop_white_path
        return self.trad_bishop_white_path

    def knight_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_knight_black_path
        return self.trad_knight_black_path

    def knight_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_knight_white_path
        return self.trad_knight_white_path

    def queen_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_queen_black_path
        return self.trad_queen_black_path

    def queen_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_queen_white_path
        return self.trad_queen_white_path

    def king_path_black(self) -> str:
        if self.shitty_mode:
            return self.shitty_king_black_path
        return self.trad_king_black_path

    def king_path_white(self) -> str:
        if self.shitty_mode:
            return self.shitty_king_white_path
        return self.trad_king_white_path

    def space_path_black(self) -> str:
        """returns path for current black board space image"""

        return self.space_path_wood_black

    def space_path_white(self) -> str:
        """returns path for current white board image image"""

        return self.space_path_wood_white

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
