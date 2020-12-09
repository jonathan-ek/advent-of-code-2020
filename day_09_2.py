from helper import get_input, flatten


def main():
    data = [int(x) for x in get_input(9).split('\n') if x]
    preamble_length = 25
    preamble = data[:preamble_length]
    sums = []
    for first_nr in preamble:
        day_sum = []
        for second_nr in preamble:
            if first_nr != second_nr:
                day_sum.append(first_nr + second_nr)
        sums.append(day_sum)
    result = None
    for index, nr in enumerate(data):
        if index < preamble_length:
            continue
        if nr not in flatten(sums):
            result = nr
            break
        sums = sums[1:]
        new_day = []
        for second_nr in data[index - preamble_length: index]:
            if nr != second_nr:
                new_day.append(nr + second_nr)
        sums.append(new_day)
    for index, first_nr in enumerate(data):
        day_sum = first_nr
        numbers = [first_nr]
        for second_nr in data[index + 1:]:
            day_sum += second_nr
            numbers.append(second_nr)
            if day_sum == result:
                print(max(numbers) + min(numbers))
                return


if __name__ == '__main__':
    main()
