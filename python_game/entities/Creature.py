import GameObject

class Creature(GameObject):
    def __init__(self, **kwargs):
        Creature.__init__(self, kwargs)
        self.name = kwargs.get('name', 'Creature_default')

    def move(self, time):
        self.x += self.xDir * time
        self.y += self.yDir * time