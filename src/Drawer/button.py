import pygame
from src.Loader import loader


class Button():
    def __init__(self, x: float, y: float, image, scale: float):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.loader = loader.Loader()

    def draw(self, surface: pygame.surface):
        """ 
            Draw button and add click Event
        """
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not self.clicked:
                    self.clicked = True
                    action = True
                    yesSound = self.loader.loadSound('yes')
                    yesSound.play()

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action
