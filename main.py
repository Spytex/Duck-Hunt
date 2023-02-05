import pygame
from src.drawer import drawer
from src.loader import loader
from src.objects.units.pig import Pig

class Game:
    def __init__(self):
        pygame.display.set_caption("Duck Hunt")
        pygame.init()
        self.draw = drawer.Drawer()
        data = loader.Loader()
        pygame.mixer.music.load("assets/sounds/menuSound.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)
        self.timer = pygame.time.Clock()
        self.fps = data.fps

    def cycle(self):
        while self.draw.run:
            self.timer.tick(self.fps)
            self.draw.DrawMenu()

if __name__ == '__main__':
    game = Game()
    game.cycle()