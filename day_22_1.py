from helper import get_input


def main():
    player_1, player_2 = [[int(y) for y in x.split('\n')[1:]] for x in get_input(22).split('\n\n') if x]
    while len(player_1) > 0 and len(player_2) > 0:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    res = player_1 + player_2
    print(sum([x * (len(res) - i) for i, x in enumerate(res)]))


if __name__ == '__main__':
    main()
