left_key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

right_key = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


win_score = {
    'win': 6,
    'draw': 3,
    'loss': 0
}

play_score = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

loss_move = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

win_move = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

result_map = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def move_for_result(opponent, result='win'):
    if result == 'win':
        return win_move[opponent]
    elif result == 'draw':
        return opponent
    else:
        return loss_move[opponent]


def winner(left, right):
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

    scores = []
    with open(file_name, 'r') as f:
        for line in f:
            line_content = line.strip().split(' ')
            left, right = line_content

            left_move = left_key[left]


            # Part 1 gameplay
            # right_move = right_key[right]
            #scores.append(win_score[winner(left_move, right_move)] + play_score[right_move])

            # Part 2 gameplay
            expected_result = result_map[right]
            right_move = move_for_result(left_move, expected_result)

            scores.append(win_score[winner(left_move, right_move)] + play_score[right_move])



    print(sum(scores))


if __name__ == '__main__':
    main()

