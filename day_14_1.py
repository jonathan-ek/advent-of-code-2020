from helper import get_input


def main():
    data = [x.split(' = ') for x in get_input(14).split('\n') if x]
    zero_mask = int('111111111111111111111111111111111111', 2)
    one_mask = int('000000000000000000000000000000000000', 2)
    mem = {}
    for operation, value in data:
        if operation == 'mask':
            tmp_one_mask = [x for x in '000000000000000000000000000000000000']
            tmp_zero_mask = [x for x in '111111111111111111111111111111111111']
            for i, char in enumerate(value):
                if char == '1':
                    tmp_one_mask[i] = '1'
                elif char == '0':
                    tmp_zero_mask[i] = '0'
            one_mask = int(''.join(tmp_one_mask), 2)
            zero_mask = int(''.join(tmp_zero_mask), 2)
        else:
            pos = int(operation[:-1].split('[')[1])
            masked_value = (int(value) | one_mask) & zero_mask
            mem[pos] = masked_value

    print(sum(mem.values()))


if __name__ == '__main__':
    main()
