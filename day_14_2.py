import itertools

from helper import get_input


def main():
    data = [x.split(' = ') for x in get_input(14).split('\n') if x]
    one_mask = int('000000000000000000000000000000000000', 2)
    x_positions = []
    mem = {}
    for operation, value in data:
        if operation == 'mask':
            tmp_one_mask = [x for x in '000000000000000000000000000000000000']
            x_positions = []
            for i, char in enumerate(value):
                if char == '1':
                    tmp_one_mask[i] = '1'
                elif char == 'X':
                    x_positions.append(i)
            one_mask = int(''.join(tmp_one_mask), 2)
        else:
            pos = int(operation[:-1].split('[')[1])
            masked_pos = (int(pos) | one_mask)
            for l in range(0, len(x_positions) + 1):
                for subset in itertools.combinations(x_positions, l):
                    tmp_0 = [x for x in '000000000000000000000000000000000000']
                    tmp_1 = [x for x in '111111111111111111111111111111111111']
                    for x in subset:
                        tmp_0[x] = '1'
                    for x in x_positions:
                        if x not in subset:
                            tmp_1[x] = '0'
                    pos = (masked_pos | int(''.join(tmp_0), 2)) & int(''.join(tmp_1), 2)
                    mem[pos] = int(value)

    print(sum(mem.values()))


if __name__ == '__main__':
    main()
