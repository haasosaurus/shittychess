# coding=utf-8


from typing import List
from typing import Tuple

import pygame

from shittychess_pieces import ShittyPiece


class ShittyLogic:
    """game logic class"""

    def __init__(self) -> None:
        self.settings = None  # ShittySettings
        self.board = None
        self.__coords_to_rect = {}
        self.__rect_to_coords = {}
        self.__coords_to_indexes = {}
        self.__indexes_to_coords = {}

    def configure(self) -> None:
        """
        configure class's properties after they have been assigned externally
        """

        self.configure_layout()

    def coords_to_indexes(self, coords: str) -> Tuple[int]:
        """
        takes chess coordinates
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        0, 5 = ShittyLogic.coords_to_indexes('f4')
        """

        if coords in self.__coords_to_indexes:
            return self.__coords_to_indexes[coords]
        return ()

    def coords_to_rect(self, coords: str) -> pygame.Rect:
        """
        takes chess coordinates
        returns a pygame.Rect object of the corresponding board space,
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.coords_to_rect('f4')
        """

        if coords not in self.__coords_to_rect:
            return pygame.Rect(0, 0, 0, 0)
        tmp_rect = pygame.Rect(self.__coords_to_rect[coords])
        if self.settings.headers_enabled:
            tmp_rect.left += self.settings.row_header_width()
            tmp_rect.top += self.settings.col_header_height()
        return tmp_rect

    def indexes_to_coords(self, indexes: Tuple[int]) -> str:
        """
        takes a zero-indexed tuple with 2D list indexes
        returns the corresponding chess notation for a board space,
        'f4' = ShittyLogic.indexes_to_coords(0, 5)
        """

        if indexes in self.__indexes_to_coords:
            return self.__indexes_to_coords[indexes]
        return ''

    def indexes_to_rect(self, indexes: Tuple[int]) -> pygame.Rect:
        """
        takes a zero-indexed tuple with 2D list indexes
        returns a pygame.Rect object of the corresponding board space,
        pygame.Rect(0, 120, 60, 60) = ShittyLogic.indexes_to_rect(0, 5)
        """

        return self.coords_to_rect(self.indexes_to_coords(indexes))

    def rect_to_coords(self, rect: pygame.Rect) -> str:
        """
        takes a pygame.Rect object
        returns the corresponding chess notation for a board space,
        'f4' = ShittyLogic.rect_to_coords(pygame.Rect(0, 120, 60, 60))
        """

        left = rect.left
        top = rect.top
        width = rect.width
        height = rect.height
        if self.settings.headers_enabled:
            left -= self.settings.row_header_width()
            top -= self.settings.col_header_height()
        tmp_tuple = (left, top, width, height)
        if tmp_tuple not in self.__rect_to_coords:
            return ''
        return self.__rect_to_coords[(left, top, width, height)]

    def rect_to_indexes(self, rect: pygame.Rect) -> Tuple[int]:
        """
        takes a pygame.Rect object
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        0, 5 = ShittyLogic.rect_to_indexes(pygame.Rect(0, 120, 60, 60))
        """

        return self.coords_to_indexes(self.rect_to_coords(rect))

    def configure_layout(self) -> None:
        """
        this sets up all the dicts and their matching dicts that i thought we needed to
        make this 'logic' work
        """

        self.settings.coords_list = []
        for row, y in zip(self.settings.row_headers, range(0, int(self.settings.space_height() * self.settings.rows), self.settings.space_height())):
            for col, x in zip(self.settings.col_headers, range(0, int(self.settings.space_width() * self.settings.cols), self.settings.space_width())):
                pos_name = col + row
                tmp_rect = pygame.Rect(x, y, self.settings.space_width(), self.settings.space_height())
                self.__coords_to_rect.update({pos_name: tmp_rect})
                self.settings.coords_list.append(pos_name)
        for i, row_number in enumerate(self.settings.row_headers):
            for j, col_letter in enumerate(self.settings.col_headers):
                self.__coords_to_indexes.update({f'{col_letter}{row_number}': (i, j)})
        for coords, indexes in self.__coords_to_indexes.items():
            self.__indexes_to_coords.update({indexes: coords})
        for coords, rect in self.__coords_to_rect.items():
            self.__rect_to_coords.update({(rect.left, rect.top, rect.width, rect.height): coords})

    def valid_spaces(self, piece: ShittyPiece) -> List[str]:
        space_coords = []
        piece_indexes = self.coords_to_indexes(piece.coords)
        if piece.move_patterns.horizontal > 0:
            pass
        if piece.move_patterns.vertical > 0:
            pass
        if piece.move_patterns.diagonal > 0:
            pass
        for pattern in piece.move_patterns.pattern_list:
            x = piece_indexes[0] + pattern[0]
            if x >= self.settings.cols or x < 0:
                continue
            y = piece_indexes[1] + pattern[1]
            if self.settings.rows > y >= 0:
                space_coords.append(self.indexes_to_coords((x, y)))
        return space_coords

    def valid_moves(self, piece: ShittyPiece) -> List[str]:
        return self.valid_spaces(piece)
