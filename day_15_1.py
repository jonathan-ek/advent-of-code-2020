from helper import get_input


def main():
    data = [int(x) for x in get_input(15).split('\n')[0].split(',')]
    i = len(data)
    while True:
        prev = data[i - 1]
        prev_list = data[:-1]
        if prev in prev_list:
            data.append(1 + prev_list[::-1].index(prev))
        else:
            data.append(0)
        if len(data) == 2020:
            print(data[-1])
            break
        i += 1


if __name__ == '__main__':
    main()
