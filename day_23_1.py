from helper import get_input, flatten


def main():
    cups = [int(x) for x in get_input(23).split('\n')[0]]
    cups.append(cups.pop(0))
    for x in range(100):
        current = cups[-1]
        picked = cups[:3]
        rest = cups[3:]
        i = -1
        while current + i not in rest:
            i -= 1
            if current + i < 1:
                if current + i != 0:
                    i += 1
                i += max(cups)
        next_index = rest.index(current + i) + 1
        for j, p in enumerate(picked):
            rest.insert(next_index + j, p)
        cups = list(rest)
        cups.append(cups.pop(0))

    part2, part1 = ''.join([str(x) for x in cups]).split('1')
    ans = f'{part1}{part2}'
    print(ans)


if __name__ == '__main__':
    main()
