import pygame
import json

class Loader():
    
    def __init__(self):
        pygame.init()
        self.settings = self.readJSONFile("src/settings", "settings")
        self.fps = self.settings['fps']
        self.sound = self.settings['sound']
        self.volume = self.settings['volume']

    def readJSONFile(self, path, fileName):
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'r') as fp:
            data = json.load(fp)
        return data

    def writeToJSONFile(self, path, fileName, data):
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)

    def updateJSONFile(self, path, fileName, dataLocation, data):
        filePathNameWExt = './' + path + '/' + fileName + '.json'
        oldData = self.readJSONFile(path, fileName)
        oldData[dataLocation] = data
        with open(filePathNameWExt, 'w') as fp:
            json.dump(oldData, fp)

    def loadMusic(self):
        pygame.mixer.music.stop()
        self.settings = self.readJSONFile("src/settings", "settings")
        self.sound = self.settings['sound']
        self.volume = self.settings['volume']
        pygame.mixer.music.load("assets/sounds/" + self.sound)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
