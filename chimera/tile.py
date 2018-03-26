from enum import Enum

from chimera.colors import str_aec


class TileType(Enum):
    GRASS = ('.', 'green', True)
    ROCK = ('@', 'light_gray', False)
    TREE = ('A', 'bold_green', False)
    WATER = ('~', 'bold_blue', False)

    def __init__(self, texture, color, walkable):
        self.texture = texture
        self.color = color
        self.walkable = walkable

    @property
    def sprite(self):
        return str_aec(self.texture, self.color)
