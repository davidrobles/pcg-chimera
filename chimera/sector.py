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
