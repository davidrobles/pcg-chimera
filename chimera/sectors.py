import random

SECTOR_SIZE = 5  # number of blocks per sector

BLOCK_SIZE = 10  # number of tiles per block

BLOCK_TYPES = ['forest', 'town', 'mountain']

TILE_TYPES = ['walkable', 'non-walkable', 'water']


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

# print([BLOCK_TYPES[i] for i in generate_sector()])


for block_id in generate_sector():
    block = generate_block() # pasar block_id
    print("Block name: ", BLOCK_TYPES[block_id])
    print()
    print_block(block)
    print()
