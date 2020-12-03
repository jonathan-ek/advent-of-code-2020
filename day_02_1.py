from helper import get_input


def main():
    data = [x.split(': ') for x in get_input(2).split('\n') if x]
    count = 0
    for policy, password in data:
        min_max, letter = policy.split(' ', 1)
        min_nr, max_nr = [int(x) for x in min_max.split('-')]
        nr_of_chosen_letter = len(password) - len(password.replace(letter, ''))
        if min_nr <= nr_of_chosen_letter <= max_nr:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
