from helper import get_input


def main():
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

    invalid_numbers = []
    for ticket in nearby_tickets:
        for number in ticket:
            if not any(
                    [True if (range_1[0] <= number <= range_1[1] or range_2[0] <= number <= range_2[1]) else False for
                     name, range_1, range_2 in row_info]):
                invalid_numbers.append(number)

    print(sum(invalid_numbers))


if __name__ == '__main__':
    main()
