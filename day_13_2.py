from helper import get_input


def main():
    data = [x for x in get_input(13).split('\n') if x]

    busses = [(-i, int(x)) for i, x in enumerate(data[1].split(',')) if x != 'x']

    # Using something called Chinese Remainder Theorem
    m = 1
    for reminder, x in busses:
        m *= x

    total = 0
    for rem, x in busses:
        div = int(m / x)
        tmp = div % x
        j = 0
        while (tmp * j) % x != 1:
            j += 1
        total += rem * div * j
    print(total % m)


if __name__ == '__main__':
    main()
