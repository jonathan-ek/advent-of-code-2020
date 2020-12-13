from helper import get_input


def main():
    data = [(x[0], int(x[1:])) for x in get_input(12).split('\n') if x]
    north = 0
    east = 0
    waypoint_north = 1
    waypoint_east = 10

    for d, l in data:
        if d == 'F':
            north += waypoint_north * l
            east += waypoint_east * l
        if d == 'L':
            d = 'R'
            l = 360 - l

        if d == 'N':
            waypoint_north += l
        elif d == 'S':
            waypoint_north -= l
        elif d == 'E':
            waypoint_east += l
        elif d == 'W':
            waypoint_east -= l
        elif d == 'R':
            for r in range(int(l/90)):
                tmp = waypoint_north
                waypoint_north = -waypoint_east
                waypoint_east = tmp

    print(abs(north)+abs(east))


if __name__ == '__main__':
    main()
