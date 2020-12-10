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
    # Looks like the difference is always 1 or 3. So we can ignore any logic for steps of 2.
    # Since the gap of 3 is required we can split on those and calculate those separately.
    # The longest such series is 4 in my input.
    # 1, 0|12|5 = 1
    # 2, 0|123|6 = 2 [123, 13]
    # 3, 0|1234|7 = 4 [1234, 124, 134, 14]
    # 4, 0|12345|8 = 7 [12345, 1245, 125, 1235, 135, 1345, 145]
    parts = [len(y) for y in (''.join([str(x) for x in diffs])).split('3') if y and len(y) > 1]
    value = 1
    for p in parts:
        if p == 2:
            value = value * 2
        elif p == 3:
            value = value * 4
        elif p == 4:
            value = value * 7
    print(value)


if __name__ == '__main__':
    main()
