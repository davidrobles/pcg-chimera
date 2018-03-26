import random
from enum import Enum

from chimera.tile import TileType


class Block:
    def __init__(self, block_type, tiles):
        self.block_type = block_type
        self.tiles = tiles

    def get_row(self, row):
        """Returns a row as a string"""
        return ' '.join([t.sprite for t in self.tiles[row]])

    def __str__(self):
        s = 'Block type: ' + self.block_type.display_name + '\n\n'
        for row in range(self.n_rows):
            s += self.get_row(row)
            s += '\n'
        s += '\n'
        return s

    @property
    def size(self):
        return len(self.tiles), len(self.tiles[0])

    @property
    def n_rows(self):
        return self.size[0]

    @property
    def n_cols(self):
        return self.size[1]


class BlockType(Enum):
    FOREST = ('Forest', (TileType.GRASS, TileType.ROCK, TileType.TREE))
    TOWN = ('Town', (TileType.GRASS, TileType.TREE))
    MOUNTAIN = ('Mountain', (TileType.GRASS, TileType.ROCK, TileType.WATER))

    def __init__(self, display_name, tile_whitelist):
        self.display_name = display_name
        self.tile_whitelist = tile_whitelist

    def generate_tile(self):
        return random.choice(self.tile_whitelist)

    def generate_blocking_tile(self):
        return random.choice([tile for tile in self.tile_whitelist if not tile.walkable])
