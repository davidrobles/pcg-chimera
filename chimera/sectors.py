import random
from abc import ABC, abstractmethod

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


class SectorGenerator(ABC):

    @abstractmethod
    def generate(self):
        pass


class GridSectorGenerator(ABC):

    def __init__(self, dims, block_generator):
        self.dims = dims
        self.block_generator = block_generator

    def generate(self):
        print('Generating sector using GridSectorGenerator...')
        blocks = []
        for row in range(self.dims[0]):
            r = []
            for col in range(self.dims[1]):
                # hacky
                block_type = random.choice(list(BlockType))
                r.append(self.block_generator.generate(block_type))
            blocks.append(r)
        return Sector(blocks)


class BlockGenerator(ABC):

    @abstractmethod
    def generate(self, block_type):
        pass


class RandomGridBlockGenerator(BlockGenerator):

    def __init__(self, dims):
        self.dims = dims

    def generate(self, block_type):
        print('Generating block using RandomGridBlockGenerator...')
        tiles = []

        def is_border(row, col):
            return row == 0 or row == self.dims[0] - 1 or col == 0 or col == self.dims[1] - 1

        for row in range(self.dims[0]):
            r = []
            for col in range(self.dims[1]):
                if is_border(row, col):
                    r.append(block_type.generate_blocking_tile())
                else:
                    r.append(block_type.generate_tile())
            tiles.append(r)
        return Block(block_type=block_type, tiles=tiles)


class Block:
    SIZE = (15, 15)  # number of tiles per block

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


class Sector:
    SIZE = (3, 5)  # number of blocks per sector

    def __init__(self, blocks):
        self.blocks = blocks

    def get_sector_row(self, sector_row):
        s = ''
        a = self.blocks[0]
        for block_row in range(self.blocks[0][0].n_rows):
            line = ''
            for block in self.blocks[sector_row]:
                line += block.get_row(block_row) + '   '
            s += line + '\n'
        return s

    @property
    def size(self):
        return len(self.blocks), len(self.blocks[0])

    @property
    def n_rows(self):
        return self.size[0]

    @property
    def n_cols(self):
        return self.size[1]

    def __str__(self):
        return '\n'.join([self.get_sector_row(sector_row) for sector_row in range(self.n_rows)])


sector = GridSectorGenerator(dims=(3, 5), block_generator=RandomGridBlockGenerator((15, 15))).generate()
print(sector)
