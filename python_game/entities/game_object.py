import os, sys, pygame

class GameObject:

    object_count = 0

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', 0)
        self.y = kwargs.get('y', 0)
        self.z = kwargs.get('z', -1)

        self.x_velocity = 0
        self.y_velocity = 0.1
        self.grounded = False
        self.movable = kwargs.get('movable', False)

        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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

    def immovable_response(object_a, object_b):
        if object_a.y_velocity > 0 and object_a.x + object_a.width > object_b.x and object_a.x < object_b.x + object_b.width:
            object_a.y = object_b.y - object_a.height
            object_a.y_velocity = 0
            object_a.grounded = True

        if object_a.x_velocity > 0 and object_a.y + object_a.height > object_b.y and object_a.y < object_b.y + object_b.height:
            object_a.x = object_b.x - object_a.width
            object_a.x_velocity = 0

        if object_a.x_velocity < 0 and object_a.y + object_a.height > object_b.y and object_a.y < object_b.y + object_b.height:
            object_a.x = object_b.x + object_b.width
            object_a.x_velocity = 0

    def handle_collision(object_a, object_b):
        if object_a.movable is False and object_b.movable is False:
            return None
        elif object_a.movable is False and object_b.movable is True:
            object_a, object_b = object_b, object_a
            object_a.immovable_response(object_b)

    def collision(object_a, object_b):
        return object_a.x + object_a.width >= object_b.x and object_a.x <= object_b.x + object_b.width and \
               object_a.y + object_a.height >= object_b.y and object_a.y <= object_b.y + object_b.height

    def gravity(self):
        if self.movable and not self.grounded:
            self.y_velocity += 0.004

    def move(self, time):
        self.gravity()
        self.x += self.x_velocity * time
        self.y += self.y_velocity * time
        self.grounded = False

        self.rect[0] = self.x
        self.rect[1] = self.y