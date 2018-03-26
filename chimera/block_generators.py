import random
from abc import ABC, abstractmethod

from chimera.block import Block
from chimera.utils import validate_probs


class BlockGenerator(ABC):

    @abstractmethod
    def generate(self, block_type):
        pass


class ProbabilisticGridBlockGenerator(BlockGenerator):
    """Independent Probabilistic Block Generator"""

    def __init__(self, dims, probs):
        validate_probs(probs)
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
            tiles_row = []
            for col in range(self.dims[1]):
                tile = block_type.generate_blocking_tile() if is_border(row, col) else self.get_tile(self.probs[block_type])
                tiles_row.append(tile)
            tiles.append(tiles_row)
        return Block(block_type=block_type, tiles=tiles)


class EmptyGrid(ProbabilisticGridBlockGenerator):
    def __init(self, dims, tile_type):
        probs = {tile_type: 1.0}
        super().__init__(dims, probs)
