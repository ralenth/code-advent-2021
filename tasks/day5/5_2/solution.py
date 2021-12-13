import numpy as np


def load_input(filename: str = 'input') -> np.array:
    with open(filename, 'r') as file:
        lines = [line.rstrip().split(' -> ') for line in file.readlines()]
        lines = [[list(map(int, n.split(','))) for n in line] for line in lines]
        return np.array(lines)


def create_table(points: np.array) -> np.array:
    n = np.max(points)
    return np.zeros((n + 1, n + 1))


def update_table(points: np.array, table: np.array) -> np.array:
    for point in points:
        p1, p2 = point
        dx, dy, start_x, start_y = get_coords(p1, p2)

        if is_diagonal(p1, p2):
            direction = check_direction(p1, p2)
            xs = list(range(start_x, start_x + dx + 1))
            if direction[0] < 0:
                xs = list(reversed(xs))
            ys = list(range(start_y, start_y + dy + 1))
            if direction[1] < 0:
                ys = list(reversed(ys))

            if len(xs) > len(ys):
                ys = [ys[0] for _ in range(len(xs))]
            elif len(ys) > len(xs):
                xs = [xs[0] for _ in range(len(ys))]

            for x, y in zip(xs, ys):
                table[x, y] += 1

        else:
            table[start_x: start_x + dx + 1, start_y: start_y + dy + 1] += 1

    return table


def is_diagonal(p1: np.array, p2: np.array) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    if x1 != x2 or y1 != y2:
        return True
    return False


def check_direction(p1: np.array, p2: np.array) -> list[int, int]:
    x1, y1 = p1
    x2, y2 = p2
    direction = [0, 0]

    if x1 > x2:
        direction[0] = -1
    elif x2 > x1:
        direction[0] = 1

    if y1 > y2:
        direction[1] = -1
    elif y2 > y1:
        direction[1] = 1

    return direction


def get_coords(p1: list, p2: list) -> tuple[int, int, int, int]:
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    start_x = min(p1[0], p2[0])
    start_y = min(p1[1], p2[1])
    return dx, dy, start_x, start_y


def get_overlap(table: np.array) -> int:
    return table[table >= 2].flatten().shape[0]


def main():
    points = load_input()
    table = create_table(points)
    table = update_table(points, table)
    x = get_overlap(table)
    print(f'At least 2 lines are overlapping {x} times')


main()
