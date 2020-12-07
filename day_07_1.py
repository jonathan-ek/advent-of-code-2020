from helper import get_input


def main():
    data = [x.split(' bags contain ') for x in get_input(7).split('\n') if x]
    bags = {}
    for bag in data:
        bags[bag[0]] = [x.split(' ', 1) for x in
                        bag[1].replace('.', '').replace(' bags', '').replace(' bag', '').split(', ') if x != 'no other']

    can_contain_bag = ['shiny gold']
    added_bag = True
    while added_bag:
        added_bag = False
        for bag, content in bags.items():
            if bag not in can_contain_bag:
                colors_in_content = [x[1] for x in content]
                for color in can_contain_bag:
                    if color in colors_in_content:
                        can_contain_bag.append(bag)
                        added_bag = True
                        break
    print(len(can_contain_bag) - 1)


if __name__ == '__main__':
    main()
