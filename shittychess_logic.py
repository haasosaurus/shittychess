# coding=utf-8


import pygame


class ShittyLogic:

    def __init__(self, settings):
        self.settings = settings
        self.space_coords = {}
        self.configure_layout()
        self.print_coords()


    def configure_layout(self):
        cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rows = ['8', '7', '6', '5', '4', '3', '2', '1']
        for row, y in zip(rows, range(0, int(self.settings.square_height() * self.settings.rows), self.settings.square_height())):
            for col, x in zip(cols, range(0, int(self.settings.square_width() * self.settings.cols), self.settings.square_width())):
                pos_name = row + col
                tmp_rect = pygame.Rect(x, y, 0, 0)
                self.space_coords.update({pos_name: tmp_rect})


    def print_coords(self):
        for key, val in self.space_coords.items():
            print(f'{key}: x: {val.left}, y: {val.top}')
