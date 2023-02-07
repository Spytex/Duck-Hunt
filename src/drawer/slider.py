import pygame
from src.loader import loader


class Slider():
    def __init__(self, x, y, width, height):
        self.slider_rect = pygame.Rect(x, y, width, height)
        self.slider_special = pygame.Rect(x-53, y-3, width+106, height+6)
        self.knob_rect = pygame.Rect(self.slider_rect.x + self.slider_rect.width * 0.5, self.slider_rect.y, 100, 100)
        self.load = loader.Loader()
        self.volume = self.load.volume #
        knob_image = pygame.image.load("assets/menu/pig.png").convert_alpha() #
        self.knob_image = pygame.transform.scale(knob_image, (100, 100))
        self.font = pygame.font.SysFont("Comic Sans MS", 50) #
        self.path = "src/settings"  # pathSettings
        self.fileName = "settings"  # fileSettings
        self.dragging = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        if self.knob_rect.collidepoint(pos):
            for event in pygame.event.get():
                # Check for mouse events
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.dragging = False
                        if self.volume != self.load.volume:
                            self.load.updateJSONFile(self.path, self.fileName, "volume", self.volume)
                            self.load.loadGeneralMusic()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Check if the mouse is over the knob
                        if self.knob_rect.collidepoint(event.pos):
                            self.dragging = True
                if event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        # Calculate the new volume based on the mouse position
                        self.volume = (event.pos[0] - self.slider_rect.x) / self.slider_rect.width
                        self.volume = max(0.0, min(1.0, self.volume))

        pygame.draw.rect(screen, (0, 0, 0), self.slider_special, 2)
        self.knob_rect.x = self.slider_rect.x + int(self.slider_rect.width * self.volume) - 50
        screen.blit(self.knob_image, self.knob_rect)
        volume_text = self.font.render("Volume: {:.2f}".format(self.volume), True, (255, 255, 255))
        text_rect = volume_text.get_rect()
        text_rect.center = (400, 450)
        screen.blit(volume_text, text_rect)
        return action