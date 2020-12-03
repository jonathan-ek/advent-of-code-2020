from helper import get_input


def main():
    data = [int(x) for x in get_input(1).split('\n') if x]
    for d in data:
        if 2020 - d in data:
            print(d, 2020 - d, d * (2020 - d))
            return


if __name__ == '__main__':
    main()
