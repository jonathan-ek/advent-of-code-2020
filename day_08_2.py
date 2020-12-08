from helper import get_input


def main():
    original_instructions = [x.split(' ') for x in get_input(8).split('\n') if x]

    for index, instruction in enumerate(original_instructions):
        instructions = [(x[0], x[1]) for x in original_instructions]
        run = False
        if instruction[0] == 'nop':
            instructions[index] = ('jmp', instructions[index][1])
            run = True
        elif instruction[0] == 'jmp':
            instructions[index] = ('nop', instructions[index][1])
            run = True
        executed_instructions = []
        acc = 0
        counter = 0
        if run:
            while True:
                if counter == len(instructions):
                    print(acc)
                    return
                inst, value = instructions[counter]
                if counter in executed_instructions:
                    break
                executed_instructions.append(counter)
                if inst == 'nop':
                    counter += 1
                elif inst == 'acc':
                    counter += 1
                    acc += int(value)
                elif inst == 'jmp':
                    counter += int(value)


if __name__ == '__main__':
    main()
