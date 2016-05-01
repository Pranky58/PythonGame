from GameObject import GameObject

class Creature(GameObject):

    def __init__(self, **kwargs):
        GameObject.__init__(self, kwargs)

        self.name = kwargs.get('name', 'CreatureDefault')
        self.health = kwargs.get('health', 100)