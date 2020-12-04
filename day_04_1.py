from helper import get_input


def has_required_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for field in required_fields:
        if field not in passport.keys():
            valid = False
    return valid


def main():
    data = [dict([y.split(':') for y in x.replace('\n', ' ').split(' ')]) for x in get_input(4).split('\n\n') if x]
    print(len([x for x in data if has_required_fields(x)]))


if __name__ == '__main__':
    main()
