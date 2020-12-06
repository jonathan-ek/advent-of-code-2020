from helper import get_input


def main():
    data = [[[z for z in y] for y in x.split('\n') if y] for x in get_input(6).split('\n\n') if x]
    print(sum([len(set(x[0]).intersection(*x)) for x in data]))


if __name__ == '__main__':
    main()
