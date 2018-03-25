import random

from enum import Enum
from chimera.colors import str_aec


class TileType(Enum):
    GRASS = ('.', 'green')
    ROCK = ('@', 'light_gray')
    TREE = ('A', 'bold_green')
    WATER = ('~', 'bold_blue')

    def __init__(self, texture, color):
        self.texture = texture
        self.color = color

    @property
    def sprite(self):
        return str_aec(self.texture, self.color)


class BlockType(Enum):
    FOREST = ('Forest', (TileType.GRASS, TileType.ROCK, TileType.TREE))
    TOWN = ('Town', (TileType.GRASS, TileType.TREE))
    MOUNTAIN = ('Mountain', (TileType.GRASS, TileType.ROCK, TileType.WATER))

    def __init__(self, display_name, tile_whitelist):
        self.display_name = display_name
        self.tile_whitelist = tile_whitelist

    def generate_tile(self):
        return random.choice(self.tile_whitelist)


SECTOR_SIZE = 6  # number of blocks per sector


class Block:
    SIZE = 10  # number of tiles per block

    def __init__(self, block_type, tiles):
        self.block_type = block_type
        self.tiles = tiles

    def get_row(self, row):
        """Returns a row as a string"""
        return ' '.join([t.sprite for t in self.tiles[row]])

    def __str__(self):
        s = 'Block type: ' + self.block_type.display_name + '\n\n'
        for row in range(len(self.tiles)):
            s += self.get_row(row)
            s += '\n'
        s += '\n'
        return s

    @classmethod
    def generate(cls):
        print('Generating random block...')
        block_type = random.choice(list(BlockType))
        tiles = []
        for row in range(cls.SIZE):
            r = []
            for col in range(cls.SIZE):
                r.append(block_type.generate_tile())
            tiles.append(r)
        return Block(block_type=block_type, tiles=tiles)


class Sector:
    def __init__(self, blocks):
        self.blocks = blocks

    def __str__(self):
        s = ''
        for block_row in range(len(self.blocks[0].tiles)):
            line = ''
            for block in self.blocks:
                line += block.get_row(block_row) + '    '
            s += line + '\n'
        return s

    @classmethod
    def generate(cls):
        print('Generating random sector...')
        blocks = [Block.generate() for _ in range(SECTOR_SIZE)]
        return Sector(blocks)


sector = Sector.generate()
print(sector)
