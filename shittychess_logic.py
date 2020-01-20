# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyLogic:
    """game logic class"""

    def __init__(self, settings: ShittySettings) -> None:
        self.settings = settings
        self.board = None
        self.__coords_to_rect = {}
        self.__rect_to_coords = {}
        self.__coords_to_indexes = {}
        self.__indexes_to_coords = {}
        self.configure_layout()

    def coords_to_indexes(self, coords: str) -> tuple:  # type hinting can be more precise here
        """
        takes chess coordinates, example: 'f4'
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        example: (0, 5)
        """

        if coords in self.__coords_to_indexes:
            return self.__coords_to_indexes[coords]
        return ()

    def coords_to_rect(self, coords: str) -> pygame.Rect:
        """
        takes chess coordinates, example: 'f4'
        returns a pygame.Rect object of the corresponding board space,
        example: pygame.Rect(0, 120, 60, 60)
        """

        if coords not in self.__coords_to_rect:
            return pygame.Rect(0, 0, 0, 0)
        tmp_rect = pygame.Rect(self.__coords_to_rect[coords])
        if self.settings.headers_enabled:
            tmp_rect.left += self.settings.row_header_width()
            tmp_rect.top += self.settings.col_header_height()
        return tmp_rect

    def indexes_to_coords(self, indexes: tuple) -> str:  # type hinting can be more precise here
        """
        takes a zero-indexed tuple with 2D list indexes, example: '(0, 5)'
        returns the corresponding chess notation for a board space,
        example: 'f4'
        """

        if indexes in self.__indexes_to_coords:
            return self.__indexes_to_coords[indexes]
        return ''

    def indexes_to_rect(self, indexes: tuple) -> pygame.Rect:
        """
        takes a zero-indexed tuple with 2D list indexes, example: '(0, 5)'
        returns a pygame.Rect object of the corresponding board space,
        example: pygame.Rect(0, 120, 60, 60)
        """

        return self.coords_to_rect(self.indexes_to_coords(indexes))

    def rect_to_coords(self, rect: pygame.Rect) -> str:
        """
        takes a pygame.Rect object, example: pygame.Rect(0, 120, 60, 60)
        returns the corresponding chess notation for a board space,
        example: 'f4'
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

    def rect_to_indexes(self, rect: pygame.Rect) -> tuple:
        """
        takes a pygame.Rect object, example: pygame.Rect(0, 120, 60, 60)
        returns the corresponding zero-indexed tuple with 2D list indexes for the board space,
        example: (0, 5)
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
