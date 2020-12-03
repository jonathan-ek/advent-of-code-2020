from helper import get_input


def main():
    data = [int(x) for x in get_input(1).split('\n') if x]
    for d in data:
        for e in data:
            if e == d:
                continue
            if 2020 - d - e in data:
                print(d, e, 2020 - d - e, d * e * (2020 - d - e))
                return


if __name__ == '__main__':
    main()
