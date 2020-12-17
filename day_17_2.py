from helper import get_input, flatten


def get_neighbours(pos, data):
    row = pos[0]
    col = pos[1]
    height = pos[2]
    magic = pos[3]
    neighbours = []
    for r in range(-1, 2):
        for c in range(-1, 2):
            for h in range(-1, 2):
                for m in range(-1, 2):
                    if r == 0 and c == 0 and h == 0 and m == 0:
                        continue
                    if (row + r, col + c, height + h, magic + m) in data:
                        neighbours.append((row + r, col + c, height + h, magic + m))
    return neighbours


def main():
    input_data = get_input(17)
    data = flatten([[(i, j, 0, 0) for j, y in enumerate(list(x)) if y == '#'] for i, x in enumerate(input_data.split('\n')) if x])
    for _ in range(6):
        new_data = []
        row_pos = [x[0] for x in data]
        col_pos = [x[1] for x in data]
        height_pos = [x[2] for x in data]
        magic_pos = [x[3] for x in data]
        for r in range(min(row_pos)-1, max(row_pos)+2):
            for c in range(min(col_pos)-1, max(col_pos)+2):
                for h in range(min(height_pos)-1, max(height_pos)+2):
                    for m in range(min(magic_pos)-1, max(magic_pos)+2):
                        pos = (r, c, h, m)
                        neighbours = get_neighbours(pos, data)
                        if pos in data and (len(neighbours) == 2 or len(neighbours) == 3):
                            new_data.append(pos)
                        if pos not in data and len(neighbours) == 3:
                            new_data.append(pos)
        data = new_data

    print(len(data))


if __name__ == '__main__':
    main()
