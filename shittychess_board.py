#!/usr/bin/env python
# coding=utf-8


import pygame

from shittychess_settings import ShittySettings


class ShittyBoard:
    """This class represents a board."""

    def __init__(self, screen: pygame.Surface, settings: ShittySettings):
        """Initialize the board's attributes."""

        self.screen = screen
        self.settings = settings

        # Get the image, its rect and set it on the screen.
        self.image = pygame.image.load(self.settings.tile_image_path)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.screen_rect = self.screen.get_rect()

        self.header_font = pygame.font.Font(self.settings.header_font_path, self.settings.header_font_size)
        self.horizontal_header_labels = []
        self.vertical_header_labels = []
        for label in self.settings.horizontal_headers:
            self.horizontal_header_labels.append(self.header_font.render(label, True, self.settings.header_font_color, None))
        for label in self.settings.vertical_headers:
            self.vertical_header_labels.append(self.header_font.render(label, True, self.settings.header_font_color, None))


    def draw(self):
        for i in range(self.settings.board_start_y(), self.settings.tile_h * 4, self.settings.tile_h):
            for j in range(self.settings.board_start_x(), self.settings.tile_w * 4, self.settings.tile_w):
                self.rect.x = i
                self.rect.y = j
                self.screen.blit(self.image, self.rect)

        # the labels could be centered more but overall not terrible
        if self.settings.headers:
            self.draw_headers()


    def draw_headers(self):
        font_width = self.settings.header_font_size
        font_height = font_width
        if len(self.horizontal_header_labels) > 0:
            tmp_rect = self.horizontal_header_labels[0].get_rect()
            font_width = tmp_rect.width
            font_height = tmp_rect.height

        horizontal_x_start = int(self.settings.vertical_header_size + (self.settings.square_width() / 2) - (font_width / 2))
        horizontal_top_y = int((self.settings.horizontal_header_size - self.settings.header_font_size) / 2)
        horizontal_bottom_y = int((self.settings.screen_height() - self.settings.horizontal_header_size) + ((self.settings.horizontal_header_size - self.settings.header_font_size) / 2))

        vertical_y_start = int(self.settings.horizontal_header_size + (self.settings.square_height() / 2) - (font_height / 2))
        vertical_left_x = int((self.settings.vertical_header_size - self.settings.header_font_size) / 2)
        vertical_right_x = int((self.settings.screen_width() - self.settings.vertical_header_size) + ((self.settings.vertical_header_size - self.settings.header_font_size) / 2))

        for label, x in zip(self.horizontal_header_labels, range(horizontal_x_start, (self.settings.square_width() * self.settings.cols) + horizontal_x_start, self.settings.square_width())):
            tmp_rect = label.get_rect()
            tmp_rect.left = x
            tmp_rect.top = horizontal_top_y
            self.screen.blit(label, tmp_rect)
            tmp_rect.top = horizontal_bottom_y
            self.screen.blit(label, tmp_rect)

        for label, y in zip(self.vertical_header_labels, range(vertical_y_start, (self.settings.square_height() * self.settings.rows) + vertical_y_start, self.settings.square_height())):
            tmp_rect = label.get_rect()
            tmp_rect.left = vertical_left_x
            tmp_rect.top = y
            self.screen.blit(label, tmp_rect)
            tmp_rect.left = vertical_right_x
            self.screen.blit(label, tmp_rect)
