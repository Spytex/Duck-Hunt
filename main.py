import pygame
from src.drawer import drawer

class Game:
    def __init__(self):
        pygame.init()
        self.game_paused = False
        self.menu_state = "main"
    def cycle(self):
        draw = drawer.Drawer()
        while draw.run:
            draw.DrawMenu()


if __name__ == '__main__':
    game = Game()
    game.cycle()