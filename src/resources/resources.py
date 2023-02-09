import pygame
import os
from src.loader import loader
from src.drawer import button
from src.drawer import slider
from src.loader import parser


class Resource():
    """
       class Resource of game
    """
    def __init__(self) -> None:
        self.load = loader.Loader()
        self.parser = parser.Parser()
        self.arg = self.parser.arguments()

        self.FPS = self.load.fps

        self.HP = 100

        # strings
        self.menu_state = "main"
        self.path = os.path.join("src", "settings")
        self.fileName = "settings"
        self.imageMenuPath = os.path.join("assets", "menu", "")
        self.imageTargetsPath = os.path.join("assets", "targets", "")
        self.data = {}

        # booleans
        self.run = True
        self.game_paused = True
        self.shot = False

        self.level = self.arg.level
        self.score = 0
        self.bgs = []

        self.TEXT_COL = (255, 255, 255)

        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.sound = self.load.sound
        # ----------------------------

        self.font = pygame.font.SysFont("Comic Sans MS", 50)

        # buttons image
        self.resume_img = pygame.image.load(self.imageMenuPath + "button_resume.png").convert_alpha()
        self.options_img = pygame.image.load(self.imageMenuPath + "button_options.png").convert_alpha()
        self.quit_img = pygame.image.load(self.imageMenuPath + "button_quit.png").convert_alpha()
        self.video_img = pygame.image.load(self.imageMenuPath + "button_video.png").convert_alpha()
        self.audio_img = pygame.image.load(self.imageMenuPath + "button_audio.png").convert_alpha()
        self.back_img = pygame.image.load(self.imageMenuPath + "button_back.png").convert_alpha()
        self.knob_image = pygame.image.load(self.imageMenuPath + "pig.png").convert_alpha()
        self.enemyImage = pygame.image.load(self.imageTargetsPath + "pig.png").convert_alpha()

        # buttons
        self.resume_button = button.Button(self.SCREEN_WIDTH*0.38, self.SCREEN_HEIGHT*0.3125, self.resume_img, 1)
        self.options_button = button.Button(self.SCREEN_WIDTH*0.37125, self.SCREEN_HEIGHT*0.46875, self.options_img, 1)
        self.quit_button = button.Button(self.SCREEN_WIDTH*0.42, self.SCREEN_HEIGHT*0.625, self.quit_img, 1)
        self.video_button = button.Button(self.SCREEN_WIDTH*0.2825, self.SCREEN_HEIGHT*0.3125, self.video_img, 1)
        self.audio_button = button.Button(self.SCREEN_WIDTH*0.28125, self.SCREEN_HEIGHT*0.46875, self.audio_img, 1)
        self.back_button = button.Button(self.SCREEN_WIDTH*0.415, self.SCREEN_HEIGHT*0.625, self.back_img, 1)
        self.fps240_button = button.Button(self.SCREEN_WIDTH*0.44375, self.SCREEN_HEIGHT*0.25, self.font.render('240', True, self.TEXT_COL), 1)
        self.fps144_button = button.Button(self.SCREEN_WIDTH*0.44375, self.SCREEN_HEIGHT*0.375, self.font.render('144', True, self.TEXT_COL), 1)
        self.fps60_button = button.Button(self.SCREEN_WIDTH*0.45625, self.SCREEN_HEIGHT*0.5, self.font.render('60', True, self.TEXT_COL), 1)
        self.sound1_button = button.Button(self.SCREEN_WIDTH*0.15, self.SCREEN_HEIGHT*0.25, self.font.render('Sound 1', True, self.TEXT_COL), 1)
        self.sound2_button = button.Button(self.SCREEN_WIDTH*0.4, self.SCREEN_HEIGHT*0.25, self.font.render('Sound 2', True, self.TEXT_COL), 1)
        self.sound3_button = button.Button(self.SCREEN_WIDTH*0.65, self.SCREEN_HEIGHT*0.25, self.font.render('Sound 3', True, self.TEXT_COL), 1)

        self.levelSurface = pygame.Surface((self.SCREEN_WIDTH - 50, 50)).convert_alpha()
        # self.levelSurface.fill((0,255,0, 1))

        self.pauseButton = button.Button(self.SCREEN_WIDTH*0.0375, self.SCREEN_HEIGHT*0.925, self.font.render('Pause', True, (255, 255, 255)), 0.7)

        self.restartButton = button.Button(340,350, self.font.render('Restart', True, (255, 255, 255)), 0.7)
        self.goMenuButton = button.Button(340,400, self.font.render('Menu', True, (255, 255, 255)), 0.7)

        self.yArrayPos = []
        self.countPigs = 10

        self.grid = []
        self.gridSize = 10

        self.slider = slider.Slider(self.SCREEN_WIDTH*0.25, self.SCREEN_HEIGHT*0.375, 400, 100)

        self.generateGrid()

    def generateGrid(self):

        """
            generate grid to situated targets
        """
        x = -500
        y = 50

        for i in range(self.gridSize):
            for j in range(self.gridSize):
                self.grid.append([x + 50 * j, y + 50 * i])
