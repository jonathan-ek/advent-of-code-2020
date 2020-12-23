from helper import get_input


def game(player_1, player_2):
    player_state = []
    while len(player_1) > 0 and len(player_2) > 0:
        if tuple([tuple(player_1), tuple(player_2)]) in player_state:
            return 1, player_1, player_2
        player_state.append(tuple([tuple(player_1), tuple(player_2)]))
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            winner, _, _ = game(player_1[:card_1], player_2[:card_2])
            if winner == 1:
                player_1.append(card_1)
                player_1.append(card_2)
            else:
                player_2.append(card_2)
                player_2.append(card_1)
        elif card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)
    return 1 if len(player_1) else 2, player_1, player_2


def main():
    player_1, player_2 = [[int(y) for y in x.split('\n')[1:]] for x in get_input(22).split('\n\n') if x]
    winner, player_1, player_2 = game(player_1, player_2)
    print(sum([x * (len(player_1) - i) for i, x in enumerate(player_1)]))
    print(sum([x * (len(player_2) - i) for i, x in enumerate(player_2)]))


if __name__ == '__main__':
    main()
