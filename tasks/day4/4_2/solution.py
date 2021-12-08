import numpy as np


def load_input(filename: str = 'input') -> tuple[list, np.array]:
    boards, board = [], []
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]
        numbers = lines[0].split(',')
        numbers = list(map(int, numbers))

        for line in lines[2:]:
            if not line:
                boards.append(board)
                board = []
            else:
                line = list(map(int, line.split()))
                board.append(line)
    boards.append(board)
    return numbers, np.array(boards)


def create_masks(boards: np.array) -> np.array:
    return np.ones(boards.shape)


def draw_number(num: int, boards: np.array,
                masks: np.array) -> tuple[np.array, np.array]:
    idx = np.where(boards == num)
    masks[idx] = 0
    return boards, masks


def check_winners(masks: np.array) -> list:
    n_boards, n_rows, n_cols = masks.shape
    winners = []

    for i in range(n_boards):
        for row in range(n_rows):
            if all(masks[i, row, :] == 0):
                winners.append(i)
        for col in range(n_cols):
            if all(masks[i, :, col] == 0):
                winners.append(i)
    return winners


def main():
    numbers, boards = load_input()
    winner_boards = list(range(len(boards)))
    masks = create_masks(boards)

    for number in numbers:
        boards, masks = draw_number(number, boards, masks)
        winners = check_winners(masks)
        if len(winner_boards) > 1 and winners:
            winner_boards = [b for b in winner_boards if b not in winners]
        elif winner_boards[0] in winners:
            break

    last_board = winner_boards[0]
    score = int(np.sum(masks[last_board] * boards[last_board]))
    print(f'Final score: {score * number}')


main()
