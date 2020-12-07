from helper import get_input


def calc_bags_in_bags(bag, data):
    total_sum = 1
    for count, content in data[bag]:
        total_sum += int(count) * calc_bags_in_bags(content, data)
    return total_sum


def main():
    data = [x.split(' bags contain ') for x in get_input(7).split('\n') if x]
    bags = {}
    for bag in data:
        bags[bag[0]] = [x.split(' ', 1) for x in
                        bag[1].replace('.', '').replace(' bags', '').replace(' bag', '').split(', ') if x != 'no other']

    current_color = 'shiny gold'
    print(calc_bags_in_bags(current_color, bags) - 1)


if __name__ == '__main__':
    main()
