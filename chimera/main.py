from chimera.block_generators import RandomGridBlockGenerator
from chimera.sector_generators import GridSectorGenerator

if __name__ == '__main__':
    sector = GridSectorGenerator(dims=(3, 5), block_generator=RandomGridBlockGenerator((15, 15))).generate()
    print(sector)
