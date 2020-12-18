from helper import get_input


def solve(equation):
    eq = [x for x in equation]
    new_eq = []
    p_count = 0
    in_p = 0
    inner_eq = []
    for i, t in enumerate(eq):
        if t == ')':
            in_p -= 1
            if in_p == 0:
                new_eq.append(str(solve(inner_eq[1:])))
                inner_eq = []
        if t == '(':
            in_p += 1
        if in_p != 0:
            inner_eq.append(t)
            continue
        if t in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            new_eq.append(t)
        if t in ['*', '+']:
            new_eq.append(')')
            new_eq.append(t)
            p_count += 1
    for _ in range(p_count):
        new_eq.insert(0, '(')
    return eval(''.join(new_eq))


def main():
    input_data = get_input(18)
    data = [x.replace(' ', '') for x in input_data.split('\n') if x]
    print(sum([solve(eq) for eq in data]))


if __name__ == '__main__':
    main()
