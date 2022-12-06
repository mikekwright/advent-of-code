LEFT_KEY = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

RIGHT_KEY = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


WIN_SCORE = {
    'win': 6,
    'draw': 3,
    'loss': 0
}

MOVE_SCORE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

LOSS_MOVE = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

WIN_MOVE = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

GAME_RESULT_MAP = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def move_for_result(opponent, result='win'):
    if result == 'win':
        return WIN_MOVE[opponent]
    elif result == 'draw':
        return opponent
    else:
        return LOSS_MOVE[opponent]


def game_result(left, right):
    if left == right:
        return 'draw'

    if left == 'rock' and right == 'paper':
        return 'win'
    if left == 'paper' and right == 'scissors':
        return 'win'
    if left == 'scissors' and right == 'rock':
        return 'win'

    return 'loss'


def main():
    file_name = 'input.txt'

    part1_scores = []
    part2_scores = []
    with open(file_name, 'r') as f:
        for line in f:
            line_content = line.strip().split(' ')
            left, right = line_content

            left_move = LEFT_KEY[left]

            # Part 1 gameplay
            right_move = RIGHT_KEY[right]
            part1_scores.append(WIN_SCORE[game_result(left_move, right_move)] + MOVE_SCORE[right_move])

            # Part 2 gameplay
            expected_result = GAME_RESULT_MAP[right]
            right_move = move_for_result(left_move, expected_result)

            part2_scores.append(WIN_SCORE[game_result(left_move, right_move)] + MOVE_SCORE[right_move])


    print(f'Part 1 - Scores: {sum(part1_scores)}')
    print(f'Part 2 - Scores: {sum(part2_scores)}')


if __name__ == '__main__':
    main()

