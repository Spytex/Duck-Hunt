import pygame


class Pig():
    def __init__(self, coords, width, height):
        self.x = coords[0]
        self.y = coords[1]
        self.size = (width, height)
        self.health = 1
        self.visible = True
        self.speed = 5
        self.rect = pygame.Rect(coords[0], coords[1], width, height)

    def move(self, width, level):
        if (self.x < width):
            self.x += self.speed * (level * 0.3 if level else 1)
        else:
            self.x = -50
        
        self.rect = pygame.Rect(self.x ,self.y , self.size[0],  self.size[1])

    def hit(self, shot):
        mouse_pos = pygame.mouse.get_pos()

        if (self.rect.collidepoint(mouse_pos)):
            if shot:
                if self.health > 0:
                    self.health -= 1
                    if self.health == 0:
                        self.visible = False
                else:
                    self.visible = False
