import pygame
from src.drawer import drawer
from src.objects.units.pig import Pig


class Game:
    def __init__(self):
        pygame.display.set_caption("Duck Hunt")
        pygame.init()
        self.draw = drawer.Drawer()
        self.draw.resources.load.loadGeneralMusic()
        self.fps = self.draw.resources.FPS
        self.timer = pygame.time.Clock()

    def cycle(self):
        while self.draw.resources.run:
            self.timer.tick(self.fps)
            self.draw.DrawMenu()


if __name__ == '__main__':
    game = Game()
    game.cycle()
