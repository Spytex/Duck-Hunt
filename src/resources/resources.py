import pygame
import math
from src.loader import loader
from src.drawer import button
from src.drawer import slider

class Resource():

    def __init__(self) -> None:
        
        self.load = loader.Loader()

        self.FPS = 60

        # strings
        self.menu_state = "main"
        self.path = "src/settings"
        self.fileName = "settings"
        self.imageMenuPath = "assets/menu/"

        self.data = {}
        # booleans
        
        self.run = True
        self.game_paused = True
        self.shot = False
        

        self.level = 1
        self.bgs = []

        self.TEXT_COL = (255, 255, 255)


        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))


        self.sound = self.load.sound
        # ----------------------------

        self.font = pygame.font.SysFont("Comic Sans MS", 50)

        #buttons image        
        self.resume_img = pygame.image.load(self.imageMenuPath + "button_resume.png").convert_alpha()
        self.options_img = pygame.image.load(self.imageMenuPath + "button_options.png").convert_alpha()
        self.quit_img = pygame.image.load(self.imageMenuPath + "button_quit.png").convert_alpha()
        self.video_img = pygame.image.load(self.imageMenuPath + "button_video.png").convert_alpha()
        self.audio_img = pygame.image.load(self.imageMenuPath + "button_audio.png").convert_alpha()
        self.back_img = pygame.image.load(self.imageMenuPath + "button_back.png").convert_alpha()

        self.enemyImage = pygame.image.load(self.imageMenuPath + "pig.png").convert_alpha()

        # buttons
        self.resume_button = button.Button(304, 200, self.resume_img, 1)
        self.options_button = button.Button(297, 325, self.options_img, 1)
        self.quit_button = button.Button(336, 450, self.quit_img, 1)
        self.video_button = button.Button(226, 125, self.video_img, 1)
        self.audio_button = button.Button(225, 250, self.audio_img, 1)
        # self.keys_button = button.Button(246, 375, self.keys_img, 1)
        self.back_button = button.Button(332, 500, self.back_img, 1)
        self.fps240_button = button.Button(355, 200, self.font.render('240', True, self.TEXT_COL), 1)
        self.fps144_button = button.Button(355, 300, self.font.render('144', True, self.TEXT_COL), 1)
        self.fps60_button = button.Button(365, 400, self.font.render('60', True, self.TEXT_COL), 1)
        self.save_button = button.Button(340, 400, self.font.render('Save', True, self.TEXT_COL), 1)
        self.sound1_button = button.Button(120, 100, self.font.render('Sound 1', True, self.TEXT_COL), 1)
        self.sound2_button = button.Button(320, 100, self.font.render('Sound 2', True, self.TEXT_COL), 1)
        self.sound3_button = button.Button(520, 100, self.font.render('Sound 3', True, self.TEXT_COL), 1)


        self.yArrayPos = []


        self.slider = slider.Slider(200, 200, 400, 100)
