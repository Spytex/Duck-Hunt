import pygame
from src.loader import loader
from src.resources import resources
from src.objects.units import pig
import random


class Drawer():
    def __init__(self):
        self.menu_state = "main"
        self.load = loader.Loader()
        self.mouse_pos = pygame.mouse.get_pos()
        self.resources = resources.Resource()

        self.targets = []
        if self.resources.level != 1:
            self.resources.countPigs += self.resources.level
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))
        else:
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))

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
                    self.resources.load.loadGeneralMusic()
                if self.resources.sound2_button.draw(self.resources.screen):
                    self.resources.sound = "music2.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadGeneralMusic()
                if self.resources.sound3_button.draw(self.resources.screen):
                    self.resources.sound = "music3.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadGeneralMusic()
                if self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
        else:
            self.DrawLevel()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.resources.game_paused = not self.resources.game_paused
                if event.key == pygame.K_ESCAPE:
                    self.resources.game_paused = not self.resources.game_paused
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_pos = pygame.mouse.get_pos()
                self.resources.shot = True
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()  # flip()

    def DrawLevel(self):
        if(self.resources.HP <= 0):
            self.resources.game_paused = True
            self.resources.menu_state = "main"
            return

        for i in range(2):
            self.resources.bgs.append(pygame.image.load(f'assets/bg/background{i+1}.png'))
        self.resources.screen.fill('black')
        self.resources.screen.blit(self.resources.bgs[self.resources.level % 2], (0, 0))

        if self.checkVisibility() != False :
            self.targets = []
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))
            self.resources.level += 1
            self.resources.countPigs += 1 

        

        self.moveTargets()

    def moveTargets(self):
        for i in self.targets:
            i.move(self.resources.SCREEN_WIDTH, self.resources.level, self.minusHP)
            self.resources.shot = i.hit(self.resources.shot, self.plusScore, self.mouse_pos)

        for i in self.targets:
            if (i.visible):
                self.resources.screen.blit(pygame.transform.scale(self.resources.enemyImage, (50,50)) , (i.x,i.y))
        self.drawBanner()
        pygame.display.update()

    def getCoords(self):
        return random.sample(self.resources.grid, self.resources.countPigs)

    def checkVisibility(self):
        for i in self.targets:
            if i.visible == True:
                return False
            
        return True

    def drawBanner(self):
        self.resources.screen.blit(self.resources.levelSurface, (25,740))
        self.resources.screen.blit(pygame.transform.scale(self.resources.font.render(f"HP: {self.resources.HP}", True, (255,255,255)), (90,40)), (350,5) )

        self.resources.levelSurface.fill((0,0,0,1))
        self.resources.levelSurface.blit(pygame.transform.scale(self.resources.font.render(f"Level: {self.resources.level}", True, (255,255,255)), (110,50)), (310,0) )
        self.resources.levelSurface.blit(pygame.transform.scale(self.resources.font.render(f"Score: {self.resources.score}", True, (255,255,255)), (110,50)), (620,0) )
        if self.resources.pauseButton.draw(self.resources.screen):
            self.resources.game_paused = True
            self.resources.menu_state = "main"

    def plusScore(self):
        self.resources.score += 10

    def minusHP(self):
        self.resources.HP -= 10
        