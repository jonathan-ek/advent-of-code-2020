import re

from helper import get_input


def has_required_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for field in required_fields:
        if field not in passport.keys():
            return False
    return valid


def has_valid_data(passport):
    try:
        assert 1920 <= int(passport['byr']) <= 2002
        assert 2010 <= int(passport['iyr']) <= 2020
        assert 2020 <= int(passport['eyr']) <= 2030
        eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        assert passport['ecl'] in eye_color
        if 'cm' in passport['hgt']:
            assert 150 <= int(passport['hgt'][:-2]) <= 193
        elif 'in' in passport['hgt']:
            assert 59 <= int(passport['hgt'][:-2]) <= 76
        else:
            return False
        match = re.search(r'^#([0-9a-fA-F]{6})$', passport['hcl'])
        if not match:
            return False
        match = re.search(r'^([0-9]{9})$', passport['pid'])
        if not match:
            return False
    except AssertionError:
        return False
    return True


def main():
    data = [dict([y.split(':') for y in x.replace('\n', ' ').split(' ')]) for x in get_input(4).split('\n\n') if x]
    print(len([x for x in data if has_required_fields(x) and has_valid_data(x)]))


if __name__ == '__main__':
    main()
