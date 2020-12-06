from helper import get_input


def main():
    data = [len(set([y for y in x.replace('\n', '')])) for x in get_input(6).split('\n\n') if x]
    print(sum(data))


if __name__ == '__main__':
    main()
