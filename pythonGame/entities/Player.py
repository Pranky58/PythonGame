import Creature
import pygame
import pygame.locals


class InputHandler():
    def __init__(self):
        self.keys = {
            'keyUp': pygame.K_UP,
            'keyDown': pygame.K_DOWN,
            'keyRight': pygame.K_RIGHT,
            'keyLeft': pygame.K_LEFT
        }

        self.keyPressed = {
            'keyUp': False,
            'keyDown': False,
            'keyRight': False,
            'keyLeft': False
        }

    def update(self):
        for key, keyCode in self.keys:
            self.keyPressed[key] = pygame.key.get_pressed()[keyCode]


class Player(GameObject):
    def __init__(self, **kwargs):
        Creature.__init__(self, kwargs)

    def movement(self, input):
        pass


