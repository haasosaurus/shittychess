# coding=utf-8


from typing import NoReturn
from typing import Tuple

import pygame

from shittychess_sprites import ShittyPiece
from shittychess_sprites import ShittySprite


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
        self.spaces = {}
        self.spaces_group = pygame.sprite.Group()

    def configure(self) -> NoReturn:
        """
        configure class's properties after they have been assigned externally
        """

        self.render_header_labels()
        self.current_board_start_x = self.settings.board_start_x()
        self.current_board_start_y = self.settings.board_start_y()
        self.create_spaces()

    def create_spaces(self) -> NoReturn:
        """
        creates all of the black and white board spaces as sprites and puts
        them all in a sprite group
        """

        for y in range(self.settings.rows):
            for x in range(self.settings.cols):
                is_black = True

                # if row even and col even or if row odd and col odd: white
                if ((y % 2 == 0) and (x % 2 == 0)) or ((x % 2 != 0) and (y % 2 != 0)):
                    is_black = False
                space_image_path = self.settings.space_path(black=is_black)

                # calculate space properties
                pos_x = x * self.settings.space_width() + self.current_board_start_x
                pos_y = y * self.settings.space_height() + self.current_board_start_y
                width = self.settings.space_width()
                height = self.settings.space_height()

                # make a temp space
                tmp_space = ShittySprite(
                    is_black,
                    pygame.Rect(pos_x, pos_y, width, height),
                    (x, y),
                    space_image_path,
                )

                # add to spaces dict
                self.spaces.update({(x, y): tmp_space})

                for space in self.spaces.values():

                    # add space to spaces_group pygame.sprite.Group
                    self.spaces_group.add(space)

    def resize(self) -> NoReturn:
        """
        changes all the x (left), y (top) coordinates of the board space
        sprites if the screen size changes
        """

        x_change = self.settings.board_start_x() - self.current_board_start_x
        y_change = self.settings.board_start_y() - self.current_board_start_y
        for space in self.spaces_group.sprites():
            space.rect.left += x_change
            space.rect.top += y_change
        self.current_board_start_x = self.settings.board_start_x()
        self.current_board_start_y = self.settings.board_start_y()

    def resize_header_label_font(self, font_size: int) -> NoReturn:
        """
        can be used to resize the header labels,
        it is not currently being used anywhere
        """

        self.settings.header_font_sz = font_size
        self.col_header_labels.clear()
        self.row_header_labels.clear()
        self.render_header_labels()

    def render_header_labels(self) -> NoReturn:
        """renders the header labels and stores them in lists"""

        header_font = pygame.font.Font(
            self.settings.header_font_path,
            self.settings.header_font_sz
        )
        for column_header in self.settings.col_headers:
            self.col_header_labels.append(header_font.render(
                column_header,  # text
                True,   # anti-alias
                self.settings.header_font_color,  # color
                None  # background
            ))
        for row_header in self.settings.row_headers:
            self.row_header_labels.append(header_font.render(
                row_header,  # text
                True,   # anti-alias
                self.settings.header_font_color,  # color
                None  # background
            ))
        if len(self.col_header_labels) > 0:
            tmp_rect = self.col_header_labels[0].get_rect()
            self.settings.header_font_width = tmp_rect.width
            self.settings.header_font_height = tmp_rect.height

    def draw(self) -> NoReturn:
        """draws all board elements on the screen"""

        # draw the board
        self.spaces_group.draw(self.screen)

        # draws headers if enabled
        if self.settings.headers_enabled:
            self.draw_headers()

        # highlight a sprite and its available moves if needed
        if self.sprite_to_highlight:
            self.highlight_valid_moves(self.sprite_to_highlight)

    def draw_headers(self) -> NoReturn:
        """draws the headers around the board, called if headers are enabled"""

        # column headers
        loop_stop = self.settings.board_width() + self.settings.col_header_x_start()
        for label, x in zip(
                self.col_header_labels,
                range(self.settings.col_header_x_start(), loop_stop, self.settings.space_width())
        ):
            tmp_rect = label.get_rect()
            tmp_rect.left = x
            tmp_rect.top = self.settings.col_header_y_top()
            self.screen.blit(label, tmp_rect)
            tmp_rect.top = self.settings.col_header_y_bottom()
            self.screen.blit(label, tmp_rect)

        # row headers
        loop_stop = self.settings.board_height() + self.settings.row_header_y_start()
        for label, y in zip(
                self.row_header_labels,
                range(self.settings.row_header_y_start(), loop_stop, self.settings.space_height())
        ):
            tmp_rect = label.get_rect()
            tmp_rect.left = self.settings.row_header_x_left()
            tmp_rect.top = y
            self.screen.blit(label, tmp_rect)
            tmp_rect.left = self.settings.row_header_x_right()
            self.screen.blit(label, tmp_rect)

    def draw_space_border(
            self,
            rect: pygame.Rect,
            color: Tuple[int, int, int],
            color_mid: Tuple[int, int, int],
            alpha: int,
            alpha_mid: int,
            thickness: int
    ) -> NoReturn:
        """borders a space based on rect argument"""

        bar_color = pygame.Color(*color, alpha)
        bar_color_mid = pygame.Color(*color_mid, alpha_mid)

        h_bar_width = int(self.settings.space_width() / 3)
        h_bar_width_mid = self.settings.space_width() - h_bar_width * 2
        v_bar_height = int(self.settings.space_height() / 3)
        v_bar_height_mid = self.settings.space_height() - v_bar_height * 2
        h_bar_v_movement = self.settings.space_height() - thickness
        v_bar_h_movement = self.settings.space_width() - thickness

        # draws vertical border bars
        v_bar = pygame.Rect(rect.left, rect.top, thickness, v_bar_height)
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.top += v_bar_height
        v_bar.height = v_bar_height_mid
        pygame.draw.rect(self.screen, bar_color_mid, v_bar)
        v_bar.top += v_bar_height_mid
        v_bar.height = v_bar_height
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.left += v_bar_h_movement
        pygame.draw.rect(self.screen, bar_color, v_bar)
        v_bar.top -= v_bar_height
        v_bar.height = v_bar_height_mid
        pygame.draw.rect(self.screen, bar_color_mid, v_bar)
        v_bar.top -= v_bar_height_mid
        v_bar.height = v_bar_height
        pygame.draw.rect(self.screen, bar_color, v_bar)

        # draws horizontal border bars
        h_bar = pygame.Rect(rect.left, rect.top, h_bar_width, thickness)
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.left += h_bar_width
        h_bar.width = h_bar_width_mid
        pygame.draw.rect(self.screen, bar_color_mid, h_bar)
        h_bar.left += h_bar_width_mid
        h_bar.width = h_bar_width
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.top += h_bar_v_movement
        pygame.draw.rect(self.screen, bar_color, h_bar)
        h_bar.left -= h_bar_width
        h_bar.width = h_bar_width_mid
        pygame.draw.rect(self.screen, bar_color_mid, h_bar)
        h_bar.left -= h_bar_width_mid
        h_bar.width = h_bar_width
        pygame.draw.rect(self.screen, bar_color, h_bar)

    def draw_space_highlight(
            self,
            rect: pygame.Rect,
            color: Tuple[int, int, int],
            alpha: int
    ) -> NoReturn:
        """highlights a space based on rect argument"""

        width = self.settings.space_width()
        height = self.settings.space_height()
        translucent_surface = pygame.Surface((width, height)).convert_alpha()
        translucent_surface.fill(pygame.Color(*color, alpha))
        self.screen.blit(translucent_surface, rect)

    def highlight_space(
            self,
            coords: Tuple[int, int],
            space_color: Tuple[int, int, int] = (0, 170, 255),
            space_alpha: int = 100
    ) -> NoReturn:
        """
        takes zero-indexed x, y board coordinates and gets a rect for it,
        then calls self.draw_space_highlight on that rect
        """

        tmp_rect = pygame.Rect.copy(self.spaces[coords].rect)
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)

    def highlight_and_border_space(
            self,
            coords: Tuple[int, int],
            space_color: Tuple[int, int, int] = (0, 170, 255),
            space_alpha: int = 100,
            border_color: Tuple[int, int, int] = (0, 0, 0),
            mid_border_color: Tuple[int, int, int] = (255, 255, 255),
            border_alpha: int = 255,
            mid_border_alpha: int = 255,
            border_thickness: int = 2
    ) -> NoReturn:
        """
        highlights and borders a space on the board from zero-indexed x, y board
        coordinates should be used to show available moves to a player
        """

        tmp_rect = pygame.Rect.copy(self.spaces[coords].rect)
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)
        self.draw_space_border(
            rect=tmp_rect,
            color=border_color,
            color_mid=mid_border_color,
            alpha=border_alpha,
            alpha_mid=mid_border_alpha,
            thickness=border_thickness
        )

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
