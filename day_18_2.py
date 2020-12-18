from helper import get_input


def solve(equation):
    eq = [x for x in equation]
    new_eq = []
    append_next = 0
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
            while append_next != 0:
                append_next -= 1
                new_eq.append(')')
        if t == '*':
            while append_next != 0:
                append_next -= 1
                new_eq.append(')')
            new_eq.append(t)
        if t == '+':
            if new_eq[len(new_eq) - 1] == ')':
                new_eq[len(new_eq) - 1] = ''
            else:
                new_eq.insert(len(new_eq) - 1, '(')
            new_eq.append(t)
            append_next += 1
    while append_next != 0:
        append_next -= 1
        new_eq.append(')')
    # print(''.join(new_eq), '=', eval(''.join(new_eq)))
    return eval(''.join(new_eq))


def main():
    input_data = get_input(18)
    data = [x for x in input_data.split('\n') if x]
    # for eq in data:
    #     print(eq)
    #     ans = solve(eq.replace(' ', ''))
    #     print('=', ans)
    response = sum([solve(eq) for eq in data])
    print(response)


if __name__ == '__main__':
    main()
