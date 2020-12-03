from helper import get_input


def main():
    data = [x for x in get_input(3).split('\n') if x]
    slope = 3
    count = 0
    for nr, row in enumerate(data):
        while (nr * slope) >= len(row):
            row += row
        if row[nr * slope] == '#':
            count += 1
    print(count)


if __name__ == '__main__':
    main()
