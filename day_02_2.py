from helper import get_input


def main():
    data = [x.split(': ') for x in get_input(2).split('\n') if x]
    count = 0
    for policy, password in data:
        min_max, letter = policy.split(' ', 1)
        min_nr, max_nr = [int(x) for x in min_max.split('-')]
        if bool(password[min_nr - 1] == letter) ^ bool(password[max_nr - 1] == letter):
            count += 1
    print(count)


if __name__ == '__main__':
    main()
