from myModules import *
import sys, os, pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = BACKGROUND_COLOR

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(background)
    pygame.display.flip()
