import re
from helper import get_input


def parse_rule(key, rules):
    tmp = rules[key]
    while any(x in rules for x in tmp.split(' ')):
        tmp = tmp.replace(' 8 ', ' eight ')
        tmp = tmp.replace(' 11 ', ' eleven ')
        parts = tmp.split(' ')
        rule = ''
        for part in parts:
            if part in rules:
                rule = f'{rule} {rules[part]}'
            else:
                rule = f'{rule} {part}'
        tmp = rule
    return tmp


def main():
    rules, messages = get_input(19).split('\n\n', 1)
    raw_rules = dict([x.split(':') for x in rules.replace('"', '').split('\n') if x])
    rules = {}
    for rule_nr, rule in raw_rules.items():
        rule = f'{rule} '
        parts = rule.split('|')
        rule = ' | '.join([f' ( {x} ) ' for x in parts])
        rules[rule_nr] = f' ( {rule} ) '.replace('  ', ' ')
    rule_0 = parse_rule('0', rules)
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rule_42 = parse_rule('42', rules)
    rule_31 = parse_rule('31', rules)
    rule_0 = rule_0.replace('eight', f'({rule_42})+')
    rule_0 = rule_0.replace(
        'eleven',
        f'('
        f'(({rule_42})({rule_31}))|'
        f'(({rule_42})({rule_42})({rule_31})({rule_31}))|'
        f'(({rule_42})({rule_42})({rule_42})({rule_31})({rule_31})({rule_31}))|'
        f'(({rule_42})({rule_42})({rule_42})({rule_42})({rule_31})({rule_31})({rule_31})({rule_31}))'
        f')')
    messages = [x for x in messages.split('\n') if x]
    matches = 0
    for message in messages:
        if re.match(f"^{rule_0.replace(' ', '')}$", message):
            matches += 1
    print(matches)


if __name__ == '__main__':
    main()
