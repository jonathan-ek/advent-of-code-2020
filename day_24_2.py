from helper import get_input


def format_row(in_data):
    in_data = 'se, '.join(in_data.split('se'))
    in_data = 'ne, '.join(in_data.split('ne'))
    in_data = 'sw, '.join(in_data.split('sw'))
    in_data = 'nw, '.join(in_data.split('nw'))
    data = in_data.split(', ')
    res = []
    for d in data:
        while d and d not in ['se', 'ne', 'sw', 'nw', 'e', 'w']:
            res.append(d[0])
            d = d[1:]
        if d:
            res.append(d)

    return res


def get_position(data):
    x = 0
    y = 0
    for ins in data:
        if ins == 'e':
            x += 2
        elif ins == 'w':
            x -= 2
        elif ins == 'ne':
            x += 1
            y += 1
        elif ins == 'nw':
            x -= 1
            y += 1
        elif ins == 'se':
            x += 1
            y -= 1
        elif ins == 'sw':
            x -= 1
            y -= 1
    return tuple([x, y])


def get_possible_neighbours(tile):
    return [
        tuple([tile[0] + 1, tile[1] + 1]),
        tuple([tile[0] + 2, tile[1]]),
        tuple([tile[0] + 1, tile[1] - 1]),
        tuple([tile[0] - 1, tile[1] + 1]),
        tuple([tile[0] - 2, tile[1]]),
        tuple([tile[0] - 1, tile[1] - 1]),
    ]


def get_new_positions(black_tiles):
    new_black_tiles = []
    affected_tiles = set()
    for black_tile in black_tiles:
        tiles = get_possible_neighbours(black_tile)
        for tile in tiles:
            affected_tiles.add(tile)
    for tile in affected_tiles:
        nr_of_black_neighbours = len([x for x in get_possible_neighbours(tile) if x in black_tiles])
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        if tile in black_tiles and nr_of_black_neighbours in [1, 2]:
            new_black_tiles.append(tile)
        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        elif tile not in black_tiles and nr_of_black_neighbours == 2:
            new_black_tiles.append(tile)
    return new_black_tiles


def main():
    data = [format_row(x) for x in get_input(24).split('\n')]
    black_tiles = []
    for d in data:
        pos = get_position(d)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.append(pos)
    for x in range(100):
        new_black = get_new_positions(black_tiles)
        print(len(new_black))
        black_tiles = new_black


if __name__ == '__main__':
    main()
