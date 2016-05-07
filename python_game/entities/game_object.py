import os, sys, pygame

class GameObject:

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.z = kwargs.get('z', -1)

        self.x_velocity = 0
        self.y_velocity = 0
        self.movable = kwargs.get('movable', False)

        self.widht = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.rect = pygame.Rect(self.x, self.y, self.widht, self.height)

        self.img_name = kwargs.get('img_name', None)
        self.img_path = os.getcwd() + '/media/'

        if self.img_name is not None:
            self.img_path += self.img_name
        else:
            self.img_path += 'default.png'

        self.img_render = pygame.image.load(self.img_path).convert_alpha()

    def render(self, screen):
        screen.blit(self.img_render, self.rect)

    def set_horizontal_velocity(self, velocity):
        self.x_velocity = velocity

    def set_vertical_velocity(self, velocity):
        self.y_velocity = velocity

    def set_velocity_xy(self, velocity):
        self.x_velocity = velocity[0]
        self.y_velocity = velocity[0]

    def gravity(self):
        if self.movable:
            self.y_velocity += 0.004

    def move(self, time):
        self.gravity()
        self.x += self.x_velocity * time
        self.y += self.y_velocity * time

        self.rect[0] = self.x
        self.rect[1] = self.y