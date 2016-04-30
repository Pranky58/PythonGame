from myModules import *
import sys, os, pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = BACKGROUND_COLOR

testObject = GameObject(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, z = 1,
                        width = 64, height = 64,
                        imgName = 'mario.png'
                        )

while 1:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    screen.fill(background)
    testObject.render(screen)

    pygame.display.flip()
