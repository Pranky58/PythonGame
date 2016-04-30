import Creature

class Player(GameObject):
    def __init__(self, **kwargs):
        Creature.__init__(self, kwargs)

