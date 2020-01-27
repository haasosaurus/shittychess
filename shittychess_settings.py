# coding=utf-8

from os import PathLike
from typing import NoReturn

import pathlib


class ShittySettings:
    """class to store the game settings in"""

    def __init__(self, resize_callback=None) -> NoReturn:
        """constructor"""

        self.resize_callback = resize_callback

        # general declarations/initializations
        app_icon = pathlib.Path('shitty_art/shitty_knight_black.png')
        self.app_icon_path = str(app_icon)
        self.debug = True
        self.cols = 8
        self.rows = 8
        self._space_width = 75
        self._space_height = 75

        spaces_solid_img_paths = {
            'black': 'shitty_art/space_solid_black.png',
            'white': 'shitty_art/space_solid_white.png',
        }

        spaces_wood_img_paths = {
            'black': 'shitty_art/space_wood_black.png',
            'white': 'shitty_art/space_wood_white.png',
        }

        pieces_shitty_img_paths = {
            'white': {
                'pawn': 'shitty_art/shitty_pawn_white.png',
                'king': 'shitty_art/shitty_king_white.png',
                'rook': 'shitty_art/shitty_rook_white.png',
                'bishop': 'shitty_art/shitty_bishop_white.png',
                'knight': 'shitty_art/shitty_knight_white.png',
                'queen': 'shitty_art/shitty_queen_white.png',
            },
            'black': {
                'pawn': 'shitty_art/shitty_pawn_black.png',
                'rook': 'shitty_art/shitty_rook_black.png',
                'bishop': 'shitty_art/shitty_bishop_black.png',
                'knight': 'shitty_art/shitty_knight_black.png',
                'queen': 'shitty_art/shitty_queen_black.png',
                'king': 'shitty_art/shitty_king_black.png',
            }
        }

        pieces_trad_img_paths = {
            'white': {
                'pawn': 'shitty_art/trad_pawn_white.png',
                'rook': 'shitty_art/trad_rook_white.png',
                'bishop': 'shitty_art/trad_bishop_white.png',
                'queen': 'shitty_art/trad_queen_white.png',
                'knight': 'shitty_art/trad_knight_white.png',
                'king': 'shitty_art/trad_king_white.png',
            },
            'black': {
                'pawn': 'shitty_art/trad_pawn_black.png',
                'rook': 'shitty_art/trad_rook_black.png',
                'bishop': 'shitty_art/trad_bishop_black.png',
                'knight': 'shitty_art/trad_knight_black.png',
                'queen': 'shitty_art/trad_queen_black.png',
                'king': 'shitty_art/trad_king_black.png',
            }
        }

        self.img_paths = {
            'spaces': {
                'solid': spaces_solid_img_paths,
                'wood': spaces_wood_img_paths,
            },
            'pieces': {
                'trad': pieces_trad_img_paths,
                'shitty': pieces_shitty_img_paths,
            }
        }

        self.piece_styles = {i:v for i, v in enumerate(self.img_paths['pieces'].keys())}
        self.space_styles = {i:v for i, v in enumerate(self.img_paths['spaces'].keys())}
        self.current_piece_style_index = 0
        self.current_space_style_index = 0
        self.current_piece_style = self.piece_styles[self.current_piece_style_index]
        self.current_space_style = self.space_styles[self.current_space_style_index]

        # header variables declarations/initializations
        self.headers_enabled = True
        self._row_header_width = 30
        self._col_header_height = 30
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
        self.exiting = False
        self.turn_black = False
        self.black_top = True

    def piece_path(self, piece_type, color):
        """returns piece image path for a given type and color of the current style"""

        return pathlib.Path(
            self.img_paths['pieces'][self.current_piece_style][color][piece_type]
        )

    def space_path(self, color) -> PathLike:
        """returns board space image path"""

        return pathlib.Path(
            self.img_paths['spaces'][self.current_space_style][color]
        )

    @property
    def row_header_width(self) -> int:
        """returns row header width in pixels"""

        return self._row_header_width

    @row_header_width.setter
    def row_header_width(self, width: int) -> NoReturn:
        if width < self.header_font_width or width <= 0:
            raise ValueError('width must be less than or equal to the header label font width, or greater than 0')
        else:
            self._row_header_width = width

    @property
    def row_header_height(self) -> int:
        """returns row header height in pixels"""

        return self.board_height() + self.col_header_height * 2

    @property
    def col_header_width(self) -> int:
        """returns column header width in pixels"""

        return self.board_width() + self.row_header_width * 2

    @property
    def col_header_height(self) -> int:
        """returns column header height in pixels"""

        return self._col_header_height

    @col_header_height.setter
    def col_header_height(self, height: int) -> NoReturn:
        if height < self.header_font_height or height <= 0:
            raise ValueError('height must be less than or equal to the header label font height, or greater than 0')
        else:
            self._col_header_height = height

    def row_header_y_start(self) -> int:
        """
        returns the y coordinate to start iterating the row header labels at,
        increment it by self.space_height
        """

        return int(
            self.col_header_height
            + (self.space_height / 2)
            - (self.header_font_height / 2)
        )

    def row_header_x_left(self) -> int:
        """returns the x coordinate for all left row header labels"""

        return int((self.row_header_width - self.header_font_width) / 2)

    def row_header_x_right(self) -> int:
        """returns the x coordinate for all right row header labels"""

        return int(
            self.board_width()
            + self.row_header_width
            + ((self.row_header_width - self.header_font_width) / 2)
        )

    def col_header_x_start(self) -> int:
        """
        returns the x coordinate to start iterating the column header labels
        at, increment it by self.space_width
        """

        return int(
            self.row_header_width
            + (self.space_width / 2)
            - (self.header_font_width / 2)
        )

    def col_header_y_top(self) -> int:
        """returns the y coordinate for all top column header labels"""

        return int((self.col_header_height - self.header_font_height) / 2)

    def col_header_y_bottom(self) -> int:
        """returns the y coordinate for all bottom column header labels"""

        return int(
            self.board_height()
            + self.col_header_height
            + ((self.col_header_height - self.header_font_height) / 2)
        )

    @property
    def space_width(self) -> int:
        """returns the width of a board space in pixels"""

        return self._space_width

    @space_width.setter
    def space_width(self, width: int) -> NoReturn:
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width

    @property
    def space_height(self) -> int:
        """returns the height of a board space in pixels"""

        return self._space_height

    @space_height.setter
    def space_height(self, height: int) -> NoReturn:
        if height <= 0:
            raise ValueError('Height must be positive')
        else:
            self._space_height = height

    def board_start_x(self) -> int:
        """
        returns the x coordinate for the left of the game board
        for use iterating the board space sprites, etc
        """

        if self.headers_enabled:
            return self.row_header_width
        return 0

    def board_start_y(self) -> int:
        """
        returns the y coordinate for the top of the game board
        for use iterating board space sprites, etc
        """

        if self.headers_enabled:
            return self.col_header_height
        return 0

    def board_width(self) -> int:
        """returns the width of the board in pixels"""

        return self.space_width * self.cols

    def board_height(self) -> int:
        """returns the height of the board in pixels"""

        return self.space_height * self.rows

    def screen_width(self) -> int:
        """returns the width of the screen in pixels"""

        if self.headers_enabled:
            return self.board_width() + self.row_header_width * 2
        return self.board_width()

    def screen_height(self) -> int:
        """returns the height of the screen in pixels"""

        if self.headers_enabled:
            return self.board_height() + self.col_header_height * 2
        return self.board_height()
