import os, sys, pygame

class GameObject:

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z = kwargs.get('z', None)

        self.x_velocity = 0
        self.y_velocity = 0

        self.widht = kwargs.get('width', None)
        self.height = kwargs.get('height', None)

        self.img_name = kwargs.get('img_name', None)
        self.img_path = os.getcwd() + '/media/'

        if self.img_name is not None:
            self.img_path += self.img_name
        else:
            self.img_path += 'default.png'

        self.img_render = pygame.image.load(self.img_path).convert_alpha()

    def render(self, screen):
        screen.blit(self.img_render, (self.x, self.y))

    def set_horizontal_velocity(self, velocity):
        self.x_velocity = velocity

    def set_vertical_velocity(self, velocity):
        self.y_velocity = velocity

    def set_velocity_xy(self, velocity):
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[0]


    def move(self, time):
        self.x += self.x_velocity * time
        self.y += self.y_velocity * time