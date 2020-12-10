from helper import get_input


def main():
    data = sorted([int(x) for x in get_input(10).split('\n') if x])
    max_val = max(data)
    diffs = []
    prev = 0
    data.append(max_val + 3)
    for d in data:
        diffs.append(d - prev)
        prev = d
    print(diffs.count(1) * diffs.count(3))


if __name__ == '__main__':
    main()
