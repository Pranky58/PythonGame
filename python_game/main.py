from entities.player import *
from constants import *
from pygame.locals import *

import sys, os, pygame

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = BACKGROUND_COLOR
        self.player = Player(
                                x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, z = 1,
                                height = 64, width = 64,
                                img_name = 'mario.png'
                            )

        self.game_input = InputHandler()
        self.clock = pygame.time.Clock()
        self.clock.tick(60)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.game_input.update()
        self.movement(self.game_input)

                