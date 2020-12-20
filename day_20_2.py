import math
import re

from helper import get_input, flatten


def rotate(content):
    return list(zip(*content[::-1]))


def mirror_x(content):
    return [x[::-1] for x in content]


def mirror_y(content):
    return content[::-1]


class Tile:
    def __init__(self, tile_data):
        tmp = [x for x in tile_data.split('\n') if x]
        self.nr = int(tmp[0].replace('Tile ', '').replace(':', ''))
        content = [[v for v in t] for t in tmp[1:]]
        self._cont = content
        self.borders = {
            'top': content[0],
            'right': [x[len(x) - 1] for x in content],
            'bottom': content[len(content) - 1],
            'left': [x[0] for x in content],
        }
        self.content = [[v for v in t[1:-1]] for t in content[1:-1]]
        self.possible_borders = flatten([[x, x[::-1]] for x in self.borders.values()])

    def nr_of_sides_that_can_be_neighbouring(self, tile):
        tmp = 0
        for pos, border in self.borders.items():
            if border in tile.possible_borders:
                tmp += 1
        return tmp

    def matching_side(self, tile):
        for pos, border in self.borders.items():
            for t_pos, t_border in tile.borders.items():
                if border == t_border:
                    return pos, t_pos, True
        for pos, border in self.borders.items():
            for t_pos, t_border in tile.borders.items():
                if border == t_border[::-1]:
                    return pos, t_pos, False
        return None, None, None

    def rotate(self):
        self.content = rotate(self.content)
        self.borders = {
            'top': self.borders['left'][::-1],
            'right': self.borders['top'],
            'bottom': self.borders['right'][::-1],
            'left': self.borders['bottom'],
        }

    def mirror_x(self):
        self.content = mirror_x(self.content)
        self.borders = {
            'top': self.borders['top'][::-1],
            'right': self.borders['left'],
            'bottom': self.borders['bottom'][::-1],
            'left': self.borders['right'],
        }

    def mirror_y(self):
        self.content = mirror_y(self.content)
        self.borders = {
            'top': self.borders['bottom'],
            'right': self.borders['right'][::-1],
            'bottom': self.borders['top'],
            'left': self.borders['left'][::-1],
        }


def rotate_first_corner(corner, neighbours):
    n_sides = []
    for n in neighbours:
        n_sides.append(corner.matching_side(n))
    while tuple(x[0] for x in n_sides) not in [('right', 'bottom'), ('bottom', 'right')]:
        corner.rotate()
        n_sides = []
        for n in neighbours:
            n_sides.append(corner.matching_side(n))


def get_bottom(tile, neighbours):
    for n in neighbours:
        tmp = tile.matching_side(n)
        if tmp[0] == 'bottom':
            while tmp[1] != 'top':
                n.rotate()
                tmp = tile.matching_side(n)
            if not tmp[2]:
                n.mirror_x()
            return n


def get_right(tile, neighbours):
    for n in neighbours:
        tmp = tile.matching_side(n)
        if tmp[0] == 'right':
            while tmp[1] != 'left':
                n.rotate()
                tmp = tile.matching_side(n)
            if not tmp[2]:
                n.mirror_y()
            return n


def main():
    tiles = [Tile(tile) for tile in get_input(20).split('\n\n') if tile]
    side_length = int(math.sqrt(len(tiles)))
    corners = []
    neighbours = {}
    for i, tile in enumerate(tiles):
        possible_neighbours = []
        for tile2 in tiles:
            if tile == tile2:
                continue
            possible_sides = tile.nr_of_sides_that_can_be_neighbouring(tile2)
            if possible_sides:
                possible_neighbours.append(tile2)
        neighbours[tile] = possible_neighbours
        if len(possible_neighbours) == 2:
            corners.append(tile)
    corner = corners[0]
    tile_map = [[None for x in range(side_length)] for y in range(side_length)]
    rotate_first_corner(corner, neighbours[corner])
    for row in range(side_length):
        for col in range(side_length):
            if row == 0 and col == 0:
                tile_map[row][col] = corner
            elif col == 0:
                prev = tile_map[row - 1][col]
                tile_map[row][col] = get_bottom(prev, neighbours[prev])
            else:
                prev = tile_map[row][col - 1]
                tile_map[row][col] = get_right(prev, neighbours[prev])

    image = []
    for row in tile_map:
        content = [tile.content for tile in row]
        for row_index in range(len(content[0])):
            new_row = [x for x in ''.join([''.join(tile.content[row_index]) for tile in row])]
            image.append(new_row)

    has_matches = False
    i = 0
    transform = [
        rotate, rotate, rotate, rotate,
        mirror_x,
        rotate, rotate, rotate, rotate,
        mirror_y,
        rotate, rotate, rotate, rotate,
        mirror_x,
        rotate, rotate, rotate, rotate,
    ]
    match_count = 0

    while not has_matches:
        pattern = r'.*.{18}#.{1}.*\n.*#.{4}##.{4}##.{4}###.*\n.*.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}.*'
        matches = re.findall(pattern, '\n'.join([''.join(row) for row in image]), re.MULTILINE)
        if not matches:
            image = transform[i](image)
            i += 1
        else:
            for x in range(len(image) - 3):
                f = ''.join(image[x])
                s = ''.join(image[x + 1])
                t = ''.join(image[x + 2])
                f_m = []
                s_m = []
                t_m = []
                for i in range(len(t) - 20):
                    f_m.append(re.findall('.{18}#.{1}', f[i:]))
                    s_m.append(re.findall('#.{4}##.{4}##.{4}###', s[i:]))
                    t_m.append(re.findall('.#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}', t[i:]))
                f_m = flatten(f_m)
                s_m = flatten(s_m)
                t_m = flatten(t_m)
                if len(f_m) > 0 and len(s_m) > 0 and len(t_m) > 0:
                    match_count += len(set([f.index(x) for x in f_m]).intersection(
                        set([s.index(x) for x in s_m]).intersection(
                            set([t.index(x) for x in t_m]))))
            break
    print(len(re.findall('#', '\n'.join([''.join(row) for row in image]), re.MULTILINE)) - (match_count * 15))


if __name__ == '__main__':
    main()
