import random

from abc import abstractmethod, ABC

from chimera.block import BlockType
from chimera.sector import Sector


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
