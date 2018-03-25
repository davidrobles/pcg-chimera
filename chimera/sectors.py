import random

from enum import Enum


class BlockType(Enum):
    FOREST = 1
    TOWN = 2
    MOUNTAIN = 3


SECTOR_SIZE = 5  # number of blocks per sector


TILE_TYPES = ['walkable', 'non-walkable', 'water']


class Block:

    SIZE = 10  # number of tiles per block

    def __init__(self, block_type, tiles):
        self.block_type = block_type
        self.tiles = tiles

    def __str__(self):
        s = 'block type: ' + str(self.block_type) + '\n\n'
        for row in tiles:
            for col in row:
                s += str(col)
            s += '\n'
        s += '\n'
        return s

    @classmethod
    def generate(cls):
        tiles = []
        for row in range(cls.SIZE):
            r = []
            for col in range(cls.SIZE):
                r.append(random.randrange(len(TILE_TYPES)))
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
