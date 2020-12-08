from helper import get_input


def main():
    instructions = [x.split(' ') for x in get_input(8).split('\n') if x]
    executed_instructions = []
    acc = 0
    counter = 0
    while True:
        inst, value = instructions[counter]
        if counter in executed_instructions:
            print(acc)
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
