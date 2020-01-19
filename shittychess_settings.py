#!/usr/bin/env python
# coding=utf-8


class ShittySettings:

    def __init__(self):
        self.screen_height = 480
        self.screen_width = 480

        # Settings for the board
        self.tile_w = 120
        self.tile_h = 120

        self.cols = 8
        self.rows = 8

        self.cols_per_tile = 2
        self.rows_per_tile = 2


    def square_width(self):
        return int(self.tile_w / self.cols_per_tile)


    def square_height(self):
        return int(self.tile_h / self.rows_per_tile)
