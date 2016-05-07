from my_modules import *
import sys, os, pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = BACKGROUND_COLOR

clock = pygame.time.Clock()
game_input = InputHandler()

game_objects = [
    Player(
        x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, z = 1,
        height = 64, width = 64,
        img_name = 'mario.png'
    ),

    GameObject(
        x = 0, y = SCREEN_HEIGHT - 64, z = 1,
        height = 64, width = SCREEN_WIDTH,
        img_name = 'floor.png',
        movable = False
    )
]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    game_input.update()

    screen.fill(background)
    pygame.display.flip()
