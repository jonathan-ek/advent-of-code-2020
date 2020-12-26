from helper import get_input


def main():
    public_keys = [int(x) for x in get_input(25).split('\n') if x]
    subject_nr = 7
    i = 0
    loop_nrs = {}
    tmp = 1
    while len(public_keys) != len(loop_nrs.keys()):
        tmp = (tmp * subject_nr) % 20201227
        if tmp in public_keys:
            loop_nrs[tmp] = i
        i += 1
    loop_nr_list = [loop_nrs[pk] for pk in public_keys]

    print(loop_nrs)
    loop_nr = loop_nr_list[0]
    subject_nr = public_keys[1]
    print(loop_nr, subject_nr)
    tmp = 1
    for _ in range(loop_nr+1):
        tmp = (tmp * subject_nr) % 20201227
    print(tmp)

if __name__ == '__main__':
    main()
