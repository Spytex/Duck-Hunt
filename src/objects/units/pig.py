import pygame


class Pig():
    def __init__(self, coords, width: int, height: int):
        self.x = coords[0]
        self.y = coords[1]
        self.size = (width, height)
        self.health = 1
        self.visible = True
        self.speed = 5
        self.rect = pygame.Rect(coords[0], coords[1], width, height)
        self.pig = 0

    def move(self, width: int, level: int, HP):
        """
            Move method, change coordinates
        """
        self.rect = pygame.Rect(self.x, self.y, self.size[0],  self.size[1])
        if self.x < width:
            self.x += self.speed * (level * 0.3 if level else 1)
        else:
            if self.visible:
                HP()
            self.x = -50

    def hit(self, shot: bool, score, mouse_pos, countPigs: int):
        """
            check hit method
        """
        self.pig += 1
        if self.rect.collidepoint(mouse_pos):
            if shot:
                shot = False
                if self.health > 0:
                    self.health -= 1
                    if self.health == 0:
                        score()
                        self.visible = False     
                else:
                    self.visible = False
        if self.pig == countPigs:
            shot = False
            self.pig = 0
        return shot
            
