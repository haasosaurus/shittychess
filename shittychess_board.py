# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyBoard:
    """This class represents a board."""

    def __init__(self, screen: pygame.Surface, settings: ShittySettings) -> None:
        """Initialize the board's attributes."""

        self.screen = screen
        self.settings = settings
        self.tile_image = pygame.image.load(self.settings.tile_image_path)
        self.tile_rect = self.tile_image.get_rect()
        self.col_header_labels = []
        self.row_header_labels = []
        self.render_header_labels()


    def resize_header_label_font(self, font_sz: int) -> None:
        self.settings.header_font_sz = font_sz
        self.col_header_labels.clear()
        self.row_header_labels.clear()
        self.render_header_labels()


    def render_header_labels(self) -> None:
        header_font = pygame.font.Font(self.settings.header_font_path, self.settings.header_font_sz)
        for label in self.settings.col_headers:
            self.col_header_labels.append(header_font.render(label, True, self.settings.header_font_color, None))
        for label in self.settings.row_headers:
            self.row_header_labels.append(header_font.render(label, True, self.settings.header_font_color, None))
        if len(self.col_header_labels) > 0:
            tmp_rect = self.col_header_labels[0].get_rect()
            self.settings.header_font_width = tmp_rect.width
            self.settings.header_font_height = tmp_rect.height


    def draw(self) -> None:
        for i in range(self.settings.board_start_y(), self.settings.board_height(), self.settings.tile_h):
            for j in range(self.settings.board_start_x(), self.settings.board_width(), self.settings.tile_w):
                self.tile_rect.x = i
                self.tile_rect.y = j
                self.screen.blit(self.tile_image, self.tile_rect)
        if self.settings.headers_enabled:
            self.draw_headers()


    def draw_headers(self) -> None:
        loop_stop = self.settings.board_width() + self.settings.col_header_x_start()
        for label, x in zip(self.col_header_labels, range(self.settings.col_header_x_start(), loop_stop, self.settings.space_width())):
            tmp_rect = label.get_rect()
            tmp_rect.left = x
            tmp_rect.top = self.settings.col_header_y_top()
            self.screen.blit(label, tmp_rect)
            tmp_rect.top = self.settings.col_header_y_bottom()
            self.screen.blit(label, tmp_rect)

        loop_stop = self.settings.board_height() + self.settings.row_header_y_start()
        for label, y in zip(self.row_header_labels, range(self.settings.row_header_y_start(), loop_stop, self.settings.space_height())):
            tmp_rect = label.get_rect()
            tmp_rect.left = self.settings.row_header_x_left()
            tmp_rect.top = y
            self.screen.blit(label, tmp_rect)
            tmp_rect.left = self.settings.row_header_x_right()
            self.screen.blit(label, tmp_rect)
