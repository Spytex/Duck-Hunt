import pygame
from src.drawer import button
from src.loader import loader
from src.drawer import slider
from src.resources import resources
from src.objects.units import pig
import random

class Drawer():
    def __init__(self):
        self.menu_state = "main"
        self.load = loader.Loader()

        self.resources = resources.Resource()

        self.targets = []

        for i in range(10):
            a = 0
            self.targets.append(pig.Pig(self.generateCoords(), 50, 50))
            self.resources.yArrayPos.append(a)
            a += 50
        

    def DrawText(self, text, font, text_col, x, y):
        self.img = font.render(text, True, text_col)
        self.resources.screen.blit(self.img, (x, y))

    def DrawMenu(self):

        self.resources.screen.fill((52, 78, 91))
        # check if game is paused   
        if self.resources.game_paused == True:
            # check menu state
            if self.resources.menu_state == "main":
                # draw pause screen buttons
                if self.resources.resume_button.draw(self.resources.screen):
                    self.resources.game_paused = False
                if self.resources.options_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
                if self.resources.quit_button.draw(self.resources.screen):
                    self.resources.run = False
            # check if the options menu is open
            if self.resources.menu_state == "options":
                # draw the different options buttons
                if self.resources.video_button.draw(self.resources.screen):
                    self.resources.menu_state = "video settings"
                if self.resources.audio_button.draw(self.resources.screen):
                    self.resources.menu_state = "audio settings"
                if self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "main"
            if self.resources.menu_state == "video settings":
                self.DrawText("Select FPS", self.resources.font, self.resources.TEXT_COL, 270, 100)
                if self.resources.fps240_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 240)
                if self.resources.fps144_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 144)
                if self.resources.fps60_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 60)
                if self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
            if self.resources.menu_state == "audio settings":
                if self.resources.slider.draw(self.resources.screen):
                    pass
                if self.resources.sound1_button.draw(self.resources.screen):
                    self.resources.sound = "music1.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadMusic()
                if self.resources.sound2_button.draw(self.resources.screen):
                    self.resources.sound = "music2.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadMusic()
                if self.resources.sound3_button.draw(self.resources.screen):
                    self.resources.sound = "music3.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadMusic()
                if self.resources.save_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadMusic()
                if self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
        else:
            self.DrawLevel()
            # self.DrawText("Press SPACE to pause", self.font, self.TEXT_COL, 145, 350)


        
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.resources.game_paused = not self.resources.game_paused
                if event.key == pygame.K_ESCAPE:
                    self.resources.game_paused = not self.resources.game_paused
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.resources.shot = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.resources.shot = False
            if event.type == pygame.QUIT:
                pygame.quit()
      

        pygame.display.update()  # flip()

    def DrawLevel(self):
        # pygame.display.set_caption("Level " + str(self.level+1))
        for i in range(2):
            self.resources.bgs.append(pygame.image.load(f'assets/bg/background{i+1}.png'))
        self.resources.screen.fill('black')
        self.resources.screen.blit(self.resources.bgs[self.resources.level % 2], (0, 0))

        if self.checkVisibility() != False :
            self.targets = []
            for i in range(10):
                self.targets.append(pig.Pig(self.generateCoords(), 50, 50))
            self.resources.level +=1
        


        for i in self.targets:
            if(i.visible):
                self.resources.screen.blit(pygame.transform.scale(self.resources.enemyImage, (50,50)), (i.x,i.y))

        self.moveTargets()

    
    def moveTargets(self):
        for i in self.targets:
            i.move(self.resources.SCREEN_WIDTH, self.resources.level)
            i.hit(self.resources.shot)

        for i in self.targets:
            if(i.visible):
                self.resources.screen.blit(pygame.transform.scale(self.resources.enemyImage, (50,50)) , (i.x,i.y))


        pygame.display.update()

    def generateCoords(self):
        return (random.randint(-250 , -50), random.randint(10, self.resources.SCREEN_HEIGHT - 100))


    def checkVisibility(self):
        for i in self.targets:
            if i.visible == True:
                return False
            
        return True
        