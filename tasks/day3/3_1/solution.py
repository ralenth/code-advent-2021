def load_input(filename: str = 'input') -> list[list[int]]:
    with open(filename, 'r') as file:
        lines = [list(line.rstrip()) for line in file.readlines()]
        lines = [[int(x) for x in line] for line in lines]
    return lines


def power_consumption(lines: list[list[int]]) -> int:
    gamma, eps = '', ''

    for i in range(len(lines[0])):
        col = [row[i] for row in lines]
        if sum(col) / len(col) >= 0.5:
            gamma += '1'
            eps += '0'
        else:
            gamma += '0'
            eps += '1'

    gamma = int(gamma, 2)
    eps = int(eps, 2)

    return gamma * eps


def main():
    lines = load_input()
    x = power_consumption(lines)
    print(f'Power consumption of the submarine: {x}')


main()
