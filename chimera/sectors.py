import random

SECTOR_SIZE = 5  # number of blocks per sector

BLOCK_SIZE = 10  # number of tiles per block

BLOCK_TYPES = ['forest', 'town', 'mountain']

TILE_TYPES = ['walkable', 'non-walkable', 'water']


class Block:

    def __init__(self, block_type, size, tiles):
        self.block_type = block_type
        self.size = size
        self.tiles = tiles

    def __str__(self):
        s = 'block type: ' + self.block_type + '\n\n'
        for row in tiles:
            for col in row:
                s += str(col)
            s += '\n'
        s += '\n'
        return s


class Sector:
    def __init__(self, blocks):
        self.blocks = blocks

    def __str__(self):
        s = ''
        for block in self.blocks:
            s += str(block)
        return s


def generate_sector():
    return [random.randrange(len(BLOCK_TYPES)) for _ in range(SECTOR_SIZE)]


def generate_block():
    map = []
    for row in range(BLOCK_SIZE):
        r = []
        for col in range(BLOCK_SIZE):
            r.append(random.randrange(len(TILE_TYPES)))
        map.append(r)
    return map


def print_block(block):
    for row in block:
        for col in row:
            print(col, end='')
        print("")


sector = generate_sector()

# block objects
blocks = []

for block_id in generate_sector():
    tiles = generate_block() # pasar block_id
    block = Block(block_type=BLOCK_TYPES[block_id], size=BLOCK_SIZE, tiles=tiles)
    blocks.append(block)


print(Sector(blocks))
