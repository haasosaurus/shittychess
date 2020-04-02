# coding=utf-8


from os import PathLike
from typing import Union

import pygame


class ShittyView:
    """game view controller"""

    def __init__(self, screen: pygame.Surface) -> None:
        """constructor"""

        self.screen = screen
        self.images = {}
        self.current_img_width = 0
        self.current_img_height = 0
        self.space_solid_img_paths = {
            'black': 'shitty_art/space_solid_black.png',
            'white': 'shitty_art/space_solid_white.png',
        }
        self.space_wood_img_paths = {
            'black': 'shitty_art/space_wood_black.png',
            'white': 'shitty_art/space_wood_white.png',
        }
        self.shitty_img_paths = {
            'pawn_black': 'shitty_art/shitty_pawn_black.png',
            'pawn_white': 'shitty_art/shitty_pawn_white.png',
            'rook_black': 'shitty_art/shitty_rook_black.png',
            'rook_white': 'shitty_art/shitty_rook_white.png',
            'bishop_black': 'shitty_art/shitty_bishop_black.png',
            'bishop_white': 'shitty_art/shitty_bishop_white.png',
            'knight_black': 'shitty_art/shitty_knight_black.png',
            'knight_white': 'shitty_art/shitty_knight_white.png',
            'queen_black': 'shitty_art/shitty_queen_black.png',
            'queen_white': 'shitty_art/shitty_queen_white.png',
            'king_black': 'shitty_art/shitty_king_black.png',
            'king_white': 'shitty_art/shitty_king_white.png',
        }
        self.trad_img_paths = {
            'pawn_black': 'shitty_art/trad_pawn_black.png',
            'pawn_white': 'shitty_art/trad_pawn_white.png',
            'rook_black': 'shitty_art/trad_rook_black.png',
            'rook_white': 'shitty_art/trad_rook_white.png',
            'bishop_black': 'shitty_art/trad_bishop_black.png',
            'bishop_white': 'shitty_art/trad_bishop_white.png',
            'knight_black': 'shitty_art/trad_knight_black.png',
            'knight_white': 'shitty_art/trad_knight_white.png',
            'queen_black': 'shitty_art/trad_queen_black.png',
            'queen_white': 'shitty_art/trad_queen_white.png',
            'king_black': 'shitty_art/trad_king_black.png',
            'king_white': 'shitty_art/trad_king_white.png',
        }
        self.img_paths = {
            'space solid': self.space_solid_img_paths,
            'space wood': self.space_wood_img_paths,
            'shitty': self.shitty_img_paths,
            'trad': self.trad_img_paths,
        }

    def __load_image(self, img_path: Union[PathLike, str]) -> pygame.image:
        """loads an individual image"""

        img_path_str = img_path if isinstance(img_path, str) else str(img_path)
        return pygame.image.load(img_path_str)

    def load_images(self, width: int, height: int) -> None:
        """iterates and loads all images in the settings image path dict"""

        for img_name, img_path in self.img_paths.items():
            img = self.__load_image(img_path)
            rect = img.get_rect()
            if rect.width != width or rect.height != height:
                img = pygame.transform.smoothscale(img, (width, height))
            self.images.update({img_name: img})
