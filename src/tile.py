class Tile:
    def __init__(self, number, restrictions=None, *args, **kwargs):
        self.number = number
        self.restictions = restrictions or []
        self.default = False
