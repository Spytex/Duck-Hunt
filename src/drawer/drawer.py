import pygame
from src.drawer import button
from src.loader import loader
from src.drawer import slider


class Drawer():
    def __init__(self):
        self.menu_state = "main"   #
        self.load = loader.Loader()
        self.path = "src/settings"  # pathSettings
        self.fileName = "settings"  # fileSettings
        self.run = True #
        self.game_paused = True   #
        self.level = 0    #
        self.bgs = []    #
        self.banners = []  #
        self.TEXT_COL = (255, 255, 255)    #
        self.SCREEN_WIDTH = 800   #
        self.SCREEN_HEIGHT = 800    #
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))   #
        self.sound = self.load.sound
        self.yes_sound = pygame.mixer.Sound('assets/sounds/yes.mp3')   #
        self.yes_sound.set_volume(1)   # Set general volume #
        self.font = pygame.font.SysFont("Comic Sans MS", 50)          #
        self.resume_img = pygame.image.load("assets/menu/button_resume.png").convert_alpha()     #
        self.options_img = pygame.image.load("assets/menu/button_options.png").convert_alpha()   #
        self.quit_img = pygame.image.load("assets/menu/button_quit.png").convert_alpha()       #
        self.video_img = pygame.image.load('assets/menu/button_video.png').convert_alpha()    #
        self.audio_img = pygame.image.load('assets/menu/button_audio.png').convert_alpha()   #
        self.keys_img = pygame.image.load('assets/menu/button_keys.png').convert_alpha()   #
        self.back_img = pygame.image.load('assets/menu/button_back.png').convert_alpha()   #
        self.resume_button = button.Button(304, 250, self.resume_img, 1)   #
        self.options_button = button.Button(297, 375, self.options_img, 1)   #
        self.quit_button = button.Button(336, 500, self.quit_img, 1)   #
        self.video_button = button.Button(226, 250, self.video_img, 1)   #
        self.audio_button = button.Button(225, 375, self.audio_img, 1)   #
        self.back_button = button.Button(332, 500, self.back_img, 1)   #
        self.fps240_button = button.Button(355, 200, self.font.render('240', True, self.TEXT_COL), 1)   #
        self.fps144_button = button.Button(355, 300, self.font.render('144', True, self.TEXT_COL), 1)   #
        self.fps60_button = button.Button(365, 400, self.font.render('60', True, self.TEXT_COL), 1)   #
        self.save_button = button.Button(340, self.SCREEN_HEIGHT/2, self.font.render('Save', True, self.TEXT_COL), 1)   #
        self.sound1_button = button.Button(120, 200, self.font.render('Sound 1', True, self.TEXT_COL), 1)   #
        self.sound2_button = button.Button(320, 200, self.font.render('Sound 2', True, self.TEXT_COL), 1)   #
        self.sound3_button = button.Button(520, 200, self.font.render('Sound 3', True, self.TEXT_COL), 1)   #
        self.slider = slider.Slider(200, 300, 400, 100)    #

    def DrawText(self, text, font, text_col, x, y):
        self.img = font.render(text, True, text_col)
        self.screen.blit(self.img, (x, y))

    def DrawMenu(self):
        self.screen.fill((52, 78, 91))
        # check if game is paused
        if self.game_paused == True:
            # check menu state
            if self.menu_state == "main":
                # draw pause screen buttons
                if self.resume_button.draw(self.screen):
                    self.game_paused = False
                if self.options_button.draw(self.screen):
                    self.menu_state = "options"
                if self.quit_button.draw(self.screen):
                    self.run = False
            # check if the options menu is open
            if self.menu_state == "options":
                # draw the different options buttons
                if self.video_button.draw(self.screen):
                    self.menu_state = "video settings"
                if self.audio_button.draw(self.screen):
                    self.menu_state = "audio settings"
                if self.back_button.draw(self.screen):
                    self.menu_state = "main"
            if self.menu_state == "video settings":
                self.DrawText("Select FPS", self.font, self.TEXT_COL, 270, 100)
                if self.fps240_button.draw(self.screen):
                    self.load.updateJSONFile(self.path, self.fileName, "fps", 240)
                    self.yes_sound.play()
                if self.fps144_button.draw(self.screen):
                    self.load.updateJSONFile(self.path, self.fileName, "fps", 144)
                    self.yes_sound.play()
                if self.fps60_button.draw(self.screen):
                    self.load.updateJSONFile(self.path, self.fileName, "fps", 60)
                    self.yes_sound.play()
                if self.back_button.draw(self.screen):
                    self.menu_state = "options"
            if self.menu_state == "audio settings":
                if self.slider.draw(self.screen):
                    pass
                if self.sound1_button.draw(self.screen):
                    self.sound = "music1.mp3"
                    self.load.updateJSONFile(self.path, self.fileName, "sound", self.sound)
                    self.load.loadMusic()
                if self.sound2_button.draw(self.screen):
                    self.sound = "music2.mp3"
                    self.load.updateJSONFile(self.path, self.fileName, "sound", self.sound)
                    self.load.loadMusic()
                if self.sound3_button.draw(self.screen):
                    self.sound = "music3.mp3"
                    self.load.updateJSONFile(self.path, self.fileName, "sound", self.sound)
                    self.load.loadMusic()
                if self.back_button.draw(self.screen):
                    self.menu_state = "options"
        else:
            self.DrawLevel()
            # self.DrawText("Press SPACE to pause", self.font, self.TEXT_COL, 145, 350)
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_paused = not self.game_paused
                if event.key == pygame.K_ESCAPE:
                    self.game_paused = not self.game_paused
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()  # flip()

    def DrawLevel(self):
        # pygame.display.set_caption("Level " + str(self.level+1))
        for i in range(2):
            self.bgs.append(pygame.image.load(f'assets/bg/background{i+1}.png'))
        self.screen.fill('black')
        self.screen.blit(self.bgs[self.level % 2], (0, 0))

    def DrawUnit(self):
        pass

    def DrawResult(self):
        pass