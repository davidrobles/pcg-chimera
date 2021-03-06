from chimera.block import BlockType
from chimera.block_generators import ProbabilisticGridBlockGenerator
from chimera.sector_generators import GridSectorGenerator
from chimera.tile import TileType


def run_probabilistic_generator():
    probs = {
        BlockType.FOREST: {
            TileType.GRASS: 0.80,
            TileType.ROCK: 0.10,
            TileType.TREE: 0.10
        },
        BlockType.TOWN: {
            TileType.GRASS: 0.80,
            TileType.TREE: 0.20
        },
        BlockType.MOUNTAIN: {
            TileType.GRASS: 0.80,
            TileType.ROCK: 0.10,
            TileType.WATER: 0.10
        }
    }
    block_generator = ProbabilisticGridBlockGenerator(dims=(15, 15), probs=probs)
    sector = GridSectorGenerator(dims=(2, 3), block_generator=block_generator).generate()
    print(sector)


def run_empty_grass_generator():
    probs = {TileType.GRASS: 1.0}
    block_generator = ProbabilisticGridBlockGenerator(dims=(15, 15), probs=probs)
    sector = GridSectorGenerator(dims=(3, 5), block_generator=block_generator).generate()
    print(sector)


if __name__ == '__main__':
    run_probabilistic_generator()
    # run_empty_grass_generator()
