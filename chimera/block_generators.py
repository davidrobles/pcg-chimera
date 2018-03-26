from abc import ABC, abstractmethod

from chimera.block import Block
from chimera.tile import TileType


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


class ProbabilisticGridBlockGenerator(BlockGenerator):
    """Independent Probabilistic Block Generator"""

    def __init__(self, dims, probs):
        self.dims = dims
        self.probs = probs

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


class EmptyGrid(ProbabilisticGridBlockGenerator):
    def __init(self, dims, tile_type):
        probs = {tile_type: 1.0}
        super().__init__(dims, probs)
