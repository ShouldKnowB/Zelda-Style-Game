import pygame
import sys
from settings import *
from level import Level


class Game:
    def __init__(self):

        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Zelda Type Game')
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run()


if __name__ == '__main__':
    game = Game()
    game.run()
