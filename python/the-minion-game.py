VOWELS = 'AEIOU'
PLAYER_ONE_NAME = "Kevin"
PLAYER_TWO_NAME = "Stuart"
DRAW = "Draw"


def minion_game(string):
    player_one_score = 0
    player_two_score = 0

    for index, first_letter in enumerate(string):
        score_for_letter = len(string) - index

        if first_letter in VOWELS:
            player_one_score += score_for_letter
        else:
            player_two_score += score_for_letter

    if player_one_score > player_two_score:
        print(PLAYER_ONE_NAME, player_one_score)
    elif player_one_score < player_two_score:
        print(PLAYER_TWO_NAME, player_two_score)
    else:
        print(DRAW)

if __name__ == '__main__':
    string = input()
    minion_game(string)
