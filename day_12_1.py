from helper import get_input


def main():
    data = [(x[0], int(x[1:])) for x in get_input(12).split('\n') if x]
    north = 0
    east = 0
    direction = 90
    directions = {180: 'S', 270: 'W', 0: 'N', 90: 'E'}
    for d, l in data:
        if d == 'F':
            d = directions[direction % 360]

        if d == 'N':
            north += l
        elif d == 'S':
            north -= l
        elif d == 'E':
            east += l
        elif d == 'W':
            east -= l
        elif d == 'R':
            direction += l
        elif d == 'L':
            direction -= l

    print(abs(north)+abs(east))


if __name__ == '__main__':
    main()
