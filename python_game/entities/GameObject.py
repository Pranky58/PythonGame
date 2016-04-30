import os, sys, pygame

class GameObject:

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z = kwargs.get('z', None)

        self.xDir = 0
        self.yDir = 0

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

