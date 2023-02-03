import pygame
from src.drawer import button


class Drawer():
    def __init__(self):
        self.menu_state = "main"
        self.game_paused = False
        self.TEXT_COL = (255, 255, 255)
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.font = pygame.font.SysFont("arialblack", 40)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Main Menu")
        self.resume_img = pygame.image.load("assets/menu/button_resume.png").convert_alpha()
        self.options_img = pygame.image.load("assets/menu/button_options.png").convert_alpha()
        self.quit_img = pygame.image.load("assets/menu/button_quit.png").convert_alpha()
        self.video_img = pygame.image.load('assets/menu/button_video.png').convert_alpha()
        self.audio_img = pygame.image.load('assets/menu/button_audio.png').convert_alpha()
        self.keys_img = pygame.image.load('assets/menu/button_keys.png').convert_alpha()
        self.back_img = pygame.image.load('assets/menu/button_back.png').convert_alpha()
        self.resume_button = button.Button(304, 125, self.resume_img, 1)
        self.options_button = button.Button(297, 250, self.options_img, 1)
        self.quit_button = button.Button(336, 375, self.quit_img, 1)
        self.video_button = button.Button(226, 75, self.video_img, 1)
        self.audio_button = button.Button(225, 200, self.audio_img, 1)
        self.keys_button = button.Button(246, 325, self.keys_img, 1)
        self.back_button = button.Button(332, 450, self.back_img, 1)

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
                    pygame.quit()
            # check if the options menu is open
            if self.menu_state == "options":
                # draw the different options buttons
                if self.video_button.draw(self.screen):
                    print("Video Settings")
                if self.audio_button.draw(self.screen):
                    print("Audio Settings")
                if self.keys_button.draw(self.screen):
                    print("Change Key Bindings")
                if self.back_button.draw(self.screen):
                    self.menu_state = "main"
        else:
            self.DrawText("Press SPACE to pause", self.font, self.TEXT_COL, 160, 250)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_paused = True
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()




    def DrawButtons(self):
        pass

    def DrawLevel(self):
        pass

    def DrawUnit(self):
        pass

    def DrawResult(self):
        pass

    def DrawPause(self):
        pass