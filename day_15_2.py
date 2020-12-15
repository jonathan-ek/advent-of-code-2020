from helper import get_input


def main():
    data = [int(x) for x in get_input(15).split('\n')[0].split(',')]
    last_position = {}
    for i, x in enumerate(data):
        last_position[x] = i
    keys = set(data[:-1])
    prev = data[-1]
    prev_index = 0
    i = len(data)
    while True:
        curr = prev
        if prev in keys:
            y = i - prev_index - 1
            prev_index = last_position[y] if y in last_position else 0
            last_position[y] = i
            prev = y
        else:
            prev_index = last_position[0]
            last_position[0] = i
            prev = 0
        keys.add(curr)
        if i == 30000000:
            print(curr)
            break
        i += 1


if __name__ == '__main__':
    main()
