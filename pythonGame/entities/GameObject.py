import os, sys, pygame

class GameObject:

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z = kwargs.get('z', None)

        self.xAcceleration = 0
        self.yAcceleration = 0

        self.widht = kwargs.get('width', None)
        self.height = kwargs.get('height', None)

        self.imgName = kwargs.get('imgName', None)
        self.imgPath = os.getcwd() + '/media/'

        if self.imgName is not None:
            self.imgPath += self.imgName
        else:
            self.imgPath += 'default.png'

        self.imgRender = pygame.image.load(self.imgPath).convert_alpha()
        self.objectRect = self.imgRender.get_rect()

    def render(self, screen):
        screen.blit(self.imgRender, self.objectRect)

    def accelerateHorizontaly(self, acceleration):
        self.xAcceleration += acceleration

    def accelerateVerticaly(self, acceleration):
        self.yAcceleration += acceleration

    def move(self, time):
        self.x += self.xAcceleration * time
        self.y += self.yAcceleration * time