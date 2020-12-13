from helper import get_input


def main():
    data = [x for x in get_input(13).split('\n') if x]
    timestamp = int(data[0])
    busses = [int(x) for x in data[1].split(',') if x != 'x']
    nearest_departure = [((int(timestamp / b) + 1) * b) - timestamp for b in busses]
    print(busses[nearest_departure.index(min(nearest_departure))] * min(nearest_departure))


if __name__ == '__main__':
    main()
