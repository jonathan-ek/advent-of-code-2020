from helper import get_input


class Item:
    def __init__(self, value):
        self.value = value
        self.next = None


def main():
    cups = [int(x) for x in get_input(23).split('\n')[0]]
    for x in range(max(cups)+1, 1000000+1):
        cups.append(x)
    first = cups[0]
    prev = None
    cup_dict = {}
    for cup in cups:
        tmp = Item(cup)
        cup_dict[cup] = tmp
        if prev:
            prev.next = tmp
        prev = tmp
    prev.next = cup_dict[first]
    current = cup_dict[first]
    for x in range(10000000):
        picked = [current.next, current.next.next, current.next.next.next]
        picked_nrs = [x.value for x in picked]
        current.next = picked[2].next
        picked[2].next = None
        i = -1
        while current.value + i in picked_nrs or current.value + i < 1:
            if current.value + i < 1:
                i += 1000000
            else:
                i -= 1
        tmp = cup_dict[current.value + i]
        tmp_next = tmp.next
        tmp.next = picked[0]
        picked[2].next = tmp_next
        current = current.next
        if x % 100000 == 0:
            print(f'\r{x/100000}%', end='')
    print()
    print(cup_dict[1].next.value * cup_dict[1].next.next.value)



if __name__ == '__main__':
    main()
