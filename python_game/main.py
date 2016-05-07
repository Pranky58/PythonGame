from entities import *
from constants import *
from pygame.locals import *

import sys, os, pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = BACKGROUND_COLOR

    def handle_events(self):
       pass
                