from helper import get_input, flatten


class Tile:
    def __init__(self, tile_data):
        tmp = [x for x in tile_data.split('\n') if x]
        self.nr = int(tmp[0].replace('Tile ', '').replace(':', ''))
        self.content = [[v for v in t] for t in tmp[1:]]
        self.borders = {
            'top': self.content[0],
            'right': [x[len(x) - 1] for x in self.content],
            'bottom': self.content[len(self.content) - 1],
            'left': [x[0] for x in self.content],
        }
        self.possible_borders = flatten([[x, x[::-1]] for x in self.borders.values()])

    def nr_of_sides_that_can_be_neighbouring(self, tile):
        tmp = 0
        for border in self.borders.values():
            if border in tile.possible_borders:
                tmp += 1
        return tmp


def main():
    tiles = [Tile(tile) for tile in get_input(20).split('\n\n') if tile]
    mult = 1
    for i, tile in enumerate(tiles):
        possible_neighbours = []
        for tile2 in tiles:
            if tile == tile2:
                continue
            possible_sides = tile.nr_of_sides_that_can_be_neighbouring(tile2)
            if possible_sides:
                possible_neighbours.append(tile2)
        if len(possible_neighbours) == 2:
            mult *= tile.nr
    print(mult)


if __name__ == '__main__':
    main()
