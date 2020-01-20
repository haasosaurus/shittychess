# coding=utf-8


import pygame

from shittychess_pieces import ShittyPiece


class ShittyBoard:
    """this class represents a chess board"""

    def __init__(self) -> None:
        self.screen = None  # pygame.Surface
        self.settings = None  # ShittySettings
        self.logic = None  # ShittyLogic
        self.tile_image = None  # pygame.image
        self.tile_rect = None  # pygame.Rect
        self.col_header_labels = []
        self.row_header_labels = []

    def configure(self) -> None:
        """
        configure class's properties after they have been assigned externally
        """

        self.tile_image = pygame.image.load(self.settings.tile_image_path)
        self.tile_rect = self.tile_image.get_rect()
        self.render_header_labels()

    def resize_header_label_font(self, font_sz: int) -> None:
        """
        can be used to resize the header labels
        it is not currently being used anywhere
        """

        self.settings.header_font_sz = font_sz
        self.col_header_labels.clear()
        self.row_header_labels.clear()
        self.render_header_labels()

    def render_header_labels(self) -> None:
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

    def draw(self, debug_piece=None) -> None:
        """
        draws all board elements on the screen
        """

        # draws the board
        for i in range(self.settings.board_start_y(), self.settings.board_height(), self.settings.tile_h):
            for j in range(self.settings.board_start_x(), self.settings.board_width(), self.settings.tile_w):
                self.tile_rect.x = i
                self.tile_rect.y = j
                self.screen.blit(self.tile_image, self.tile_rect)

        # draws headers if enabled
        if self.settings.headers_enabled:
            self.draw_headers()

        # debug testing space highlight
        if self.settings.debug and debug_piece:
            self.highlight_valid_moves(debug_piece)

    def draw_headers(self) -> None:
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


    def draw_space_border(self, rect: pygame.Rect, color=(255, 255, 255), alpha=255) -> None:
        """
        borders a space based on rect argument
        """

        side_rect_width = 2
        side_rect_height = int(self.settings.space_height() / 3)
        top_bottom_rect_width = int(self.settings.space_width() / 3)
        top_bottom_rect_height = 2

        # calculate rects for the sides
        right_top = pygame.Rect(rect.left, rect.top, side_rect_width, side_rect_height)
        right_bottom = pygame.Rect.copy(right_top)
        right_bottom.top += self.settings.space_height() - side_rect_height
        left_top = pygame.Rect.copy(right_top)
        left_top.left += self.settings.space_width() - side_rect_width
        left_bottom = pygame.Rect.copy(right_bottom)
        left_bottom.left += self.settings.space_width() - side_rect_width

        # calculate rects for the top and bottom
        top_left = pygame.Rect(rect.left, rect.top, top_bottom_rect_width, top_bottom_rect_height)
        bottom_left = pygame.Rect.copy(top_left)
        bottom_left.top += self.settings.space_height() - top_bottom_rect_height
        top_right = pygame.Rect.copy(top_left)
        top_right.left += self.settings.space_width() - top_bottom_rect_width
        bottom_right = pygame.Rect.copy(top_right)
        bottom_right.top += self.settings.space_height() - top_bottom_rect_height

        # draw the lines around the target square
        tmp_color = pygame.Color(*color)
        tmp_color.a = alpha
        pygame.draw.rect(self.screen, tmp_color, right_bottom)
        pygame.draw.rect(self.screen, tmp_color, right_top)
        pygame.draw.rect(self.screen, tmp_color, left_top)
        pygame.draw.rect(self.screen, tmp_color, left_bottom)
        pygame.draw.rect(self.screen, tmp_color, top_left)
        pygame.draw.rect(self.screen, tmp_color, bottom_left)
        pygame.draw.rect(self.screen, tmp_color, top_right)
        pygame.draw.rect(self.screen, tmp_color, bottom_right)

    def draw_space_highlight(self, rect: pygame.Rect, color=(255, 255, 255), alpha=100) -> None:
        """
        highlights a space based on rect argument
        """

        tmp_color = pygame.Color(*color)
        tmp_color.a = alpha
        tmp_surface = pygame.Surface((self.settings.space_width(), self.settings.space_height())).convert_alpha()
        tmp_surface.fill(tmp_color)
        self.screen.blit(tmp_surface, rect)

    def highlight_space(self, coords: str, space_color=(255, 255, 255), space_alpha=100) -> None:
        """
        takes chess coordinates and gets a rect for it, then calls self.draw_space_highlight on that rect
        """

        tmp_rect = pygame.Rect.copy(self.logic.coords_to_rect(coords))
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)

    def highlight_and_border_space(self, coords: str, space_color=(255, 255, 255), space_alpha=100, border_color=(255, 255, 255), border_alpha=255) -> None:
        """
        highlights and borders a space on the board from a chess coord str
        should be used to show available moves to a player
        """

        tmp_rect = pygame.Rect.copy(self.logic.coords_to_rect(coords))
        self.draw_space_highlight(tmp_rect, color=space_color, alpha=space_alpha)
        self.draw_space_border(tmp_rect, color=border_color, alpha=border_alpha)

    def highlight_valid_moves(self, piece: ShittyPiece) -> None:
        """
        takes a reference to a ShittyPiece and highlights that piece,
        then it highlights and borders all valid moves for that piece
        """

        if piece:
            self.highlight_space(piece.coords, space_alpha=150)
            valid_spaces = self.logic.valid_moves(piece)
            for space in valid_spaces:
                self.highlight_and_border_space(space)
