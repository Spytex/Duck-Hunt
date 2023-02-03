import pygame
from src.drawer import drawer

class Game:
    def __init__(self):
        pygame.init()
        self.game_paused = False
        self.menu_state = "main"
    def run(self):
        draw = drawer.Drawer()
        while True:
            draw.DrawMenu()


if __name__ == '__main__':
    game = Game()
    game.run()