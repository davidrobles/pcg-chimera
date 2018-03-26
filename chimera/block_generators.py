import random
from abc import ABC, abstractmethod

from chimera.block import Block


class BlockGenerator(ABC):

    @abstractmethod
    def generate(self, block_type):
        pass


class ProbabilisticGridBlockGenerator(BlockGenerator):
    """Independent Probabilistic Block Generator"""

    def __init__(self, dims, probs):
        self.dims = dims
        self.probs = probs

    def get_tile(self, probs):
        pick = random.random()
        current = 0
        for tile, prob in probs.items():
            current += prob
            if current > pick:
                return tile

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
                    r.append(self.get_tile(self.probs[block_type]))
            tiles.append(r)
        return Block(block_type=block_type, tiles=tiles)


class EmptyGrid(ProbabilisticGridBlockGenerator):
    def __init(self, dims, tile_type):
        probs = {tile_type: 1.0}
        super().__init__(dims, probs)
