from chimera.block_generators import RandomGridBlockGenerator, ProbabilisticGridBlockGenerator
from chimera.sector_generators import GridSectorGenerator
from chimera.tile import TileType

def run_random_generator():
    block_generator = RandomGridBlockGenerator((15, 15))
    sector = GridSectorGenerator(dims=(3, 5), block_generator=block_generator).generate()
    print(sector)


def run_probabilistic_generator():
    probs = {
        TileType.GRASS: 0.80,
        TileType.ROCK: 0.10,
        TileType.WATER: 0.10,
    }
    block_generator = ProbabilisticGridBlockGenerator(dims=(3, 5), probs=probs)
    sector = GridSectorGenerator(dims=(3, 5), block_generator=block_generator).generate()
    print(sector)


if __name__ == '__main__':
    run_random_generator()
    # run_probabilistic_generator()
