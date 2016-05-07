from creature import Creature
import pygame
import pygame.locals


class InputHandler():
    def __init__(self):
        self.keys = {
            'key_up': pygame.K_UP,
            'key_down': pygame.K_DOWN,
            'key_right': pygame.K_RIGHT,
            'key_left': pygame.K_LEFT
        }

        self.key_pressed = {
            'key_up': False,
            'key_down': False,
            'key_right': False,
            'key_left': False
        }

    def update(self):
        pressed = pygame.key.get_pressed()
        for key, key_code in self.keys.iteritems():
            self.key_pressed[key] = pressed[key_code]

    def is_pressed(self, key):
        return self.key_pressed[key]

class Player(Creature):
    def __init__(self, **kwargs):
        Creature.__init__(self, movable = True, **kwargs)
        self.moves = {
            'Stop': self.set_velocity_xy,
            'Jump': self.set_vertical_velocity,
            'Fall': self.set_vertical_velocity,
            'Left': self.set_horizontal_velocity,
            'Right': self.set_horizontal_velocity,
            'Stop_horizontaly':self.set_horizontal_velocity
        }

    def movement(self, input):
        if input.is_pressed('key_up'):
            self.moves['Jump'](-0.2)

        if input.is_pressed('key_left') is input.is_pressed('key_right'):
            self.moves['Stop_horizontaly'](0)
        elif input.is_pressed('key_left'):
            self.moves['Left'](-0.6)
        elif (input.is_pressed('key_right')):
            self.moves['Right'](0.6)


