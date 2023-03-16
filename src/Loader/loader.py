import pygame
import json
import os


class Loader():
    def __init__(self):
        pygame.init()
        self.settings = self.readJSONFile(os.path.join('src', 'settings'), "settings")
        self.fps = self.settings['fps']
        self.sound = self.settings['sound']
        self.volume = self.settings['volume']
        self.yesSound = self.loadSound('yes')

    def readJSONFile(self, path: str, fileName: str):
        """
        Read from json file
        """
        filePathNameWExt = os.path.join(path, fileName + '.json')
        with open(filePathNameWExt, 'r') as fp:
            data = json.load(fp)
        return data

    def writeToJSONFile(self, path: str, fileName: str, data):
        """
        write in json file
        """
        filePathNameWExt = os.path.join(path, fileName + '.json')
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)

    def updateJSONFile(self, path: str, fileName: str, dataLocation, data):
        """
        update JSON File
        """
        filePathNameWExt = os.path.join(path, fileName + '.json')
        oldData = self.readJSONFile(path, fileName)
        oldData[dataLocation] = data
        with open(filePathNameWExt, 'w') as fp:
            json.dump(oldData, fp)

    def loadGeneralMusic(self):
        """
        Set sound to play
        """
        
        pygame.mixer.music.stop()
        self.settings = self.readJSONFile(os.path.join('src', 'settings'), "settings")
        self.sound = self.settings['sound']
        self.volume = self.settings['volume']
        pygame.mixer.music.load(os.path.join("assets", "sounds", "") + self.sound)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)

    def loadSound(self, fileName: str):
        """
        load all sounds
        """
        filePathNameWExt = os.path.join('assets', 'sounds', fileName + '.mp3')
        self.settings = self.readJSONFile(os.path.join('src', 'settings'), 'settings')
        self.volume = self.settings['volume']
        sound = pygame.mixer.Sound(filePathNameWExt)
        sound.set_volume(self.volume)
        return sound