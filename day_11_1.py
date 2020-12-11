from helper import get_input, flatten


def get_neighbours(pos, data):
    col = pos[0]
    row = pos[1]
    neighbours = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == 0 and c == 0:
                continue
            if row + r < 0 or col + c < 0 or row + r >= len(data) or col + c >= len(data[row + r]):
                continue
            if data[row + r][col + c] == 'L':
                neighbours.append((col + c, row + r))
    return neighbours


def main():
    data = [[y for y in x] for x in get_input(11).split('\n') if x]
    neighbour_lists = []
    for row_index, row in enumerate(data):
        for col_index, col, in enumerate(row):
            if col == 'L':
                neighbours = get_neighbours((col_index, row_index), data)
                neighbour_lists.append(((col_index, row_index), neighbours))
    change = True
    current_layout = [[y for y in x] for x in data]
    while change:
        change = False
        new_layout = [[y for y in x] for x in current_layout]
        for (col, row), neighbour_set in neighbour_lists:
            if current_layout[row][col] == 'L':
                if all([current_layout[y][x] == 'L' for (x, y) in neighbour_set]):
                    new_layout[row][col] = '#'
                    change = True
            if current_layout[row][col] == '#':
                if len([(x, y) for (x, y) in neighbour_set if current_layout[y][x] == '#']) >= 4:
                    new_layout[row][col] = 'L'
                    change = True
        current_layout = new_layout

    print(len([x for x in flatten(current_layout) if x == '#']))


if __name__ == '__main__':
    main()
