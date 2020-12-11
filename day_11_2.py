from helper import get_input, flatten


def get_neighbours(pos, data):
    col = pos[0]
    row = pos[1]
    neighbours = []
    # diagonals
    i = 1
    while True:
        if row + i < 0 or col + i < 0 or row + i >= len(data) or col + i >= len(data[row + i]):
            break
        if data[row + i][col + i] == 'L':
            neighbours.append((col + i, row + i))
            break
        i += 1
    i = 1
    while True:
        if row - i < 0 or col + i < 0 or row - i >= len(data) or col + i >= len(data[row - i]):
            break
        if data[row - i][col + i] == 'L':
            neighbours.append((col + i, row - i))
            break
        i += 1
    i = 1
    while True:
        if row - i < 0 or col - i < 0 or row - i >= len(data) or col - i >= len(data[row - i]):
            break
        if data[row - i][col - i] == 'L':
            neighbours.append((col - i, row - i))
            break
        i += 1
    i = 1
    while True:
        if row + i < 0 or col - i < 0 or row + i >= len(data) or col - i >= len(data[row + i]):
            break
        if data[row + i][col - i] == 'L':
            neighbours.append((col - i, row + i))
            break
        i += 1
    # Up and down
    i = 1
    while True:
        if row + i < 0 or row + i >= len(data):
            break
        if data[row + i][col] == 'L':
            neighbours.append((col, row + i))
            break
        i += 1
    i = 1
    while True:
        if row - i < 0 or row - i >= len(data):
            break
        if data[row - i][col] == 'L':
            neighbours.append((col, row - i))
            break
        i += 1
    # left and right
    i = 1
    while True:
        if col + i < 0 or col + i >= len(data[row]):
            break
        if data[row][col + i] == 'L':
            neighbours.append((col + i, row))
            break
        i += 1
    i = 1
    while True:
        if col - i < 0 or col - i >= len(data[row]):
            break
        if data[row][col - i] == 'L':
            neighbours.append((col - i, row))
            break
        i += 1

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
                if len([(x, y) for (x, y) in neighbour_set if current_layout[y][x] == '#']) >= 5:
                    new_layout[row][col] = 'L'
                    change = True
        current_layout = new_layout

    print(len([x for x in flatten(current_layout) if x == '#']))


if __name__ == '__main__':
    main()
