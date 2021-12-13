import numpy as np


def load_input(filename: str = 'input') -> np.array:
    with open(filename, 'r') as file:
        lines = [line.rstrip().split(' -> ') for line in file.readlines()]
        lines = [[list(map(int, n.split(','))) for n in line] for line in lines]
        points = []
        for l in lines:
            if l[0][0] == l[1][0] or l[0][1] == l[1][1]:
                points.append(l)

        return np.array(points)


def create_table(points: np.array) -> np.array:
    n = np.max(points)
    return np.zeros((n + 1, n + 1))


def update_table(points: np.array, table: np.array) -> np.array:
    for point in points:
        dx, dy, start_x, start_y = get_coords(point[0], point[1])
        table[start_x: start_x + dx + 1, start_y: start_y + dy + 1] += 1

    return table


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
