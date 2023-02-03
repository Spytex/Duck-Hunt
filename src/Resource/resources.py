import pygame
import math


class Resource():

    # consts
    FPS = 60
    WIDTH = 900
    HEIGHT = 800    

    # main timer
    timer = None


    # booleans
   
    # settungs
    fullScreen = False
    soundEnable = False

    new_coords = False
    shot = False
    menu = True
    game_over = False
    pause = False


    level = 0
    points = 0
    total_shots = 0
    time_passed = 0

    targets = {1: [10, 5, 3],
           2: [12, 8, 5],
           3: [15, 12, 8, 3]}

    # images
    target_images = [[], [], []]
    backGroundImage = []
    bannersImage = []
    gunsImage = []
    menu_img = None
    game_over_img = None
    pause_img = None


    # fonts
    # font = pygame.font.Font(None,32)
    # big_font = pygame.font.Font(None,60)


    # sounds


    def __init__(self) -> None:
        self.timer = pygame.time.Clock()
        self.timer.tick(self.FPS)