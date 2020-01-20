# coding=utf-8


import pygame

from shittychess_settings import ShittySettings
from shittychess_logic import ShittyLogic


class ShittyBoard:
    """This class represents a board."""

    def __init__(self, screen: pygame.Surface, settings: ShittySettings, logic: ShittyLogic) -> None:
        """Initialize the board's attributes."""

        self.screen = screen
        self.settings = settings
        self.logic = logic
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
        if self.settings.debug:
            self.highlight_space('a1')


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


    def highlight_space(self, coords: str) -> None:
        side_rect_width = 2
        side_rect_height = int(self.settings.space_height() / 3)
        top_bottom_rect_width = int(self.settings.space_width() / 3)
        top_bottom_rect_height = 2
        tmp_rect = pygame.Rect.copy(self.logic.coords_to_rect(coords))

        # calculate rects for the sides
        right_top = pygame.Rect(tmp_rect.left, tmp_rect.top, side_rect_width, side_rect_height)
        right_bottom = pygame.Rect.copy(right_top)
        right_bottom.top += self.settings.space_height() - side_rect_height
        left_top = pygame.Rect.copy(right_top)
        left_top.left += self.settings.space_width() - side_rect_width
        left_bottom = pygame.Rect.copy(right_bottom)
        left_bottom.left += self.settings.space_width() - side_rect_width

        # calculate rects for the top and bottom
        top_left = pygame.Rect(tmp_rect.left, tmp_rect.top, top_bottom_rect_width, top_bottom_rect_height)
        bottom_left = pygame.Rect.copy(top_left)
        bottom_left.top += self.settings.space_height() - top_bottom_rect_height
        top_right = pygame.Rect.copy(top_left)
        top_right.left += self.settings.space_width() - top_bottom_rect_width
        bottom_right = pygame.Rect.copy(top_right)
        bottom_right.top += self.settings.space_height() - top_bottom_rect_height

        # draw the lines around the target square
        pygame.draw.rect(self.screen, self.settings.color_white, right_top)
        pygame.draw.rect(self.screen, self.settings.color_white, right_bottom)
        pygame.draw.rect(self.screen, self.settings.color_white, left_top)
        pygame.draw.rect(self.screen, self.settings.color_white, left_bottom)
        pygame.draw.rect(self.screen, self.settings.color_white, top_left)
        pygame.draw.rect(self.screen, self.settings.color_white, bottom_left)
        pygame.draw.rect(self.screen, self.settings.color_white, top_right)
        pygame.draw.rect(self.screen, self.settings.color_white, bottom_right)

        # highlight the background of the target square
        tmp_color = pygame.Color(255, 255, 255, 100)
        tmp_surface = pygame.Surface((self.settings.space_width(), self.settings.space_height())).convert_alpha()
        tmp_surface.fill(tmp_color)
        self.screen.blit(tmp_surface, tmp_rect)
