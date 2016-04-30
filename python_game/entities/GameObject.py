def testing():
    print "test"

class GameObject:

    def __init__(self, **kwargs):
        self.x = kwargs.get('x', None)
        self.y = kwargs.get('y', None)
        self.z = kwargs.get('z', None)

        self.widht = kwargs.get('width', None)
        self.height = kwargs.get('height', None)

        self.img_adress = kwargs.get('img_adress', None)
