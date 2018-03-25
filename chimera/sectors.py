import random

from enum import Enum


class BlockType(Enum):
    FOREST = 1
    TOWN = 2
    MOUNTAIN = 3


class TileType(Enum):
    GRASS = ('.',)
    ROCK = ('@',)
    TREE = ('A',)
    WATER = ('~',)

    def __init__(self, texture):
        self.texture = texture


SECTOR_SIZE = 5  # number of blocks per sector


class Block:

    SIZE = 10  # number of tiles per block

    def __init__(self, block_type, tiles):
        self.block_type = block_type
        self.tiles = tiles

    def __str__(self):
        s = 'block type: ' + str(self.block_type) + '\n\n'
        for row in tiles:
            for tile in row:
                s += str(tile.texture)
            s += '\n'
        s += '\n'
        return s

    @classmethod
    def generate(cls):
        tiles = []
        for row in range(cls.SIZE):
            r = []
            for col in range(cls.SIZE):
                r.append(random.choice(list(TileType)))
            tiles.append(r)
        return tiles


class Sector:
    def __init__(self, blocks):
        self.blocks = blocks

    def __str__(self):
        s = ''
        for block in self.blocks:
            s += str(block)
        return s


def generate_sector():
    return [random.choice(list(BlockType)) for _ in range(SECTOR_SIZE)]


sector = generate_sector()

# block objects
blocks = []

for block_type in generate_sector():
    tiles = Block.generate() # pasar block_id
    block = Block(block_type=block_type, tiles=tiles)
    blocks.append(block)


print(Sector(blocks))
