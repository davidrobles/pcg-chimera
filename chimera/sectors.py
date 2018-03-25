import random

from enum import Enum


class BlockType(Enum):
    FOREST = ('Forest',)
    TOWN = ('Town',)
    MOUNTAIN = ('Mountain',)

    def __init__(self, display_name):
        self.display_name = display_name


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
        s = 'Block type: ' + self.block_type.display_name + '\n\n'
        for row in self.tiles:
            for tile in row:
                s += str(tile.texture)
            s += '\n'
        s += '\n'
        return s

    @classmethod
    def generate(cls):
        print('Generating random block...')
        tiles = []
        for row in range(cls.SIZE):
            r = []
            for col in range(cls.SIZE):
                r.append(random.choice(list(TileType)))
            tiles.append(r)
        random_block_type = random.choice(list(BlockType))
        return Block(block_type=random_block_type, tiles=tiles)


class Sector:
    def __init__(self, blocks):
        self.blocks = blocks

    def __str__(self):
        s = ''
        for block in self.blocks:
            s += str(block)
        return s

    @classmethod
    def generate(cls):
        print('Generating random sector...')
        blocks = [Block.generate() for _ in range(SECTOR_SIZE)]
        return Sector(blocks)


sector = Sector.generate()
print(sector)
