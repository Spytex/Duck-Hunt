import pygame
from src.drawer import drawer

class Game:
    def __init__(self):
        pygame.init()
        self.win_width = 800
        self.win_height = 800
        self.win = pygame.display.set_mode((self.win_width, self.win_height))
    def run(self):
        while True:
            pass


if __name__ == '__main__':
    game = Game()
    drawer.Drawer()
    # game.run()