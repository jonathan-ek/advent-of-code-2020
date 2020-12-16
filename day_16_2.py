from helper import get_input


def main():
    # Parse data
    row_info_raw, rest = get_input(16).split('your ticket:')
    your_ticket_raw, nearby_tickets_raw = rest.split('nearby tickets:')
    row_info = []
    for x in row_info_raw.split('\n'):
        if x:
            name, range_raw = x.split(': ')
            r1, r2 = range_raw.split(' or ')
            row_info.append([name, [int(x) for x in r1.split('-')], [int(x) for x in r2.split('-')]])
    your_ticket = [int(x.strip()) for x in your_ticket_raw.split(',') if x]
    nearby_tickets = [[int(y) for y in x.split(',')] for x in nearby_tickets_raw.split('\n') if x]

    # Find valid tickets.
    valid_tickets = []
    for ticket in nearby_tickets:
        invalid = False
        for number in ticket:
            if not any(
                    [True if (range_1[0] <= number <= range_1[1] or range_2[0] <= number <= range_2[1]) else False for
                     name, range_1, range_2 in row_info]):
                invalid = True
        if not invalid:
            valid_tickets.append(ticket)

    # Find possible columns for each row
    row_columns = []
    for name, range_1, range_2 in row_info:
        possible_columns = []
        for i in range(len(row_info)):
            if all([True if (range_1[0] <= number <= range_1[1] or range_2[0] <= number <= range_2[1]) else False for
                    number in [x[i] for x in valid_tickets]]):
                possible_columns.append(i)
        row_columns.append([name, possible_columns])

    # Figure out which column is which.
    definitive_columns = []
    used_numbers = []
    change = True
    while change:
        change = False
        for name, all_possibilities in row_columns:
            possibilities = [x for x in all_possibilities if x not in used_numbers]
            if len(possibilities) == 1:
                definitive_columns.append([name, possibilities[0]])
                used_numbers.append(possibilities[0])
                change = True

    # Calculate the answer
    value = 1
    for index in [index for name, index in definitive_columns if 'departure' in name]:
        value *= your_ticket[index]

    print(value)


if __name__ == '__main__':
    main()
