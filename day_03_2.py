from functools import reduce
from helper import get_input


def main():
    data = [x for x in get_input(3).split('\n') if x]
    slopes = [0.5, 1, 3, 5, 7]
    counts = [0, 0, 0, 0, 0]
    for nr, row in enumerate(data):
        while (nr * max(slopes)) >= len(row):
            row += row
        for slope_index, slope in enumerate(slopes):
            if (nr * slope) == int(nr * slope):
                if row[int(nr * slope)] == '#':
                    counts[slope_index] += 1
    print(reduce(lambda x, y: x * y, counts))


if __name__ == '__main__':
    main()
