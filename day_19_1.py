import re
from helper import get_input


def main():
    rules, messages = get_input(19).split('\n\n', 1)
    raw_rules = dict([x.split(':') for x in rules.replace('"', '').split('\n') if x])
    rules = {}
    for rule_nr, rule in raw_rules.items():
        rule = f'{rule} '
        parts = rule.split('|')
        rule = ' | '.join([f' ( {x} ) ' for x in parts])
        rules[rule_nr] = f' ( {rule} ) '.replace('  ', ' ')
    tmp = rules['0']
    while any(x in rules for x in tmp.split(' ')):
        parts = tmp.split(' ')
        rule = ''
        for part in parts:
            if part in rules:
                rule = f'{rule} {rules[part]}'
            else:
                rule = f'{rule} {part}'
        tmp = rule
    rules['0'] = tmp
    messages = [x for x in messages.split('\n') if x]
    matches = 0
    for message in messages:
        if re.match(f"^{rules['0'].replace(' ', '')}$", message):
            matches += 1
    print(matches)


if __name__ == '__main__':
    main()
