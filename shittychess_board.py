# coding=utf-8


from typing import NoReturn
from typing import Tuple

import pygame

from shittychess_pieces import ShittyPiece
from shittychess_sprites import ShittySpace


class ShittyBoard:
    """this class represents a chess board"""

    def __init__(self) -> NoReturn:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.logic = None  # ShittyLogic
        self.layout = None  # ShittyLayout
        self.col_header_labels = []
        self.row_header_labels = []
        self.sprite_to_highlight = None  # ShittyPiece

        self.current_board_start_x = 0
        self.current_board_start_y = 0
        self.board_space_group = pygame.sprite.Group()

    def configure(self) -> NoReturn:
        """
        configure class's properties after they have been assigned externally
        """

        self.render_header_labels()
        self.current_board_start_x = self.settings.board_start_x()
        self.current_board_start_y = self.settings.board_start_y()
        self.create_board_space_group()

    def create_board_space_group(self) -> NoReturn:
        """
        creates all of the black and white board spaces and puts them all in a sprite group
        """

        for y, number in enumerate(self.settings.row_headers):
            for x, letter in enumerate(self.settings.col_headers):
                black = True

                # if row even and col even or if row odd and col odd: white
                if ((y % 2 == 0) and (x % 2 == 0)) or ((x % 2 != 0) and (y % 2 != 0)):
                    space_image_path = self.settings.space_path_white()
                    black = False

                # else: black
                else:
                    space_image_path = self.settings.space_path_black()

                # calculate space properties
                pos_x = x * self.settings.space_width() + self.current_board_start_x
                pos_y = y * self.settings.space_height() + self.current_board_start_y
                width = self.settings.space_width()
                height = self.settings.space_height()

                # make a temp space
                tmp_space = ShittySpace(
                    black,
                    pygame.Rect(pos_x, pos_y, width, height),
                    f'{letter}{number}',
                    space_image_path,
                )
                tmp_space.indexes = x, y

                # add space to board_space_group pygame.sprite.Group
                self.board_space_group.add(tmp_space)

    def resize(self) -> NoReturn:
        """
        changes all the x, y coordinates of the board space sprites if the screen size changes
        """

        x_change = self.settings.board_start_x() - self.current_board_start_x
        y_change = self.settings.board_start_y() - self.current_board_start_y
        for space in self.board_space_group.sprites():
            space.rect.left += x_change
            space.rect.top += y_change
        self.current_board_start_x = self.settings.board_start_x()
        self.current_board_start_y = self.settings.board_start_y()

    def resize_header_label_font(self, font_sz: int) -> NoReturn:
        """
        can be used to resize the header labels
        it is not currently being used anywhere
        """

        self.settings.header_font_sz = font_sz
        self.col_header_labels.clear()
        self.row_header_labels.clear()
        self.render_header_labels()

    def render_header_labels(self) -> NoReturn:
        """
        renders the header labels and stores them in lists
        """

        header_font = pygame.font.Font(self.settings.header_font_path, self.settings.header_font_sz)
        for label in self.settings.col_headers:
            self.col_header_labels.append(header_font.render(label, True, self.settings.header_font_color, None))
        for label in self.settings.row_headers:
            self.row_header_labels.append(header_font.render(label, True, self.settings.header_font_color, None))
        if len(self.col_header_labels) > 0:
            tmp_rect = self.col_header_labels[0].get_rect()
            self.settings.header_font_width = tmp_rect.width
            self.settings.header_font_height = tmp_rect.height

    def draw(self) -> NoReturn:
        """
        draws all board elements on the screen
        """

        # draw the board
        self.board_space_group.draw(self.screen)

        # draws headers if enabled
        if self.settings.headers_enabled:
            self.draw_headers()

        # highlight a sprite and its available moves if needed
        if self.sprite_to_highlight:
            self.highlight_valid_moves(self.sprite_to_highlight)

    def draw_headers(self) -> NoReturn:
        """
        draws the headers around the board
        called if headers are enabled
        """

        # column headers
        loop_stop = self.settings.board_width() + self.settings.col_header_x_start()
        for label, x in zip(self.col_header_labels, range(self.settings.col_header_x_start(), loop_stop, self.settings.space_width())):
            tmp_rect = label.get_rect()
            tmp_rect.left = x
            tmp_rect.top = self.settings.col_header_y_top()
            self.screen.blit(label, tmp_rect)
            tmp_rect.top = self.settings.col_header_y_bottom()
            self.screen.blit(label, tmp_rect)

        # row headers
        loop_stop = self.settings.board_height() + self.settings.row_header_y_start()
        for label, y in zip(self.row_header_labels, range(self.settings.row_header_y_start(), loop_stop, self.settings.space_height())):
            tmp_rect = label.get_rect()
            tmp_rect.left = self.settings.row_header_x_left()
            tmp_rect.top = y
            self.screen.blit(label, tmp_rect)
            tmp_rect.left = self.settings.row_header_x_right()
            self.screen.blit(label, tmp_rect)

    # there should be a way to make this method accept any sequence of 3 ints, or a pygame.Color, and still work
    def draw_space_border(self, rect: pygame.Rect, color: Tuple[int, int, int], alpha: int) -> NoReturn:
        """
        borders a space based on rect argument
        """

        bar_color = pygame.Color(*color)
        bar_color.a = alpha
        bar_sz = 2
        h_bar_width = int(self.settings.space_width() / 3)
        v_bar_height = int(self.settings.space_height() / 3)
        h_bar_h_movement = self.settings.space_width() - h_bar_width
        h_bar_v_movement = self.settings.space_height() - bar_sz
        v_bar_h_movement = self.settings.space_width() - bar_sz
        v_bar_v_movement = self.settings.space_height() - v_bar_height

        # draws vertical border bars
        v_bar = pygame.Rect(rect.left, rect.top, bar_sz, v_bar_height)
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.top += v_bar_v_movement
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.left += v_bar_h_movement
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.top -= v_bar_v_movement
        pygame.draw.rect(self.screen, bar_color, v_bar)

        # draws horizontal border bars
        h_bar = pygame.Rect(rect.left, rect.top, h_bar_width, bar_sz)
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.top += h_bar_v_movement
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.left += h_bar_h_movement
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.top -= h_bar_v_movement
        pygame.draw.rect(self.screen, bar_color, h_bar)

    def draw_space_highlight(self, rect: pygame.Rect, color: Tuple[int, int, int], alpha: int) -> NoReturn:
        """
        highlights a space based on rect argument
        """

        width = self.settings.space_width()
        height = self.settings.space_height()
        translucent_surface = pygame.Surface((width, height)).convert_alpha()
        translucent_surface.fill(pygame.Color(*color, alpha))
        self.screen.blit(translucent_surface, rect)

    def highlight_space(self, coords: str, space_color=(0, 170, 255), space_alpha=100) -> NoReturn:
        """
        takes chess coordinates and gets a rect for it, then calls self.draw_space_highlight on that rect
        """

        tmp_rect = pygame.Rect.copy(self.logic.coords_to_rect(coords))
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)

    def highlight_and_border_space(self, coords: str, space_color=(0, 170, 255), space_alpha=100, border_color=(0, 0, 0), border_alpha=255) -> NoReturn:
        """
        highlights and borders a space on the board from a chess coord str
        should be used to show available moves to a player
        """

        tmp_rect = pygame.Rect.copy(self.logic.coords_to_rect(coords))
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)
        self.draw_space_border(tmp_rect, color=border_color, alpha=border_alpha)

    def highlight_valid_moves(self, piece: ShittyPiece) -> NoReturn:
        """
        takes a reference to a ShittyPiece and highlights that piece,
        then it highlights and borders all valid moves for that piece
        """

        if piece:
            self.highlight_space(piece.coords, space_alpha=150)
            valid_spaces = self.logic.valid_move_coords(piece)
            for space in valid_spaces:
                self.highlight_and_border_space(space)
