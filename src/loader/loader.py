import pygame
import json

class Loader():
    def __init__(self):
        pygame.init()
        self.settings = self.readJSONFile("src/settings", "settings")
        self.fps = self.settings['fps']

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