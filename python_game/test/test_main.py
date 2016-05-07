from my_modules import *
import sys, os, pygame

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = BACKGROUND_COLOR
game_input = InputHandler()
clock = pygame.time.Clock()
clock.tick(60)

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
    ),

    GameObject(
        x = 128, y = SCREEN_HEIGHT - 128, z = 1,
        height = 64, width = 64,
        movable = False
    ),

    GameObject(
        x = SCREEN_WIDTH - 128, y = SCREEN_HEIGHT - 128, z = 1,
        height = 64, width = 64,
        movable = False
    )
]

player = game_objects[0]

while True:

    #handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    game_input.update()
    player.movement(game_input)

    #checking collision
    for object_a in game_objects:
        for object_b in game_objects:
            if GameObject.collision(object_a, object_b):
                GameObject.handle_collision(object_a, object_b)

    #movement update
    time_dif = clock.tick_busy_loop()
    for object_a in game_objects:
        if object_a.movable:
            object_a.move(time_dif)

    #rendering things
    screen.fill(background)

    for object in game_objects:
        object.render(screen)

    pygame.display.flip()
