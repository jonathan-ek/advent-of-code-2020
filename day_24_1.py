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


def main():
    data = [format_row(x) for x in get_input(24).split('\n')]
    positions = []
    for d in data:
        pos = get_position(d)
        if pos in positions:
            positions.remove(pos)
        else:
            positions.append(pos)
    print(len(positions))
    assert len(positions) > 201


if __name__ == '__main__':
    main()
