import pygame
from settings import *
from tile import Tile
from player import Player


class Level:
    def __init__(self):

        # Get The Display Surface
        self.display_surface = pygame.display.get_surface()

        # Sprite Group Setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # Sprite Setup
        self.create_map()

    def create_map(self):
        # Create The Map
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites,
                         self.obstacles_sprites])
                    if col == 'p':
                        Player((x, y), [self.visible_sprites])

    def run(self):
        # Update and Draw The Game
        self.visible_sprites.draw(self.display_surface)
