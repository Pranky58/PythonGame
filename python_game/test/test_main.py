from my_modules import *
import sys, os, pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = BACKGROUND_COLOR

clock = pygame.time.Clock()
game_input = InputHandler()
mario = Player(
                x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2,
                height = 64, width = 64,
                img_name = 'mario.png'
        )

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    game_input.update()
    mario.movement(game_input)
    mario.move(clock.tick_busy_loop())

    screen.fill(background)
    mario.render(screen)
    pygame.display.flip()
