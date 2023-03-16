import pygame
import random
import os
from src.Loader import loader
from src.Resources import resources
from src.Objects.units import pig


class Drawer():
    def __init__(self):
        self.menu_state = "main"
        self.load = loader.Loader()
        self.mouse_pos = pygame.mouse.get_pos()
        self.resources = resources.Resource()

        self.targets = []
        self.initTargets()

    def DrawText(self, text: str, font, text_col, x: int, y: int):
        """ 
            Draw Text
        """
        self.img = font.render(text, True, text_col)
        self.resources.screen.blit(self.img, (x, y))

    def DrawMenu(self):
        """ 
            Draw Menu
        """
        self.resources.screen.fill((52, 78, 91))
        # check if game is paused
        if self.resources.game_paused:
            # check menu state
            if self.resources.menu_state == "main":
                # draw pause screen buttons
                if self.resources.resume_button.draw(self.resources.screen):
                    self.resources.game_paused = False
                elif self.resources.options_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
                elif self.resources.quit_button.draw(self.resources.screen):
                    self.resources.run = False
            # check if the options menu is open
            elif self.resources.menu_state == "options":
                # draw the different options buttons
                if self.resources.video_button.draw(self.resources.screen):
                    self.resources.menu_state = "video settings"
                elif self.resources.audio_button.draw(self.resources.screen):
                    self.resources.menu_state = "audio settings"
                elif self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "main"
            elif self.resources.menu_state == "video settings":
                self.DrawText("Select FPS", self.resources.font, self.resources.TEXT_COL, 270, 100)
                if self.resources.fps240_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 240)
                elif self.resources.fps144_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 144)
                elif self.resources.fps60_button.draw(self.resources.screen):
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "fps", 60)
                elif self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
            elif self.resources.menu_state == "audio settings":
                if self.resources.slider.draw(self.resources.screen):
                    pass
                elif self.resources.sound1_button.draw(self.resources.screen):
                    self.resources.sound = "music1.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadGeneralMusic()
                elif self.resources.sound2_button.draw(self.resources.screen):
                    self.resources.sound = "music2.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadGeneralMusic()
                elif self.resources.sound3_button.draw(self.resources.screen):
                    self.resources.sound = "music3.mp3"
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "volume", self.resources.slider.volume)
                    self.resources.load.updateJSONFile(self.resources.path, self.resources.fileName, "sound", self.resources.sound)
                    self.resources.load.loadGeneralMusic()
                elif self.resources.back_button.draw(self.resources.screen):
                    self.resources.menu_state = "options"
            elif self.resources.menu_state == "game_over":
                self.resources.level = 1
                self.resources.countPigs = 10
                self.initTargets()
                self.resources.screen.blit(pygame.transform.scale(self.resources.font.render(f"Score: {self.resources.score}", True, (255,255,255)), (110,50)), (340,300) )
                if self.resources.restartButton.draw(self.resources.screen):
                    self.resources.score = 0
                    self.resources.game_paused = False
                elif self.resources.goMenuButton.draw(self.resources.screen):
                    self.resources.score = 0
                    self.resources.game_paused = True
                    self.resources.menu_state = "main"

        else:
            self.DrawLevel()

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.resources.game_paused = not self.resources.game_paused
                elif event.key == pygame.K_ESCAPE:
                    self.resources.game_paused = not self.resources.game_paused
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_pos = pygame.mouse.get_pos()
                self.resources.shot = True
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()  # flip()

    def DrawLevel(self):
        """ 
            Draw Level
        """
        if self.resources.HP <= 0:
            self.resources.game_paused = True
            self.resources.menu_state = "game_over"
            self.resources.HP = 100
            self.initTargets()
            return

        for i in range(2):
            self.resources.bgs.append(pygame.image.load(os.path.join('assets', 'bg', f'background{i+1}.png')))
        self.resources.screen.fill('black')
        self.resources.screen.blit(self.resources.bgs[self.resources.level % 2], (0, 0))

        if self.checkVisibility():
            self.targets = []
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))
            self.resources.level += 1
            self.resources.countPigs += 1 

        self.moveTargets()

    def moveTargets(self):
        """ 
           moveTargets method
        """
        for i in self.targets:
            i.move(self.resources.SCREEN_WIDTH, self.resources.level, self.minusHP)
            self.resources.shot = i.hit(self.resources.shot, self.plusScore, self.mouse_pos, self.resources.countPigs)

        for i in self.targets:
            if (i.visible):
                self.resources.screen.blit(pygame.transform.scale(self.resources.enemyImage, (50,50)), (i.x,i.y))
        self.drawBanner()
        pygame.display.update()

    def getCoords(self):
        """ 
           return list of coordianter for targent
        """
        return random.sample(self.resources.grid, self.resources.countPigs)

    def checkVisibility(self):
        """ 
           check Visibility of each target
        """
        for i in self.targets:
            if i.visible:
                return False
            
        return True

    def drawBanner(self):
        """ 
           draw banner wit h level score and button pause
        """
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

    def initTargets(self):
        """ 
           init Targets method
        """
        self.targets = []
        if self.resources.level != 1 and self.resources.menu_state != "game_over":
            self.resources.countPigs += self.resources.level
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))
        else:
            self.coords = self.getCoords()
            for i in range(self.resources.countPigs):
                self.targets.append(pig.Pig(self.coords[i], 50, 50))
        